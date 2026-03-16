"""Skill permission boundary and abuse risk scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import walk_files, read_file_safe, truncate_evidence

SKILL_DIRS = {"skills"}

_SKILL_EXTENSIONS = {
    ".py", ".sh", ".bash", ".ts", ".js", ".md", ".yaml", ".yml", ".json",
}

SKILL_RULES: list[dict] = [
    {
        "rule_id": "SKILL-001",
        "title": "Unsandboxed Exec",
        "pattern": re.compile(
            r"(?i)(subprocess\.(run|call|Popen|check_output)"
            r"|os\.(system|popen|exec)"
            r"|child_process|exec\(|execSync)"
        ),
        "severity": "critical",
        "cwe": "CWE-78",
        "remediation": "Use sandboxed execution or restrict command allowlist",
    },
    {
        "rule_id": "SKILL-002",
        "title": "Sensitive Path Access",
        "pattern": re.compile(
            r"(?i)(\/etc\/passwd|\/etc\/shadow"
            r"|~\/\."
            r"|\/root\/"
            r"|\/home\/[^/]+\/\."
            r"|\.ssh\/"
            r"|\.aws\/"
            r"|\.gnupg\/)"
        ),
        "severity": "critical",
        "cwe": "CWE-552",
        "remediation": "Restrict file access to skill's own directory",
    },
    {
        "rule_id": "SKILL-003",
        "title": "Gateway Control Escalation",
        "pattern": re.compile(
            r"(?i)(ws:\/\/127\.0\.0\.1:18789"
            r"|gateway.*restart"
            r"|gateway.*shutdown"
            r"|daemon.*kill)"
        ),
        "severity": "warn",
        "cwe": "CWE-269",
        "remediation": "Skills should not directly control the gateway; use approved APIs",
    },
    {
        "rule_id": "SKILL-004",
        "title": "Broad Tool Permissions",
        "pattern": re.compile(
            r"(?i)(allowedTools\s*:\s*\[?\s*['\"]?\*['\"]?\]?"
            r"|tools:\s*\*"
            r"|dangerouslySkipPermissions)"
        ),
        "severity": "warn",
        "cwe": "CWE-250",
        "remediation": "Restrict tool permissions to minimum required set",
    },
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan skill scripts for permission boundary violations and abuse risks."""
    t0 = time.monotonic()
    findings: list[Finding] = []
    files_scanned = 0

    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return ScanResult(
            scanner_name="skill_scanner",
            findings=[],
            files_scanned=0,
            duration_seconds=round(time.monotonic() - t0, 3),
        )

    seen: set[tuple[str, str]] = set()  # (rule_id, rel_path)

    for filepath in walk_files(skills_dir, extensions=_SKILL_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(filepath)
        if not content:
            continue
        files_scanned += 1
        rel = str(filepath.relative_to(root))

        for line_no, line in enumerate(content.splitlines(), start=1):
            for rule in SKILL_RULES:
                key = (rule["rule_id"], rel)
                if key in seen:
                    continue

                match = rule["pattern"].search(line)
                if match is None:
                    continue

                seen.add(key)
                findings.append(
                    Finding(
                        rule_id=rule["rule_id"],
                        category="skill",
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
        scanner_name="skill_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=round(time.monotonic() - t0, 3),
    )
