"""Risk scoring engine for security findings."""

from __future__ import annotations

from scripts.models import Finding

SEVERITY_WEIGHTS = {
    "critical": 40,
    "warn": 20,
    "info": 5,
}

CATEGORY_MULTIPLIERS = {
    ("secrets", "exfiltration"): 2.2,
    ("obfuscation", "malicious-code"): 1.8,
    ("identity-hijacking",): 2.0,
    ("prompt-injection",): 1.5,
    ("pii-exposure", "exfiltration"): 3.0,
    ("cryptominer",): 2.5,
    ("ransomware",): 3.0,
    ("malicious-downloader",): 2.8,
    ("persistence",): 2.0,
}


def calculate_risk_score(findings: list[Finding]) -> dict:
    """Calculate overall risk score and verdict."""
    if not findings:
        return {"score": 0, "verdict": "SAFE", "breakdown": {}}

    # Base score
    base_score = 0.0
    for f in findings:
        weight = SEVERITY_WEIGHTS.get(f.severity, 5)
        base_score += weight * f.confidence

    # Category breakdown
    categories = {}
    for f in findings:
        categories[f.category] = categories.get(f.category, 0) + 1

    # Apply multipliers
    multiplier = 1.0
    category_set = set(categories.keys())
    for combo, mult in CATEGORY_MULTIPLIERS.items():
        if all(c in category_set for c in combo):
            multiplier = max(multiplier, mult)

    final_score = min(base_score * multiplier, 100)

    # Verdict
    if final_score < 30:
        verdict = "SAFE"
    elif final_score < 80:
        verdict = "SUSPICIOUS"
    else:
        verdict = "MALICIOUS"

    return {
        "score": round(final_score, 1),
        "verdict": verdict,
        "breakdown": categories,
        "multiplier": multiplier,
    }
