"""Tests for report generation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.models import AuditReport, Finding, ScanResult
from scripts.report import generate_markdown, generate_json


def test_generate_markdown():
    """Test Markdown report generation."""
    findings = [
        Finding("SECRET-001", "secrets", "critical", "AWS Key", "Hardcoded AWS key", "file.ts", 10, "AKIA***", "Rotate key"),
        Finding("CONFIG-001", "config", "warn", "Debug Mode", "Debug enabled", "config.json", 5, "debug: true", "Disable debug"),
    ]
    report = AuditReport(
        timestamp="2026-03-12 00:00:00 UTC",
        target_path="/test",
        scan_results=[ScanResult("test_scanner", findings, 2, 1.0)],
        summary={"critical": 1, "warn": 1, "info": 0, "total": 2},
        priority_ranking=findings,
    )

    md = generate_markdown(report)
    assert "# OpenClaw Security Scan Report" in md
    assert "SECRET-001" in md
    assert "CONFIG-001" in md
    assert "🔴 CRITICAL" in md
    assert "🟡 WARN" in md
    print("✓ test_generate_markdown passed")


def test_generate_json():
    """Test JSON report generation."""
    findings = [Finding("TEST-001", "test", "info", "Test", "Detail")]
    report = AuditReport(
        timestamp="2026-03-12 00:00:00 UTC",
        target_path="/test",
        scan_results=[ScanResult("test", findings, 1, 0.5)],
        summary={"critical": 0, "warn": 0, "info": 1, "total": 1},
        priority_ranking=findings,
    )

    json_str = generate_json(report)
    assert '"timestamp"' in json_str
    assert '"TEST-001"' in json_str
    print("✓ test_generate_json passed")


if __name__ == "__main__":
    test_generate_markdown()
    test_generate_json()
    print("\n✅ All report tests passed")
