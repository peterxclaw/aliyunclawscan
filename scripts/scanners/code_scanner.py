"""Code-level vulnerability scanner (injection, SSRF, RCE, XSS, log leaks)."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".mts", ".cts", ".py"}

CODE_RULES: list[dict] = [
    {
        "rule_id": "INJECT-001",
        "title": "Command Injection",
        "pattern": r"(?i)(child_process|exec|execSync|spawn|execFile)\s*\(",
        "severity": "critical",
        "cwe": "CWE-78",
        "remediation": "Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.",
        "category": "injection",
    },
    {
        "rule_id": "INJECT-002",
        "title": "eval/Function Usage",
        "pattern": r"(?i)\b(eval|new\s+Function)\s*\(",
        "severity": "critical",
        "cwe": "CWE-95",
        "remediation": "Replace eval/new Function with safer alternatives (JSON.parse, structured parsers).",
        "category": "injection",
    },
    {
        "rule_id": "INJECT-003",
        "title": "Path Traversal",
        "pattern": r"(?i)(\.\.\/|\.\.\\\\|path\.join\s*\([^)]*\+)",
        "severity": "warn",
        "cwe": "CWE-22",
        "remediation": "Canonicalise and validate paths against an allowed base directory.",
        "category": "injection",
    },
    {
        "rule_id": "INJECT-004",
        "title": "Unsafe Deserialization",
        "pattern": r"(?i)(JSON\.parse\s*\(\s*(req\.|request\.|body|params|query)|pickle\.loads|yaml\.load\s*\([^)]*Loader)",
        "severity": "warn",
        "cwe": "CWE-502",
        "remediation": "Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.",
        "category": "injection",
    },
    {
        "rule_id": "INJECT-005",
        "title": "SSRF Risk",
        "pattern": r"(?i)(fetch|axios|http\.get|https\.get|request)\s*\(\s*[^'\")\s]",
        "severity": "warn",
        "cwe": "CWE-918",
        "remediation": "Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.",
        "category": "injection",
    },
    {
        "rule_id": "INJECT-006",
        "title": "Dangerous innerHTML",
        "pattern": r"(?i)(innerHTML|outerHTML|document\.write)\s*[=\(]",
        "severity": "warn",
        "cwe": "CWE-79",
        "remediation": "Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.",
        "category": "xss",
    },
    {
        "rule_id": "INJECT-007",
        "title": "SQL Injection",
        "pattern": r"(?i)(query|execute)\s*\(\s*[`'\"].*\$\{|(\+\s*req\.)",
        "severity": "critical",
        "cwe": "CWE-89",
        "remediation": "Use parameterised queries or an ORM. Never concatenate user input into SQL strings.",
        "category": "injection",
    },
    {
        "rule_id": "LOG-001",
        "title": "Sensitive Data in Logs",
        "pattern": r"(?i)(console\.(log|info|warn|error)|logger\.\w+)\s*\(.*\b(password|secret|token|apiKey|api_key|credential|ssn|credit.?card)\b",
        "severity": "warn",
        "cwe": "CWE-532",
        "remediation": "Redact or mask sensitive values before logging. Use structured logging with field filtering.",
        "category": "log-leak",
    },
    {
        "rule_id": "LOG-002",
        "title": "Error Stack Exposure",
        "pattern": r"(?i)(res\.(send|json|write)|response\.(send|json))\s*\(.*\b(stack|err\.message|error\.message)\b",
        "severity": "info",
        "cwe": "CWE-209",
        "remediation": "Return generic error messages to clients. Log full stack traces server-side only.",
        "category": "log-leak",
    },
    {
        "rule_id": "RCE-001",
        "title": "Reverse Shell via /dev/tcp",
        "pattern": r"/dev/tcp/[\d\.]+/\d+|bash\s+-i\s*>\s*&\s*/dev/tcp",
        "severity": "critical",
        "cwe": "CWE-78",
        "remediation": "Remove reverse shell code. This is a backdoor pattern.",
        "category": "rce",
    },
    {
        "rule_id": "RCE-002",
        "title": "Netcat Backdoor",
        "pattern": r"nc\s+-[a-z]*e\s+|ncat\s+-[a-z]*e\s+|netcat.*-e",
        "severity": "critical",
        "cwe": "CWE-78",
        "remediation": "Remove netcat backdoor. This enables remote command execution.",
        "category": "rce",
    },
    {
        "rule_id": "RCE-003",
        "title": "Python Reverse Shell",
        "pattern": r"socket\.socket\(.*\).*\.connect\(.*\).*os\.dup2|subprocess\.call\(\[.*sh.*\].*stdin.*socket",
        "severity": "critical",
        "cwe": "CWE-78",
        "remediation": "Remove Python reverse shell code.",
        "category": "rce",
    },
    {
        "rule_id": "RCE-004",
        "title": "Node.js Reverse Shell",
        "pattern": r"net\.connect\(.*\).*spawn\(.*sh.*\)|child_process.*net\.Socket",
        "severity": "critical",
        "cwe": "CWE-78",
        "remediation": "Remove Node.js reverse shell code.",
        "category": "rce",
    },
]

# Pre-compile patterns for performance.
_COMPILED_RULES: list[tuple[dict, re.Pattern]] = [
    (rule, re.compile(rule["pattern"])) for rule in CODE_RULES
]


def is_test_file(path: Path) -> bool:
    """Check if file is a test file"""
    path_str = str(path).lower()
    return any(x in path_str for x in [".test.", ".spec.", "/tests/", "/__tests__/", "/fixtures/"])


def is_safe_path_context(line: str) -> bool:
    """Check if path usage is in a safe context"""
    if re.match(r'^\s*import\s+', line):
        return True
    if re.search(r'(__dirname|__filename|process\.cwd\(\))', line):
        return True
    return False


def _has_concat_or_template(line: str) -> bool:
    """Return True if the line contains string concatenation or a template literal interpolation."""
    return "+" in line or "${" in line


def _arg_is_string_literal(match: re.Match) -> bool:
    """Return True if the first argument after the opening paren looks like a string literal."""
    end = match.end()
    # match.string is the full line; peek at what follows the match
    rest = match.string[end - 1:]  # include the char captured by [^'")\s]
    first_char = rest[0] if rest else ""
    return first_char in ("'", '"', "`")


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan code files under *root* for common vulnerability patterns."""
    start = time.monotonic()
    findings: list[Finding] = []
    files_scanned = 0

    # Track (rule_id, file_path) pairs for deduplication.
    seen: set[tuple[str, str]] = set()

    for path in walk_files(root, extensions=CODE_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(path)
        if not content:
            continue
        files_scanned += 1
        rel = str(path)

        for line_no, line in enumerate(content.splitlines(), start=1):
            for rule, compiled in _COMPILED_RULES:
                dedup_key = (rule["rule_id"], rel)
                if dedup_key in seen:
                    continue

                m = compiled.search(line)
                if m is None:
                    continue

                # INJECT-001: only flag when user input may flow into the command.
                if rule["rule_id"] == "INJECT-001":
                    if not _has_concat_or_template(line):
                        continue

                # INJECT-003: skip test files and safe path contexts.
                if rule["rule_id"] == "INJECT-003":
                    if is_test_file(path) or is_safe_path_context(line):
                        continue

                # INJECT-005: skip when the URL argument is a string literal.
                if rule["rule_id"] == "INJECT-005":
                    if _arg_is_string_literal(m):
                        continue

                seen.add(dedup_key)
                findings.append(
                    Finding(
                        rule_id=rule["rule_id"],
                        category=rule["category"],
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"{rule['title']} detected in {path.name}",
                        file_path=rel,
                        line=line_no,
                        evidence=truncate_evidence(line),
                        remediation=rule["remediation"],
                        cwe=rule["cwe"],
                    )
                )

    duration = time.monotonic() - start
    return ScanResult(
        scanner_name="code_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=round(duration, 3),
    )
