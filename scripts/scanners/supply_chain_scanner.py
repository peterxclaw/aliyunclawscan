"""Supply chain security scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".json", ".ts", ".js", ".py"}

SUPPLY_CHAIN_RULES = [
    {"id": "SUPPLY_TYPOSQUAT", "pattern": re.compile(r"(?:lodash|express|react|axios|request)[-_](?:js|npm|pkg|lib)", re.I), "severity": "critical", "title": "Potential typosquatting package"},
    {"id": "SUPPLY_PREINSTALL", "pattern": re.compile(r"\"(?:preinstall|postinstall)\":\s*\"(?!echo|exit)"), "severity": "warn", "title": "Lifecycle script in package.json"},
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, CODE_EXTENSIONS, exclude_tests=exclude_tests):
        if fpath.name != "package.json" and not fpath.suffix in {".ts", ".js", ".py"}:
            continue

        content = read_file_safe(fpath)
        if not content:
            continue
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            for rule in SUPPLY_CHAIN_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="supply-chain",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Supply chain risk: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Verify package authenticity and review lifecycle scripts",
                        confidence=0.7,
                        rationale="Matches supply chain attack pattern",
                        exploit_precondition="Malicious package installed or executed",
                    ))

    return ScanResult("supply_chain_scanner", findings, files_scanned, time.time() - t0)
