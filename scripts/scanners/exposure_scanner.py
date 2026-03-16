"""Public network exposure risk scanner."""

from __future__ import annotations

import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".mts", ".cts"}

_BIND_ALL_PATTERN = re.compile(r"(?i)(0\.0\.0\.0|::|\[::\]|INADDR_ANY)")
_BIND_CONTEXT_PATTERN = re.compile(r"(?i)(listen|bind|createServer)")

_DEBUG_PATTERN = re.compile(r"(?i)(--inspect|--inspect-brk|--debug-port|debugger\s*;)")

_ROUTE_PATTERN = re.compile(
    r"(?i)(app\.(get|post|put|delete|patch|all)|router\.(get|post|put|delete|patch|all))"
    r"\s*\(\s*['\"][^'\"]+['\"]"
)
_AUTH_PATTERN = re.compile(r"(?i)(auth|middleware|protect|verify|authenticate)")
_UPNP_PATTERN = re.compile(r"(?i)(upnp|nat-pmp|natpmp|portMapping|addPortMapping)")
_MDNS_PATTERN = re.compile(r"(?i)(mdns|bonjour|multicastdns|\.local\b)")

EXPOSURE_RULES = [
    {
        "rule_id": "EXPOSE-001",
        "title": "Bind to All Interfaces",
        "severity": "warn",
        "cwe": "CWE-668",
        "category": "exposure",
        "remediation": "Bind to 127.0.0.1 or specific interface instead of 0.0.0.0",
    },
    {
        "rule_id": "EXPOSE-002",
        "title": "Debug Port Exposed",
        "severity": "warn",
        "cwe": "CWE-489",
        "category": "exposure",
        "remediation": "Remove debug flags from production configurations",
    },
    {
        "rule_id": "EXPOSE-003",
        "title": "Unauthenticated Endpoint",
        "severity": "info",
        "cwe": "CWE-306",
        "category": "exposure",
        "remediation": "Add authentication middleware to route handlers",
    },
    {
        "rule_id": "EXPOSE-004",
        "title": "UPnP/NAT-PMP Enabled",
        "severity": "critical",
        "cwe": "CWE-668",
        "category": "exposure",
        "remediation": "Disable UPnP/NAT-PMP to prevent automatic port forwarding",
    },
    {
        "rule_id": "EXPOSE-005",
        "title": "mDNS/Bonjour Broadcasting",
        "severity": "warn",
        "cwe": "CWE-200",
        "category": "exposure",
        "remediation": "Disable mDNS/Bonjour in production to prevent service discovery",
    },
]


def _has_bind_context(lines: list[str], line_idx: int) -> bool:
    """Check if listen/bind/createServer appears within ±5 lines of *line_idx*."""
    start = max(0, line_idx - 5)
    end = min(len(lines), line_idx + 6)
    for i in range(start, end):
        if _BIND_CONTEXT_PATTERN.search(lines[i]):
            return True
    return False


def _has_auth_reference(lines: list[str], line_idx: int) -> bool:
    """Check if auth-related references appear on the route line or adjacent lines."""
    start = max(0, line_idx - 2)
    end = min(len(lines), line_idx + 3)
    for i in range(start, end):
        if _AUTH_PATTERN.search(lines[i]):
            return True
    return False


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Scan code files under *root* for public network exposure risks."""
    start = time.monotonic()
    findings: list[Finding] = []
    files_scanned = 0

    seen: set[tuple[str, str]] = set()

    for path in walk_files(root, extensions=CODE_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(path)
        if not content:
            continue
        files_scanned += 1
        rel = str(path)
        lines = content.splitlines()

        for line_idx, line in enumerate(lines):
            line_no = line_idx + 1

            # EXPOSE-001: Bind to all interfaces
            dedup_001 = ("EXPOSE-001", rel)
            if dedup_001 not in seen and _BIND_ALL_PATTERN.search(line):
                if _has_bind_context(lines, line_idx):
                    seen.add(dedup_001)
                    rule = EXPOSURE_RULES[0]
                    findings.append(Finding(
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
                    ))

            # EXPOSE-002: Debug port exposed
            dedup_002 = ("EXPOSE-002", rel)
            if dedup_002 not in seen and _DEBUG_PATTERN.search(line):
                seen.add(dedup_002)
                rule = EXPOSURE_RULES[1]
                findings.append(Finding(
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
                ))

            # EXPOSE-003: Unauthenticated endpoint
            dedup_003 = ("EXPOSE-003", rel)
            if dedup_003 not in seen and _ROUTE_PATTERN.search(line):
                if not _has_auth_reference(lines, line_idx):
                    seen.add(dedup_003)
                    rule = EXPOSURE_RULES[2]
                    findings.append(Finding(
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
                    ))

            # EXPOSE-004: UPnP/NAT-PMP
            dedup_004 = ("EXPOSE-004", rel)
            if dedup_004 not in seen and _UPNP_PATTERN.search(line):
                seen.add(dedup_004)
                rule = EXPOSURE_RULES[3]
                findings.append(Finding(
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
                ))

            # EXPOSE-005: mDNS/Bonjour
            dedup_005 = ("EXPOSE-005", rel)
            if dedup_005 not in seen and _MDNS_PATTERN.search(line):
                seen.add(dedup_005)
                rule = EXPOSURE_RULES[4]
                findings.append(Finding(
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
                ))

    duration = time.monotonic() - start
    return ScanResult(
        scanner_name="exposure_scanner",
        findings=findings,
        files_scanned=files_scanned,
        duration_seconds=round(duration, 3),
    )
