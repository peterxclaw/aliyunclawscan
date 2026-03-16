"""Data exfiltration detection scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash"}
ALL_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".sh", ".bash", ".md", ".txt"}

EXFILTRATION_RULES = [
    {"id": "EXFIL_WEBHOOK", "pattern": re.compile(r"webhook\.site|requestbin\.com|hookbin\.com|pipedream\.net", re.I), "severity": "critical", "title": "Known exfiltration endpoint", "code_only": False},
    {"id": "EXFIL_POST", "pattern": re.compile(r"(?:method:\s*['\"]POST['\"]|\.post\s*\()\s*[^\n]*(?:secret|token|key|cred|env|password)", re.I), "severity": "warn", "title": "POST with sensitive data", "code_only": True},
    {"id": "EXFIL_CURL_DATA", "pattern": re.compile(r"curl\s+[^\n]*(?:-d|--data)\s+[^\n]*(?:\$|env|key|token|secret)", re.I), "severity": "warn", "title": "curl exfiltration of secrets", "code_only": False},
    {"id": "EXFIL_DNS", "pattern": re.compile(r"dns\.resolve|nslookup\s+.*\$|dig\s+.*\$"), "severity": "warn", "title": "DNS-based exfiltration", "code_only": True},
]


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, ALL_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(fpath)
        if not content:
            continue

        is_code = fpath.suffix in CODE_EXTENSIONS
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            for rule in EXFILTRATION_RULES:
                if rule["code_only"] and not is_code:
                    continue

                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="exfiltration",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Data exfiltration risk: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Remove exfiltration endpoints and review data transmission",
                        confidence=0.9,
                        rationale="Matches data exfiltration pattern",
                        exploit_precondition="Sensitive data transmitted to external endpoint",
                    ))

    return ScanResult("exfiltration_scanner", findings, files_scanned, time.time() - t0)
