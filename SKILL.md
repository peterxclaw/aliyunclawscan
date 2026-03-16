---
name: aliclawscan
description: Comprehensive security scanner for OpenClaw with 400+ threat patterns covering OWASP Agentic Security Top 10. Detects secrets, prompt injection, memory poisoning, identity hijacking, code injection, PII exposure, obfuscation, exfiltration, financial access, MCP security issues, supply chain risks, cryptominers, ransomware, malicious downloaders, and persistence mechanisms. Includes risk scoring engine (0-100) with SAFE/SUSPICIOUS/MALICIOUS verdicts. Use for security scans, audits, vulnerability assessments, or risk analysis.
---

# aliclawscan — OpenClaw Security Scanner

## When to Use

- User asks for a security scan, audit, or vulnerability assessment
- Before a major release or deployment
- After adding new channels, skills, or dependencies
- Periodic security health checks

## Workflow

### Step 1: Run Built-in Audit

Execute the OpenClaw built-in security audit first:

```bash
cd <project-root>
pnpm openclaw security audit --deep --json > /tmp/openclaw-audit.json
```

Review the JSON output for critical findings.

### Step 2: Run aliclawscan

```bash
cd skills/aliclawscan
python3 scripts/aliclawscan.py \
  --target <project-root> \
  --output report \
  --format both \
  --severity-threshold info
```

## 使用方式 / Usage

### 基础扫描 / Basic Scan

```bash
cd skills/aliclawscan
python3 scripts/aliclawscan.py --target /path/to/openclaw
```

### 排除测试文件 / Exclude Test Files (推荐用于生产环境检查)

```bash
python3 scripts/aliclawscan.py --target /path/to/openclaw --exclude-tests
```

### 仅显示严重问题 / Show Only Critical Issues

```bash
python3 scripts/aliclawscan.py --target /path/to/openclaw --severity-threshold critical
```

### Scanners

This runs 20 independent scanners covering 450+ threat patterns:

**Core Security (Enhanced 6 Scanners)**

1. **Secret Scanner** — hardcoded API keys, passwords, private keys, high-entropy strings, credential harvesting paths (~/.ssh, ~/.aws, ~/.kube, ~/.docker, ~/.config/gh)
2. **Config Scanner** — dangerous flags, debug mode, missing auth, permissive CORS, auto-approved dangerous tools, browser control, workspace boundaries, open room settings
3. **Code Scanner** — command injection, eval, path traversal, SSRF, XSS, SQL injection, reverse shells (/dev/tcp, netcat, Python/Node.js backdoors)
4. **Dependency Scanner** — CVE vulnerabilities via pnpm audit, outdated packages
5. **Exposure Scanner** — 0.0.0.0 binds, debug ports, unauthenticated endpoints, UPnP/NAT-PMP, mDNS/Bonjour broadcasting
6. **Skill Scanner** — unsandboxed exec, sensitive path access, gateway escalation

**AI Agent Security (10 Scanners)**

7. **Prompt Injection Scanner** — ignore instructions, role override, system impersonation, Unicode attacks, homoglyphs, BiDi control characters, XML/tag injection, base64-encoded payloads, hex-encoded payloads
8. **Memory Poisoning Scanner** — SOUL.md/IDENTITY.md tampering, agent memory modification, behavioral rule override
9. **Identity Scanner** — identity swap attempts, persona hijacking, identity death attacks
10. **Trust Scanner** — authority claims (OWASP ASI09), creator impersonation, urgency-based manipulation
11. **Obfuscation Scanner** — hex encoding, Base64→exec chains, character code construction, shell obfuscation
12. **Exfiltration Scanner** — webhook endpoints, DNS exfiltration, curl data exfil, POST with secrets
13. **Financial Scanner** — cryptocurrency transactions, payment API access, fund transfers
14. **PII Scanner** — credit cards, SSN, My Number (個人番号), email addresses
15. **MCP Security Scanner** — MCP tool poisoning, SSRF via dynamic URLs, shadow servers
16. **Supply Chain Scanner** — typosquatting, slopsquatting, malicious lifecycle scripts

**Advanced Threat Detection (4 New Scanners)**

17. **Cryptominer Scanner** — mining pools (XMR, Monero, etc.), mining software (xmrig, ccminer), stratum protocols, common mining ports
18. **Ransomware Scanner** — ransomware extensions (.encrypted, .locked), mass file encryption, ransom notes, payment demands
19. **Malicious Downloader Scanner** — curl|bash patterns, wget|sh, download-and-execute, base64 eval, social engineering language
20. **Persistence Scanner** — LaunchAgents/Daemons (macOS), cron jobs (Linux), systemd services, shell config modifications

### Risk Scoring Engine

The scanner includes an advanced risk scoring engine that:

- Calculates overall risk score (0-100) based on severity, confidence, and attack chain multipliers
- Provides verdict: **SAFE** (<30), **SUSPICIOUS** (30-79), **MALICIOUS** (≥80)
- Detects attack chain combinations (e.g., secrets + exfiltration = 2.2x multiplier)
- Shows category breakdown of detected threats

### Step 3: Review Report

The scanner produces:

- `report.md` — human-readable security report with prioritized findings
- `report.json` — machine-readable report for automation

### Step 4: Triage and Remediate

Findings are ranked by severity:

- **critical** — must fix before deployment
- **warn** — should fix, potential risk
- **info** — informational, review when convenient

Each finding includes:

- Rule ID (e.g., SECRET-001, INJECT-003) for tracking
- File path and line number
- Evidence (redacted for secrets)
- Specific remediation steps
- CWE reference

## 参数说明 / Parameters

| Parameter                    | Description                               | Default           |
| ---------------------------- | ----------------------------------------- | ----------------- |
| `--target PATH`              | Target directory to scan                  | Current directory |
| `--output NAME`              | Report file base name (without extension) | report            |
| `--format FORMAT`            | Output format: markdown, json, both       | both              |
| `--severity-threshold LEVEL` | Minimum severity: info, warn, critical    | info              |
| `--exclude-tests`            | Exclude test files from scan              | false             |
| `--skip-builtin`             | Skip built-in openclaw audit              | false             |

## 误报处理 / False Positive Handling

If you encounter false positives:

1. Use `--exclude-tests` to exclude test files
2. Use `--severity-threshold warn` to show only warnings and above
3. Test files are marked with ⚠️ in the report

## Rule Catalog

See [references/rule-catalog.md](references/rule-catalog.md) for the complete list of detection rules with examples and CWE mappings.
