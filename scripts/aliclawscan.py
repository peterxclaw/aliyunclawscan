#!/usr/bin/env python3
"""aliclawscan — OpenClaw security scanner orchestrator."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Ensure the scripts package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.models import AuditReport, Finding, ScanResult
from scripts.report import write_report
from scripts.utils import parse_openclaw_audit_json, truncate_evidence
from scripts.scanners.secret_scanner import scan as scan_secrets
from scripts.scanners.config_scanner import scan as scan_config
from scripts.scanners.code_scanner import scan as scan_code
from scripts.scanners.dependency_scanner import scan as scan_deps
from scripts.scanners.exposure_scanner import scan as scan_exposure
from scripts.scanners.skill_scanner import scan as scan_skills
from scripts.scanners.prompt_injection_scanner import scan as scan_prompt_injection
from scripts.scanners.memory_poisoning_scanner import scan as scan_memory_poisoning
from scripts.scanners.identity_scanner import scan as scan_identity
from scripts.scanners.trust_scanner import scan as scan_trust
from scripts.scanners.obfuscation_scanner import scan as scan_obfuscation
from scripts.scanners.exfiltration_scanner import scan as scan_exfiltration
from scripts.scanners.financial_scanner import scan as scan_financial
from scripts.scanners.pii_scanner import scan as scan_pii
from scripts.scanners.mcp_security_scanner import scan as scan_mcp_security
from scripts.scanners.supply_chain_scanner import scan as scan_supply_chain
from scripts.scanners.cryptominer_scanner import scan as scan_cryptominer
from scripts.scanners.ransomware_scanner import scan as scan_ransomware
from scripts.scanners.downloader_scanner import scan as scan_downloader
from scripts.scanners.persistence_scanner import scan as scan_persistence
from scripts.risk_engine import calculate_risk_score

SEVERITY_ORDER = {"critical": 0, "warn": 1, "info": 2}


def run_openclaw_audit(target: Path) -> ScanResult:
    """Run `openclaw security audit --deep --json` and convert to ScanResult."""
    t0 = time.time()
    findings: list[Finding] = []
    try:
        result = subprocess.run(
            ["pnpm", "openclaw", "security", "audit", "--deep", "--json"],
            cwd=str(target),
            capture_output=True,
            text=True,
            timeout=120,
        )
        data = parse_openclaw_audit_json(result.stdout)
        for f in data.get("findings", []):
            sev = f.get("severity", "info")
            findings.append(
                Finding(
                    rule_id=f.get("checkId", "AUDIT-???"),
                    category="builtin-audit",
                    severity=sev,
                    title=f.get("title", ""),
                    detail=f.get("detail", ""),
                    remediation=f.get("remediation", ""),
                )
            )
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError) as exc:
        print(f"[WARN] openclaw audit skipped: {exc}", file=sys.stderr)

    return ScanResult(
        scanner_name="openclaw_builtin_audit",
        findings=findings,
        files_scanned=0,
        duration_seconds=time.time() - t0,
    )


def merge_and_dedup(results: list[ScanResult]) -> list[Finding]:
    """Merge findings from all scanners, deduplicate, sort by severity."""
    seen: set[tuple[str, str, int]] = set()
    merged: list[Finding] = []
    for sr in results:
        for f in sr.findings:
            key = (f.rule_id, f.file_path, f.line)
            if key not in seen:
                seen.add(key)
                merged.append(f)
    merged.sort(key=lambda f: (SEVERITY_ORDER.get(f.severity, 9), f.rule_id))
    return merged


def build_summary(findings: list[Finding]) -> dict:
    crit = sum(1 for f in findings if f.severity == "critical")
    warn = sum(1 for f in findings if f.severity == "warn")
    info = sum(1 for f in findings if f.severity == "info")
    return {"critical": crit, "warn": warn, "info": info, "total": crit + warn + info}


def filter_by_severity(findings: list[Finding], threshold: str) -> list[Finding]:
    max_order = SEVERITY_ORDER.get(threshold, 2)
    return [f for f in findings if SEVERITY_ORDER.get(f.severity, 9) <= max_order]


def main() -> None:
    parser = argparse.ArgumentParser(description="aliclawscan — OpenClaw security scanner")
    parser.add_argument("--target", type=Path, default=Path("."), help="Root directory to scan")
    parser.add_argument("--output", default="report", help="Output file base name")
    parser.add_argument("--format", choices=["markdown", "json", "both"], default="both")
    parser.add_argument(
        "--severity-threshold",
        choices=["info", "warn", "critical"],
        default="info",
        help="Minimum severity to include",
    )
    parser.add_argument("--skip-builtin", action="store_true", help="Skip openclaw audit")
    parser.add_argument("--exclude-tests", action="store_true", help="Exclude test files from scan")
    args = parser.parse_args()

    target = args.target.resolve()
    if not target.is_dir():
        print(f"[ERROR] Target directory not found: {target}", file=sys.stderr)
        sys.exit(1)

    print(f"[aliclawscan] Scanning {target} ...")

    results: list[ScanResult] = []

    # 1. Built-in audit
    if not args.skip_builtin:
        print("  → Running openclaw built-in audit ...")
        results.append(run_openclaw_audit(target))

    # 2. Run all scanners
    scanners = [
        ("secret_scanner", scan_secrets),
        ("config_scanner", scan_config),
        ("code_scanner", scan_code),
        ("dependency_scanner", scan_deps),
        ("exposure_scanner", scan_exposure),
        ("skill_scanner", scan_skills),
        ("prompt_injection_scanner", scan_prompt_injection),
        ("memory_poisoning_scanner", scan_memory_poisoning),
        ("identity_scanner", scan_identity),
        ("trust_scanner", scan_trust),
        ("obfuscation_scanner", scan_obfuscation),
        ("exfiltration_scanner", scan_exfiltration),
        ("financial_scanner", scan_financial),
        ("pii_scanner", scan_pii),
        ("mcp_security_scanner", scan_mcp_security),
        ("supply_chain_scanner", scan_supply_chain),
        ("cryptominer_scanner", scan_cryptominer),
        ("ransomware_scanner", scan_ransomware),
        ("downloader_scanner", scan_downloader),
        ("persistence_scanner", scan_persistence),
    ]
    for name, scan_fn in scanners:
        print(f"  → Running {name} ...")
        results.append(scan_fn(target, exclude_tests=args.exclude_tests))

    # 3. Merge and filter
    all_findings = merge_and_dedup(results)
    filtered = filter_by_severity(all_findings, args.severity_threshold)

    # 4. Calculate risk score
    risk_score = calculate_risk_score(filtered)

    # 5. Build report
    summary = build_summary(filtered)
    summary["risk_score"] = risk_score["score"]
    summary["verdict"] = risk_score["verdict"]
    summary["category_breakdown"] = risk_score["breakdown"]

    report = AuditReport(
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        target_path=str(target),
        scan_results=results,
        summary=summary,
        priority_ranking=filtered,
    )

    # 5. Write output
    output_dir = Path(__file__).resolve().parent.parent
    written = write_report(report, args.output, args.format, output_dir)
    for p in written:
        print(f"  ✓ Written: {p}")

    s = report.summary
    print(
        f"\n[aliclawscan] Done. "
        f"Risk Score: {s.get('risk_score', 0)}/100 ({s.get('verdict', 'UNKNOWN')}) | "
        f"Critical: {s['critical']}, Warn: {s['warn']}, Info: {s['info']}, "
        f"Total: {s['total']}"
    )

    if s["critical"] > 0:
        sys.exit(2)


if __name__ == "__main__":
    main()
