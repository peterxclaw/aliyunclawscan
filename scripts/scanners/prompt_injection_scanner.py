"""Prompt injection detection scanner."""

from __future__ import annotations

import base64
import re
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import read_file_safe, truncate_evidence, walk_files

DOC_EXTENSIONS = {".md", ".txt", ".mdx"}
ALL_EXTENSIONS = {".md", ".txt", ".mdx", ".ts", ".tsx", ".js", ".jsx", ".py", ".sh"}

PROMPT_INJECTION_RULES = [
    {"id": "PI_IGNORE", "pattern": re.compile(r"ignore\s+(all\s+)?previous\s+instructions|disregard\s+(all\s+)?prior", re.I), "severity": "critical", "title": "Prompt injection: ignore instructions", "doc_only": True},
    {"id": "PI_ROLE", "pattern": re.compile(r"you\s+are\s+(now|actually)|your\s+new\s+role|forget\s+your\s+(rules|instructions)", re.I), "severity": "critical", "title": "Prompt injection: role override", "doc_only": True},
    {"id": "PI_SYSTEM", "pattern": re.compile(r"\[SYSTEM\]|<system>|<<SYS>>|system:\s*you\s+are", re.I), "severity": "critical", "title": "Prompt injection: system message impersonation", "doc_only": True},
    {"id": "PI_ZWSP", "pattern": re.compile(r"[\u200b\u200c\u200d\u2060\ufeff]"), "severity": "critical", "title": "Zero-width Unicode (hidden text)", "doc_only": False},
    {"id": "PI_BIDI", "pattern": re.compile(r"[\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069]"), "severity": "critical", "title": "Unicode BiDi control character", "doc_only": False},
    {"id": "PI_INVISIBLE", "pattern": re.compile(r"[\u00ad\u034f\u061c\u180e\u2000-\u200f\u2028-\u202f\u205f-\u2064\u206a-\u206f\u3000](?!\ufe0f)"), "severity": "warn", "title": "Invisible/formatting Unicode", "doc_only": False},
    {"id": "PI_HOMOGLYPH", "pattern": re.compile(r"[а-яА-Я].*[a-zA-Z]|[a-zA-Z].*[а-яА-Я]"), "severity": "warn", "title": "Cyrillic/Latin homoglyph mixing", "doc_only": False},
    {"id": "PI_TAG_INJECTION", "pattern": re.compile(r"</?(?:system|user|assistant|human|tool_call|function_call|antml|anthropic)[>\s]", re.I), "severity": "critical", "title": "XML/tag-based prompt injection", "doc_only": False},
    {"id": "PI_BASE64_MD", "pattern": re.compile(r"(?:run|execute|eval|decode)\s+(?:this\s+)?base64", re.I), "severity": "critical", "title": "Base64 execution instruction", "doc_only": True},
    {"id": "PI_HEX_ENCODED", "pattern": re.compile(r"\\x[0-9a-f]{2}(?:\\x[0-9a-f]{2}){10,}", re.I), "severity": "warn", "title": "Hex-encoded payload (10+ bytes)", "doc_only": False},
]

_BASE64_PATTERN = re.compile(r"[A-Za-z0-9+/]{20,}={0,2}")

def _check_base64_payload(content: str) -> bool:
    """Check if base64 string decodes to suspicious content"""
    try:
        decoded = base64.b64decode(content, validate=True).decode('utf-8', errors='ignore')
        suspicious = ["ignore", "system", "assistant", "eval", "exec", "<system>", "you are"]
        return any(s in decoded.lower() for s in suspicious)
    except Exception:
        return False


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    t0 = time.time()
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()
    files_scanned = 0

    for fpath in walk_files(root, ALL_EXTENSIONS, exclude_tests=exclude_tests):
        content = read_file_safe(fpath)
        if not content:
            continue

        is_doc = fpath.suffix in DOC_EXTENSIONS
        files_scanned += 1
        lines = content.splitlines()

        for i, line in enumerate(lines, 1):
            for rule in PROMPT_INJECTION_RULES:
                if rule["doc_only"] and not is_doc:
                    continue

                match = rule["pattern"].search(line)
                if match:
                    key = (rule["id"], str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)

                    findings.append(Finding(
                        rule_id=rule["id"],
                        category="prompt-injection",
                        severity=rule["severity"],
                        title=rule["title"],
                        detail=f"Prompt injection pattern detected: {rule['title']}",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(line.strip()),
                        remediation="Sanitize input, remove dynamic evaluation, or restrict execution scope",
                        confidence=0.95,
                        rationale="Matches known prompt injection syntax",
                        exploit_precondition="Agent executes payload in vulnerable context",
                    ))

            # Check for base64-encoded injection payloads
            for match in _BASE64_PATTERN.finditer(line):
                if _check_base64_payload(match.group(0)):
                    key = ("PI_BASE64_PAYLOAD", str(fpath))
                    if key in seen:
                        continue
                    seen.add(key)
                    findings.append(Finding(
                        rule_id="PI_BASE64_PAYLOAD",
                        category="prompt-injection",
                        severity="critical",
                        title="Base64-encoded injection payload",
                        detail="Base64 string decodes to prompt injection content",
                        file_path=str(fpath.relative_to(root)),
                        line=i,
                        evidence=truncate_evidence(match.group(0)[:50] + "..."),
                        remediation="Remove or sanitize base64-encoded injection attempts",
                        confidence=0.90,
                        rationale="Base64 decodes to known injection patterns",
                        exploit_precondition="Decoded payload executed by agent",
                    ))

    return ScanResult("prompt_injection_scanner", findings, files_scanned, time.time() - t0)
