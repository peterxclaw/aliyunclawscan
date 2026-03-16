"""Report generation for aliclawscan — Markdown and JSON output."""

from __future__ import annotations

from pathlib import Path

from .models import AuditReport, Finding
from .utils import is_test_file

SEVERITY_ORDER = {"critical": 0, "warn": 1, "info": 2}


def _severity_badge(sev: str) -> str:
    return {"critical": "🔴 CRITICAL", "warn": "🟡 WARN", "info": "🔵 INFO"}.get(
        sev, sev.upper()
    )


def generate_markdown(report: AuditReport) -> str:
    """Generate a Markdown security report."""
    lines: list[str] = []
    w = lines.append

    w("# OpenClaw Security Scan Report")
    w("")
    w(f"**Scan Date:** {report.timestamp}")
    w(f"**Target:** `{report.target_path}`")
    w("")

    # Summary table
    total = len(report.priority_ranking)
    crit = sum(1 for f in report.priority_ranking if f.severity == "critical")
    warn = sum(1 for f in report.priority_ranking if f.severity == "warn")
    info = sum(1 for f in report.priority_ranking if f.severity == "info")

    w("## Summary")
    w("")

    # Risk score
    risk_score = report.summary.get("risk_score", 0)
    verdict = report.summary.get("verdict", "UNKNOWN")
    verdict_emoji = {"SAFE": "✅", "SUSPICIOUS": "⚠️", "MALICIOUS": "🚨"}.get(verdict, "❓")

    w(f"**Risk Score:** {risk_score}/100 {verdict_emoji} **{verdict}**")
    w("")

    w(f"| Severity | Count |")
    w(f"|----------|-------|")
    w(f"| 🔴 Critical | {crit} |")
    w(f"| 🟡 Warn | {warn} |")
    w(f"| 🔵 Info | {info} |")
    w(f"| **Total** | **{total}** |")
    w("")

    # Category breakdown
    category_breakdown = report.summary.get("category_breakdown", {})
    if category_breakdown:
        w("### Threat Categories Detected")
        w("")
        for cat, count in sorted(category_breakdown.items(), key=lambda x: -x[1]):
            w(f"- **{cat}**: {count} finding(s)")
        w("")

    # File type distribution
    test_findings = [f for f in report.priority_ranking if is_test_file(Path(f.file_path))]
    prod_findings = [f for f in report.priority_ranking if not is_test_file(Path(f.file_path))]

    if total > 0:
        w("## File Type Distribution")
        w("")
        w("| Type | Findings | Percentage |")
        w("|------|----------|------------|")
        w(f"| Production Code | {len(prod_findings)} | {len(prod_findings)/total*100:.1f}% |")
        w(f"| Test Code | {len(test_findings)} | {len(test_findings)/total*100:.1f}% |")
        w("")

    # Scan coverage
    w("## Scan Coverage")
    w("")
    w("| Scanner | Files Scanned | Findings | Duration |")
    w("|---------|--------------|----------|----------|")
    for sr in report.scan_results:
        w(
            f"| {sr.scanner_name} | {sr.files_scanned} "
            f"| {len(sr.findings)} | {sr.duration_seconds:.1f}s |"
        )
    w("")

    # Detailed findings by priority
    w("## Findings")
    w("")
    if not report.priority_ranking:
        w("No security findings detected. ✅")
        w("")
    else:
        for i, f in enumerate(report.priority_ranking, 1):
            test_marker = " ⚠️ Test File" if is_test_file(Path(f.file_path)) else ""
            w(f"### {i}. [{f.rule_id}] {f.title}{test_marker}")
            w("")
            w(f"**Severity:** {_severity_badge(f.severity)}")
            if f.cwe:
                w(f"  |  **CWE:** {f.cwe}")
            w("")
            w(f"**Detail:** {f.detail}")
            w("")
            if f.file_path:
                loc = f"`{f.file_path}"
                if f.line:
                    loc += f":{f.line}"
                loc += "`"
                w(f"**Location:** {loc}")
                w("")
            if f.evidence:
                w(f"**Evidence:** `{f.evidence}`")
                w("")
            if f.remediation:
                w(f"**Remediation:** {f.remediation}")
                w("")
            w("---")
            w("")

    # Conclusion
    w("## Conclusion")
    w("")
    w(report.conclusion or _default_conclusion(crit, warn, info))
    w("")

    return "\n".join(lines)


def _default_conclusion(crit: int, warn: int, info: int) -> str:
    total = crit + warn + info
    if total == 0:
        return "No security issues detected. The codebase appears clean."
    parts = []
    if crit:
        parts.append(f"{crit} critical issue(s) requiring immediate attention")
    if warn:
        parts.append(f"{warn} warning(s) that should be reviewed")
    if info:
        parts.append(f"{info} informational finding(s)")
    return (
        f"Scan completed with {total} total findings: "
        + "; ".join(parts)
        + ". Address critical issues before deployment."
    )


def generate_json(report: AuditReport) -> str:
    """Generate JSON report."""
    return report.to_json(indent=2)


def write_report(
    report: AuditReport,
    output_base: str,
    fmt: str = "both",
    output_dir: Path | None = None,
) -> list[Path]:
    """Write report files. Returns list of written paths."""
    base_dir = output_dir or Path(".")
    written: list[Path] = []

    if fmt in ("markdown", "both"):
        md_path = base_dir / f"{output_base}.md"
        md_path.write_text(generate_markdown(report), encoding="utf-8")
        written.append(md_path)

    if fmt in ("json", "both"):
        json_path = base_dir / f"{output_base}.json"
        json_path.write_text(generate_json(report), encoding="utf-8")
        written.append(json_path)

    return written
