"""PII exposure detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

ALL_EXTENSIONS = {".md", ".txt", ".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".json", ".env"}

PII_RULES = [
    {"id": "PII_CREDIT_CARD", "pattern": re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b"), "severity": "critical", "title": "Credit card number"},
    {"id": "PII_SSN", "pattern": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "severity": "critical", "title": "Social Security Number"},
    {"id": "PII_MY_NUMBER", "pattern": re.compile(r"(?<!\d)\d{4}\s*\d{4}\s*\d{4}(?!\d)"), "severity": "critical", "title": "My Number (個人番号)"},
    {"id": "PII_EMAIL", "pattern": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"), "severity": "info", "title": "Email address"},
]


def is_placeholder(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in ["example", "test", "dummy", "sample", "placeholder", "xxx", "user@"])


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, ALL_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(fpath)
        if not content:
            continue
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            for rule in PII_RULES:
                match = rule["pattern"].search(line)
                if match:
                    val = match.group(0)
                    if is_placeholder(val):
                        continue

                    key = (rule["id"], str(fpath), i)
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="pii-exposure",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"PII detected: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence("[REDACTED]"),
                        remediation="Remove PII from source code and documentation",
                        cwe="CWE-359",
                        confidence=0.8,
                        rationale="Matches PII pattern",
                        exploit_precondition="PII exposed in logs or public repositories",
                    ))

    return ScanResult("pii_scanner", findings, files_scanned, time.time() - t0)
