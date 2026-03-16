"""Ransomware detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

SCAN_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash"}

RANSOMWARE_RULES: list[dict] = [
    {
        "rule_id": "RANSOM-001",
        "title": "Ransomware Extension",
        "pattern": r"\.(encrypted|locked|crypto|crypt|enc|locky|cerber|zepto|odin|thor|aesir|zzzzz)\b",
        "severity": "critical",
        "cwe": "CWE-506",
        "remediation": "Remove ransomware code immediately.",
        "category": "ransomware",
    },
    {
        "rule_id": "RANSOM-002",
        "title": "Mass File Encryption",
        "pattern": r"(?i)(\.encrypt\s*\(|AES\.encrypt|RSA\.encrypt|crypto\.encrypt|cipher\.encrypt)",
        "severity": "warn",
        "cwe": "CWE-506",
        "remediation": "Review encryption usage. Mass file encryption is suspicious.",
        "category": "ransomware",
    },
    {
        "rule_id": "RANSOM-003",
        "title": "Directory Traversal Pattern",
        "pattern": r"(?i)(\.glob\([\"'].*\*|os\.walk\(|walkdir|readdir.*recursive)",
        "severity": "info",
        "cwe": "CWE-506",
        "remediation": "Review file iteration patterns for malicious intent.",
        "category": "ransomware",
    },
    {
        "rule_id": "RANSOM-004",
        "title": "Ransom Payment Reference",
        "pattern": r"(?i)\b(bitcoin|btc|wallet|ransom|payment|decrypt.*key)\b",
        "severity": "warn",
        "cwe": "CWE-506",
        "remediation": "Review payment-related code for ransomware indicators.",
        "category": "ransomware",
    },
]

_COMPILED_RULES: list[tuple[dict, re.Pattern]] = [
    (rule, re.compile(rule["pattern"])) for rule in RANSOMWARE_RULES
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan for ransomware patterns."""
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

        # Check filename for ransom note patterns
        file_name = path.name.upper()
        if any(x in file_name for x in ["README_DECRYPT", "HOW_TO_DECRYPT", "DECRYPT_INSTRUCTIONS", "YOUR_FILES_ARE_ENCRYPTED"]):
            findings.append(
                Finding(
                    rule_id="RANSOM-000",
                    category="ransomware",
                    severity="critical",
                    title="Ransom Note File Detected",
                    detail=f"File name matches ransom note pattern: {path.name}",
                    file_path=rel,
                    line=1,
                    evidence=path.name,
                    remediation="Remove ransomware artifacts immediately. Investigate system compromise.",
                    cwe="CWE-506",
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
        scanner_name="ransomware_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=duration,
    )
