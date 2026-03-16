"""Shared data models for aliclawscan."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Finding:
    """A single security finding."""

    rule_id: str
    category: str
    severity: str  # "critical" | "warn" | "info"
    title: str
    detail: str
    file_path: str = ""
    line: int = 0
    evidence: str = ""
    remediation: str = ""
    cwe: str = ""
    confidence: float = 1.0  # 0.0-1.0
    rationale: str = ""
    exploit_precondition: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ScanResult:
    """Result from a single scanner module."""

    scanner_name: str
    findings: list[Finding] = field(default_factory=list)
    files_scanned: int = 0
    duration_seconds: float = 0.0

    def to_dict(self) -> dict:
        return {
            "scanner_name": self.scanner_name,
            "findings": [f.to_dict() for f in self.findings],
            "files_scanned": self.files_scanned,
            "duration_seconds": self.duration_seconds,
        }


@dataclass
class AuditReport:
    """Complete audit report."""

    timestamp: str
    target_path: str
    scan_results: list[ScanResult] = field(default_factory=list)
    summary: dict = field(default_factory=dict)
    priority_ranking: list[Finding] = field(default_factory=list)
    conclusion: str = ""

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "target_path": self.target_path,
            "scan_results": [r.to_dict() for r in self.scan_results],
            "summary": self.summary,
            "priority_ranking": [f.to_dict() for f in self.priority_ranking],
            "conclusion": self.conclusion,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)
