"""Financial access detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py"}

FINANCIAL_RULES = [
    {"id": "FIN_CRYPTO", "pattern": re.compile(r"private[_-]?key\s*[:=]|send[_-]?transaction|sign[_-]?transaction|transfer[_-]?funds", re.I), "severity": "warn", "title": "Cryptocurrency transaction operations"},
    {"id": "FIN_PAYMENT", "pattern": re.compile(r"stripe\.(?:charges|payments)|paypal\.(?:payment|payout)|plaid\.(?:link|transactions)", re.I), "severity": "info", "title": "Payment API integration"},
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, CODE_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(fpath)
        if not content:
            continue
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            for rule in FINANCIAL_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="financial-access",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Financial access: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Review financial operations for proper authorization",
                        confidence=0.75,
                        rationale="Matches financial API pattern",
                        exploit_precondition="Unauthorized financial transaction execution",
                    ))

    return ScanResult("financial_scanner", findings, files_scanned, time.time() - t0)
