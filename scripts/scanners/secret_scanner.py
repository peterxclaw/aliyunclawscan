"""Hardcoded secret detection scanner."""

from __future__ import annotations

import math
import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, redact_secret, truncate_evidence, walk_files

CODE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".mts", ".cts", ".py", ".sh", ".bash", ".env"}

SECRET_RULES = [
    {"rule_id": "SECRET-001", "title": "AWS Access Key", "pattern": re.compile(r"AKIA[0-9A-Z]{16}"), "severity": "critical", "cwe": "CWE-798", "remediation": "Remove AWS key, rotate via IAM, use env vars"},
    {"rule_id": "SECRET-002", "title": "AWS Secret Key", "pattern": re.compile(r"(?i)aws_secret_access_key\s*[=:]\s*\S{20,}"), "severity": "critical", "cwe": "CWE-798", "remediation": "Remove AWS secret, rotate via IAM"},
    {"rule_id": "SECRET-003", "title": "Private Key", "pattern": re.compile(r"-----BEGIN\s+(RSA|EC|DSA|OPENSSH)\s+PRIVATE KEY-----"), "severity": "critical", "cwe": "CWE-321", "remediation": "Remove private key from source"},
    {"rule_id": "SECRET-004", "title": "JWT Token", "pattern": re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}"), "severity": "warn", "cwe": "CWE-522", "remediation": "Remove JWT token"},
    {"rule_id": "SECRET-005", "title": "Connection String", "pattern": re.compile(r"(?i)(mongodb|postgres|mysql|redis)://[^\s'\"]+@[^\s'\"]+"), "severity": "critical", "cwe": "CWE-798", "remediation": "Use env vars for connection strings"},
    {"rule_id": "SECRET-006", "title": "Generic Password", "pattern": re.compile(r"(?i)(password|passwd|secret|api_key|apikey|token)\s*[=:]\s*['\"][^'\"]{8,}['\"]"), "severity": "warn", "cwe": "CWE-798", "remediation": "Use env vars or secrets manager"},
    {"rule_id": "SECRET-008", "title": "SSH Key Path Access", "pattern": re.compile(r"~/\.ssh/id_[a-z]+|\.ssh/id_rsa|\.ssh/id_ed25519"), "severity": "critical", "cwe": "CWE-522", "remediation": "Avoid hardcoded SSH key paths; use SSH agent"},
    {"rule_id": "SECRET-009", "title": "AWS Credentials Path", "pattern": re.compile(r"~/\.aws/credentials|\.aws/config"), "severity": "critical", "cwe": "CWE-798", "remediation": "Use IAM roles instead of credential files"},
    {"rule_id": "SECRET-010", "title": "GitHub Token Path", "pattern": re.compile(r"~/\.config/gh/hosts\.yml"), "severity": "warn", "cwe": "CWE-522", "remediation": "Use GitHub App tokens with limited scope"},
    {"rule_id": "SECRET-011", "title": "Docker Config Path", "pattern": re.compile(r"~/\.docker/config\.json"), "severity": "warn", "cwe": "CWE-522", "remediation": "Use credential helpers instead of storing tokens"},
    {"rule_id": "SECRET-012", "title": "Kubernetes Config Path", "pattern": re.compile(r"~/\.kube/config"), "severity": "critical", "cwe": "CWE-522", "remediation": "Use service accounts or OIDC instead of kubeconfig"},
]


def is_test_file(path: Path) -> bool:
    """Check if file is a test file"""
    path_str = str(path).lower()
    return any(x in path_str for x in [".test.", ".spec.", "/tests/", "/__tests__/", "/fixtures/"])


def is_test_context(line: str, file_path: Path) -> bool:
    """Check if line is in a test context"""
    if is_test_file(file_path):
        return True
    line_lower = line.lower()
    test_keywords = ["test", "mock", "fixture", "dummy", "example", "sample", "fake", "stub"]
    return any(kw in line_lower for kw in test_keywords)


def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    ent = 0.0
    for cnt in counts.values():
        p = cnt / len(s)
        ent -= p * math.log2(p)
    return ent


def is_placeholder(value: str) -> bool:
    lower = value.lower()
    # Check for common placeholder patterns, but be specific to avoid false negatives
    if len(value) < 8:
        return "xxx" in lower or "test" in lower
    return any(p in lower for p in ["xxx", "your-", "change_me", "todo", "placeholder", "-example", "test-", "dummy", "${", "process.env", "<", ">"])


def is_type_annotation_line(line: str) -> bool:
    return any(t in line for t in [": string", ": number", "type ", "interface "])


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen_rules: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, CODE_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(fpath)
        if not content:
            continue
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            if is_type_annotation_line(line):
                continue
            for rule in SECRET_RULES:
                match = rule["pattern"].search(line)
                if match:
                    val = match.group(0)
                    if is_placeholder(val):
                        continue
                    if rule["rule_id"] == "SECRET-006":
                        if is_test_context(line, fpath):
                            continue
                    key = (rule["rule_id"], str(fpath))
                    if key in seen_rules:
                        continue
                    seen_rules.add(key)
                    findings.append(Finding(
                        rule_id=rule["rule_id"],
                        category="secrets",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Hardcoded secret detected: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(redact_secret(val)),
                        remediation=rule["remediation"],
                        cwe=rule["cwe"],
                    ))

            # SECRET-007: High entropy
            for match in re.finditer(r"['\"]([A-Za-z0-9+/=_-]{20,})['\"]", line):
                val = match.group(1)
                if is_placeholder(val) or shannon_entropy(val) <= 4.5:
                    continue
                key = ("SECRET-007", str(fpath))
                if key in seen_rules:
                    continue
                seen_rules.add(key)
                findings.append(Finding(
                    rule_id="SECRET-007",
                    category="secrets",
                    severity="info",
                    title="High-Entropy String",
                    detail="Potential secret with high entropy",
                    file_path=str(fpath.relative_to(root)),
                    line=i,
                    evidence=truncate_evidence(redact_secret(val)),
                    remediation="Review if this is a secret; use env vars if so",
                    cwe="CWE-798",
                ))

    return ScanResult("secret_scanner", findings, files_scanned, time.time() - t0)
