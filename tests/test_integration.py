"""Integration test for new scanners."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.scanners.prompt_injection_scanner import scan as scan_pi
from scripts.scanners.memory_poisoning_scanner import scan as scan_mp
from scripts.scanners.obfuscation_scanner import scan as scan_obf
from scripts.scanners.pii_scanner import scan as scan_pii
from scripts.risk_engine import calculate_risk_score


def test_new_scanners():
    """Test that new scanners are functional."""
    root = Path(__file__).parent.parent.parent.parent

    print("Testing new scanners...")

    # Test prompt injection scanner
    result = scan_pi(root, exclude_tests=True)
    print(f"✓ Prompt Injection Scanner: {len(result.findings)} findings in {result.duration_seconds:.1f}s")

    # Test memory poisoning scanner
    result = scan_mp(root, exclude_tests=True)
    print(f"✓ Memory Poisoning Scanner: {len(result.findings)} findings in {result.duration_seconds:.1f}s")

    # Test obfuscation scanner
    result = scan_obf(root, exclude_tests=True)
    print(f"✓ Obfuscation Scanner: {len(result.findings)} findings in {result.duration_seconds:.1f}s")

    # Test PII scanner
    result = scan_pii(root, exclude_tests=True)
    print(f"✓ PII Scanner: {len(result.findings)} findings in {result.duration_seconds:.1f}s")

    # Test risk engine
    from scripts.models import Finding
    test_findings = [
        Finding("TEST-001", "secrets", "critical", "Test", "Test", confidence=0.9),
        Finding("TEST-002", "exfiltration", "warn", "Test", "Test", confidence=0.8),
    ]
    risk = calculate_risk_score(test_findings)
    print(f"✓ Risk Engine: score={risk['score']}, verdict={risk['verdict']}, multiplier={risk['multiplier']}")

    print("\n✅ All new scanners operational!")


if __name__ == "__main__":
    test_new_scanners()
