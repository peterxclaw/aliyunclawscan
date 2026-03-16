"""Tests for code_scanner."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.scanners.code_scanner import scan


def test_scan_clean_file():
    """Test scanning clean file."""
    fixtures = Path(__file__).parent / "fixtures"
    result = scan(fixtures)
    clean_findings = [f for f in result.findings if "clean_sample.ts" in f.file_path]
    assert len(clean_findings) == 0, f"Expected 0 findings in clean file, got {len(clean_findings)}"
    print("✓ test_scan_clean_file passed")


def test_scan_injection_file():
    """Test scanning file with injection vulnerabilities."""
    fixtures = Path(__file__).parent / "fixtures"
    result = scan(fixtures)
    injection_findings = [f for f in result.findings if "injection_sample.ts" in f.file_path]
    assert len(injection_findings) > 0, "Expected findings in injection file"

    rule_ids = {f.rule_id for f in injection_findings}
    assert "INJECT-001" in rule_ids, "Expected command injection detection"
    assert "INJECT-002" in rule_ids, "Expected eval detection"
    assert "INJECT-006" in rule_ids, "Expected innerHTML detection"

    print(f"✓ test_scan_injection_file passed ({len(injection_findings)} findings)")


if __name__ == "__main__":
    test_scan_clean_file()
    test_scan_injection_file()
    print("\n✅ All code_scanner tests passed")
