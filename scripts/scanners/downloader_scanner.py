"""Malicious downloader detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

SCAN_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash"}

DOWNLOADER_RULES: list[dict] = [
    {
        "rule_id": "DOWNLOAD-001",
        "title": "Curl Pipe to Bash",
        "pattern": r"curl.*\|.*bash",
        "severity": "critical",
        "cwe": "CWE-494",
        "remediation": "Remove curl|bash patterns. Never execute downloaded code directly.",
        "category": "malicious-downloader",
    },
    {
        "rule_id": "DOWNLOAD-002",
        "title": "Wget Pipe to Shell",
        "pattern": r"wget.*\|.*(sh|bash)",
        "severity": "critical",
        "cwe": "CWE-494",
        "remediation": "Remove wget|sh patterns. Never execute downloaded code directly.",
        "category": "malicious-downloader",
    },
    {
        "rule_id": "DOWNLOAD-003",
        "title": "Download and Execute",
        "pattern": r"(curl|wget).*-o.*&&.*chmod.*\+x",
        "severity": "critical",
        "cwe": "CWE-494",
        "remediation": "Remove download-and-execute patterns.",
        "category": "malicious-downloader",
    },
    {
        "rule_id": "DOWNLOAD-004",
        "title": "Base64 Eval Pattern",
        "pattern": r"(eval|exec)\s*\(\s*base64",
        "severity": "critical",
        "cwe": "CWE-494",
        "remediation": "Remove base64 eval patterns. This is obfuscated code execution.",
        "category": "malicious-downloader",
    },
    {
        "rule_id": "DOWNLOAD-005",
        "title": "Direct IP Connection",
        "pattern": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
        "severity": "warn",
        "cwe": "CWE-494",
        "remediation": "Verify direct IP connections. Use domain names instead.",
        "category": "malicious-downloader",
    },
    {
        "rule_id": "DOWNLOAD-006",
        "title": "URL Shortener",
        "pattern": r"(?i)(bit\.ly|tinyurl|goo\.gl)/",
        "severity": "warn",
        "cwe": "CWE-494",
        "remediation": "Avoid URL shorteners. They obscure the actual destination.",
        "category": "malicious-downloader",
    },
    {
        "rule_id": "DOWNLOAD-007",
        "title": "Social Engineering Language",
        "pattern": r"(?i)(update required|security patch|critical update|verify your account|confirm identity|urgent action)",
        "severity": "warn",
        "cwe": "CWE-494",
        "remediation": "Review user-facing messages for manipulation tactics.",
        "category": "malicious-downloader",
    },
]

_COMPILED_RULES: list[tuple[dict, re.Pattern]] = [
    (rule, re.compile(rule["pattern"])) for rule in DOWNLOADER_RULES
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan for malicious downloader patterns."""
    start = time.monotonic()
    findings: list[Finding] = []
    files_scanned = 0
    seen: set[tuple[str, str]] = set()

    for path in walk_files(root, extensions=SCAN_EXTENSIONS, exclude_tests=exclude_tests):
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

                if compiled.search(line):
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
        scanner_name="downloader_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=duration,
    )
