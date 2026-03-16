"""Obfuscation detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash"}

OBFUSCATION_RULES = [
    {"id": "OBF_HEX", "pattern": re.compile(r"\\x[0-9a-f]{2}(?:\\x[0-9a-f]{2}){4,}", re.I), "severity": "warn", "title": "Hex-encoded string (5+ bytes)"},
    {"id": "OBF_BASE64_EXEC", "pattern": re.compile(r"(?:atob|Buffer\.from)\s*\([^)]+\)[\s\S]{0,30}(?:eval|exec|spawn|Function)"), "severity": "critical", "title": "Base64 decode → execute chain"},
    {"id": "OBF_BASE64", "pattern": re.compile(r"atob\s*\(|Buffer\.from\s*\([^)]+,\s*['\"]base64['\"]"), "severity": "info", "title": "Base64 decoding"},
    {"id": "OBF_CHARCODE", "pattern": re.compile(r"String\.fromCharCode\s*\(\s*(?:\d+\s*,\s*){3,}"), "severity": "warn", "title": "Character code construction (4+ chars)"},
    {"id": "OBF_BASE64_BASH", "pattern": re.compile(r"base64\s+(-[dD]|--decode)\s*\|\s*(sh|bash)"), "severity": "critical", "title": "Base64 decode piped to shell"},
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
            for rule in OBFUSCATION_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="obfuscation",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Code obfuscation detected: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Review obfuscated code for malicious intent",
                        confidence=0.85,
                        rationale="Matches code obfuscation pattern",
                        exploit_precondition="Obfuscated code executes malicious payload",
                    ))

    return ScanResult("obfuscation_scanner", findings, files_scanned, time.time() - t0)
