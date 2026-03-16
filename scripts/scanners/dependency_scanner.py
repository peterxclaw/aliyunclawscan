"""Dependency vulnerability scanner.

Checks for known CVEs (DEP-001), outdated packages (DEP-002),
and phantom dependencies (DEP-003) using pnpm tooling.
"""

from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path

from ..models import Finding, ScanResult
from ..utils import truncate_evidence

_SEVERITY_MAP = {
    "critical": "critical",
    "high": "critical",
    "moderate": "warn",
    "low": "info",
}

_IMPORT_RE = re.compile(
    r'(?:from\s+["\']|require\s*\(\s*["\']|import\s+["\']|import\s+\w+\s+from\s+["\'])'
    r"([^./\"'][^\"']*)[\"']",
)

_SOURCE_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".mts", ".cts"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _run_cmd(cmd: list[str], cwd: Path) -> tuple[str, int]:
    """Run *cmd* with a 60-second timeout, returning (stdout, returncode)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.stdout, result.returncode
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return "", -1


def _parse_advisories(data: dict | list) -> list[dict]:
    """Normalise pnpm audit JSON into a flat list of advisory dicts.

    pnpm audit may return:
      - ``{"advisories": {id: {...}, ...}}``  (npm v6-style)
      - a flat list of vulnerability objects     (newer pnpm)
      - ``{"vulnerabilities": {pkg: {...}, ...}}`` (npm v7+ style)
    """
    advisories: list[dict] = []

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        # npm v6 / pnpm classic format
        if "advisories" in data and isinstance(data["advisories"], dict):
            advisories.extend(data["advisories"].values())
        # npm v7+ / pnpm modern format
        elif "vulnerabilities" in data and isinstance(data["vulnerabilities"], dict):
            for pkg_name, vuln in data["vulnerabilities"].items():
                advisories.append({
                    "module_name": pkg_name,
                    "severity": vuln.get("severity", "info"),
                    "title": vuln.get("title", vuln.get("name", pkg_name)),
                    "findings": vuln.get("via", []),
                    "range": vuln.get("range", ""),
                    "fix_available": vuln.get("fixAvailable", None),
                })
        # Fallback: maybe the dict itself is a single advisory
        elif "module_name" in data or "name" in data:
            advisories.append(data)

    return advisories


def _collect_source_imports(root: Path) -> set[str]:
    """Scan source files for bare-specifier imports (simple heuristic)."""
    packages: set[str] = set()
    src_dir = root / "src"
    search_roots = [src_dir] if src_dir.is_dir() else [root]

    for search_root in search_roots:
        for path in search_root.rglob("*"):
            if not path.is_file() or path.suffix not in _SOURCE_EXTENSIONS:
                continue
            if "node_modules" in path.parts:
                continue
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for match in _IMPORT_RE.finditer(content):
                specifier = match.group(1)
                # Normalise scoped packages: @scope/pkg/sub → @scope/pkg
                if specifier.startswith("@"):
                    parts = specifier.split("/")
                    pkg = "/".join(parts[:2]) if len(parts) >= 2 else specifier
                else:
                    pkg = specifier.split("/")[0]
                packages.add(pkg)

    return packages


# ---------------------------------------------------------------------------
# Main scan
# ---------------------------------------------------------------------------


def scan(root: Path, exclude_tests: bool = False) -> ScanResult:
    """Run dependency checks and return findings."""
    start = time.monotonic()
    findings: list[Finding] = []

    # ── DEP-001: Known CVE vulnerabilities ──────────────────────────────
    stdout, rc = _run_cmd(["pnpm", "audit", "--json"], root)
    if stdout:
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError:
            data = {}

        for adv in _parse_advisories(data):
            pkg = adv.get("module_name") or adv.get("name", "unknown")
            raw_sev = str(adv.get("severity", "info")).lower()
            severity = _SEVERITY_MAP.get(raw_sev, "info")
            title = adv.get("title", "Vulnerability")
            cve = adv.get("cves", adv.get("cve", ""))
            if isinstance(cve, list):
                cve = cve[0] if cve else ""
            version = adv.get("vulnerable_versions") or adv.get("range", "")
            recommendation = adv.get("recommendation") or ""
            fix = adv.get("fix_available")
            if fix and isinstance(fix, dict):
                recommendation = recommendation or f"upgrade to {fix.get('name', '')}@{fix.get('version', '')}"

            findings.append(Finding(
                rule_id="DEP-001",
                category="dependency",
                severity=severity,
                title=f"Known vulnerability in {pkg}: {title}",
                detail=f"Package {pkg} ({version}) has a known vulnerability.",
                evidence=truncate_evidence(f"{pkg}@{version}: {title}"),
                remediation=recommendation or "Upgrade to a patched version.",
                cwe=str(cve),
            ))

    # ── DEP-002: Outdated dependencies ──────────────────────────────────
    stdout, rc = _run_cmd(["pnpm", "outdated", "--json"], root)
    if stdout:
        try:
            outdated_data = json.loads(stdout)
        except json.JSONDecodeError:
            outdated_data = {}

        # pnpm outdated --json returns {pkg: {current, latest, wanted, ...}}
        if isinstance(outdated_data, dict):
            for pkg, info in outdated_data.items():
                if not isinstance(info, dict):
                    continue
                current = str(info.get("current", "0.0.0"))
                latest = str(info.get("latest", "0.0.0"))
                try:
                    cur_major = int(current.split(".")[0])
                    lat_major = int(latest.split(".")[0])
                except (ValueError, IndexError):
                    continue
                if lat_major - cur_major >= 2:
                    findings.append(Finding(
                        rule_id="DEP-002",
                        category="dependency",
                        severity="warn",
                        title=f"Outdated dependency: {pkg}",
                        detail=(
                            f"{pkg} is {lat_major - cur_major} major versions behind "
                            f"(current: {current}, latest: {latest})."
                        ),
                        evidence=truncate_evidence(f"{pkg}: {current} → {latest}"),
                        remediation=f"Upgrade {pkg} to {latest}.",
                    ))

    # ── DEP-003: Phantom dependencies ───────────────────────────────────
    pkg_json_path = root / "package.json"
    if pkg_json_path.is_file():
        try:
            pkg_data = json.loads(pkg_json_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pkg_data = {}

        declared: set[str] = set()
        for dep_key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
            declared.update(pkg_data.get(dep_key, {}).keys())

        # Node built-in modules to ignore
        builtins = {
            "assert", "buffer", "child_process", "cluster", "console",
            "constants", "crypto", "dgram", "dns", "domain", "events",
            "fs", "http", "http2", "https", "module", "net", "os",
            "path", "perf_hooks", "process", "punycode", "querystring",
            "readline", "repl", "stream", "string_decoder", "sys",
            "timers", "tls", "tty", "url", "util", "v8", "vm", "wasi",
            "worker_threads", "zlib", "node",
        }

        imported = _collect_source_imports(root)
        phantoms = imported - declared - builtins
        # Filter out node: protocol prefixed and relative-looking specifiers
        phantoms = {p for p in phantoms if not p.startswith("node:")}

        for pkg in sorted(phantoms):
            findings.append(Finding(
                rule_id="DEP-003",
                category="dependency",
                severity="info",
                title=f"Possible phantom dependency: {pkg}",
                detail=(
                    f"'{pkg}' is imported in source but not listed in package.json. "
                    "It may be provided transitively."
                ),
                evidence=truncate_evidence(f"import from '{pkg}' not in package.json"),
                remediation=f"Add {pkg} to dependencies or verify it is intentionally transitive.",
            ))

    elapsed = time.monotonic() - start
    return ScanResult(
        scanner_name="dependency_scanner",
        findings=findings,
        duration_seconds=round(elapsed, 3),
    )
