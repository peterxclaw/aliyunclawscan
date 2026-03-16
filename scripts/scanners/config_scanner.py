"""Scanner for insecure configuration patterns."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import walk_files, read_file_safe, truncate_evidence

_CONFIG_EXTENSIONS = {".json", ".yaml", ".yml", ".toml", ".env"}

CONFIG_RULES: list[dict] = [
    {
        "rule_id": "CONFIG-001",
        "title": "Dangerous Skip Flags",
        "pattern": re.compile(
            r"(?i)(dangerouslyDisableSandbox|dangerouslySkipPermissions"
            r"|--no-verify|--force|skipVerification)\s*[=:]\s*true"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-693",
        "remediation": "Remove dangerous skip flags; use proper validation",
    },
    {
        "rule_id": "CONFIG-002",
        "title": "Debug Mode Enabled",
        "pattern": re.compile(
            r"(?i)(debug|verbose|devMode)\s*[=:]\s*true"
        ),
        "severity": "warn",
        "file_filter": _CONFIG_EXTENSIONS,
        "cwe": "CWE-489",
        "remediation": "Disable debug/verbose mode in production configurations",
    },
    {
        "rule_id": "CONFIG-003",
        "title": "No Auth Gateway",
        "pattern": re.compile(
            r"(?i)(requireAuth|authentication)\s*[=:]\s*false"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-306",
        "remediation": "Enable authentication on all gateway endpoints",
    },
    {
        "rule_id": "CONFIG-004",
        "title": "Permissive CORS",
        "pattern": re.compile(
            r"(?i)(cors|allowOrigin|access-control-allow-origin)\s*[=:]\s*['\"]"
            r"\*['\"]"
        ),
        "severity": "warn",
        "file_filter": None,
        "cwe": "CWE-942",
        "remediation": "Restrict CORS to specific trusted origins instead of wildcard",
    },
    {
        "rule_id": "CONFIG-005",
        "title": "Sandbox Disabled",
        "pattern": re.compile(
            r"(?i)(sandbox|sandboxMode|enableSandbox)\s*[=:]\s*false"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-693",
        "remediation": "Enable sandbox mode to isolate untrusted operations",
    },
    {
        "rule_id": "CONFIG-006",
        "title": "Insecure TLS",
        "pattern": re.compile(
            r"(?i)(rejectUnauthorized|NODE_TLS_REJECT_UNAUTHORIZED)\s*[=:]\s*(false|0)"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-295",
        "remediation": "Enable TLS certificate verification; never disable in production",
    },
    {
        "rule_id": "CONFIG-007",
        "title": "Auto-Approved Bash Tool",
        "pattern": re.compile(
            r"(?i)(\"Bash\"|'Bash')\s*[,\]].*autoApprove|autoApprove.*[,\[].*[\"']Bash[\"']"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-78",
        "remediation": "Remove Bash from auto-approved tools; require manual approval",
    },
    {
        "rule_id": "CONFIG-008",
        "title": "Unrestricted Browser Control",
        "pattern": re.compile(
            r"(?i)(browserControl|headlessBrowser|puppeteer)\s*[=:]\s*true"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-250",
        "remediation": "Restrict browser control capabilities; require approval",
    },
    {
        "rule_id": "CONFIG-009",
        "title": "Workspace Boundary Disabled",
        "pattern": re.compile(
            r"(?i)(enforceWorkspace|workspaceBoundary)\s*[=:]\s*false"
        ),
        "severity": "critical",
        "file_filter": None,
        "cwe": "CWE-22",
        "remediation": "Enable workspace boundary enforcement to prevent path traversal",
    },
    {
        "rule_id": "CONFIG-010",
        "title": "Open Room Without Auth",
        "pattern": re.compile(
            r"(?i)(openRoom|publicAccess|allowGuests)\s*[=:]\s*true"
        ),
        "severity": "warn",
        "file_filter": None,
        "cwe": "CWE-306",
        "remediation": "Require authentication for room access; disable guest access",
    },
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan for insecure configuration patterns under *root*."""
    t0 = time.monotonic()
    findings: list[Finding] = []
    files_scanned = 0

    for filepath in walk_files(root, exclude_tests=exclude_tests):
        content = read_file_safe(filepath)
        if not content:
            continue
        files_scanned += 1
        rel = str(filepath.relative_to(root))

        for rule in CONFIG_RULES:
            # CONFIG-002 only applies to config file extensions
            if rule["file_filter"] is not None:
                if filepath.suffix not in rule["file_filter"]:
                    continue

            match = rule["pattern"].search(content)
            if match is None:
                continue

            # Determine line number of first match
            line_no = content[: match.start()].count("\n") + 1

            findings.append(
                Finding(
                    rule_id=rule["rule_id"],
                    category="config",
                    severity=rule["severity"],
                    title=rule["title"],
                    detail=f"{rule['title']} detected in {rel}",
                    file_path=rel,
                    line=line_no,
                    evidence=truncate_evidence(match.group(0)),
                    remediation=rule["remediation"],
                    cwe=rule["cwe"],
                )
            )

    return ScanResult(
        scanner_name="config_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=round(time.monotonic() - t0, 3),
    )
