"""Tests for secret_scanner."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.scanners.secret_scanner import scan, shannon_entropy, is_placeholder, is_type_annotation_line


def test_shannon_entropy():
    """Test entropy calculation."""
    assert shannon_entropy("aaaa") < 1.0
    assert shannon_entropy("abcdefgh12345678") > 3.0
    print("✓ test_shannon_entropy passed")


def test_is_placeholder():
    """Test placeholder detection."""
    assert is_placeholder("xxx")
    assert is_placeholder("your-key-here")
    assert is_placeholder("CHANGE_ME")
    assert is_placeholder("${API_KEY}")
    assert is_placeholder("process.env.SECRET")
    assert not is_placeholder("AKIAIOSFODNN7EXAMPLE")
    print("✓ test_is_placeholder passed")


def test_is_type_annotation_line():
    """Test type annotation detection."""
    assert is_type_annotation_line("const key: string = 'value'")
    assert is_type_annotation_line("interface Config {")
    assert is_type_annotation_line("type ApiKey = string")
    assert not is_type_annotation_line("const key = 'AKIAIOSFODNN7EXAMPLE'")
    print("✓ test_is_type_annotation_line passed")


def test_scan_clean_file():
    """Test scanning clean file."""
    fixtures = Path(__file__).parent / "fixtures"
    result = scan(fixtures)
    clean_findings = [f for f in result.findings if "clean_sample.ts" in f.file_path]
    assert len(clean_findings) == 0, f"Expected 0 findings in clean file, got {len(clean_findings)}"
    print("✓ test_scan_clean_file passed")


def test_scan_secrets_file():
    """Test scanning file with secrets."""
    fixtures = Path(__file__).parent / "fixtures"
    result = scan(fixtures)
    secret_findings = [f for f in result.findings if "secrets_sample.ts" in f.file_path]
    assert len(secret_findings) > 0, "Expected findings in secrets file"

    rule_ids = {f.rule_id for f in secret_findings}
    assert "SECRET-001" in rule_ids, "Expected AWS key detection"
    assert "SECRET-005" in rule_ids, "Expected connection string detection"

    # Check evidence redaction
    for f in secret_findings:
        if f.evidence:
            assert "***" in f.evidence, f"Evidence should be redacted: {f.evidence}"

    print(f"✓ test_scan_secrets_file passed ({len(secret_findings)} findings)")


if __name__ == "__main__":
    test_shannon_entropy()
    test_is_placeholder()
    test_is_type_annotation_line()
    test_scan_clean_file()
    test_scan_secrets_file()
    print("\n✅ All secret_scanner tests passed")
