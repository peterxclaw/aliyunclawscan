"""Tests for aliclawscan main orchestrator."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.aliclawscan import merge_and_dedup, build_summary, filter_by_severity
from scripts.models import Finding, ScanResult


def test_merge_and_dedup():
    """Test merging and deduplication of findings."""
    f1 = Finding("SECRET-001", "secrets", "critical", "AWS Key", "detail", "file.ts", 10, "evidence")
    f2 = Finding("SECRET-001", "secrets", "critical", "AWS Key", "detail", "file.ts", 10, "evidence")  # dup
    f3 = Finding("CONFIG-001", "config", "warn", "Debug Mode", "detail", "config.json", 5, "evidence")

    r1 = ScanResult("scanner1", [f1, f2], 1, 0.1)
    r2 = ScanResult("scanner2", [f3], 1, 0.1)

    merged = merge_and_dedup([r1, r2])
    assert len(merged) == 2, f"Expected 2 findings, got {len(merged)}"
    assert merged[0].severity == "critical"
    assert merged[1].severity == "warn"
    print("✓ test_merge_and_dedup passed")


def test_build_summary():
    """Test summary building."""
    findings = [
        Finding("A", "cat", "critical", "t", "d"),
        Finding("B", "cat", "critical", "t", "d"),
        Finding("C", "cat", "warn", "t", "d"),
        Finding("D", "cat", "info", "t", "d"),
    ]
    summary = build_summary(findings)
    assert summary["critical"] == 2
    assert summary["warn"] == 1
    assert summary["info"] == 1
    assert summary["total"] == 4
    print("✓ test_build_summary passed")


def test_filter_by_severity():
    """Test severity filtering."""
    findings = [
        Finding("A", "cat", "critical", "t", "d"),
        Finding("B", "cat", "warn", "t", "d"),
        Finding("C", "cat", "info", "t", "d"),
    ]

    crit_only = filter_by_severity(findings, "critical")
    assert len(crit_only) == 1

    warn_up = filter_by_severity(findings, "warn")
    assert len(warn_up) == 2

    all_findings = filter_by_severity(findings, "info")
    assert len(all_findings) == 3
    print("✓ test_filter_by_severity passed")


if __name__ == "__main__":
    test_merge_and_dedup()
    test_build_summary()
    test_filter_by_severity()
    print("\n✅ All aliclawscan tests passed")
