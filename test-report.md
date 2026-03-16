# OpenClaw Security Scan Report

**Scan Date:** 2026-03-12 07:44:26 UTC
**Target:** `/Users/peter/llms/openclaw/skills/aliclawscan/tests/fixtures`

## Summary

| Severity    | Count  |
| ----------- | ------ |
| 🔴 Critical | 4      |
| 🟡 Warn     | 5      |
| 🔵 Info     | 1      |
| **Total**   | **10** |

## Scan Coverage

| Scanner            | Files Scanned | Findings | Duration |
| ------------------ | ------------- | -------- | -------- |
| secret_scanner     | 3             | 5        | 0.0s     |
| config_scanner     | 4             | 0        | 0.0s     |
| code_scanner       | 3             | 4        | 0.0s     |
| dependency_scanner | 0             | 2        | 6.1s     |
| exposure_scanner   | 3             | 0        | 0.0s     |
| skill_scanner      | 0             | 0        | 0.0s     |

## Findings

### 1. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in injection_sample.ts

**Location:** `/Users/peter/llms/openclaw/skills/aliclawscan/tests/fixtures/injection_sample.ts:7`

**Evidence:** `exec("ls " + userInput);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 2. [INJECT-002] eval/Function Usage

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-95

**Detail:** eval/Function Usage detected in injection_sample.ts

**Location:** `/Users/peter/llms/openclaw/skills/aliclawscan/tests/fixtures/injection_sample.ts:12`

**Evidence:** `return eval(code);`

**Remediation:** Replace eval/new Function with safer alternatives (JSON.parse, structured parsers).

---

### 3. [SECRET-001] AWS Access Key

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: AWS Access Key

**Location:** `secrets_sample.ts:2`

**Evidence:** `AKIA***MPLE`

**Remediation:** Remove AWS key, rotate via IAM, use env vars

---

### 4. [SECRET-005] Connection String

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Connection String

**Location:** `secrets_sample.ts:5`

**Evidence:** `mong***mydb`

**Remediation:** Use env vars for connection strings

---

### 5. [DEP-002] Outdated dependency: hono

**Severity:** 🟡 WARN

**Detail:** hono is 4 major versions behind (current: 0.0.0, latest: 4.12.7).

**Evidence:** `hono: 0.0.0 → 4.12.7`

**Remediation:** Upgrade hono to 4.12.7.

---

### 6. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in injection_sample.ts

**Location:** `/Users/peter/llms/openclaw/skills/aliclawscan/tests/fixtures/injection_sample.ts:22`

**Evidence:** `return fetch(url);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 7. [INJECT-006] Dangerous innerHTML

**Severity:** 🟡 WARN
| **CWE:** CWE-79

**Detail:** Dangerous innerHTML detected in injection_sample.ts

**Location:** `/Users/peter/llms/openclaw/skills/aliclawscan/tests/fixtures/injection_sample.ts:27`

**Evidence:** `document.body.innerHTML = content;`

**Remediation:** Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.

---

### 8. [SECRET-004] JWT Token

**Severity:** 🟡 WARN
| **CWE:** CWE-522

**Detail:** Hardcoded secret detected: JWT Token

**Location:** `secrets_sample.ts:7`

**Evidence:** `eyJh***wIn0`

**Remediation:** Remove JWT token

---

### 9. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `secrets_sample.ts:3`

**Evidence:** `SECR***KEY"`

**Remediation:** Use env vars or secrets manager

---

### 10. [SECRET-007] High-Entropy String

**Severity:** 🔵 INFO
| **CWE:** CWE-798

**Detail:** Potential secret with high entropy

**Location:** `secrets_sample.ts:3`

**Evidence:** `wJal***EKEY`

**Remediation:** Review if this is a secret; use env vars if so

---

## Conclusion

Scan completed with 10 total findings: 4 critical issue(s) requiring immediate attention; 5 warning(s) that should be reviewed; 1 informational finding(s). Address critical issues before deployment.
