"""Persistence mechanism detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

SCAN_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash", ".plist", ".service"}

PERSISTENCE_RULES: list[dict] = [
    {
        "rule_id": "PERSIST-001",
        "title": "macOS LaunchAgent Path",
        "pattern": r"(/Library/LaunchAgents/|/Library/LaunchDaemons/|~/Library/LaunchAgents/|/System/Library/LaunchAgents/|/System/Library/LaunchDaemons/)",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Verify LaunchAgent/Daemon legitimacy. Unauthorized persistence is malicious.",
        "category": "persistence",
    },
    {
        "rule_id": "PERSIST-002",
        "title": "Linux Persistence Path",
        "pattern": r"(/etc/cron\.(d|daily|hourly)/|/var/spool/cron/|/etc/systemd/system/|~/.config/autostart/)",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Verify cron/systemd service legitimacy.",
        "category": "persistence",
    },
    {
        "rule_id": "PERSIST-003",
        "title": "LaunchControl Command",
        "pattern": r"launchctl\s+(load|submit)",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Review persistence setup. Unauthorized autostart is suspicious.",
        "category": "persistence",
    },
    {
        "rule_id": "PERSIST-004",
        "title": "Crontab Modification",
        "pattern": r"crontab\s+-e",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Review cron job modifications.",
        "category": "persistence",
    },
    {
        "rule_id": "PERSIST-005",
        "title": "Systemd Service Enable",
        "pattern": r"systemctl\s+enable",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Review systemd service enablement.",
        "category": "persistence",
    },
    {
        "rule_id": "PERSIST-006",
        "title": "Shell Config Modification",
        "pattern": r"echo.*>>\s*~/\.(bashrc|zshrc|profile|bash_profile|zprofile|zshenv)",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Review shell config modifications for unauthorized persistence.",
        "category": "persistence",
    },
]

_COMPILED_RULES: list[tuple[dict, re.Pattern]] = [
    (rule, re.compile(rule["pattern"])) for rule in PERSISTENCE_RULES
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan for persistence mechanisms."""
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

        # Check shell config filenames
        file_name = path.name
        if file_name in [".bashrc", ".bash_profile", ".zshrc", ".profile", ".zprofile", ".zshenv"]:
            findings.append(
                Finding(
                    rule_id="PERSIST-000",
                    category="persistence",
                    severity="info",
                    title="Shell Configuration File",
                    detail=f"Shell config file: {file_name}",
                    file_path=rel,
                    line=1,
                    evidence=file_name,
                    remediation="Review shell config for unauthorized modifications.",
                    cwe="CWE-912",
                )
            )

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
        scanner_name="persistence_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=duration,
    )
