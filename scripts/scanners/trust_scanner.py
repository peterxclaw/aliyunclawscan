"""Trust exploitation detection scanner (OWASP ASI09)."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

DOC_EXTENSIONS = {".md", ".txt", ".mdx"}

TRUST_RULES = [
    {"id": "TRUST_AUTHORITY", "pattern": re.compile(r"(?:I\s+am|this\s+is)\s+(?:your\s+)?(?:creator|developer|admin|owner|maintainer)", re.I), "severity": "critical", "title": "Authority claim (creator impersonation)"},
    {"id": "TRUST_URGENT", "pattern": re.compile(r"(?:urgent|emergency|critical|immediately).*(?:override|bypass|ignore|disable)", re.I), "severity": "warn", "title": "Urgency-based trust exploitation"},
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, DOC_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(fpath)
        if not content:
            continue
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            for rule in TRUST_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="trust-exploitation",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Trust exploitation: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Remove authority claims and urgency-based manipulation",
                        confidence=0.85,
                        rationale="Matches OWASP ASI09 trust exploitation pattern",
                        exploit_precondition="Agent trusts claimed authority without verification",
                    ))

    return ScanResult("trust_scanner", findings, files_scanned, time.time() - t0)
