"""Identity hijacking detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

DOC_EXTENSIONS = {".md", ".txt", ".mdx"}

IDENTITY_RULES = [
    {"id": "IDENTITY_SWAP", "pattern": re.compile(r"(?:you\s+are|act\s+as|pretend\s+to\s+be|roleplay\s+as)\s+(?:a\s+)?(?:different|another|new)\s+(?:agent|assistant|AI|persona)", re.I), "severity": "critical", "title": "Identity swap attempt"},
    {"id": "IDENTITY_DEATH", "pattern": re.compile(r"(?:delete|remove|erase|forget)\s+(?:your\s+)?(?:identity|persona|character|SOUL)", re.I), "severity": "critical", "title": "Identity death attack"},
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
            for rule in IDENTITY_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="identity-hijacking",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Identity hijacking: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Remove identity manipulation instructions",
                        confidence=0.9,
                        rationale="Matches identity hijacking pattern",
                        exploit_precondition="Agent processes identity override instructions",
                    ))

    return ScanResult("identity_scanner", findings, files_scanned, time.time() - t0)
