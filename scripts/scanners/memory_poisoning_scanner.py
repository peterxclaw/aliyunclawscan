"""Memory poisoning detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

DOC_EXTENSIONS = {".md", ".txt", ".mdx"}

MEMORY_POISONING_RULES = [
    {"id": "MEMPOIS_WRITE_SOUL", "pattern": re.compile(r"(?:write|add|append|modify|update|edit|change)\s+(?:to\s+)?(?:SOUL\.md|IDENTITY\.md|AGENTS\.md)", re.I), "severity": "critical", "title": "SOUL/IDENTITY file modification"},
    {"id": "MEMPOIS_WRITE_MEMORY", "pattern": re.compile(r"(?:write|add|append|insert)\s+(?:to|into)\s+(?:MEMORY\.md|memory\/|long[_\s-]term\s+memory)", re.I), "severity": "warn", "title": "Agent memory modification"},
    {"id": "MEMPOIS_CHANGE_RULES", "pattern": re.compile(r"(?:change|modify|override|replace|update)\s+(?:your\s+)?(?:rules|instructions|system\s+prompt|behavior|personality|guidelines)", re.I), "severity": "critical", "title": "Behavioral rule override"},
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
            for rule in MEMORY_POISONING_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="memory-poisoning",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Memory poisoning attempt: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Remove instructions that modify agent memory or identity files",
                        confidence=0.9,
                        rationale="Matches memory poisoning attack pattern",
                        exploit_precondition="Agent has write access to memory/identity files",
                    ))

    return ScanResult("memory_poisoning_scanner", findings, files_scanned, time.time() - t0)
