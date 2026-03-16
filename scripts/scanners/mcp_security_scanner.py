"""MCP security scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".json"}

MCP_RULES = [
    {"id": "MCP_TOOL_POISON", "pattern": re.compile(r"mcp.*tool.*(?:override|replace|hijack)", re.I), "severity": "critical", "title": "MCP tool poisoning"},
    {"id": "MCP_SSRF", "pattern": re.compile(r"mcp.*(?:fetch|request).*\$\{", re.I), "severity": "warn", "title": "MCP SSRF via dynamic URL"},
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
            for rule in MCP_RULES:
                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="mcp-security",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"MCP security issue: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Review MCP tool configuration for security issues",
                        confidence=0.7,
                        rationale="Matches MCP security pattern",
                        exploit_precondition="MCP tool executes malicious operations",
                    ))

    return ScanResult("mcp_security_scanner", findings, files_scanned, time.time() - t0)
