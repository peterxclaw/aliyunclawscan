"""Cryptominer detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

SCAN_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash", ".json", ".yaml", ".yml"}

CRYPTOMINER_RULES: list[dict] = [
    {
        "rule_id": "CRYPTO-001",
        "title": "Mining Pool Connection",
        "pattern": r"(?i)(xmr-|monero|pool\.minexmr|supportxmr|nanopool|f2pool|antpool|slushpool|ethermine|hiveon)",
        "severity": "critical",
        "cwe": "CWE-912",
        "remediation": "Remove mining pool connections. Cryptomining is unauthorized resource usage.",
        "category": "cryptominer",
    },
    {
        "rule_id": "CRYPTO-002",
        "title": "Mining Software Reference",
        "pattern": r"(?i)\b(xmrig|ccminer|cgminer|bfgminer|ethminer|phoenixminer|claymore|nbminer|gminer)\b",
        "severity": "critical",
        "cwe": "CWE-912",
        "remediation": "Remove mining software references. This indicates unauthorized cryptomining.",
        "category": "cryptominer",
    },
    {
        "rule_id": "CRYPTO-003",
        "title": "Stratum Mining Protocol",
        "pattern": r"(?i)(stratum\+tcp://|stratum\+ssl://|mining\.pool|worker[_-]?id|pool[_-]?address)",
        "severity": "critical",
        "cwe": "CWE-912",
        "remediation": "Remove mining protocol connections.",
        "category": "cryptominer",
    },
    {
        "rule_id": "CRYPTO-004",
        "title": "Common Mining Port",
        "pattern": r":(3333|45700|14444|5555|8888|9999)\b",
        "severity": "warn",
        "cwe": "CWE-912",
        "remediation": "Verify port usage. These ports are commonly used for mining.",
        "category": "cryptominer",
    },
]

_COMPILED_RULES: list[tuple[dict, re.Pattern]] = [
    (rule, re.compile(rule["pattern"])) for rule in CRYPTOMINER_RULES
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan for cryptocurrency mining patterns."""
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
        scanner_name="cryptominer_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=duration,
    )
