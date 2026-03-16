# OpenClaw Security Scan Report

**Scan Date:** 2026-03-12 08:49:09 UTC
**Target:** `/Users/peter/llms/openclaw`

## Summary

| Severity    | Count    |
| ----------- | -------- |
| 🔴 Critical | 75       |
| 🟡 Warn     | 968      |
| 🔵 Info     | 14       |
| **Total**   | **1057** |

## File Type Distribution

| Type            | Findings | Percentage |
| --------------- | -------- | ---------- |
| Production Code | 1057     | 100.0%     |
| Test Code       | 0        | 0.0%       |

## Scan Coverage

| Scanner                | Files Scanned | Findings | Duration |
| ---------------------- | ------------- | -------- | -------- |
| openclaw_builtin_audit | 0             | 0        | 2.0s     |
| secret_scanner         | 3743          | 25       | 3.6s     |
| config_scanner         | 4404          | 8        | 5.4s     |
| code_scanner           | 3679          | 939      | 6.7s     |
| dependency_scanner     | 0             | 16       | 11.7s    |
| exposure_scanner       | 3656          | 37       | 2.5s     |
| skill_scanner          | 90            | 46       | 0.3s     |

## Findings

### 1. [CONFIG-001] Dangerous Skip Flags

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-693

**Detail:** Dangerous Skip Flags detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:581`

**Evidence:** `skipVerification: true`

**Remediation:** Remove dangerous skip flags; use proper validation

---

### 2. [CONFIG-003] No Auth Gateway

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-306

**Detail:** No Auth Gateway detected in extensions/line/src/card-command.ts

**Location:** `extensions/line/src/card-command.ts:162`

**Evidence:** `requireAuth: false`

**Remediation:** Enable authentication on all gateway endpoints

---

### 3. [CONFIG-003] No Auth Gateway

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-306

**Detail:** No Auth Gateway detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:569`

**Evidence:** `requireAuth: false`

**Remediation:** Enable authentication on all gateway endpoints

---

### 4. [CONFIG-005] Sandbox Disabled

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-693

**Detail:** Sandbox Disabled detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:605`

**Evidence:** `Sandbox: false`

**Remediation:** Enable sandbox mode to isolate untrusted operations

---

### 5. [CONFIG-005] Sandbox Disabled

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-693

**Detail:** Sandbox Disabled detected in src/agents/sandbox/browser.ts

**Location:** `src/agents/sandbox/browser.ts:86`

**Evidence:** `Sandbox: false`

**Remediation:** Enable sandbox mode to isolate untrusted operations

---

### 6. [CONFIG-005] Sandbox Disabled

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-693

**Detail:** Sandbox Disabled detected in src/browser/server-context.remote-tab-ops.harness.ts

**Location:** `src/browser/server-context.remote-tab-ops.harness.ts:29`

**Evidence:** `Sandbox: false`

**Remediation:** Enable sandbox mode to isolate untrusted operations

---

### 7. [CONFIG-006] Insecure TLS

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-295

**Detail:** Insecure TLS detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:689`

**Evidence:** `rejectUnauthorized = false`

**Remediation:** Enable TLS certificate verification; never disable in production

---

### 8. [CONFIG-006] Insecure TLS

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-295

**Detail:** Insecure TLS detected in src/gateway/client.ts

**Location:** `src/gateway/client.ts:174`

**Evidence:** `rejectUnauthorized = false`

**Remediation:** Enable TLS certificate verification; never disable in production

---

### 9. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in probe.ts

**Location:** `/Users/peter/llms/openclaw/extensions/bluebubbles/src/probe.ts:115`

**Evidence:** `const match = /^(\d+)/.exec(version.trim());`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 10. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/attachments/shared.ts:188`

**Evidence:** `const match = /^data:(image\/[a-z0-9.+-]+)?(;base64)?,(.*)$/i.exec(src);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 11. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in inbound.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/inbound.ts:17`

**Evidence:** `const match = /(?:^|;)messageid=([^;]+)/i.exec(raw);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 12. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in release-check.ts

**Location:** `/Users/peter/llms/openclaw/scripts/release-check.ts:121`

**Evidence:** `const base = /^([0-9]+\.[0-9]+\.[0-9]+)/.exec(normalized)?.[1];`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 13. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in sparkle-build.ts

**Location:** `/Users/peter/llms/openclaw/scripts/sparkle-build.ts:43`

**Evidence:** `const numericSuffix = /([0-9]+)$/.exec(suffix)?.[1];`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 14. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in update-clawtributors.ts

**Location:** `/Users/peter/llms/openclaw/scripts/update-clawtributors.ts:541`

**Evidence:** `const match = /^https?:\/\/github\.com\/([^/?#]+)/i.exec(url);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 15. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in models-config.providers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/models-config.providers.ts:78`

**Evidence:** `const match = /^\$\{([A-Z0-9_]+)\}$/.exec(trimmed);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 16. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in subagent-spawn.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-spawn.ts:351`

**Evidence:** `error: `agentId is not allowed for sessions_spawn (allowed: ${allowedText})`,`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 17. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in image-tool.helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/image-tool.helpers.ts:17`

**Evidence:** `const match = /^data:([^;,]+);base64,([a-z0-9+/=\r\n]+)$/i.exec(trimmed);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 18. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in pdf-tool.helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/pdf-tool.helpers.ts:35`

**Evidence:** `const dashMatch = /^(\d+)\s*-\s*(\d+)$/.exec(part);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 19. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in parse-bytes.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/parse-bytes.ts:25`

**Evidence:** `const m = /^(\d+(?:\.\d+)?)([a-z]+)?$/.exec(trimmed);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 20. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in parse-duration.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/parse-duration.ts:22`

**Evidence:** `const single = /^(\d+(?:\.\d+)?)(ms|s|m|h|d)?$/.exec(trimmed);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 21. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in restart-helper.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/restart-helper.ts:159`

**Evidence:** `* `spawn({ detached: true })`+`unref()` ensures the script survives`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 22. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in types.discord.ts

**Location:** `/Users/peter/llms/openclaw/src/config/types.discord.ts:180`

**Evidence:** `* Allow `sessions_spawn({ thread: true })` to auto-create + bind Discord`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 23. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in provider.lifecycle.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/provider.lifecycle.ts:128`

**Evidence:** `const match = /code\s+(\d{3,5})/i.exec(message);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 24. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in chat-attachments.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/chat-attachments.ts:68`

**Evidence:** `const dataUrlMatch = /^data:[^;]+;base64,(.*)$/.exec(base64);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 25. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in usage.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/usage.ts:124`

**Evidence:** `const match = /^UTC([+-])(\d{1,2})(?::([0-5]\d))?$/.exec(raw.trim());`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 26. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in test-helpers.openai-mock.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/test-helpers.openai-mock.ts:68`

**Evidence:** `const quoted = /"([^"]+)"/.exec(prompt)?.[1];`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 27. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in exec-command-resolution.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/exec-command-resolution.ts:35`

**Evidence:** `const match = /^[^\s]+/.exec(trimmed);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 28. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in message-action-params.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/message-action-params.ts:144`

**Evidence:** `const match = /^data:([^;]+);base64,(.*)$/i.exec(params.base64.trim());`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 29. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in update-check.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/update-check.ts:373`

**Evidence:** `const match = /^v?([0-9]+)\.([0-9]+)\.([0-9]+)(?:-([0-9A-Za-z.-]+))?(?:\+[0-9A-Za-z.-]+)?$/.exec(`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 30. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/media/fetch.ts:48`

**Evidence:** `const starMatch = /filename\*\s*=\s*([^;]+)/i.exec(header);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 31. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in manager-sync-ops.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/manager-sync-ops.ts:242`

**Evidence:** `this.db.exec(`DROP TABLE IF EXISTS ${VECTOR_TABLE}`);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 32. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in memory-schema.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/memory-schema.ts:95`

**Evidence:** `db.exec(`ALTER TABLE ${table} ADD COLUMN ${column} ${definition}`);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 33. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in qmd-manager.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/qmd-manager.ts:587`

**Evidence:** `const collectionLine = /^\s*([a-z0-9._-]+)\s+\(qmd:\/\/[^)]+\)\s*$/i.exec(line);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 34. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in configure.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/configure.ts:135`

**Evidence:** `return `exec (${provider.jsonOnly === false ? "json+text" : "json"})`;`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 35. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in ip.ts

**Location:** `/Users/peter/llms/openclaw/src/shared/net/ip.ts:95`

**Evidence:** `const match = /^(.*:)([^:%]+(?:\.[^:%]+){3})(%[0-9A-Za-z]+)?$/i.exec(raw);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 36. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in provider.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/provider.ts:66`

**Evidence:** `const match = /^xapp-\d-([a-z0-9]+)-/i.exec(token);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 37. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in outbound-params.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/outbound-params.ts:29`

**Evidence:** `const scopedMatch = /^-?\d+:(-?\d+)$/.exec(trimmed);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 38. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in targets.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/targets.ts:55`

**Evidence:** `const tmeMatch = /^(?:https?:\/\/)?t\.me\/([A-Za-z0-9_]+)$/i.exec(stripped);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 39. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in chat.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/chat.ts:96`

**Evidence:** `const match = /^data:([^;]+);base64,(.+)$/.exec(dataUrl);`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 40. [INJECT-001] Command Injection

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Command Injection detected in usage-helpers.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/usage-helpers.ts:297`

**Evidence:** `const match = /^\[Tool:\s*([^\]]+)\]/.exec(line.trim());`

**Remediation:** Avoid passing user input to shell commands. Use parameterised APIs and allowlists instead.

---

### 41. [INJECT-002] eval/Function Usage

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-95

**Detail:** eval/Function Usage detected in pw-tools-core.interactions.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/pw-tools-core.interactions.ts:302`

**Evidence:** `const elementEvaluator = new Function(`

**Remediation:** Replace eval/new Function with safer alternatives (JSON.parse, structured parsers).

---

### 42. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/references/rule-catalog.md

**Location:** `skills/aliclawscan/references/rule-catalog.md:30`

**Evidence:** `exec(`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 43. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:816`

**Evidence:** `exec(`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 44. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/report-optimized.md

**Location:** `skills/aliclawscan/report-optimized.md:240`

**Evidence:** `exec(`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 45. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/report.md

**Location:** `skills/aliclawscan/report.md:233`

**Evidence:** `exec(`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 46. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/scripts/aliclawscan.py

**Location:** `skills/aliclawscan/scripts/aliclawscan.py:35`

**Evidence:** `subprocess.run`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 47. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/scripts/scanners/code_scanner.py

**Location:** `skills/aliclawscan/scripts/scanners/code_scanner.py:18`

**Evidence:** `child_process`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 48. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/scripts/scanners/dependency_scanner.py

**Location:** `skills/aliclawscan/scripts/scanners/dependency_scanner.py:41`

**Evidence:** `subprocess.run`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 49. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/scripts/scanners/skill_scanner.py

**Location:** `skills/aliclawscan/scripts/scanners/skill_scanner.py:25`

**Evidence:** `child_process`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 50. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/aliclawscan/test-report.md

**Location:** `skills/aliclawscan/test-report.md:37`

**Evidence:** `exec(`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 51. [SKILL-001] Unsandboxed Exec

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-78

**Detail:** Unsandboxed Exec detected in skills/model-usage/scripts/model_usage.py

**Location:** `skills/model-usage/scripts/model_usage.py:37`

**Evidence:** `subprocess.check_output`

**Remediation:** Use sandboxed execution or restrict command allowlist

---

### 52. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/aliclawscan/references/rule-catalog.md

**Location:** `skills/aliclawscan/references/rule-catalog.md:61`

**Evidence:** `/etc/passwd`

**Remediation:** Restrict file access to skill's own directory

---

### 53. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:14109`

**Evidence:** `/etc/passwd`

**Remediation:** Restrict file access to skill's own directory

---

### 54. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/aliclawscan/report-optimized.md

**Location:** `skills/aliclawscan/report-optimized.md:1020`

**Evidence:** `/etc/passwd`

**Remediation:** Restrict file access to skill's own directory

---

### 55. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/aliclawscan/report.md

**Location:** `skills/aliclawscan/report.md:998`

**Evidence:** `/etc/passwd`

**Remediation:** Restrict file access to skill's own directory

---

### 56. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/bear-notes/SKILL.md

**Location:** `skills/bear-notes/SKILL.md:33`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 57. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/camsnap/SKILL.md

**Location:** `skills/camsnap/SKILL.md:31`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 58. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/canvas/SKILL.md

**Location:** `skills/canvas/SKILL.md:60`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 59. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/coding-agent/SKILL.md

**Location:** `skills/coding-agent/SKILL.md:110`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 60. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/eightctl/SKILL.md

**Location:** `skills/eightctl/SKILL.md:31`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 61. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/gh-issues/SKILL.md

**Location:** `skills/gh-issues/SKILL.md:82`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 62. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/himalaya/SKILL.md

**Location:** `skills/himalaya/SKILL.md:37`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 63. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/himalaya/references/configuration.md

**Location:** `skills/himalaya/references/configuration.md:3`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 64. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/model-usage/references/codexbar-cli.md

**Location:** `skills/model-usage/references/codexbar-cli.md:31`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 65. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/nano-banana-pro/SKILL.md

**Location:** `skills/nano-banana-pro/SKILL.md:51`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 66. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/notion/SKILL.md

**Location:** `skills/notion/SKILL.md:23`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 67. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/openai-whisper/SKILL.md

**Location:** `skills/openai-whisper/SKILL.md:36`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 68. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/openai-whisper-api/SKILL.md

**Location:** `skills/openai-whisper-api/SKILL.md:42`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 69. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/oracle/SKILL.md

**Location:** `skills/oracle/SKILL.md:96`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 70. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/session-logs/SKILL.md

**Location:** `skills/session-logs/SKILL.md:17`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 71. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/sherpa-onnx-tts/SKILL.md

**Location:** `skills/sherpa-onnx-tts/SKILL.md:66`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 72. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/spotify-player/SKILL.md

**Location:** `skills/spotify-player/SKILL.md:62`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 73. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/summarize/SKILL.md

**Location:** `skills/summarize/SKILL.md:78`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 74. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/wacli/SKILL.md

**Location:** `skills/wacli/SKILL.md:68`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 75. [SKILL-002] Sensitive Path Access

**Severity:** 🔴 CRITICAL
| **CWE:** CWE-552

**Detail:** Sensitive Path Access detected in skills/xurl/SKILL.md

**Location:** `skills/xurl/SKILL.md:57`

**Evidence:** `~/.`

**Remediation:** Restrict file access to skill's own directory

---

### 76. [DEP-002] Outdated dependency: hono

**Severity:** 🟡 WARN

**Detail:** hono is 4 major versions behind (current: 0.0.0, latest: 4.12.7).

**Evidence:** `hono: 0.0.0 → 4.12.7`

**Remediation:** Upgrade hono to 4.12.7.

---

### 77. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in interactions.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/interactions.ts:76`

**Evidence:** `return host === "0.0.0.0" || host === "::" || host === "0:0:0:0:0:0:0:0" || host === "::0";`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 78. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in slash-commands.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/slash-commands.ts:555`

**Evidence:** `// destinations. Don't emit callback URLs like http://0.0.0.0:3015/... or http://[::]:3015/...`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 79. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/nextcloud-talk/src/monitor.ts:411`

**Evidence:** ``http://${host === "0.0.0.0" ? "localhost" : host}:${port}${path}`;`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 80. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in runtime.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/runtime.ts:80`

**Evidence:** `return bind === "127.0.0.1" || bind === "::1" || bind === "localhost";`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 81. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in browser.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/sandbox/browser.ts:249`

**Evidence:** `args.push("-p", `127.0.0.1::${params.cfg.browser.cdpPort}`);`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 82. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in cdp.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/cdp.ts:22`

**Evidence:** `// Treat 0.0.0.0 and :: as wildcard bind addresses that need rewriting.`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 83. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in extension-relay.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/extension-relay.ts:696`

**Evidence:** `// When bindHost is explicitly non-loopback (e.g. 0.0.0.0 for WSL2),`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 84. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/shared.ts:79`

**Evidence:** `// bind=lan controls which interfaces the server listens on (0.0.0.0),`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 85. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in status.gather.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/status.gather.ts:202`

**Evidence:** `? `bind=lan listens on 0.0.0.0 (all interfaces); probing via ${probeHost}.``

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 86. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in run.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/gateway-cli/run.ts:261`

**Evidence:** `? "0.0.0.0"`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 87. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in ports.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/ports.ts:342`

**Evidence:** `export function probePortFree(port: number, host = "0.0.0.0"): Promise<boolean> {`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 88. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in configure.gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/configure.gateway.ts:67`

**Evidence:** `hint: "Bind to 0.0.0.0 - accessible from anywhere on your network",`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 89. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in doctor-security.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-security.ts:79`

**Evidence:** `: "0.0.0.0";`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 90. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in legacy.migrations.part-1.ts

**Location:** `/Users/peter/llms/openclaw/src/config/legacy.migrations.part-1.ts:558`

**Evidence:** `normalized === "0.0.0.0" ||`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 91. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in legacy.rules.ts

**Location:** `/Users/peter/llms/openclaw/src/config/legacy.rules.ts:203`

**Evidence:** `"gateway.bind host aliases (for example 0.0.0.0/localhost) are legacy; use bind modes (lan/loopback/custom/tailnet/auto)…`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 92. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in schema.help.ts

**Location:** `/Users/peter/llms/openclaw/src/config/schema.help.ts:254`

**Evidence:** `"Bind IP address for the Chrome extension relay listener. Leave unset for loopback-only access, or set an explicit non-l…`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 93. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in types.browser.ts

**Location:** `/Users/peter/llms/openclaw/src/config/types.browser.ts:71`

**Evidence:** `* Default: "127.0.0.1". Set to "0.0.0.0" for WSL2 or other environments where`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 94. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in types.gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/config/types.gateway.ts:379`

**Evidence:** `* - auto: Loopback (127.0.0.1) if available, else 0.0.0.0 (fallback to all interfaces)`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 95. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in net.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/net.ts:214`

**Evidence:** `* - lan: always 0.0.0.0 (no fallback)`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 96. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in server-runtime-config.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-runtime-config.ts:158`

**Evidence:** `isTrustedProxyAddress("::1", trustedProxies);`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 97. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in server.impl.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.impl.ts:219`

**Evidence:** `* - lan: 0.0.0.0`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 98. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in ports-inspect.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/ports-inspect.ts:327`

**Evidence:** `const hosts = ["127.0.0.1", "0.0.0.0", "::1", "::"];`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 99. [EXPOSE-001] Bind to All Interfaces

**Severity:** 🟡 WARN
| **CWE:** CWE-668

**Detail:** Bind to All Interfaces detected in onboarding.gateway-config.ts

**Location:** `/Users/peter/llms/openclaw/src/wizard/onboarding.gateway-config.ts:79`

**Evidence:** `{ value: "lan", label: "LAN (0.0.0.0)" },`

**Remediation:** Bind to 127.0.0.1 or specific interface instead of 0.0.0.0

---

### 100. [EXPOSE-002] Debug Port Exposed

**Severity:** 🟡 WARN
| **CWE:** CWE-489

**Detail:** Debug Port Exposed detected in lobster-tool.ts

**Location:** `/Users/peter/llms/openclaw/extensions/lobster/src/lobster-tool.ts:63`

**Evidence:** `if (nodeOptions.includes("--inspect")) {`

**Remediation:** Remove debug flags from production configurations

---

### 101. [EXPOSE-002] Debug Port Exposed

**Severity:** 🟡 WARN
| **CWE:** CWE-489

**Detail:** Debug Port Exposed detected in invoke-system-run-plan.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-system-run-plan.ts:82`

**Evidence:** `"--inspect",`

**Remediation:** Remove debug flags from production configurations

---

### 102. [EXPOSE-002] Debug Port Exposed

**Severity:** 🟡 WARN
| **CWE:** CWE-489

**Detail:** Debug Port Exposed detected in test-env.ts

**Location:** `/Users/peter/llms/openclaw/test/test-env.ts:120`

**Evidence:** `// Avoid leaking local dev tooling flags into tests (e.g. --inspect).`

**Remediation:** Remove debug flags from production configurations

---

### 103. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in rolldown.config.mjs

**Location:** `/Users/peter/llms/openclaw/apps/shared/OpenClawKit/Tools/CanvasA2UI/rolldown.config.mjs:6`

**Evidence:** `const repoRoot = path.resolve(here, "../../../../..");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 104. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-fixtures.ts

**Location:** `/Users/peter/llms/openclaw/extensions/acpx/src/test-utils/runtime-fixtures.ts:325`

**Evidence:** `const logPath = path.join(dir, `calls-${logFileSequence++}.log`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 105. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in viewer-assets.ts

**Location:** `/Users/peter/llms/openclaw/extensions/diffs/src/viewer-assets.ts:9`

**Evidence:** `const VIEWER_RUNTIME_FILE_URL = new URL("../assets/viewer-runtime.js", import.meta.url);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 106. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in docx.ts

**Location:** `/Users/peter/llms/openclaw/extensions/feishu/src/docx.ts:448`

**Evidence:** `// local path: ~, ./ and ../ are unambiguous (not in base64 alphabet).`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 107. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in llm-task-tool.ts

**Location:** `/Users/peter/llms/openclaw/extensions/llm-task/src/llm-task-tool.ts:17`

**Evidence:** `const mod = await import("../../../src/agents/pi-embedded-runner.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 108. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/extensions/lobster/src/test-helpers.ts:43`

**Evidence:** `export { createWindowsCmdShimFixture } from "../../shared/windows-cmd-shim-test-fixtures.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 109. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config.ts

**Location:** `/Users/peter/llms/openclaw/extensions/matrix/src/matrix/client/config.ts:7`

**Evidence:** `} from "../../secret-input.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 110. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in handler.ts

**Location:** `/Users/peter/llms/openclaw/extensions/matrix/src/matrix/monitor/handler.ts:25`

**Evidence:** `} from "../poll-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 111. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in index.ts

**Location:** `/Users/peter/llms/openclaw/extensions/matrix/src/matrix/monitor/index.ts:21`

**Evidence:** `} from "../client.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 112. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/extensions/matrix/src/matrix/send/types.ts:88`

**Evidence:** `cfg?: import("../../types.js").CoreConfig;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 113. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in inbound-media.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/monitor-handler/inbound-media.ts:9`

**Evidence:** `} from "../attachments.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 114. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/monitor-handler/message-handler.ts:28`

**Evidence:** `} from "../attachments.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 115. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in plugin.ts

**Location:** `/Users/peter/llms/openclaw/extensions/twitch/src/plugin.ts:137`

**Evidence:** `runtime: import("../../../src/runtime.js").RuntimeEnv;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 116. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in setup.ts

**Location:** `/Users/peter/llms/openclaw/extensions/twitch/test/setup.ts:7`

**Evidence:** `export * from "../../../test/setup.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 117. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in outbound.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/manager/outbound.ts:8`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 118. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in base.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/base.ts:15`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 119. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in mock.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/mock.ts:17`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 120. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in plivo.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/plivo.ts:18`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 121. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in telnyx.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/telnyx.ts:18`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 122. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in twilio.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/twilio.ts:21`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 123. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sync-moonshot-docs.ts

**Location:** `/Users/peter/llms/openclaw/scripts/sync-moonshot-docs.ts:10`

**Evidence:** `} from "../ui/src/ui/data/moonshot-kimi-k2";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 124. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-shell-completion.ts

**Location:** `/Users/peter/llms/openclaw/scripts/test-shell-completion.ts:33`

**Evidence:** `} from "../src/commands/doctor-completion.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 125. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in write-cli-compat.ts

**Location:** `/Users/peter/llms/openclaw/scripts/write-cli-compat.ts:7`

**Evidence:** `} from "../src/cli/daemon-cli-compat.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 126. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in client.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/client.ts:21`

**Evidence:** `} from "../plugin-sdk/windows-spawn.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 127. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in manager.core.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/control-plane/manager.core.ts:9`

**Evidence:** `} from "../runtime/errors.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 128. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in manager.identity-reconcile.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/control-plane/manager.identity-reconcile.ts:10`

**Evidence:** `} from "../runtime/session-identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 129. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in manager.types.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/control-plane/manager.types.ts:7`

**Evidence:** `} from "../../config/sessions/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 130. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in persistent-bindings.resolve.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/persistent-bindings.resolve.ts:9`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 131. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-identity.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/runtime/session-identity.ts:5`

**Evidence:** `} from "../../config/sessions/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 132. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-meta.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/runtime/session-meta.ts:11`

**Evidence:** `} from "../../config/sessions/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 133. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in translator.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/translator.ts:37`

**Evidence:** `} from "../infra/fixed-window-rate-limit.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 134. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in acp-spawn.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/acp-spawn.ts:6`

**Evidence:** `} from "../acp/control-plane/spawn.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 135. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-scope.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/agent-scope.ts:12`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 136. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in external-cli-sync.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/auth-profiles/external-cli-sync.ts:4`

**Evidence:** `} from "../cli-credentials.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 137. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in order.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/auth-profiles/order.ts:6`

**Evidence:** `} from "../model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 138. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-override.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/auth-profiles/session-override.ts:7`

**Evidence:** `} from "../auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 139. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bash-tools.exec-host-gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/bash-tools.exec-host-gateway.ts:7`

**Evidence:** `} from "../infra/exec-approval-surface.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 140. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bash-tools.exec-host-node.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/bash-tools.exec-host-node.ts:8`

**Evidence:** `} from "../infra/exec-approval-surface.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 141. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bash-tools.exec-host-shared.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/bash-tools.exec-host-shared.ts:8`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 142. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bash-tools.exec-runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/bash-tools.exec-runtime.ts:13`

**Evidence:** `export { applyPathPrepend, findPathKey, normalizePathPrepend } from "../infra/path-prepend.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 143. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bash-tools.exec.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/bash-tools.exec.ts:9`

**Evidence:** `} from "../infra/shell-env.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 144. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-tools.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/channel-tools.ts:7`

**Evidence:** `} from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 145. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/cli-runner/helpers.ts:337`

**Evidence:** `const filePath = path.join(tempDir, `image-${i + 1}.${ext}`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 146. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reliability.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/cli-runner/reliability.ts:7`

**Evidence:** `} from "../cli-watchdog-defaults.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 147. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in cli-runner.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/cli-runner.ts:65`

**Evidence:** `streamParams?: import("../commands/agent/types.js").AgentStreamParams;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 148. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in identity-avatar.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/identity-avatar.ts:10`

**Evidence:** `} from "../shared/avatar-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 149. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in kilocode-models.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/kilocode-models.ts:9`

**Evidence:** `} from "../providers/kilocode-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 150. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in memory-search.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/memory-search.ts:11`

**Evidence:** `} from "../memory/multimodal.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 151. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in model-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/model-auth.ts:11`

**Evidence:** `} from "../utils/normalize-secret-input.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 152. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in model-fallback.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/model-fallback.ts:5`

**Evidence:** `} from "../config/model-input.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 153. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in models-config.providers.static.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/models-config.providers.static.ts:8`

**Evidence:** `} from "../providers/kilocode-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 154. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in models-config.providers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/models-config.providers.ts:6`

**Evidence:** `} from "../providers/github-copilot-token.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 155. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in models-config.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/models-config.ts:8`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 156. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in openclaw-tools.subagents.sessions-spawn.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/openclaw-tools.subagents.sessions-spawn.test-harness.ts:3`

**Evidence:** `type SessionsSpawnTestConfig = ReturnType<(typeof import("../config/config.js"))["loadConfig"]>;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 157. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in openclaw-tools.subagents.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/openclaw-tools.subagents.test-harness.ts:4`

**Evidence:** `export type LoadedConfig = ReturnType<(typeof import("../config/config.js"))["loadConfig"]>;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 158. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in anthropic-stream-wrappers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/anthropic-stream-wrappers.ts:7`

**Evidence:** `} from "../provider-capabilities.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 159. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in compact.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/compact.ts:17`

**Evidence:** `} from "../../context-engine/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 160. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in google.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/google.ts:10`

**Evidence:** `} from "../../sessions/input-provenance.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 161. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in attempt.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/run/attempt.ts:17`

**Evidence:** `} from "../../../infra/net/undici-global-dispatcher.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 162. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in failover-observation.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/run/failover-observation.ts:6`

**Evidence:** `} from "../../pi-embedded-error-observation.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 163. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in images.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/run/images.ts:10`

**Evidence:** `} from "../../sandbox-media-paths.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 164. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in payloads.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/run/payloads.ts:14`

**Evidence:** `} from "../../pi-embedded-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 165. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run.overflow-compaction.mocks.shared.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/run.overflow-compaction.mocks.shared.ts:7`

**Evidence:** `} from "../../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 166. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/run.ts:7`

**Evidence:** `} from "../../context-engine/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 167. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runs.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-runner/runs.ts:5`

**Evidence:** `} from "../../logging/diagnostic.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 168. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in pi-embedded-subscribe.handlers.tools.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-embedded-subscribe.handlers.tools.ts:6`

**Evidence:** `} from "../infra/exec-approval-reply.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 169. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in compaction-safeguard.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-extensions/compaction-safeguard.ts:21`

**Evidence:** `} from "../compaction.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 170. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in pi-tools.before-tool-call.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-tools.before-tool-call.runtime.ts:1`

**Evidence:** `export { getDiagnosticSessionState } from "../logging/diagnostic-session-state.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 171. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in pi-tools.read.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/pi-tools.read.ts:12`

**Evidence:** `} from "../infra/fs-safe.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 172. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in browser.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/sandbox/browser.ts:8`

**Evidence:** `} from "../../browser/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 173. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in docker.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/sandbox/docker.ts:6`

**Evidence:** `} from "../../plugin-sdk/windows-spawn.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 174. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in fs-bridge.test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/sandbox/fs-bridge.test-helpers.ts:10`

**Evidence:** `vi.mock("../../infra/boundary-file-read.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 175. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in workspace.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/sandbox/workspace.ts:15`

**Evidence:** `} from "../workspace.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 176. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in typebox.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/schema/typebox.ts:5`

**Evidence:** `} from "../../infra/outbound/channel-target.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 177. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-tool-result-guard-wrapper.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/session-tool-result-guard-wrapper.ts:6`

**Evidence:** `} from "../sessions/input-provenance.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 178. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-tool-result-guard.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/session-tool-result-guard.ts:6`

**Evidence:** `} from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 179. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/skills/config.ts:8`

**Evidence:** `} from "../../shared/config-eval.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 180. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in frontmatter.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/skills/frontmatter.ts:14`

**Evidence:** `} from "../../shared/frontmatter.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 181. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in plugin-skills.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/skills/plugin-skills.ts:9`

**Evidence:** `} from "../../plugins/config-state.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 182. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in workspace.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/skills/workspace.ts:41`

**Evidence:** `* Example: `/Users/alice/.bun/.../skills/github/SKILL.md``

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 183. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in skills-install-extract.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/skills-install-extract.ts:9`

**Evidence:** `} from "../infra/archive.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 184. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in skills-install.test-mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/skills-install.test-mocks.ts:25`

**Evidence:** `importOriginal: () => Promise<typeof import("../security/skill-scanner.js")>,`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 185. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagent-announce-queue.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-announce-queue.ts:7`

**Evidence:** `} from "../utils/delivery-context.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 186. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagent-announce.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-announce.ts:10`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 187. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagent-control.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-control.ts:8`

**Evidence:** `} from "../auto-reply/reply/subagents-utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 188. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagent-registry.mocks.shared.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-registry.mocks.shared.ts:5`

**Evidence:** `vi.mock("../gateway/call.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 189. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagent-registry.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-registry.ts:10`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 190. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagent-spawn.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/subagent-spawn.ts:13`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 191. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in fast-core-tools.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/test-helpers/fast-core-tools.ts:4`

**Evidence:** `vi.mock("../tools/browser-tool.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 192. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in fast-tool-stubs.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/test-helpers/fast-tool-stubs.ts:18`

**Evidence:** `vi.mock("../tools/image-tool.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 193. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tool-images.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tool-images.ts:10`

**Evidence:** `} from "../media/image-ops.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 194. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents-list-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/agents-list-tool.ts:7`

**Evidence:** `} from "../../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 195. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in browser-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/browser-tool.ts:9`

**Evidence:** `} from "../../browser/client-actions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 196. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in discord-actions-guild.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/discord-actions-guild.ts:23`

**Evidence:** `} from "../../discord/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 197. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in discord-actions-messaging.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/discord-actions-messaging.ts:26`

**Evidence:** `} from "../../discord/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 198. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in discord-actions-moderation.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/discord-actions-moderation.ts:8`

**Evidence:** `} from "../../discord/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 199. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/gateway-tool.ts:10`

**Evidence:** `} from "../../infra/restart-sentinel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 200. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in image-tool.helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/image-tool.helpers.ts:6`

**Evidence:** `} from "../../config/model-input.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 201. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/message-tool.ts:10`

**Evidence:** `} from "../../channels/plugins/message-actions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 202. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nodes-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/nodes-tool.ts:11`

**Evidence:** `} from "../../cli/nodes-camera.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 203. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in pdf-tool.helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/pdf-tool.helpers.ts:6`

**Evidence:** `} from "../../config/model-input.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 204. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-status-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/session-status-tool.ts:12`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 205. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/sessions-helpers.ts:37`

**Evidence:** `} from "../pi-embedded-utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 206. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions-list-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/sessions-list-tool.ts:8`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 207. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions-send-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/sessions-send-helpers.ts:4`

**Evidence:** `} from "../../channels/plugins/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 208. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions-send-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/sessions-send-tool.ts:10`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 209. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slack-actions.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/slack-actions.ts:19`

**Evidence:** `} from "../../slack/actions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 210. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in subagents-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/subagents-tool.ts:17`

**Evidence:** `} from "../subagent-control.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 211. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in telegram-actions.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/telegram-actions.ts:8`

**Evidence:** `} from "../../telegram/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 212. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tool-runtime.helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/tool-runtime.helpers.ts:1`

**Evidence:** `export { getApiKeyForModel, requireApiKey } from "../model-auth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 213. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in web-guarded-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/web-guarded-fetch.ts:7`

**Evidence:** `} from "../../infra/net/fetch-guard.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 214. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in workspace-run.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/workspace-run.ts:9`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 215. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in workspace-templates.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/workspace-templates.ts:8`

**Evidence:** `"../../docs/reference/templates",`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 216. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in command-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/command-auth.ts:11`

**Evidence:** `} from "../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 217. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in envelope.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/envelope.ts:9`

**Evidence:** `} from "../infra/format-time/format-datetime.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 218. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in abort.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/abort.ts:7`

**Evidence:** `} from "../../agents/subagent-registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 219. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-runner-execution.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/agent-runner-execution.ts:16`

**Evidence:** `} from "../../agents/pi-embedded-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 220. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-runner-memory.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/agent-runner-memory.ts:15`

**Evidence:** `} from "../../agents/usage.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 221. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-runner.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/agent-runner.ts:16`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 222. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audio-tags.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/audio-tags.ts:1`

**Evidence:** `export { parseAudioTag } from "../../media/audio-tags.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 223. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in block-streaming.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/block-streaming.ts:10`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 224. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in context.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-acp/context.ts:4`

**Evidence:** `} from "../../../acp/conversation-id.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 225. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in lifecycle.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-acp/lifecycle.ts:7`

**Evidence:** `} from "../../../acp/control-plane/spawn.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 226. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-options.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-acp/runtime-options.ts:9`

**Evidence:** `} from "../../../acp/control-plane/runtime-options.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 227. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-acp/shared.ts:34`

**Evidence:** `export { SESSION_ID_RE } from "../../../sessions/session-id.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 228. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-allowlist.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-allowlist.ts:7`

**Evidence:** `} from "../../channels/plugins/config-writes.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 229. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-approve.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-approve.ts:6`

**Evidence:** `} from "../../telegram/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 230. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-compact.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-compact.ts:6`

**Evidence:** `} from "../../agents/pi-embedded.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 231. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-config.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-config.ts:6`

**Evidence:** `} from "../../channels/plugins/config-writes.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 232. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-context-report.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-context-report.ts:5`

**Evidence:** `} from "../../agents/pi-embedded-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 233. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-export-session.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-export-session.ts:10`

**Evidence:** `} from "../../config/sessions/paths.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 234. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-info.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-info.ts:7`

**Evidence:** `} from "../status.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 235. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-models.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-models.ts:10`

**Evidence:** `} from "../../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 236. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-session.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-session.ts:12`

**Evidence:** `} from "../../discord/monitor/thread-bindings.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 237. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-status.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-status.ts:5`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 238. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in action-focus.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-subagents/action-focus.ts:4`

**Evidence:** `} from "../../../acp/runtime/session-identifiers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 239. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in action-kill.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-subagents/action-kill.ts:4`

**Evidence:** `} from "../../../agents/subagent-control.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 240. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in action-send.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-subagents/action-send.ts:4`

**Evidence:** `} from "../../../agents/subagent-control.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 241. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-subagents/shared.ts:6`

**Evidence:** `} from "../../../agents/subagent-registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 242. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-subagents.test-mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-subagents.test-mocks.ts:4`

**Evidence:** `vi.mock("../../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 243. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in commands-tts.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/commands-tts.ts:18`

**Evidence:** `} from "../../tts/tts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 244. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in directive-handling.auth.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/directive-handling.auth.ts:6`

**Evidence:** `} from "../../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 245. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in directive-handling.impl.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/directive-handling.impl.ts:5`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 246. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in directive-handling.model.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/directive-handling.model.ts:8`

**Evidence:** `} from "../../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 247. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in directive-handling.params.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/directive-handling.params.ts:24`

**Evidence:** `ReturnType<typeof import("../../agents/model-catalog.js").loadModelCatalog>`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 248. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in directive-handling.persist.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/directive-handling.persist.ts:5`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 249. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in directives.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/directives.ts:12`

**Evidence:** `} from "../thinking.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 250. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in dispatch-acp.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/dispatch-acp.ts:11`

**Evidence:** `} from "../../acp/runtime/session-identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 251. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in dispatch-from-config.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/dispatch-from-config.ts:8`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 252. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in get-reply-inline-actions.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/get-reply-inline-actions.ts:15`

**Evidence:** `} from "../skill-commands.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 253. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in get-reply-run.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/get-reply-run.ts:9`

**Evidence:** `} from "../../agents/pi-embedded.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 254. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in get-reply.test-mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/get-reply.test-mocks.ts:4`

**Evidence:** `vi.mock("../../agents/agent-scope.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 255. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in get-reply.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/get-reply.ts:6`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 256. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in groups.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/groups.ts:5`

**Evidence:** `} from "../../channels/plugins/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 257. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in line-directives.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/line-directives.ts:7`

**Evidence:** `} from "../../line/flex-templates.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 258. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-preprocess-hooks.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/message-preprocess-hooks.ts:8`

**Evidence:** `} from "../../hooks/message-hook-mappers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 259. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in model-selection.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/model-selection.ts:13`

**Evidence:** `} from "../../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 260. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in normalize-reply.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/normalize-reply.ts:8`

**Evidence:** `} from "../tokens.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 261. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in provider-dispatcher.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/provider-dispatcher.ts:6`

**Evidence:** `} from "../dispatch.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 262. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in drain.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/queue/drain.ts:11`

**Evidence:** `} from "../../../utils/queue-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 263. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reply-media-paths.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/reply-media-paths.ts:18`

**Evidence:** `media.startsWith("../") ||`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 264. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in route-reply.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/route-reply.ts:22`

**Evidence:** `typeof import("../../infra/outbound/deliver-runtime.js")`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 265. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-delivery.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/session-delivery.ts:8`

**Evidence:** `} from "../../utils/delivery-context.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 266. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-reset-model.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/session-reset-model.ts:8`

**Evidence:** `} from "../../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 267. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-updates.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/session-updates.ts:12`

**Evidence:** `} from "../../infra/format-time/format-datetime.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 268. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-usage.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/session-usage.ts:6`

**Evidence:** `} from "../../agents/usage.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 269. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/session.ts:6`

**Evidence:** `} from "../../acp/conversation-id.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 270. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in stage-sandbox-media.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/stage-sandbox-media.ts:15`

**Evidence:** `} from "../../media/inbound-path-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 271. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reply.directive.directive-behavior.e2e-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply.directive.directive-behavior.e2e-harness.ts:8`

**Evidence:** `export { loadModelCatalog } from "../agents/model-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 272. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reply.directive.directive-behavior.e2e-mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply.directive.directive-behavior.e2e-mocks.ts:5`

**Evidence:** `vi.mock("../agents/pi-embedded.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 273. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reply.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply.test-harness.ts:54`

**Evidence:** `const home = path.join(fixtureRoot, `case-${++caseId}`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 274. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reply.triggers.trigger-handling.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply.triggers.trigger-handling.test-harness.ts:38`

**Evidence:** `vi.mock("../agents/pi-embedded.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 275. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in skill-commands.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/skill-commands.ts:6`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 276. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/status.ts:9`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 277. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in templating.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/templating.ts:5`

**Evidence:** `} from "../media-understanding/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 278. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/config.ts:7`

**Evidence:** `} from "../config/port-defaults.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 279. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in navigation-guard.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/navigation-guard.ts:7`

**Evidence:** `} from "../infra/net/ssrf.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 280. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent.snapshot.plan.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.snapshot.plan.ts:6`

**Evidence:** `} from "../constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 281. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent.snapshot.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.snapshot.ts:9`

**Evidence:** `} from "../screenshot.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 282. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in path-output.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/path-output.ts:1`

**Evidence:** `export * from "../paths.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 283. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in screenshot.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/screenshot.ts:6`

**Evidence:** `} from "../media/image-ops.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 284. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.control-server.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/server.control-server.test-harness.ts:150`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 285. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in a2ui.ts

**Location:** `/Users/peter/llms/openclaw/src/canvas-host/a2ui.ts:27`

**Evidence:** `path.resolve(here, "../canvas-host/a2ui"),`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 286. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.ts

**Location:** `/Users/peter/llms/openclaw/src/canvas-host/server.ts:270`

**Evidence:** `/(^|[\\/])\../, // dotfiles`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 287. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in dock.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/dock.ts:4`

**Evidence:** `} from "../config/group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 288. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in inbound-debounce-policy.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/inbound-debounce-policy.ts:7`

**Evidence:** `} from "../auto-reply/inbound-debounce.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 289. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in account-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/account-helpers.ts:6`

**Evidence:** `} from "../../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 290. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in handle-action.guild-admin.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/actions/discord/handle-action.guild-admin.ts:7`

**Evidence:** `} from "../../../../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 291. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in handle-action.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/actions/discord/handle-action.ts:6`

**Evidence:** `} from "../../../../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 292. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in telegram.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/actions/telegram.ts:6`

**Evidence:** `} from "../../../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 293. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in whatsapp-login.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/agent-tools/whatsapp-login.ts:21`

**Evidence:** `const { startWebLoginWithQr, waitForWebLogin } = await import("../../../web/login-qr.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 294. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in allowlist-match.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/allowlist-match.ts:1`

**Evidence:** `export type { AllowlistMatch, AllowlistMatchSource } from "../allowlist-match.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 295. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-config.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/channel-config.ts:1`

**Evidence:** `export type { ChannelEntryMatch, ChannelMatchSource } from "../channel-config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 296. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in group-mentions.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/group-mentions.ts:6`

**Evidence:** `} from "../../config/group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 297. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in group-policy-warnings.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/group-policy-warnings.ts:6`

**Evidence:** `} from "../../config/runtime-group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 298. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in index.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/index.ts:4`

**Evidence:** `} from "../../plugins/runtime.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 299. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in discord.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/discord.ts:9`

**Evidence:** `} from "../../../discord/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 300. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/helpers.ts:4`

**Evidence:** `} from "../../../commands/auth-choice.apply-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 301. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in imessage.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/imessage.ts:7`

**Evidence:** `} from "../../../imessage/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 302. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in signal.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/signal.ts:9`

**Evidence:** `} from "../../../signal/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 303. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slack.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/slack.ts:9`

**Evidence:** `} from "../../../slack/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 304. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in telegram.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/telegram.ts:10`

**Evidence:** `} from "../../../telegram/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 305. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in whatsapp.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/onboarding/whatsapp.ts:15`

**Evidence:** `} from "../../../web/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 306. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in discord.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/outbound/discord.ts:5`

**Evidence:** `} from "../../../discord/monitor/thread-bindings.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 307. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in telegram.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/outbound/telegram.ts:8`

**Evidence:** `} from "../../../telegram/outbound-params.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 308. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in whatsapp.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/plugins/outbound/whatsapp.ts:44`

**Evidence:** `deps?.sendWhatsApp ?? (await import("../../../web/outbound.js")).sendMessageWhatsApp;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 309. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in read-only-account-inspect.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/read-only-account-inspect.ts:7`

**Evidence:** `} from "../telegram/account-inspect.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 310. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reply-prefix.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/reply-prefix.ts:5`

**Evidence:** `} from "../auto-reply/reply/response-prefix-template.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 311. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/session.ts:7`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 312. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in index.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/web/index.ts:13`

**Evidence:** `} from "../../channel-web.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 313. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in argv.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/argv.ts:6`

**Evidence:** `} from "../infra/cli-root-options.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 314. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-actions-input/shared.ts:6`

**Evidence:** `} from "../../browser/form-fields.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 315. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in browser-cli-extension.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-extension.ts:31`

**Evidence:** `return path.resolve(here, "../../assets/chrome-extension");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 316. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in browser-cli-manage.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-manage.ts:9`

**Evidence:** `} from "../browser/client.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 317. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/channels-cli.ts:10`

**Evidence:** `} from "../commands/channels.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 318. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in command-secret-gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/command-secret-gateway.ts:8`

**Evidence:** `} from "../secrets/command-config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 319. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/config-cli.ts:413`

**Evidence:** `const { configureCommandFromSectionsArg } = await import("../commands/configure.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 320. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in install.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/install.ts:5`

**Evidence:** `} from "../../commands/daemon-runtime.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 321. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in restart-health.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/restart-health.ts:9`

**Evidence:** `} from "../../infra/ports.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 322. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/shared.ts:5`

**Evidence:** `} from "../../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 323. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.gather.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/status.gather.ts:6`

**Evidence:** `} from "../../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 324. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.print.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/daemon-cli/status.print.ts:6`

**Evidence:** `} from "../../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 325. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps-send-discord.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps-send-discord.runtime.ts:1`

**Evidence:** `export { sendMessageDiscord } from "../discord/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 326. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps-send-imessage.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps-send-imessage.runtime.ts:1`

**Evidence:** `export { sendMessageIMessage } from "../imessage/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 327. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps-send-signal.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps-send-signal.runtime.ts:1`

**Evidence:** `export { sendMessageSignal } from "../signal/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 328. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps-send-slack.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps-send-slack.runtime.ts:1`

**Evidence:** `export { sendMessageSlack } from "../slack/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 329. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps-send-telegram.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps-send-telegram.runtime.ts:1`

**Evidence:** `export { sendMessageTelegram } from "../telegram/send.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 330. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps-send-whatsapp.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps-send-whatsapp.runtime.ts:1`

**Evidence:** `export { sendMessageWhatsApp } from "../channels/web/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 331. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deps.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/deps.ts:94`

**Evidence:** `export { logWebSelfId } from "../web/auth-store.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 332. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in devices-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/devices-cli.ts:9`

**Evidence:** `} from "../infra/device-pairing.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 333. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approvals-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/exec-approvals-cli.ts:9`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 334. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run-loop.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/gateway-cli/run-loop.ts:5`

**Evidence:** `} from "../../agents/pi-embedded-runner/runs.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 335. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/gateway-cli/run.ts:12`

**Evidence:** `} from "../../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 336. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/gateway-cli/shared.ts:5`

**Evidence:** `} from "../../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 337. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in hooks-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/hooks-cli.ts:12`

**Evidence:** `} from "../hooks/hooks-status.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 338. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in models-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/models-cli.ts:27`

**Evidence:** `} from "../commands/models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 339. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in daemon.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/node-cli/daemon.ts:5`

**Evidence:** `} from "../../commands/node-daemon-runtime.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 340. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in format.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/nodes-cli/format.ts:1`

**Evidence:** `export { parseNodeList, parsePairingList } from "../../shared/node-list-parse.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 341. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.camera.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/nodes-cli/register.camera.ts:12`

**Evidence:** `} from "../nodes-camera.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 342. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.invoke.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/nodes-cli/register.invoke.ts:16`

**Evidence:** `} from "../../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 343. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.screen.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/nodes-cli/register.screen.ts:8`

**Evidence:** `} from "../nodes-screen.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 344. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/nodes-cli/types.ts:51`

**Evidence:** `} from "../../shared/node-list-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 345. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in npm-resolution.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/npm-resolution.ts:4`

**Evidence:** `} from "../infra/install-source-utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 346. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in pairing-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/pairing-cli.ts:10`

**Evidence:** `} from "../pairing/pairing-store.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 347. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in plugins-config.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/plugins-config.ts:1`

**Evidence:** `export { setPluginEnabledInConfig } from "../plugins/toggle-config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 348. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in command-registry.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/command-registry.ts:91`

**Evidence:** `const mod = await import("../config-cli.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 349. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in preaction.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/preaction.ts:11`

**Evidence:** `} from "../argv.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 350. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.agent.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/register.agent.ts:11`

**Evidence:** `} from "../../commands/agents.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 351. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.configure.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/register.configure.ts:5`

**Evidence:** `} from "../../commands/configure.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 352. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.onboard.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/register.onboard.ts:13`

**Evidence:** `} from "../../commands/onboard-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 353. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in register.subclis.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/register.subclis.ts:33`

**Evidence:** `const mod = await import("../../config/config.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 354. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in routes.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program/routes.ts:9`

**Evidence:** `} from "../argv.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 355. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in program.test-mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/program.test-mocks.ts:31`

**Evidence:** `vi.mock("../commands/message.js", () => ({ messageCommand }));`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 356. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in progress.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/progress.ts:7`

**Evidence:** `} from "../terminal/progress-line.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 357. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run-main.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/run-main.ts:18`

**Evidence:** `const { closeAllMemorySearchManagers } = await import("../memory/search-manager.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 358. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in skills-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/skills-cli.ts:17`

**Evidence:** `ReturnType<(typeof import("../agents/skills-status.js"))["buildWorkspaceSkillStatus"]>`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 359. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in progress.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/progress.ts:7`

**Evidence:** `} from "../../infra/update-runner.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 360. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in restart-helper.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/restart-helper.ts:11`

**Evidence:** `} from "../../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 361. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/shared.ts:17`

**Evidence:** `} from "../../infra/update-global.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 362. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/status.ts:5`

**Evidence:** `} from "../../commands/status.update.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 363. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in update-command.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/update-command.ts:6`

**Evidence:** `} from "../../commands/doctor-completion.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 364. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in wizard.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/update-cli/wizard.ts:7`

**Evidence:** `} from "../../infra/update-channels.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 365. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in webhooks-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/webhooks-cli.ts:8`

**Evidence:** `} from "../hooks/gmail-ops.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 366. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in delivery.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent/delivery.ts:9`

**Evidence:** `} from "../../infra/outbound/agent-delivery.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 367. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-store.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent/session-store.ts:12`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 368. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent/session.ts:10`

**Evidence:** `} from "../../auto-reply/thinking.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 369. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-via-gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent-via-gateway.ts:13`

**Evidence:** `} from "../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 370. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent.ts:17`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 371. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents.commands.add.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agents.commands.add.ts:7`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 372. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents.config.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agents.config.ts:6`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 373. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents.providers.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agents.providers.ts:6`

**Evidence:** `} from "../channels/plugins/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 374. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth-choice.apply-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/auth-choice.apply-helpers.ts:7`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 375. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth-choice.apply.huggingface.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/auth-choice.apply.huggingface.ts:4`

**Evidence:** `} from "../agents/huggingface-models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 376. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth-choice.apply.plugin-provider.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/auth-choice.apply.plugin-provider.ts:6`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 377. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in backup-shared.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/backup-shared.ts:8`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 378. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in backup-verify.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/backup-verify.ts:78`

**Evidence:** `if (!normalized || normalized === "." || normalized === ".." || normalized.startsWith("../")) {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 379. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in backup.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/backup.ts:6`

**Evidence:** `} from "../infra/backup-create.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 380. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in add.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/channels/add.ts:19`

**Evidence:** `} from "../onboarding/plugin-install.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 381. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in remove.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/channels/remove.ts:6`

**Evidence:** `} from "../../channels/plugins/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 382. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/channels/shared.ts:5`

**Evidence:** `} from "../../cli/command-secret-gateway.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 383. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/channels/status.ts:4`

**Evidence:** `} from "../../channels/account-snapshot-fields.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 384. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels.mock-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/channels.mock-harness.ts:18`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 385. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in chutes-oauth.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/chutes-oauth.ts:10`

**Evidence:** `} from "../agents/chutes-oauth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 386. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in cleanup-plan.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/cleanup-plan.ts:7`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 387. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in configure.gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/configure.gateway.ts:9`

**Evidence:** `} from "../gateway/gateway-config-prompts.shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 388. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-auth.ts:5`

**Evidence:** `} from "../agents/auth-health.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 389. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-bootstrap-size.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-bootstrap-size.ts:5`

**Evidence:** `} from "../agents/bootstrap-budget.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 390. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-completion.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-completion.ts:11`

**Evidence:** `} from "../cli/completion-cli.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 391. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-config-flow.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-config-flow.ts:7`

**Evidence:** `} from "../channels/telegram/allow-from.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 392. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-format.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-format.ts:6`

**Evidence:** `} from "../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 393. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-gateway-auth-token.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-gateway-auth-token.ts:2`

**Evidence:** `export { shouldRequireGatewayTokenForInstall } from "../gateway/auth-install-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 394. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-gateway-daemon-flow.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-gateway-daemon-flow.ts:7`

**Evidence:** `} from "../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 395. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-gateway-services.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-gateway-services.ts:13`

**Evidence:** `} from "../daemon/inspect.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 396. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-legacy-config.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-legacy-config.ts:10`

**Evidence:** `} from "../config/discord-preview-streaming.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 397. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-sandbox.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-sandbox.ts:8`

**Evidence:** `} from "../agents/sandbox.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 398. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-state-integrity.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-state-integrity.ts:17`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 399. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-state-migrations.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-state-migrations.ts:1`

**Evidence:** `export type { LegacyStateDetection } from "../infra/state-migrations.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 400. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor-ui.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor-ui.ts:6`

**Evidence:** `} from "../infra/control-ui-assets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 401. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor.e2e-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor.e2e-harness.ts:178`

**Evidence:** `vi.mock("../agents/skills-status.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 402. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in doctor.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/doctor.ts:10`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 403. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in health.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/health.ts:16`

**Evidence:** `} from "../infra/heartbeat-runner.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 404. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/message.ts:4`

**Evidence:** `} from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 405. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in model-picker.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/model-picker.ts:11`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 406. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth-order.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/auth-order.ts:6`

**Evidence:** `} from "../../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 407. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/auth.ts:12`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 408. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.auth-overview.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.auth-overview.ts:8`

**Evidence:** `} from "../../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 409. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.configured.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.configured.ts:6`

**Evidence:** `} from "../../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 410. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.format.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.format.ts:2`

**Evidence:** `export { maskApiKey } from "../../utils/mask-api-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 411. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.list-command.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.list-command.ts:28`

**Evidence:** `const { ensureAuthProfileStore } = await import("../../agents/auth-profiles.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 412. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.probe.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.probe.ts:13`

**Evidence:** `} from "../../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 413. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.registry.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.registry.ts:10`

**Evidence:** `} from "../../agents/model-auth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 414. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in list.status-command.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/list.status-command.ts:7`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 415. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in load-config.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/load-config.ts:8`

**Evidence:** `} from "../../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 416. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in scan.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/scan.ts:12`

**Evidence:** `} from "../../terminal/prompt-style.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 417. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models/shared.ts:8`

**Evidence:** `} from "../../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 418. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in models.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/models.ts:1`

**Evidence:** `export { githubCopilotLoginCommand } from "../providers/github-copilot-auth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 419. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in ollama-setup.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/ollama-setup.ts:9`

**Evidence:** `} from "../agents/ollama-models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 420. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-auth.config-core.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-auth.config-core.ts:5`

**Evidence:** `} from "../agents/huggingface-models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 421. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-auth.config-gateways.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-auth.config-gateways.ts:4`

**Evidence:** `} from "../agents/cloudflare-ai-gateway.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 422. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-auth.config-shared.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-auth.config-shared.ts:7`

**Evidence:** `} from "../config/types.models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 423. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-auth.credentials.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-auth.credentials.ts:12`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 424. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-auth.models.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-auth.models.ts:9`

**Evidence:** `} from "../providers/kilocode-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 425. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-auth.ts:4`

**Evidence:** `} from "../agents/synthetic-models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 426. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-channels.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-channels.ts:10`

**Evidence:** `} from "../channels/registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 427. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-custom.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-custom.ts:13`

**Evidence:** `} from "../utils/normalize-secret-input.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 428. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-helpers.ts:26`

**Evidence:** `} from "../utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 429. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in api-keys.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-non-interactive/api-keys.ts:5`

**Evidence:** `} from "../../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 430. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth-choice.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-non-interactive/local/auth-choice.ts:65`

**Evidence:** `} from "../../onboard-auth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 431. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in local.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-non-interactive/local.ts:14`

**Evidence:** `} from "../onboard-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 432. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboard-search.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboard-search.ts:8`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 433. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in plugin-install.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboarding/plugin-install.ts:11`

**Evidence:** `} from "../../plugins/bundled-sources.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 434. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/onboarding/types.ts:1`

**Evidence:** `export * from "../../channels/plugins/onboarding-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 435. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sandbox-explain.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/sandbox-explain.ts:5`

**Evidence:** `} from "../agents/sandbox.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 436. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sandbox.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/sandbox.ts:9`

**Evidence:** `} from "../agents/sandbox.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 437. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions-cleanup.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/sessions-cleanup.ts:14`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 438. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions.test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/sessions.test-helpers.ts:9`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 439. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status-all/channels.ts:5`

**Evidence:** `} from "../../channels/account-snapshot-fields.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 440. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in diagnosis.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status-all/diagnosis.ts:8`

**Evidence:** `} from "../../infra/restart-sentinel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 441. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in format.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status-all/format.ts:1`

**Evidence:** `export { formatTimeAgo } from "../../infra/format-time/format-relative.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 442. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status-all/gateway.ts:183`

**Evidence:** `export { pickGatewaySelfPresence } from "../gateway-presence.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 443. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status-all.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status-all.ts:10`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 444. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.command.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status.command.ts:16`

**Evidence:** `} from "../memory/status-format.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 445. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.summary.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status.summary.ts:12`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 446. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in status.update.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/status.update.ts:7`

**Evidence:** `} from "../infra/update-check.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 447. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in systemd-linger.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/systemd-linger.ts:5`

**Evidence:** `} from "../daemon/systemd.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 448. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in env-vars.ts

**Location:** `/Users/peter/llms/openclaw/src/config/env-vars.ts:5`

**Evidence:** `} from "../infra/host-env-security.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 449. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in io.ts

**Location:** `/Users/peter/llms/openclaw/src/config/io.ts:15`

**Evidence:** `} from "../infra/shell-env.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 450. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in plugin-auto-enable.ts

**Location:** `/Users/peter/llms/openclaw/src/config/plugin-auto-enable.ts:5`

**Evidence:** `} from "../channels/plugins/catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 451. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in prototype-keys.ts

**Location:** `/Users/peter/llms/openclaw/src/config/prototype-keys.ts:1`

**Evidence:** `export { isBlockedObjectKey } from "../infra/prototype-keys.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 452. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in schema.help.ts

**Location:** `/Users/peter/llms/openclaw/src/config/schema.help.ts:4`

**Evidence:** `} from "../discord/monitor/timeouts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 453. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in schema.hints.ts

**Location:** `/Users/peter/llms/openclaw/src/config/schema.hints.ts:11`

**Evidence:** `export type { ConfigUiHint, ConfigUiHints } from "../shared/config-ui-hints-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 454. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in main-session.ts

**Location:** `/Users/peter/llms/openclaw/src/config/sessions/main-session.ts:7`

**Evidence:** `} from "../../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 455. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in paths.ts

**Location:** `/Users/peter/llms/openclaw/src/config/sessions/paths.ts:219`

**Evidence:** `// keep only canonical .../agents/<agentId>/sessions/<file> shapes.`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 456. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-key.ts

**Location:** `/Users/peter/llms/openclaw/src/config/sessions/session-key.ts:6`

**Evidence:** `} from "../../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 457. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in store.ts

**Location:** `/Users/peter/llms/openclaw/src/config/sessions/store.ts:8`

**Evidence:** `} from "../../gateway/session-utils.fs.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 458. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in validation.ts

**Location:** `/Users/peter/llms/openclaw/src/config/validation.ts:8`

**Evidence:** `} from "../plugins/config-state.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 459. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in zod-schema.core.ts

**Location:** `/Users/peter/llms/openclaw/src/config/zod-schema.core.ts:8`

**Evidence:** `} from "../secrets/ref-contract.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 460. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in legacy.ts

**Location:** `/Users/peter/llms/openclaw/src/context-engine/legacy.ts:75`

**Evidence:** `await import("../agents/pi-embedded-runner/compact.runtime.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 461. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in delivery-target.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/isolated-agent/delivery-target.ts:7`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 462. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/isolated-agent/run.test-harness.ts:49`

**Evidence:** `vi.mock("../../agents/agent-scope.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 463. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in run.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/isolated-agent/run.ts:7`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 464. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/isolated-agent/session.ts:10`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 465. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in isolated-agent.mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/isolated-agent.mocks.ts:7`

**Evidence:** `vi.mock("../agents/pi-embedded.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 466. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in jobs.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/service/jobs.ts:8`

**Evidence:** `} from "../schedule.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 467. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in state.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/service/state.ts:13`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 468. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in timer.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/service/timer.ts:14`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 469. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in service.issue-regressions.test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/service.issue-regressions.test-helpers.ts:50`

**Evidence:** `const storePath = path.join(fixtureRoot, `case-${fixtureCount++}.jobs.json`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 470. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in service.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/service.test-harness.ts:43`

**Evidence:** `const dir = path.join(fixtureRoot, `case-${caseId++}`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 471. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-reaper.ts

**Location:** `/Users/peter/llms/openclaw/src/cron/session-reaper.ts:14`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 472. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-components.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/agent-components.ts:45`

**Evidence:** `} from "../../security/dm-policy-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 473. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in allow-list.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/allow-list.ts:8`

**Evidence:** `} from "../../channels/channel-config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 474. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auto-presence.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/auto-presence.ts:9`

**Evidence:** `} from "../../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 475. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in dm-command-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/dm-command-auth.ts:6`

**Evidence:** `} from "../../security/dm-policy-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 476. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approvals.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/exec-approvals.ts:25`

**Evidence:** `} from "../../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 477. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway-plugin.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/gateway-plugin.ts:11`

**Evidence:** `intentsConfig?: import("../../config/types.discord.js").DiscordIntentsConfig,`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 478. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in listeners.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/listeners.ts:20`

**Evidence:** `} from "../../security/dm-policy-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 479. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.preflight.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/message-handler.preflight.ts:5`

**Evidence:** `} from "../../acp/persistent-bindings.route.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 480. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.preflight.types.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/message-handler.preflight.types.ts:14`

**Evidence:** `export type LoadedConfig = ReturnType<typeof import("../../config/config.js").loadConfig>;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 481. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.process.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/message-handler.process.ts:10`

**Evidence:** `} from "../../auto-reply/reply/history.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 482. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/message-handler.ts:5`

**Evidence:** `} from "../../channels/inbound-debounce-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 483. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in model-picker.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/model-picker.ts:18`

**Evidence:** `} from "../../auto-reply/reply/commands-models.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 484. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in native-command.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/native-command.ts:20`

**Evidence:** `} from "../../acp/persistent-bindings.route.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 485. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in preflight-audio.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/preflight-audio.ts:53`

**Evidence:** `const { transcribeFirstAudio } = await import("../../media-understanding/audio-preflight.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 486. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in provider.allowlist.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/provider.allowlist.ts:7`

**Evidence:** `} from "../../channels/allowlists/resolve-utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 487. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in provider.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/provider.ts:24`

**Evidence:** `} from "../../channels/thread-bindings-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 488. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in route-resolution.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/route-resolution.ts:7`

**Evidence:** `} from "../../routing/resolve-route.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 489. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in thread-bindings.config.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/thread-bindings.config.ts:5`

**Evidence:** `} from "../../channels/thread-bindings-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 490. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in thread-bindings.manager.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/thread-bindings.manager.ts:10`

**Evidence:** `} from "../../infra/outbound/session-binding-service.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 491. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in thread-bindings.messages.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/thread-bindings.messages.ts:6`

**Evidence:** `} from "../../channels/thread-bindings-messages.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 492. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor.tool-result.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor.tool-result.test-harness.ts:18`

**Evidence:** `vi.mock("../auto-reply/dispatch.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 493. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in targets.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/targets.ts:9`

**Evidence:** `} from "../channels/targets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 494. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in command.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/voice/command.ts:25`

**Evidence:** `} from "../monitor/allow-list.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 495. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in manager.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/voice/manager.ts:34`

**Evidence:** `} from "../../media-understanding/runner.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 496. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in assistant-identity.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/assistant-identity.ts:11`

**Evidence:** `} from "../shared/avatar-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 497. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/auth.ts:6`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 498. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in boot.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/boot.ts:12`

**Evidence:** `} from "../config/sessions/main-session.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 499. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in call.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/call.ts:8`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 500. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in chat-sanitize.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/chat-sanitize.ts:4`

**Evidence:** `} from "../auto-reply/reply/strip-inbound-meta.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 501. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in client.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/client.ts:7`

**Evidence:** `} from "../infra/device-auth-store.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 502. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in control-ui-shared.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/control-ui-shared.ts:5`

**Evidence:** `} from "../shared/avatar-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 503. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in control-ui.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/control-ui.ts:9`

**Evidence:** `} from "../infra/control-ui-assets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 504. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approval-manager.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/exec-approval-manager.ts:5`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 505. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway-connection.test-mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/gateway-connection.test-mocks.ts:10`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 506. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in net.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/net.ts:10`

**Evidence:** `} from "../shared/net/ip.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 507. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in node-command-policy.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/node-command-policy.ts:6`

**Evidence:** `} from "../infra/node-commands.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 508. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in node-invoke-system-run-approval-match.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/node-invoke-system-run-approval-match.ts:7`

**Evidence:** `} from "../infra/system-run-approval-binding.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 509. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in openai-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/openai-http.ts:19`

**Evidence:** `} from "../media/input-files.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 510. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in openresponses-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/openresponses-http.ts:30`

**Evidence:** `} from "../media/input-files.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 511. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in primitives.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/protocol/schema/primitives.ts:7`

**Evidence:** `} from "../../../secrets/ref-contract.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 512. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in hooks.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/hooks.ts:14`

**Evidence:** `} from "../hooks.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 513. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in http-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/http-auth.ts:10`

**Evidence:** `} from "../auth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 514. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in path-context.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/plugins-http/path-context.ts:4`

**Evidence:** `} from "../../security-path.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 515. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in readiness.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/readiness.ts:8`

**Evidence:** `} from "../channel-health-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 516. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tls.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/tls.ts:5`

**Evidence:** `} from "../../infra/tls/gateway.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 517. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auth-context.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/ws-connection/auth-context.ts:7`

**Evidence:** `} from "../../auth-rate-limit.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 518. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/ws-connection/message-handler.ts:9`

**Evidence:** `} from "../../../infra/device-identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 519. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-browser.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-browser.ts:14`

**Evidence:** `const mod = override ? await import(override) : await import("../browser/server.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 520. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-channels.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-channels.ts:79`

**Evidence:** `* import { createPluginRuntime } from "../plugins/runtime/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 521. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-cron.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-cron.ts:9`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 522. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-http.ts:573`

**Evidence:** `openAiChatCompletionsConfig?: import("../config/types.gateway.js").GatewayHttpChatCompletionsConfig;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 523. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/agent.ts:7`

**Evidence:** `} from "../../agents/spawned-context.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 524. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/agents.ts:7`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 525. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in browser.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/browser.ts:5`

**Evidence:** `} from "../../browser/control-service.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 526. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/channels.ts:8`

**Evidence:** `} from "../../channels/plugins/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 527. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in chat.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/chat.ts:20`

**Evidence:** `} from "../../utils/directive-tags.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 528. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/config.ts:12`

**Evidence:** `} from "../../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 529. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in cron.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/cron.ts:6`

**Evidence:** `} from "../../cron/run-log.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 530. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in devices.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/devices.ts:11`

**Evidence:** `} from "../../infra/device-pairing.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 531. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approval.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/exec-approval.ts:5`

**Evidence:** `} from "../../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 532. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approvals.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/exec-approvals.ts:9`

**Evidence:** `} from "../../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 533. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in logs.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/logs.ts:10`

**Evidence:** `} from "../protocol/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 534. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in models.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/models.ts:9`

**Evidence:** `} from "../protocol/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 535. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nodes-pending.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/nodes-pending.ts:6`

**Evidence:** `} from "../node-pending-work.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 536. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nodes.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/nodes.ts:11`

**Evidence:** `} from "../../infra/node-pairing.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 537. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in push.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/push.ts:6`

**Evidence:** `} from "../../infra/push-apns.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 538. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in secrets.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/secrets.ts:8`

**Evidence:** `} from "../protocol/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 539. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in send.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/send.ts:11`

**Evidence:** `} from "../../infra/outbound/outbound-session.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 540. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/sessions.ts:9`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 541. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in skills.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/skills.ts:5`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 542. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in talk.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/talk.ts:10`

**Evidence:** `} from "../protocol/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 543. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tools-catalog.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/tools-catalog.ts:6`

**Evidence:** `} from "../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 544. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tts.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/tts.ts:16`

**Evidence:** `} from "../../tts/tts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 545. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/types.ts:73`

**Evidence:** `channel: import("../../channels/plugins/types.js").ChannelId,`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 546. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in update.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/update.ts:8`

**Evidence:** `} from "../../infra/restart-sentinel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 547. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in usage.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/usage.ts:6`

**Evidence:** `} from "../../config/sessions/paths.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 548. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in web.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/web.ts:8`

**Evidence:** `} from "../protocol/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 549. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in wizard.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/wizard.ts:11`

**Evidence:** `} from "../protocol/index.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 550. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-model-catalog.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-model-catalog.ts:5`

**Evidence:** `} from "../agents/model-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 551. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-reload-handlers.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-reload-handlers.ts:16`

**Evidence:** `} from "../infra/restart.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 552. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-restart-sentinel.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-restart-sentinel.ts:13`

**Evidence:** `} from "../infra/restart-sentinel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 553. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-runtime-config.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-runtime-config.ts:6`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 554. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-runtime-state.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-runtime-state.ts:40`

**Evidence:** `cfg: import("../config/config.js").OpenClawConfig;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 555. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-startup.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-startup.ts:9`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 556. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server-tailscale.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-tailscale.ts:7`

**Evidence:** `} from "../infra/tailscale.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 557. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.agent.gateway-server-agent.mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.agent.gateway-server-agent.mocks.ts:29`

**Evidence:** `const { setActivePluginRegistry } = await import("../plugins/runtime.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 558. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.auth.control-ui.suite.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.auth.control-ui.suite.ts:113`

**Evidence:** `const { loadOrCreateDeviceIdentity } = await import("../infra/device-identity.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 559. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.auth.default-token.suite.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.auth.default-token.suite.ts:97`

**Evidence:** `const { STATE_DIR, createConfigIO } = await import("../config/config.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 560. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.auth.shared.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.auth.shared.ts:173`

**Evidence:** `await import("../infra/device-identity.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 561. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.e2e-registry-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.e2e-registry-helpers.ts:1`

**Evidence:** `export { createTestRegistry as createRegistry } from "../test-utils/channel-plugins.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 562. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in server.impl.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server.impl.ts:20`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 563. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-reset-service.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/session-reset-service.ts:14`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 564. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-utils.fs.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/session-utils.fs.ts:11`

**Evidence:** `} from "../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 565. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-utils.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/session-utils.ts:11`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 566. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-utils.types.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/session-utils.types.ts:7`

**Evidence:** `} from "../shared/session-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 567. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sessions-patch.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/sessions-patch.ts:8`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 568. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in startup-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/startup-auth.ts:6`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 569. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in startup-control-ui-origins.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/startup-control-ui-origins.ts:5`

**Evidence:** `} from "../config/gateway-control-ui-origins.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 570. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-helpers.e2e.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/test-helpers.e2e.ts:10`

**Evidence:** `} from "../infra/device-identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 571. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-helpers.mocks.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/test-helpers.mocks.ts:240`

**Evidence:** `vi.mock("../agents/pi-model-discovery.js", async () => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 572. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-helpers.server.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/test-helpers.server.ts:13`

**Evidence:** `} from "../infra/device-identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 573. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tools-invoke-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/tools-invoke-http.ts:9`

**Evidence:** `} from "../agents/pi-tools.policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 574. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in handler.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/bundled/bootstrap-extra-files/handler.ts:4`

**Evidence:** `} from "../../../agents/workspace.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 575. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in handler.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/bundled/session-memory/handler.ts:14`

**Evidence:** `} from "../../../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 576. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bundled-dir.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/bundled-dir.ts:35`

**Evidence:** `// This path works in dev: dist/hooks/bundled-dir.js -> ../../src/hooks/bundled`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 577. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/config.ts:8`

**Evidence:** `} from "../shared/config-eval.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 578. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in frontmatter.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/frontmatter.ts:12`

**Evidence:** `} from "../shared/frontmatter.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 579. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gmail-ops.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/gmail-ops.ts:11`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 580. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gmail.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/gmail.ts:7`

**Evidence:** `} from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 581. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in install.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/install.ts:10`

**Evidence:** `} from "../infra/install-mode-options.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 582. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in llm-slug-generator.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/llm-slug-generator.ts:13`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 583. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-hook-mappers.ts

**Location:** `/Users/peter/llms/openclaw/src/hooks/message-hook-mappers.ts:7`

**Evidence:** `} from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 584. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in inbound-processing.ts

**Location:** `/Users/peter/llms/openclaw/src/imessage/monitor/inbound-processing.ts:7`

**Evidence:** `} from "../../auto-reply/envelope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 585. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor-provider.ts

**Location:** `/Users/peter/llms/openclaw/src/imessage/monitor/monitor-provider.ts:9`

**Evidence:** `} from "../../auto-reply/reply/history.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 586. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in archive-path.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/archive-path.ts:24`

**Evidence:** `if (normalized === ".." || normalized.startsWith("../")) {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 587. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in backup-create.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/backup-create.ts:13`

**Evidence:** `} from "../commands/backup-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 588. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-summary.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/channel-summary.ts:4`

**Evidence:** `} from "../channels/account-snapshot-fields.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 589. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in control-ui-assets.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/control-ui-assets.ts:224`

**Evidence:** `addCandidate(candidates, path.join(moduleDir, "../control-ui"));`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 590. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in device-auth-store.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/device-auth-store.ts:9`

**Evidence:** `} from "../shared/device-auth-store.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 591. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approval-forwarder.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/exec-approval-forwarder.ts:8`

**Evidence:** `} from "../config/types.approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 592. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-safe-bin-policy-validator.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/exec-safe-bin-policy-validator.ts:16`

**Evidence:** `if (trimmed.startsWith("./") || trimmed.startsWith("../") || trimmed.startsWith("~")) {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 593. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in executable-path.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/executable-path.ts:50`

**Evidence:** `const candidate = path.join(entry, executable + ext);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 594. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in file-lock.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/file-lock.ts:1`

**Evidence:** `export type { FileLockHandle, FileLockOptions } from "../plugin-sdk/file-lock.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 595. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in git-commit.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/git-commit.ts:151`

**Evidence:** `const pkg = require("../../package.json") as {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 596. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in heartbeat-runner.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/heartbeat-runner.ts:7`

**Evidence:** `} from "../agents/agent-scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 597. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in ssrf.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/net/ssrf.ts:14`

**Evidence:** `} from "../../shared/net/ip.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 598. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-delivery.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/agent-delivery.ts:11`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 599. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-resolution.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/channel-resolution.ts:12`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 600. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-selection.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/channel-selection.ts:9`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 601. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in deliver.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/deliver.ts:6`

**Evidence:** `} from "../../auto-reply/chunk.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 602. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-action-normalization.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/message-action-normalization.ts:4`

**Evidence:** `} from "../../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 603. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-action-params.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/message-action-params.ts:9`

**Evidence:** `} from "../../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 604. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-action-runner.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/message-action-runner.ts:7`

**Evidence:** `} from "../../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 605. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/message.ts:11`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 606. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in outbound-policy.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/outbound-policy.ts:5`

**Evidence:** `} from "../../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 607. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in outbound-session.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/outbound-session.ts:16`

**Evidence:** `} from "../../signal/identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 608. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in payloads.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/payloads.ts:5`

**Evidence:** `} from "../../auto-reply/reply/reply-payloads.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 609. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in target-resolver.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/target-resolver.ts:6`

**Evidence:** `} from "../../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 610. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in targets.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/outbound/targets.ts:16`

**Evidence:** `} from "../../utils/message-channel.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 611. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in provider-usage.auth.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/provider-usage.auth.ts:10`

**Evidence:** `} from "../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 612. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in restart.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/restart.ts:7`

**Evidence:** `} from "../daemon/constants.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 613. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in scripts-modules.d.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/scripts-modules.d.ts:1`

**Evidence:** `declare module "../../scripts/watch-node.mjs" {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 614. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-cost-usage.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/session-cost-usage.ts:11`

**Evidence:** `} from "../config/sessions/paths.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 615. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-cost-usage.types.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/session-cost-usage.types.ts:5`

**Evidence:** `} from "../shared/session-usage-timeseries-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 616. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in state-migrations.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/state-migrations.ts:11`

**Evidence:** `} from "../config/paths.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 617. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in accounts.ts

**Location:** `/Users/peter/llms/openclaw/src/line/accounts.ts:7`

**Evidence:** `} from "../routing/account-id.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 618. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-access.ts

**Location:** `/Users/peter/llms/openclaw/src/line/bot-access.ts:5`

**Evidence:** `} from "../channels/allow-from.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 619. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-handlers.ts

**Location:** `/Users/peter/llms/openclaw/src/line/bot-handlers.ts:16`

**Evidence:** `} from "../auto-reply/reply/history.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 620. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in webhook-node.ts

**Location:** `/Users/peter/llms/openclaw/src/line/webhook-node.ts:8`

**Evidence:** `} from "../infra/http-body.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 621. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runner.ts

**Location:** `/Users/peter/llms/openclaw/src/link-understanding/runner.ts:11`

**Evidence:** `} from "../media-understanding/scope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 622. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in console.ts

**Location:** `/Users/peter/llms/openclaw/src/logging/console.ts:24`

**Evidence:** `const loaded = requireConfig?.("../config/config.js") as`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 623. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in diagnostic.ts

**Location:** `/Users/peter/llms/openclaw/src/logging/diagnostic.ts:29`

**Evidence:** `typeof import("../agents/command-poll-backoff.runtime.js")`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 624. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in logger.ts

**Location:** `/Users/peter/llms/openclaw/src/logging/logger.ts:89`

**Evidence:** `const loaded = requireConfig?.("../config/config.js") as`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 625. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in redact.ts

**Location:** `/Users/peter/llms/openclaw/src/logging/redact.ts:111`

**Evidence:** `const loaded = requireConfig?.("../config/config.js") as`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 626. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in parse.ts

**Location:** `/Users/peter/llms/openclaw/src/media/parse.ts:28`

**Evidence:** `candidate.startsWith("../") ||`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 627. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in apply.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/apply.ts:10`

**Evidence:** `} from "../media/input-files.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 628. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in attachments.cache.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/attachments.cache.ts:10`

**Evidence:** `} from "../media/inbound-path-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 629. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in echo-transcript.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/echo-transcript.ts:6`

**Evidence:** `let deliverRuntimePromise: Promise<typeof import("../infra/outbound/deliver-runtime.js")> | null =`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 630. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audio.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/deepgram/audio.ts:7`

**Evidence:** `} from "../shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 631. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in image.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/image.ts:11`

**Evidence:** `typeof import("../../agents/pi-model-discovery-runtime.js")`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 632. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audio.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/openai/audio.ts:8`

**Evidence:** `} from "../shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 633. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/shared.ts:4`

**Evidence:** `export { fetchWithTimeout } from "../../utils/fetch-timeout.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 634. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in resolve.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/resolve.ts:7`

**Evidence:** `} from "../config/types.tools.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 635. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runner.entries.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/runner.entries.ts:6`

**Evidence:** `} from "../agents/api-key-rotation.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 636. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runner.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/runner.ts:10`

**Evidence:** `} from "../agents/model-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 637. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/types.ts:101`

**Evidence:** `cfg: import("../config/config.js").OpenClawConfig;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 638. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in backend-config.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/backend-config.ts:13`

**Evidence:** `} from "../config/types.memory.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 639. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in embeddings-gemini.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/embeddings-gemini.ts:4`

**Evidence:** `} from "../agents/api-key-rotation.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 640. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in qmd-process.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/qmd-process.ts:6`

**Evidence:** `} from "../plugin-sdk/windows-spawn.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 641. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in secret-input.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/secret-input.ts:4`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 642. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in invoke-browser.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-browser.ts:6`

**Evidence:** `} from "../browser/control-service.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 643. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in invoke-system-run-allowlist.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-system-run-allowlist.ts:11`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 644. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in invoke-system-run-plan.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-system-run-plan.ts:7`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 645. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in invoke-system-run.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-system-run.ts:14`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 646. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in invoke.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke.ts:15`

**Evidence:** `} from "../infra/exec-approvals.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 647. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runner.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/runner.ts:13`

**Evidence:** `} from "../infra/node-commands.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 648. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in setup-code.ts

**Location:** `/Users/peter/llms/openclaw/src/pairing/setup-code.ts:8`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 649. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in account-id.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/account-id.ts:5`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 650. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in acpx.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/acpx.ts:4`

**Evidence:** `export type { AcpRuntimeErrorCode } from "../acp/runtime/errors.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 651. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bluebubbles.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/bluebubbles.ts:4`

**Evidence:** `export { resolveAckReaction } from "../agents/identity.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 652. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-config-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/channel-config-helpers.ts:4`

**Evidence:** `} from "../channels/plugins/config-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 653. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-plugin-common.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/channel-plugin-common.ts:1`

**Evidence:** `export type { ChannelPlugin } from "../channels/plugins/types.plugin.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 654. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in copilot-proxy.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/copilot-proxy.ts:4`

**Evidence:** `export { emptyPluginConfigSchema } from "../plugins/config-schema.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 655. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in core.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/core.ts:7`

**Evidence:** `} from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 656. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in device-pair.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/device-pair.ts:4`

**Evidence:** `export { approveDevicePairing, listDevicePairing } from "../infra/device-pairing.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 657. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in diagnostics-otel.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/diagnostics-otel.ts:4`

**Evidence:** `export type { DiagnosticEventPayload } from "../infra/diagnostic-events.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 658. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in diffs.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/diffs.ts:4`

**Evidence:** `export type { OpenClawConfig } from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 659. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in discord.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/discord.ts:1`

**Evidence:** `export type { ChannelMessageActionAdapter } from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 660. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in feishu.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/feishu.ts:4`

**Evidence:** `export type { HistoryEntry } from "../auto-reply/reply/history.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 661. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in google-gemini-cli-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/google-gemini-cli-auth.ts:4`

**Evidence:** `export { fetchWithSsrFGuard } from "../infra/net/fetch-guard.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 662. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in googlechat.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/googlechat.ts:10`

**Evidence:** `} from "../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 663. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in imessage.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/imessage.ts:1`

**Evidence:** `export type { ResolvedIMessageAccount } from "../imessage/accounts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 664. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in inbound-reply-dispatch.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/inbound-reply-dispatch.ts:5`

**Evidence:** `} from "../auto-reply/reply/dispatch-from-config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 665. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in index.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/index.ts:1`

**Evidence:** `export { createAccountListHelpers } from "../channels/plugins/account-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 666. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in irc.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/irc.ts:4`

**Evidence:** `export { resolveControlCommandGate } from "../channels/command-gating.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 667. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in line.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/line.ts:5`

**Evidence:** `} from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 668. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in llm-task.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/llm-task.ts:4`

**Evidence:** `export { resolvePreferredOpenClawTmpDir } from "../infra/tmp-openclaw-dir.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 669. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in lobster.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/lobster.ts:14`

**Evidence:** `} from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 670. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in matrix.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/matrix.ts:10`

**Evidence:** `} from "../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 671. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in mattermost.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/mattermost.ts:4`

**Evidence:** `export { formatInboundFromLabel } from "../auto-reply/envelope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 672. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in memory-core.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/memory-core.ts:4`

**Evidence:** `export { emptyPluginConfigSchema } from "../plugins/config-schema.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 673. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in memory-lancedb.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/memory-lancedb.ts:4`

**Evidence:** `export type { OpenClawPluginApi } from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 674. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in minimax-portal-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/minimax-portal-auth.ts:4`

**Evidence:** `export { emptyPluginConfigSchema } from "../plugins/config-schema.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 675. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in msteams.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/msteams.ts:4`

**Evidence:** `export type { ChunkMode } from "../auto-reply/chunk.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 676. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nextcloud-talk.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/nextcloud-talk.ts:4`

**Evidence:** `export { logInboundDrop } from "../channels/logging.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 677. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nostr.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/nostr.ts:4`

**Evidence:** `export { buildChannelConfigSchema } from "../channels/plugins/config-schema.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 678. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in open-prose.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/open-prose.ts:4`

**Evidence:** `export type { OpenClawPluginApi } from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 679. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in phone-control.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/phone-control.ts:9`

**Evidence:** `} from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 680. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in qwen-portal-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/qwen-portal-auth.ts:4`

**Evidence:** `export { emptyPluginConfigSchema } from "../plugins/config-schema.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 681. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in secret-input-schema.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/secret-input-schema.ts:8`

**Evidence:** `} from "../secrets/ref-contract.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 682. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in signal.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/signal.ts:1`

**Evidence:** `export type { ChannelMessageActionAdapter } from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 683. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slack.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/slack.ts:1`

**Evidence:** `export type { OpenClawConfig } from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 684. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in synology-chat.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/synology-chat.ts:4`

**Evidence:** `export { setAccountEnabledInConfigSection } from "../channels/plugins/config-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 685. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in talk-voice.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/talk-voice.ts:4`

**Evidence:** `export type { OpenClawPluginApi } from "../plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 686. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in telegram.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/telegram.ts:5`

**Evidence:** `} from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 687. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-utils.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/test-utils.ts:4`

**Evidence:** `export { removeAckReactionAfterReply, shouldAckReaction } from "../channels/ack-reactions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 688. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in thread-ownership.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/thread-ownership.ts:4`

**Evidence:** `export type { OpenClawConfig } from "../config/config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 689. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tlon.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/tlon.ts:4`

**Evidence:** `export type { ReplyPayload } from "../auto-reply/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 690. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in twitch.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/twitch.ts:4`

**Evidence:** `export type { ReplyPayload } from "../auto-reply/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 691. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in voice-call.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/voice-call.ts:9`

**Evidence:** `} from "../config/zod-schema.core.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 692. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in webhook-request-guards.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/webhook-request-guards.ts:7`

**Evidence:** `} from "../infra/http-body.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 693. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in whatsapp.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/whatsapp.ts:1`

**Evidence:** `export type { ChannelMessageActionName } from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 694. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in zalo.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/zalo.ts:4`

**Evidence:** `export { jsonResult, readStringParam } from "../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 695. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in zalouser.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/zalouser.ts:4`

**Evidence:** `export type { ReplyPayload } from "../auto-reply/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 696. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in install.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/install.ts:9`

**Evidence:** `} from "../infra/install-mode-options.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 697. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in registry.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/registry.ts:9`

**Evidence:** `} from "../gateway/server-methods/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 698. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway-request-scope.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/gateway-request-scope.ts:5`

**Evidence:** `} from "../../gateway/server-methods/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 699. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in index.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/index.ts:5`

**Evidence:** `} from "../../agents/model-auth.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 700. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-channel.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/runtime-channel.ts:11`

**Evidence:** `} from "../../auto-reply/chunk.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 701. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-whatsapp-login.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/runtime-whatsapp-login.runtime.ts:1`

**Evidence:** `export { loginWeb } from "../../web/login.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 702. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-whatsapp-outbound.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/runtime-whatsapp-outbound.runtime.ts:1`

**Evidence:** `export { sendMessageWhatsApp, sendPollWhatsApp } from "../../web/outbound.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 703. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-whatsapp.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/runtime-whatsapp.ts:9`

**Evidence:** `} from "../../web/auth-store.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 704. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types-channel.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/types-channel.ts:2`

**Evidence:** `typeof import("../../pairing/pairing-store.js").readChannelAllowFromStore;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 705. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types-core.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/types-core.ts:13`

**Evidence:** `loadConfig: typeof import("../../config/config.js").loadConfig;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 706. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in source-display.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/source-display.ts:20`

**Evidence:** `if (rel.startsWith(`..${path.sep}`) || rel.startsWith("../") || rel.startsWith("..\\")) {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 707. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/types.ts:20`

**Evidence:** `export type { AnyAgentTool } from "../agents/tools/common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 708. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-key.ts

**Location:** `/Users/peter/llms/openclaw/src/routing/session-key.ts:12`

**Evidence:** `} from "../sessions/session-key-utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 709. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audit.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/audit.ts:7`

**Evidence:** `} from "../agents/model-auth-markers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 710. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in configure-plan.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/configure-plan.ts:8`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 711. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in ref-contract.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/ref-contract.ts:5`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 712. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in resolve-secret-input-string.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/resolve-secret-input-string.ts:6`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 713. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in resolve.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/resolve.ts:11`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 714. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/secrets/runtime.ts:8`

**Evidence:** `} from "../agents/auth-profiles.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 715. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audit-channel.ts

**Location:** `/Users/peter/llms/openclaw/src/security/audit-channel.ts:4`

**Evidence:** `} from "../channels/account-snapshot-fields.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 716. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audit-extra.async.ts

**Location:** `/Users/peter/llms/openclaw/src/security/audit-extra.async.ts:13`

**Evidence:** `} from "../agents/sandbox.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 717. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audit-extra.sync.ts

**Location:** `/Users/peter/llms/openclaw/src/security/audit-extra.sync.ts:5`

**Evidence:** `} from "../agents/sandbox.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 718. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audit-tool-policy.ts

**Location:** `/Users/peter/llms/openclaw/src/security/audit-tool-policy.ts:1`

**Evidence:** `export { pickSandboxToolPolicy } from "../agents/sandbox-tool-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 719. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in audit.ts

**Location:** `/Users/peter/llms/openclaw/src/security/audit.ts:19`

**Evidence:** `} from "../infra/exec-safe-bin-runtime-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 720. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in config-eval.ts

**Location:** `/Users/peter/llms/openclaw/src/shared/config-eval.ts:168`

**Evidence:** `const candidate = path.join(part, bin + ext);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 721. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in usage-types.ts

**Location:** `/Users/peter/llms/openclaw/src/shared/usage-types.ts:11`

**Evidence:** `} from "../infra/session-cost-usage.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 722. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in format.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/format.ts:7`

**Evidence:** `} from "../markdown/ir.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 723. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in access-policy.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/monitor/access-policy.ts:6`

**Evidence:** `} from "../../security/dm-policy-shared.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 724. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in event-handler.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/monitor/event-handler.ts:8`

**Evidence:** `} from "../../auto-reply/envelope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 725. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor.tool-result.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/monitor.tool-result.test-harness.ts:71`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 726. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/monitor.ts:10`

**Evidence:** `} from "../config/runtime-group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 727. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reaction-level.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/reaction-level.ts:6`

**Evidence:** `} from "../utils/reaction-level.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 728. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in blocks.test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/blocks.test-helpers.ts:20`

**Evidence:** `vi.mock("../config/config.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 729. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in allow-list.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/allow-list.ts:5`

**Evidence:** `} from "../../channels/allowlist-match.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 730. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-config.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/channel-config.ts:6`

**Evidence:** `} from "../../channels/channel-config.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 731. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in context.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/context.ts:53`

**Evidence:** `slashCommand: Required<import("../../config/config.js").SlackSlashCommandConfig>;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 732. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/events/channels.ts:13`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 733. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-subtype-handlers.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/events/message-subtype-handlers.ts:6`

**Evidence:** `} from "../types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 734. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in dispatch.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/message-handler/dispatch.ts:22`

**Evidence:** `} from "../../stream-mode.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 735. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in prepare-content.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/message-handler/prepare-content.ts:9`

**Evidence:** `} from "../media.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 736. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in prepare-thread-context.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/message-handler/prepare-thread-context.ts:12`

**Evidence:** `} from "../media.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 737. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in prepare.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/message-handler/prepare.ts:7`

**Evidence:** `} from "../../../auto-reply/envelope.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 738. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-handler.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/message-handler.ts:4`

**Evidence:** `} from "../../channels/inbound-debounce-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 739. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in provider.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/provider.ts:11`

**Evidence:** `} from "../../channels/allowlists/resolve-utils.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 740. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slash-commands.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/slash-commands.runtime.ts:7`

**Evidence:** `} from "../../auto-reply/commands-registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 741. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slash-dispatch.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/slash-dispatch.runtime.ts:1`

**Evidence:** `export { resolveChunkMode } from "../../auto-reply/chunk.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 742. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slash-skill-commands.runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/slash-skill-commands.runtime.ts:1`

**Evidence:** `export { listSkillCommandsForAgents } from "../../auto-reply/skill-commands.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 743. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slash.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/slash.test-harness.ts:15`

**Evidence:** `vi.mock("../../auto-reply/reply/provider-dispatcher.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 744. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in slash.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/slash.ts:5`

**Evidence:** `} from "../../auto-reply/commands-registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 745. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor.test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor.test-helpers.ts:151`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 746. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in send.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/send.ts:6`

**Evidence:** `} from "../auto-reply/chunk.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 747. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in stream-mode.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/stream-mode.ts:7`

**Evidence:** `} from "../config/discord-preview-streaming.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 748. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in targets.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/targets.ts:9`

**Evidence:** `} from "../channels/targets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 749. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in threading-tool-context.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/threading-tool-context.ts:4`

**Evidence:** `} from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 750. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in account-inspect.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/account-inspect.ts:6`

**Evidence:** `} from "../config/types.secrets.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 751. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in accounts.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/accounts.ts:10`

**Evidence:** `} from "../plugin-sdk/account-resolution.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 752. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in delivery.replies.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot/delivery.replies.ts:14`

**Evidence:** `} from "../../hooks/message-hook-mappers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 753. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot/helpers.ts:8`

**Evidence:** `} from "../../config/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 754. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-access.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-access.ts:5`

**Evidence:** `} from "../channels/allow-from.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 755. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-handlers.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-handlers.ts:6`

**Evidence:** `} from "../auto-reply/inbound-debounce.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 756. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-message-context.body.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-message-context.body.ts:5`

**Evidence:** `} from "../agents/model-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 757. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-message-context.session.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-message-context.session.ts:6`

**Evidence:** `} from "../auto-reply/reply/history.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 758. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-message-context.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-message-context.ts:8`

**Evidence:** `} from "../channels/status-reactions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 759. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-message-context.types.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-message-context.types.ts:9`

**Evidence:** `} from "../config/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 760. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-message-dispatch.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-message-dispatch.ts:7`

**Evidence:** `} from "../agents/model-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 761. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-native-command-menu.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-native-command-menu.ts:10`

**Evidence:** `} from "../config/telegram-custom-commands.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 762. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot-native-commands.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot-native-commands.ts:13`

**Evidence:** `} from "../auto-reply/commands-registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 763. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot.create-telegram-bot.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot.create-telegram-bot.test-harness.ts:23`

**Evidence:** `vi.mock("../web/media.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 764. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot.media.e2e-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot.media.e2e-harness.ts:95`

**Evidence:** `vi.mock("../media/store.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 765. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot.media.test-utils.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot.media.test-utils.ts:106`

**Evidence:** `const replyModule = await import("../auto-reply/reply.js");`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 766. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in bot.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot.ts:12`

**Evidence:** `} from "../channels/thread-bindings-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 767. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in conversation-route.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/conversation-route.ts:10`

**Evidence:** `} from "../routing/resolve-route.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 768. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in exec-approvals-handler.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/exec-approvals-handler.ts:10`

**Evidence:** `} from "../infra/exec-approval-reply.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 769. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in format.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/format.ts:7`

**Evidence:** `} from "../markdown/ir.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 770. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in group-access.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/group-access.ts:9`

**Evidence:** `} from "../config/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 771. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in group-config-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/group-config-helpers.ts:5`

**Evidence:** `} from "../config/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 772. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in network-errors.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/network-errors.ts:6`

**Evidence:** `} from "../infra/errors.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 773. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in proxy.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/proxy.ts:1`

**Evidence:** `export { getProxyUrlFromFetch, makeProxyFetch } from "../infra/net/proxy-fetch.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 774. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in reaction-level.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/reaction-level.ts:6`

**Evidence:** `} from "../utils/reaction-level.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 775. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in send.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/send.test-harness.ts:43`

**Evidence:** `vi.mock("../web/media.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 776. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in sticker-cache.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/sticker-cache.ts:9`

**Evidence:** `} from "../agents/model-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 777. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in thread-bindings.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/thread-bindings.ts:14`

**Evidence:** `} from "../infra/outbound/session-binding-service.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 778. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in webhook.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/webhook.ts:13`

**Evidence:** `} from "../logging/diagnostic.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 779. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in note.ts

**Location:** `/Users/peter/llms/openclaw/src/terminal/note.ts:43`

**Evidence:** `word.startsWith("../")`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 780. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channel-plugins.ts

**Location:** `/Users/peter/llms/openclaw/src/test-utils/channel-plugins.ts:6`

**Evidence:** `} from "../channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 781. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in fixture-suite.ts

**Location:** `/Users/peter/llms/openclaw/src/test-utils/fixture-suite.ts:24`

**Evidence:** `const dir = path.join(fixtureRoot, `${prefix}-${fixtureCount++}`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 782. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in runtime-group-policy-contract.ts

**Location:** `/Users/peter/llms/openclaw/src/test-utils/runtime-group-policy-contract.ts:5`

**Evidence:** `} from "../config/runtime-group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 783. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in secret-ref-test-vectors.ts

**Location:** `/Users/peter/llms/openclaw/src/test-utils/secret-ref-test-vectors.ts:6`

**Evidence:** `"a/.../b",`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 784. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tts-core.ts

**Location:** `/Users/peter/llms/openclaw/src/tts/tts-core.ts:11`

**Evidence:** `} from "../agents/model-selection.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 785. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tts.ts

**Location:** `/Users/peter/llms/openclaw/src/tts/tts.ts:24`

**Evidence:** `} from "../config/types.tts.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 786. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in selectors.ts

**Location:** `/Users/peter/llms/openclaw/src/tui/components/selectors.ts:7`

**Evidence:** `} from "../theme/theme.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 787. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway-chat.ts

**Location:** `/Users/peter/llms/openclaw/src/tui/gateway-chat.ts:9`

**Evidence:** `} from "../gateway/call.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 788. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tui-command-handlers.ts

**Location:** `/Users/peter/llms/openclaw/src/tui/tui-command-handlers.ts:7`

**Evidence:** `} from "../auto-reply/thinking.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 789. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tui-formatters.ts

**Location:** `/Users/peter/llms/openclaw/src/tui/tui-formatters.ts:71`

**Evidence:** `token.startsWith("../")`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 790. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tui-session-actions.ts

**Location:** `/Users/peter/llms/openclaw/src/tui/tui-session-actions.ts:7`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 791. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tui.ts

**Location:** `/Users/peter/llms/openclaw/src/tui/tui.ts:18`

**Evidence:** `} from "../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 792. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in extension-api.d.ts

**Location:** `/Users/peter/llms/openclaw/src/types/extension-api.d.ts:1`

**Evidence:** `declare module "../../../dist/extensionAPI.js" {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 793. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in message-channel.ts

**Location:** `/Users/peter/llms/openclaw/src/utils/message-channel.ts:6`

**Evidence:** `} from "../channels/registry.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 794. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in version.ts

**Location:** `/Users/peter/llms/openclaw/src/version.ts:7`

**Evidence:** `"../package.json",`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 795. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in heartbeat-runner.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/heartbeat-runner.ts:7`

**Evidence:** `} from "../../auto-reply/heartbeat.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 796. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in broadcast.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/monitor/broadcast.ts:8`

**Evidence:** `} from "../../../routing/session-key.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 797. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in group-activation.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/monitor/group-activation.ts:6`

**Evidence:** `} from "../../../config/group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 798. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in on-message.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/monitor/on-message.ts:29`

**Evidence:** `replyLogger: ReturnType<(typeof import("../../../logging.js"))["getChildLogger"]>;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 799. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in process-message.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/monitor/process-message.ts:9`

**Evidence:** `} from "../../../auto-reply/reply/history.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 800. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/monitor.ts:25`

**Evidence:** `} from "../reconnect.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 801. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in session-snapshot.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply/session-snapshot.ts:11`

**Evidence:** `} from "../../config/sessions.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 802. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auto-reply.impl.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply.impl.ts:1`

**Evidence:** `export { HEARTBEAT_PROMPT, stripHeartbeatToken } from "../auto-reply/heartbeat.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 803. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in auto-reply.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/web/auto-reply.test-harness.ts:32`

**Evidence:** `vi.mock("../agents/pi-embedded.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 804. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in access-control.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/web/inbound/access-control.test-harness.ts:36`

**Evidence:** `vi.mock("../../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 805. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in access-control.ts

**Location:** `/Users/peter/llms/openclaw/src/web/inbound/access-control.ts:6`

**Evidence:** `} from "../../config/runtime-group-policy.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 806. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in media.ts

**Location:** `/Users/peter/llms/openclaw/src/web/media.ts:14`

**Evidence:** `} from "../media/image-ops.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 807. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in monitor-inbox.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/web/monitor-inbox.test-harness.ts:84`

**Evidence:** `vi.mock("../media/store.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 808. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/web/test-helpers.ts:33`

**Evidence:** `vi.mock("../config/config.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 809. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboarding.completion.ts

**Location:** `/Users/peter/llms/openclaw/src/wizard/onboarding.completion.ts:9`

**Evidence:** `} from "../commands/doctor-completion.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 810. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboarding.finalize.ts

**Location:** `/Users/peter/llms/openclaw/src/wizard/onboarding.finalize.ts:8`

**Evidence:** `} from "../commands/daemon-install-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 811. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboarding.gateway-config.ts

**Location:** `/Users/peter/llms/openclaw/src/wizard/onboarding.gateway-config.ts:4`

**Evidence:** `} from "../commands/auth-choice.apply-helpers.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 812. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in onboarding.ts

**Location:** `/Users/peter/llms/openclaw/src/wizard/onboarding.ts:7`

**Evidence:** `} from "../commands/onboard-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 813. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in envelope-timestamp.ts

**Location:** `/Users/peter/llms/openclaw/test/helpers/envelope-timestamp.ts:4`

**Evidence:** `} from "../../src/infra/format-time/format-datetime.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 814. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in inbound-contract-capture.ts

**Location:** `/Users/peter/llms/openclaw/test/helpers/inbound-contract-capture.ts:16`

**Evidence:** `const actual = await importOriginal<typeof import("../../src/auto-reply/dispatch.js")>();`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 815. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in inbound-contract-dispatch-mock.ts

**Location:** `/Users/peter/llms/openclaw/test/helpers/inbound-contract-dispatch-mock.ts:7`

**Evidence:** `vi.mock("../../src/auto-reply/dispatch.js", async (importOriginal) => {`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 816. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in memory-tool-manager-mock.ts

**Location:** `/Users/peter/llms/openclaw/test/helpers/memory-tool-manager-mock.ts:36`

**Evidence:** `vi.mock("../../src/memory/index.js", () => ({`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 817. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in temp-home.ts

**Location:** `/Users/peter/llms/openclaw/test/helpers/temp-home.ts:96`

**Evidence:** `const base = path.join(root, `case-${state.nextCaseId++}`);`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 818. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in setup.ts

**Location:** `/Users/peter/llms/openclaw/test/setup.ts:35`

**Evidence:** `} from "../src/channels/plugins/types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 819. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in registry.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/i18n/lib/registry.ts:18`

**Evidence:** `loader: () => import("../locales/zh-CN.ts"),`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 820. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in app-gateway.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/app-gateway.ts:4`

**Evidence:** `} from "../../../src/gateway/events.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 821. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agent-files.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/agent-files.ts:7`

**Evidence:** `} from "../types.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 822. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in control-ui-bootstrap.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/control-ui-bootstrap.ts:4`

**Evidence:** `} from "../../../../src/gateway/control-ui-contract.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 823. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in cron.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/cron.ts:18`

**Evidence:** `} from "../types.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 824. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in device-auth.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/device-auth.ts:6`

**Evidence:** `} from "../../../src/shared/device-auth-store.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 825. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in gateway.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/gateway.ts:7`

**Evidence:** `} from "../../../src/gateway/protocol/client-info.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 826. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in tool-display.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/tool-display.ts:8`

**Evidence:** `} from "../../../src/agents/tool-display-common.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 827. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in types.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/types.ts:1`

**Evidence:** `export type UpdateAvailable = import("../../../src/infra/update-startup.js").UpdateAvailable;`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 828. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in usage-types.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/usage-types.ts:4`

**Evidence:** `} from "../../../src/shared/session-usage-timeseries-types.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 829. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents-panels-status-files.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/agents-panels-status-files.ts:8`

**Evidence:** `} from "../presenter.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 830. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents-utils.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/agents-utils.ts:5`

**Evidence:** `} from "../../../../src/agents/tool-catalog.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 831. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in agents.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/agents.ts:11`

**Evidence:** `} from "../types.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 832. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/channels.ts:16`

**Evidence:** `} from "../types.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 833. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in channels.types.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/channels.types.ts:14`

**Evidence:** `} from "../types.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 834. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in chat.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/chat.ts:8`

**Evidence:** `} from "../chat/grouped-render.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 835. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in cron.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/cron.ts:9`

**Evidence:** `} from "../controllers/cron.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 836. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nodes-exec-approvals.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/nodes-exec-approvals.ts:5`

**Evidence:** `} from "../controllers/exec-approvals.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 837. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in nodes.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/nodes.ts:7`

**Evidence:** `} from "../controllers/devices.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 838. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in usage-metrics.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/usage-metrics.ts:6`

**Evidence:** `} from "../../../../src/shared/usage-aggregates.js";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 839. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in usageTypes.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/views/usageTypes.ts:7`

**Evidence:** `} from "../usage-types.ts";`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 840. [INJECT-003] Path Traversal

**Severity:** 🟡 WARN
| **CWE:** CWE-22

**Detail:** Path Traversal detected in vite.config.ts

**Location:** `/Users/peter/llms/openclaw/ui/vite.config.ts:31`

**Evidence:** `outDir: path.resolve(here, "../dist/control-ui"),`

**Remediation:** Canonicalise and validate paths against an allowed base directory.

---

### 841. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in send.ts

**Location:** `/Users/peter/llms/openclaw/extensions/bluebubbles/src/send.ts:117`

**Evidence:** `const parsed = JSON.parse(body) as unknown;`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 842. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in slash-commands.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/slash-commands.ts:427`

**Evidence:** `const parsed = JSON.parse(body) as Record<string, unknown>;`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 843. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in slash-state.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/slash-state.ts:248`

**Evidence:** `token = (JSON.parse(bodyStr) as { token?: string }).token ?? null;`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 844. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/nextcloud-talk/src/monitor.ts:55`

**Evidence:** `const data = JSON.parse(body);`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 845. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in webhook-handler.ts

**Location:** `/Users/peter/llms/openclaw/extensions/synology-chat/src/webhook-handler.ts:112`

**Evidence:** `const parsed = JSON.parse(body);`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 846. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in web-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/web-fetch.ts:644`

**Evidence:** `text = JSON.stringify(JSON.parse(body), null, 2);`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 847. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in client-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/client-fetch.ts:260`

**Evidence:** `body = JSON.parse(body);`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 848. [INJECT-004] Unsafe Deserialization

**Severity:** 🟡 WARN
| **CWE:** CWE-502

**Detail:** Unsafe Deserialization detected in test-helpers.openai-mock.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/test-helpers.openai-mock.ts:227`

**Evidence:** `const parsed = bodyText ? (JSON.parse(bodyText) as Record<string, unknown>) : {};`

**Remediation:** Validate and sanitise input before deserialisation. Use yaml.safe_load instead of yaml.load.

---

### 849. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in background.js

**Location:** `/Users/peter/llms/openclaw/assets/chrome-extension/background.js:1010`

**Evidence:** `fetch(url, { method: 'GET', headers, signal: AbortSignal.timeout(2000) })`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 850. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in chat.ts

**Location:** `/Users/peter/llms/openclaw/extensions/bluebubbles/src/chat.ts:33`

**Evidence:** `async function sendBlueBubblesChatEndpointRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 851. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/bluebubbles/src/monitor.ts:43`

**Evidence:** `const handled = await handleBlueBubblesWebhookRequest(req, res);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 852. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in types.ts

**Location:** `/Users/peter/llms/openclaw/extensions/bluebubbles/src/types.ts:133`

**Evidence:** `return await fetch(url, { ...init, signal: controller.signal });`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 853. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in notify.ts

**Location:** `/Users/peter/llms/openclaw/extensions/device-pair/notify.ts:278`

**Evidence:** `if (!shouldNotifySubscriberForRequest(subscriber, request)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 854. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in bot.ts

**Location:** `/Users/peter/llms/openclaw/extensions/feishu/src/bot.ts:807`

**Evidence:** `if (isMentionForwardRequest(event, botOpenId)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 855. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in client.ts

**Location:** `/Users/peter/llms/openclaw/extensions/feishu/src/client.ts:52`

**Evidence:** `request: (opts) => base.request(injectTimeout(opts)),`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 856. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in mention.ts

**Location:** `/Users/peter/llms/openclaw/extensions/feishu/src/mention.ts:50`

**Evidence:** `export function isMentionForwardRequest(event: FeishuMessageEvent, botOpenId?: string): boolean {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 857. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.account.ts

**Location:** `/Users/peter/llms/openclaw/extensions/feishu/src/monitor.account.ts:211`

**Evidence:** `if (isMentionForwardRequest(entry, botOpenId)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 858. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in probe.ts

**Location:** `/Users/peter/llms/openclaw/extensions/feishu/src/probe.ts:77`

**Evidence:** `(client as any).request({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 859. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in auth.ts

**Location:** `/Users/peter/llms/openclaw/extensions/googlechat/src/auth.ts:82`

**Evidence:** `const res = await fetch(CHAT_CERTS_URL);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 860. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor-webhook.ts

**Location:** `/Users/peter/llms/openclaw/extensions/googlechat/src/monitor-webhook.ts:131`

**Evidence:** `const verification = await verifyGoogleChatRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 861. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/googlechat/src/monitor.ts:59`

**Evidence:** `const handled = await handleGoogleChatWebhookRequest(req, res);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 862. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/monitor.ts:1049`

**Evidence:** `const { code } = await pairing.upsertPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 863. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in probe.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/probe.ts:27`

**Evidence:** `const res = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 864. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in slash-http.ts

**Location:** `/Users/peter/llms/openclaw/extensions/mattermost/src/mattermost/slash-http.ts:164`

**Evidence:** `const { code } = await core.channel.pairing.upsertPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 865. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in oauth.ts

**Location:** `/Users/peter/llms/openclaw/extensions/minimax-portal-auth/oauth.ts:68`

**Evidence:** `const response = await fetch(endpoints.codeEndpoint, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 866. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/attachments/shared.ts:351`

**Evidence:** `export async function safeFetch(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 867. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in message-handler.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/monitor-handler/message-handler.ts:213`

**Evidence:** `const request = await pairing.upsertPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 868. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.test-fixtures.ts

**Location:** `/Users/peter/llms/openclaw/extensions/nextcloud-talk/src/monitor.test-fixtures.ts:3`

**Evidence:** `export function createSignedCreateMessageRequest(params?: { backend?: string }) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 869. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in send.ts

**Location:** `/Users/peter/llms/openclaw/extensions/nextcloud-talk/src/send.ts:108`

**Evidence:** `const response = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 870. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in oauth.ts

**Location:** `/Users/peter/llms/openclaw/extensions/qwen-portal-auth/oauth.ts:38`

**Evidence:** `const response = await fetch(QWEN_OAUTH_DEVICE_CODE_ENDPOINT, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 871. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in webhook-handler.ts

**Location:** `/Users/peter/llms/openclaw/extensions/synology-chat/src/webhook-handler.ts:248`

**Evidence:** `* 6. Immediately ACKs request (204)`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 872. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in channel.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/channel.ts:58`

**Evidence:** `const { response, release } = await urbitFetch({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 873. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in approval.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/monitor/approval.ts:68`

**Evidence:** `export function formatApprovalRequest(approval: PendingApproval): string {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 874. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in index.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/monitor/index.ts:588`

**Evidence:** `async function queueApprovalRequest(approval: PendingApproval): Promise<void> {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 875. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in utils.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/monitor/utils.ts:324`

**Evidence:** `export function isSummarizationRequest(messageText: string): boolean {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 876. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in auth.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/urbit/auth.ts:17`

**Evidence:** `const { response, release } = await urbitFetch({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 877. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in channel-ops.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/urbit/channel-ops.ts:29`

**Evidence:** `const { response, release } = await urbitFetch({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 878. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in fetch.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/urbit/fetch.ts:20`

**Evidence:** `export async function urbitFetch(params: UrbitFetchOptions) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 879. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in sse-client.ts

**Location:** `/Users/peter/llms/openclaw/extensions/tlon/src/urbit/sse-client.ts:118`

**Evidence:** `const { response, release } = await urbitFetch({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 880. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in index.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/index.ts:267`

**Evidence:** `const request = await resolveCallMessageRequest(params);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 881. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in plivo.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/plivo.ts:340`

**Evidence:** `await this.apiRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 882. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in twilio.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/providers/twilio.ts:110`

**Evidence:** `* webhook request (notify mode). Subsequent webhooks should not reuse it.`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 883. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in webhook-security.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/webhook-security.ts:162`

**Evidence:** `* The IP address of the incoming request (for proxy validation).`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 884. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in webhook.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/webhook.ts:225`

**Evidence:** `this.handleRequest(req, res, webhookPath).catch((err) => {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 885. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in channel.ts

**Location:** `/Users/peter/llms/openclaw/extensions/zalo/src/channel.ts:314`

**Evidence:** `probeZalo(account.token, timeoutMs, resolveZaloProxyFetch(account.config.proxy)),`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 886. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/zalo/src/monitor.ts:116`

**Evidence:** `const handled = await handleZaloWebhookRequest(req, res);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 887. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in proxy.ts

**Location:** `/Users/peter/llms/openclaw/extensions/zalo/src/proxy.ts:7`

**Evidence:** `export function resolveZaloProxyFetch(proxyUrl?: string | null): ZaloFetch | undefined {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 888. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in send.ts

**Location:** `/Users/peter/llms/openclaw/extensions/zalo/src/send.ts:35`

**Evidence:** `return { token, fetcher: resolveZaloProxyFetch(proxy) };`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 889. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in firecrawl-compare.ts

**Location:** `/Users/peter/llms/openclaw/scripts/firecrawl-compare.ts:37`

**Evidence:** `const res = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 890. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in readability-basic-compare.ts

**Location:** `/Users/peter/llms/openclaw/scripts/readability-basic-compare.ts:14`

**Evidence:** `async function runFetch(url: string, readability: boolean) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 891. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in client.ts

**Location:** `/Users/peter/llms/openclaw/src/acp/client.ts:548`

**Evidence:** `return resolvePermissionRequest(params, { cwd });`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 892. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in bash-tools.exec-approval-request.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/bash-tools.exec-approval-request.ts:144`

**Evidence:** `const registration = await registerExecApprovalRequest(params);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 893. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in kilocode-models.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/kilocode-models.ts:142`

**Evidence:** `const response = await fetch(KILOCODE_MODELS_URL, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 894. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in minimax-vlm.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/minimax-vlm.ts:76`

**Evidence:** `const res = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 895. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in models-config.providers.discovery.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/models-config.providers.discovery.ts:112`

**Evidence:** `const response = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 896. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in ollama-stream.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/ollama-stream.ts:482`

**Evidence:** `const response = await fetch(chatUrl, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 897. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in openai-ws-stream.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/openai-ws-stream.ts:853`

**Evidence:** `new Error(`WebSocket closed mid-request (code=${code}, reason=${reason || "unknown"})`),`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 898. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in openclaw-tools.subagents.sessions-spawn.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/openclaw-tools.subagents.sessions-spawn.test-harness.ts:43`

**Evidence:** `export function findGatewayRequest(method: string): GatewayRequest | undefined {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 899. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/sandbox/browser.ts:49`

**Evidence:** `const res = await fetch(url, { signal: ctrl.signal });`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 900. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser-tool.actions.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/browser-tool.actions.ts:95`

**Evidence:** `const result = await proxyRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 901. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser-tool.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/browser-tool.ts:364`

**Evidence:** `await proxyRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 902. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in pdf-native-providers.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/pdf-native-providers.ts:145`

**Evidence:** `const res = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 903. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in web-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/agents/tools/web-fetch.ts:385`

**Evidence:** `const res = await fetch(endpoint, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 904. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in bash-command.ts

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/bash-command.ts:62`

**Evidence:** `function parseBashRequest(raw: string): BashRequest | null {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 905. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in cdp.helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/cdp.helpers.ts:173`

**Evidence:** `fetch(url, { ...init, headers, signal: ctrl.signal }),`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 906. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in client-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/client-fetch.ts:214`

**Evidence:** `const res = await fetch(url, { ...init, signal: ctrl.signal });`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 907. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in extension-relay-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/extension-relay-auth.ts:98`

**Evidence:** `const res = await fetch(versionUrl, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 908. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in extension-relay.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/extension-relay.ts:102`

**Evidence:** `function getRelayAuthTokenFromRequest(req: IncomingMessage, url?: URL): string | undefined {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 909. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in agent.storage.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.storage.ts:34`

**Evidence:** `const parsed = parseStorageMutationRequest(kindParam, body);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 910. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in server-middleware.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/server-middleware.ts:32`

**Evidence:** `if (isAuthorizedBrowserRequest(req, auth)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 911. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in server.agent-contract.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/server.agent-contract.test-harness.ts:20`

**Evidence:** `const res = await realFetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 912. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in server.ts

**Location:** `/Users/peter/llms/openclaw/src/canvas-host/server.ts:421`

**Evidence:** `if (await handleA2uiHttpRequest(req, res)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 913. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in api.ts

**Location:** `/Users/peter/llms/openclaw/src/channels/telegram/api.ts:8`

**Evidence:** `const res = await fetch(url, params.signal ? { signal: params.signal } : undefined);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 914. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser-cli-debug.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-debug.ts:82`

**Evidence:** `const result = await callDebugRequest(parent, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 915. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser-cli-manage.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-manage.ts:66`

**Evidence:** `await callBrowserRequest(parent, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 916. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser-cli-state.cookies-storage.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-state.cookies-storage.ts:31`

**Evidence:** `async function runMutationRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 917. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in browser-cli-state.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/browser-cli-state.ts:22`

**Evidence:** `async function runBrowserSetRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 918. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in devices-cli.ts

**Location:** `/Users/peter/llms/openclaw/src/cli/devices-cli.ts:179`

**Evidence:** `function selectLatestPendingRequest(pending: PendingDevice[] | undefined) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 919. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in session.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent/session.ts:43`

**Evidence:** `export function resolveSessionKeyForRequest(opts: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 920. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in agent-via-gateway.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/agent-via-gateway.ts:113`

**Evidence:** `const sessionKey = resolveSessionKeyForRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 921. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in configure.wizard.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/configure.wizard.ts:282`

**Evidence:** `message: "Enable web_fetch (keyless HTTP fetch)?",`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 922. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in signal-install.ts

**Location:** `/Users/peter/llms/openclaw/src/commands/signal-install.ts:97`

**Evidence:** `const req = request(url, (res) => {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 923. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in schema.help.ts

**Location:** `/Users/peter/llms/openclaw/src/config/schema.help.ts:396`

**Evidence:** `"Max cumulative decoded bytes across all `image_url` parts in one request (default: 20MB).",`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 924. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in api.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/api.ts:102`

**Evidence:** `const fetchImpl = resolveFetch(fetcher);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 925. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in agent-components.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/agent-components.ts:535`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 926. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in dm-command-decision.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/dm-command-decision.ts:32`

**Evidence:** `await upsertPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 927. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in provider.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/provider.ts:309`

**Evidence:** `const discordRestFetch = resolveDiscordRestFetch(rawDiscordCfg.proxy, runtime);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 928. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in rest-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor/rest-fetch.ts:17`

**Evidence:** `undiciFetch(input as string | URL, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 929. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.tool-result.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/monitor.tool-result.test-harness.ts:33`

**Evidence:** `upsertChannelPairingRequest(...args: unknown[]) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 930. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in pluralkit.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/pluralkit.ts:38`

**Evidence:** `const fetchImpl = resolveFetch(params.fetcher);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 931. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in probe.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/probe.ts:65`

**Evidence:** `getResolvedFetch(fetcher),`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 932. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in voice-message.ts

**Location:** `/Users/peter/llms/openclaw/src/discord/voice-message.ts:262`

**Evidence:** `const uploadUrlResponse = await request(async () => {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 933. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in auth.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/auth.ts:177`

**Evidence:** `function isTailscaleProxyRequest(req?: IncomingMessage): boolean {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 934. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in control-ui-routing.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/control-ui-routing.ts:11`

**Evidence:** `export function classifyControlUiRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 935. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in control-ui.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/control-ui.ts:311`

**Evidence:** `const route = classifyControlUiRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 936. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in hooks-test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/hooks-test-helpers.ts:23`

**Evidence:** `export function createGatewayRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 937. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in http-common.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/http-common.ts:67`

**Evidence:** `export function sendInvalidRequest(res: ServerResponse, message: string) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 938. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in http-utils.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/http-utils.ts:53`

**Evidence:** `export function resolveAgentIdForRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 939. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in node-invoke-system-run-approval.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/node-invoke-system-run-approval.ts:120`

**Evidence:** `const cmdTextResolution = resolveSystemRunCommandRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 940. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in openai-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/openai-http.ts:389`

**Evidence:** `function coerceRequest(val: unknown): OpenAiChatCompletionRequest {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 941. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in http-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/http-auth.ts:58`

**Evidence:** `export async function authorizeCanvasRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 942. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in message-handler.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server/ws-connection/message-handler.ts:324`

**Evidence:** `const isLocalClient = isLocalDirectRequest(upgradeReq, trustedProxies, allowRealIpFallback);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 943. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in server-http.test-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-http.test-harness.ts:27`

**Evidence:** `export function createRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 944. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in server-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-http.ts:166`

**Evidence:** `if (isLocalDirectRequest(params.req, params.trustedProxies, params.allowRealIpFallback)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 945. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in config.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-methods/config.ts:187`

**Evidence:** `function resolveConfigRestartRequest(params: unknown): {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 946. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in server-plugins.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/server-plugins.ts:81`

**Evidence:** `await handleGatewayRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 947. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in test-helpers.openai-mock.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/test-helpers.openai-mock.ts:219`

**Evidence:** `if (isResponsesRequest(url)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 948. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in tools-invoke-http.ts

**Location:** `/Users/peter/llms/openclaw/src/gateway/tools-invoke-http.ts:180`

**Evidence:** `sendInvalidRequest(res, "tools.invoke requires body.tool");`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 949. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor-provider.ts

**Location:** `/Users/peter/llms/openclaw/src/imessage/monitor/monitor-provider.ts:300`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 950. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in device-pairing.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/device-pairing.ts:291`

**Evidence:** `const merged = mergePendingDevicePairingRequest(existing, req, isRepair);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 951. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/fetch.ts:103`

**Evidence:** `export function resolveFetch(fetchImpl?: typeof fetch): typeof fetch | undefined {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 952. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in fetch-guard.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/net/fetch-guard.ts:247`

**Evidence:** ``security: blocked URL fetch (${context}) target=${parsedUrl.origin}${parsedUrl.pathname} reason=${err.message}`,`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 953. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in proxy-fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/net/proxy-fetch.ts:14`

**Evidence:** `export function makeProxyFetch(proxyUrl: string): typeof fetch {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 954. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in node-pairing.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/node-pairing.ts:119`

**Evidence:** `return await upsertPendingPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 955. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in pairing-files.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/pairing-files.ts:46`

**Evidence:** `const request = params.createRequest(params.isRepair);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 956. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in provider-usage.load.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/provider-usage.load.ts:38`

**Evidence:** `const fetchFn = resolveFetch(opts.fetch);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 957. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in push-apns.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/push-apns.ts:300`

**Evidence:** `async function sendApnsRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 958. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in system-run-approval-context.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/system-run-approval-context.ts:136`

**Evidence:** `const command = resolveSystemRunCommandRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 959. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in system-run-command.ts

**Location:** `/Users/peter/llms/openclaw/src/infra/system-run-command.ts:212`

**Evidence:** `export function resolveSystemRunCommandRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 960. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in bot-handlers.ts

**Location:** `/Users/peter/llms/openclaw/src/line/bot-handlers.ts:253`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 961. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in webhook-node.ts

**Location:** `/Users/peter/llms/openclaw/src/line/webhook-node.ts:85`

**Evidence:** `if (isLineWebhookVerificationRequest(body)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 962. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in webhook.ts

**Location:** `/Users/peter/llms/openclaw/src/line/webhook.ts:49`

**Evidence:** `if (isLineWebhookVerificationRequest(body)) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 963. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in audio.test-helpers.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/audio.test-helpers.ts:45`

**Evidence:** `export function createAuthCaptureJsonFetch(responseBody: unknown) {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 964. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in audio.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/deepgram/audio.ts:58`

**Evidence:** `const { response: res, release } = await postTranscriptionRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 965. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in inline-data.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/google/inline-data.ts:64`

**Evidence:** `const { response: res, release } = await postJsonRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 966. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in video.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/moonshot/video.ts:87`

**Evidence:** `const { response: res, release } = await postJsonRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 967. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in audio.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/openai/audio.ts:47`

**Evidence:** `const { response: res, release } = await postTranscriptionRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 968. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in shared.ts

**Location:** `/Users/peter/llms/openclaw/src/media-understanding/providers/shared.ts:35`

**Evidence:** `export async function postTranscriptionRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 969. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in batch-voyage.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/batch-voyage.ts:105`

**Evidence:** `buildVoyageBatchRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 970. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in embeddings-gemini.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/embeddings-gemini.ts:64`

**Evidence:** `export function buildGeminiTextEmbeddingRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 971. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in manager-embedding-ops.ts

**Location:** `/Users/peter/llms/openclaw/src/memory/manager-embedding-ops.ts:509`

**Evidence:** `request: buildGeminiEmbeddingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 972. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in invoke-system-run-plan.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-system-run-plan.ts:735`

**Evidence:** `const command = resolveSystemRunCommandRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 973. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in invoke-system-run.ts

**Location:** `/Users/peter/llms/openclaw/src/node-host/invoke-system-run.ts:191`

**Evidence:** `const command = resolveSystemRunCommandRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 974. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in pairing-challenge.ts

**Location:** `/Users/peter/llms/openclaw/src/pairing/pairing-challenge.ts:27`

**Evidence:** `const { code, created } = await params.upsertPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 975. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in pairing-store.ts

**Location:** `/Users/peter/llms/openclaw/src/pairing/pairing-store.ts:697`

**Evidence:** `export async function upsertChannelPairingRequest(params: {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 976. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in pairing-access.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/pairing-access.ts:30`

**Evidence:** `params.core.channel.pairing.upsertPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 977. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in webhook-targets.ts

**Location:** `/Users/peter/llms/openclaw/src/plugin-sdk/webhook-targets.ts:273`

**Evidence:** `export function rejectNonPostWebhookRequest(req: IncomingMessage, res: ServerResponse): boolean {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 978. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in runtime-channel.ts

**Location:** `/Users/peter/llms/openclaw/src/plugins/runtime/runtime-channel.ts:155`

**Evidence:** `upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 979. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in github-copilot-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/providers/github-copilot-auth.ts:46`

**Evidence:** `const res = await fetch(DEVICE_CODE_URL, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 980. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in qwen-portal-oauth.ts

**Location:** `/Users/peter/llms/openclaw/src/providers/qwen-portal-oauth.ts:16`

**Evidence:** `const response = await fetch(QWEN_OAUTH_TOKEN_ENDPOINT, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 981. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in access-policy.ts

**Location:** `/Users/peter/llms/openclaw/src/signal/monitor/access-policy.ts:71`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 982. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in dm-auth.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/dm-auth.ts:46`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 983. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in media.ts

**Location:** `/Users/peter/llms/openclaw/src/slack/monitor/media.ts:53`

**Evidence:** `function createSlackMediaFetch(token: string): FetchLike {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 984. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in audit-membership-runtime.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/audit-membership-runtime.ts:20`

**Evidence:** `const proxyFetch = params.proxyUrl ? makeProxyFetch(params.proxyUrl) : undefined;`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 985. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in bot.media.e2e-harness.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot.media.e2e-harness.ts:10`

**Evidence:** `globalThis.fetch(input, init),`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 986. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in bot.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/bot.ts:101`

**Evidence:** `const fetchImpl = resolveTelegramFetch(opts.proxyFetch, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 987. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in dm-access.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/dm-access.ts:83`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 988. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in fetch.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/fetch.ts:258`

**Evidence:** `function resolveWrappedFetch(fetchImpl: typeof fetch): typeof fetch {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 989. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/monitor.ts:114`

**Evidence:** `opts.proxyFetch ?? (account.config.proxy ? makeProxyFetch(account.config.proxy) : undefined);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 990. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in network-errors.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/network-errors.ts:55`

**Evidence:** `/^network request(?:\s+for\s+["']?[^"']+["']?)?\s+failed\s+after\b.*[!.]?$/i;`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 991. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in probe.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/probe.ts:84`

**Evidence:** `const proxyFetch = proxyUrl ? makeProxyFetch(proxyUrl) : undefined;`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 992. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in send.ts

**Location:** `/Users/peter/llms/openclaw/src/telegram/send.ts:233`

**Evidence:** `const proxyFetch = proxyUrl ? makeProxyFetch(proxyUrl) : undefined;`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 993. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in tts-core.ts

**Location:** `/Users/peter/llms/openclaw/src/tts/tts-core.ts:595`

**Evidence:** `const response = await fetch(url.toString(), {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 994. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in access-control.ts

**Location:** `/Users/peter/llms/openclaw/src/web/inbound/access-control.ts:180`

**Evidence:** `await upsertChannelPairingRequest({`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 995. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in mock-incoming-request.ts

**Location:** `/Users/peter/llms/openclaw/test/helpers/mock-incoming-request.ts:4`

**Evidence:** `export function createMockIncomingRequest(chunks: string[]): IncomingMessage {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 996. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in app-channels.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/app-channels.ts:153`

**Evidence:** `const response = await fetch(buildNostrProfileUrl(accountId), {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 997. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in app-chat.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/app-chat.ts:255`

**Evidence:** `const res = await fetch(url, { method: "GET" });`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 998. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in control-ui-bootstrap.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/control-ui-bootstrap.ts:30`

**Evidence:** `const res = await fetch(url, {`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 999. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in debug.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/debug.ts:55`

**Evidence:** `const res = await state.client.request(state.debugCallMethod.trim(), params);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 1000. [INJECT-005] SSRF Risk

**Severity:** 🟡 WARN
| **CWE:** CWE-918

**Detail:** SSRF Risk detected in exec-approvals.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/controllers/exec-approvals.ts:137`

**Evidence:** `await state.client.request(rpc.method, rpc.params);`

**Remediation:** Validate and allowlist URLs before making outbound requests. Block internal/private IP ranges.

---

### 1001. [INJECT-006] Dangerous innerHTML

**Severity:** 🟡 WARN
| **CWE:** CWE-79

**Detail:** Dangerous innerHTML detected in viewer-client.ts

**Location:** `/Users/peter/llms/openclaw/extensions/diffs/src/viewer-client.ts:99`

**Evidence:** `button.innerHTML = params.iconMarkup;`

**Remediation:** Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.

---

### 1002. [INJECT-006] Dangerous innerHTML

**Severity:** 🟡 WARN
| **CWE:** CWE-79

**Detail:** Dangerous innerHTML detected in template.js

**Location:** `/Users/peter/llms/openclaw/src/auto-reply/reply/export-html/template.js:813`

**Evidence:** `container.innerHTML = "";`

**Remediation:** Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.

---

### 1003. [INJECT-006] Dangerous innerHTML

**Severity:** 🟡 WARN
| **CWE:** CWE-79

**Detail:** Dangerous innerHTML detected in cdp.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/cdp.ts:450`

**Evidence:** `let outerHTML = "";`

**Remediation:** Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.

---

### 1004. [INJECT-006] Dangerous innerHTML

**Severity:** 🟡 WARN
| **CWE:** CWE-79

**Detail:** Dangerous innerHTML detected in server.ts

**Location:** `/Users/peter/llms/openclaw/src/canvas-host/server.ts:113`

**Evidence:** `statusEl.innerHTML =`

**Remediation:** Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.

---

### 1005. [INJECT-006] Dangerous innerHTML

**Severity:** 🟡 WARN
| **CWE:** CWE-79

**Detail:** Dangerous innerHTML detected in app-mount.ts

**Location:** `/Users/peter/llms/openclaw/ui/src/ui/test-helpers/app-mount.ts:20`

**Evidence:** `document.body.innerHTML = "";`

**Remediation:** Use textContent or a sanitisation library (e.g. DOMPurify) instead of innerHTML.

---

### 1006. [LOG-001] Sensitive Data in Logs

**Severity:** 🟡 WARN
| **CWE:** CWE-532

**Detail:** Sensitive Data in Logs detected in twitch-client.ts

**Location:** `/Users/peter/llms/openclaw/extensions/twitch/src/twitch-client.ts:59`

**Evidence:** `this.logger.error(`Failed to refresh access token for user ${userId}: ${error.message}`);`

**Remediation:** Redact or mask sensitive values before logging. Use structured logging with field filtering.

---

### 1007. [LOG-001] Sensitive Data in Logs

**Severity:** 🟡 WARN
| **CWE:** CWE-532

**Detail:** Sensitive Data in Logs detected in webhook.ts

**Location:** `/Users/peter/llms/openclaw/extensions/voice-call/src/webhook.ts:120`

**Evidence:** `console.warn(`[voice-call] Rejecting media stream: invalid token for ${callId}`);`

**Remediation:** Redact or mask sensitive values before logging. Use structured logging with field filtering.

---

### 1008. [LOG-001] Sensitive Data in Logs

**Severity:** 🟡 WARN
| **CWE:** CWE-532

**Detail:** Sensitive Data in Logs detected in debug-claude-usage.ts

**Location:** `/Users/peter/llms/openclaw/scripts/debug-claude-usage.ts:346`

**Evidence:** `console.log("Auth profiles: no Anthropic token profiles found");`

**Remediation:** Redact or mask sensitive values before logging. Use structured logging with field filtering.

---

### 1009. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `docker-setup.sh:236`

**Evidence:** `TOKE***ue)"`

**Remediation:** Use env vars or secrets manager

---

### 1010. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `extensions/nextcloud-talk/src/monitor.test-fixtures.ts:19`

**Evidence:** `secr***ret"`

**Remediation:** Use env vars or secrets manager

---

### 1011. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `scripts/e2e/gateway-network-docker.sh:8`

**Evidence:** `TOKE***-$$"`

**Remediation:** Use env vars or secrets manager

---

### 1012. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `scripts/run-openclaw-podman.sh:146`

**Evidence:** `TOKE***32)"`

**Remediation:** Use env vars or secrets manager

---

### 1013. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `scripts/test-install-sh-e2e-docker.sh:26`

**Evidence:** `API_***KEY"`

**Remediation:** Use env vars or secrets manager

---

### 1014. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `setup-podman.sh:237`

**Evidence:** `TOKE***32)"`

**Remediation:** Use env vars or secrets manager

---

### 1015. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/agents/pi-embedded-runner/model.ts:297`

**Evidence:** `API_***cal"`

**Remediation:** Use env vars or secrets manager

---

### 1016. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/agents/tools/sessions-send-helpers.ts:8`

**Evidence:** `TOKE***KIP"`

**Remediation:** Use env vars or secrets manager

---

### 1017. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/auto-reply/tokens.ts:3`

**Evidence:** `TOKE***_OK"`

**Remediation:** Use env vars or secrets manager

---

### 1018. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/commands/auth-choice.preferred-provider.ts:7`

**Evidence:** `toke***pic"`

**Remediation:** Use env vars or secrets manager

---

### 1019. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/commands/ollama-setup.ts:269`

**Evidence:** `apiK***KEY"`

**Remediation:** Use env vars or secrets manager

---

### 1020. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/commands/onboard-auth.config-minimax.ts:37`

**Evidence:** `apiK***dio"`

**Remediation:** Use env vars or secrets manager

---

### 1021. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/commands/vllm-setup.ts:60`

**Evidence:** `apiK***KEY"`

**Remediation:** Use env vars or secrets manager

---

### 1022. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/gateway/auth-rate-limit.ts:39`

**Evidence:** `SECR***ret"`

**Remediation:** Use env vars or secrets manager

---

### 1023. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/gateway/hooks-test-helpers.ts:7`

**Evidence:** `toke***ret"`

**Remediation:** Use env vars or secrets manager

---

### 1024. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/gateway/server.auth.control-ui.suite.ts:410`

**Evidence:** `Toke***ken"`

**Remediation:** Use env vars or secrets manager

---

### 1025. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `src/line/bot-handlers.ts:401`

**Evidence:** `Toke***ken"`

**Remediation:** Use env vars or secrets manager

---

### 1026. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `ui/src/i18n/locales/de.ts:60`

**Evidence:** `toke***ken"`

**Remediation:** Use env vars or secrets manager

---

### 1027. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `ui/src/i18n/locales/en.ts:60`

**Evidence:** `toke***ken"`

**Remediation:** Use env vars or secrets manager

---

### 1028. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `ui/src/i18n/locales/es.ts:60`

**Evidence:** `toke***ace"`

**Remediation:** Use env vars or secrets manager

---

### 1029. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `ui/src/i18n/locales/pt-BR.ts:60`

**Evidence:** `toke***way"`

**Remediation:** Use env vars or secrets manager

---

### 1030. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `ui/src/i18n/locales/zh-CN.ts:61`

**Evidence:** `pass***存储)"`

**Remediation:** Use env vars or secrets manager

---

### 1031. [SECRET-006] Generic Password

**Severity:** 🟡 WARN
| **CWE:** CWE-798

**Detail:** Hardcoded secret detected: Generic Password

**Location:** `ui/src/i18n/locales/zh-TW.ts:61`

**Evidence:** `pass***存儲)"`

**Remediation:** Use env vars or secrets manager

---

### 1032. [SKILL-003] Gateway Control Escalation

**Severity:** 🟡 WARN
| **CWE:** CWE-269

**Detail:** Gateway Control Escalation detected in skills/aliclawscan/references/rule-catalog.md

**Location:** `skills/aliclawscan/references/rule-catalog.md:62`

**Evidence:** `ws://127.0.0.1:18789`

**Remediation:** Skills should not directly control the gateway; use approved APIs

---

### 1033. [SKILL-003] Gateway Control Escalation

**Severity:** 🟡 WARN
| **CWE:** CWE-269

**Detail:** Gateway Control Escalation detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:8314`

**Evidence:** `gateway/server-restart`

**Remediation:** Skills should not directly control the gateway; use approved APIs

---

### 1034. [SKILL-003] Gateway Control Escalation

**Severity:** 🟡 WARN
| **CWE:** CWE-269

**Detail:** Gateway Control Escalation detected in skills/aliclawscan/report-optimized.md

**Location:** `skills/aliclawscan/report-optimized.md:8770`

**Evidence:** `gateway/server-restart`

**Remediation:** Skills should not directly control the gateway; use approved APIs

---

### 1035. [SKILL-003] Gateway Control Escalation

**Severity:** 🟡 WARN
| **CWE:** CWE-269

**Detail:** Gateway Control Escalation detected in skills/aliclawscan/report.md

**Location:** `skills/aliclawscan/report.md:32388`

**Evidence:** `gateway/server-restart`

**Remediation:** Skills should not directly control the gateway; use approved APIs

---

### 1036. [SKILL-003] Gateway Control Escalation

**Severity:** 🟡 WARN
| **CWE:** CWE-269

**Detail:** Gateway Control Escalation detected in skills/aliclawscan/scripts/scanners/skill_scanner.py

**Location:** `skills/aliclawscan/scripts/scanners/skill_scanner.py:52`

**Evidence:** `gateway.*restart`

**Remediation:** Skills should not directly control the gateway; use approved APIs

---

### 1037. [SKILL-003] Gateway Control Escalation

**Severity:** 🟡 WARN
| **CWE:** CWE-269

**Detail:** Gateway Control Escalation detected in skills/bluebubbles/SKILL.md

**Location:** `skills/bluebubbles/SKILL.md:124`

**Evidence:** `gateway may expose both short and full message ids; full ids are more durable across restart`

**Remediation:** Skills should not directly control the gateway; use approved APIs

---

### 1038. [SKILL-004] Broad Tool Permissions

**Severity:** 🟡 WARN
| **CWE:** CWE-250

**Detail:** Broad Tool Permissions detected in skills/aliclawscan/references/rule-catalog.md

**Location:** `skills/aliclawscan/references/rule-catalog.md:19`

**Evidence:** `dangerouslySkipPermissions`

**Remediation:** Restrict tool permissions to minimum required set

---

### 1039. [SKILL-004] Broad Tool Permissions

**Severity:** 🟡 WARN
| **CWE:** CWE-250

**Detail:** Broad Tool Permissions detected in skills/aliclawscan/report-optimized.json

**Location:** `skills/aliclawscan/report-optimized.json:14085`

**Evidence:** `dangerouslySkipPermissions`

**Remediation:** Restrict tool permissions to minimum required set

---

### 1040. [SKILL-004] Broad Tool Permissions

**Severity:** 🟡 WARN
| **CWE:** CWE-250

**Detail:** Broad Tool Permissions detected in skills/aliclawscan/report-optimized.md

**Location:** `skills/aliclawscan/report-optimized.md:17442`

**Evidence:** `dangerouslySkipPermissions`

**Remediation:** Restrict tool permissions to minimum required set

---

### 1041. [SKILL-004] Broad Tool Permissions

**Severity:** 🟡 WARN
| **CWE:** CWE-250

**Detail:** Broad Tool Permissions detected in skills/aliclawscan/report.md

**Location:** `skills/aliclawscan/report.md:58040`

**Evidence:** `dangerouslySkipPermissions`

**Remediation:** Restrict tool permissions to minimum required set

---

### 1042. [SKILL-004] Broad Tool Permissions

**Severity:** 🟡 WARN
| **CWE:** CWE-250

**Detail:** Broad Tool Permissions detected in skills/aliclawscan/scripts/scanners/config_scanner.py

**Location:** `skills/aliclawscan/scripts/scanners/config_scanner.py:19`

**Evidence:** `dangerouslySkipPermissions`

**Remediation:** Restrict tool permissions to minimum required set

---

### 1043. [SKILL-004] Broad Tool Permissions

**Severity:** 🟡 WARN
| **CWE:** CWE-250

**Detail:** Broad Tool Permissions detected in skills/aliclawscan/scripts/scanners/skill_scanner.py

**Location:** `skills/aliclawscan/scripts/scanners/skill_scanner.py:66`

**Evidence:** `dangerouslySkipPermissions`

**Remediation:** Restrict tool permissions to minimum required set

---

### 1044. [DEP-003] Possible phantom dependency: ${defaultAgentId}

**Severity:** 🔵 INFO

**Detail:** '${defaultAgentId}' is imported in source but not listed in package.json. It may be provided transitively.

**Evidence:** `import from '${defaultAgentId}' not in package.json`

**Remediation:** Add ${defaultAgentId} to dependencies or verify it is intentionally transitive.

---

### 1045. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in monitor.ts

**Location:** `/Users/peter/llms/openclaw/extensions/msteams/src/monitor.ts:295`

**Evidence:** `expressApp.post("/api/messages", messageHandler);`

**Remediation:** Add authentication middleware to route handlers

---

### 1046. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in bridge-server.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/bridge-server.ts:78`

**Evidence:** `app.get("/sandbox/novnc", (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1047. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in agent.act.download.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.act.download.ts:20`

**Evidence:** `app.post("/wait/download", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1048. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in agent.act.hooks.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.act.hooks.ts:11`

**Evidence:** `app.post("/hooks/file-chooser", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1049. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in agent.act.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.act.ts:25`

**Evidence:** `app.post("/act", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1050. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in agent.debug.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.debug.ts:19`

**Evidence:** `app.get("/console", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1051. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in agent.snapshot.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.snapshot.ts:92`

**Evidence:** `app.post("/navigate", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1052. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in agent.storage.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/agent.storage.ts:70`

**Evidence:** `app.get("/cookies", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1053. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in basic.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/basic.ts:32`

**Evidence:** `app.get("/profiles", async (_req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1054. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in tabs.ts

**Location:** `/Users/peter/llms/openclaw/src/browser/routes/tabs.ts:103`

**Evidence:** `app.get("/tabs", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1055. [EXPOSE-003] Unauthenticated Endpoint

**Severity:** 🔵 INFO
| **CWE:** CWE-306

**Detail:** Unauthenticated Endpoint detected in server.ts

**Location:** `/Users/peter/llms/openclaw/src/media/server.ts:35`

**Evidence:** `app.get("/media/:id", async (req, res) => {`

**Remediation:** Add authentication middleware to route handlers

---

### 1056. [SECRET-007] High-Entropy String

**Severity:** 🔵 INFO
| **CWE:** CWE-798

**Detail:** Potential secret with high entropy

**Location:** `src/agents/sandbox/novnc-auth.ts:6`

**Evidence:** `0123***WXYZ`

**Remediation:** Review if this is a secret; use env vars if so

---

### 1057. [SECRET-007] High-Entropy String

**Severity:** 🔵 INFO
| **CWE:** CWE-798

**Detail:** Potential secret with high entropy

**Location:** `src/pairing/pairing-store.ts:14`

**Evidence:** `ABCD***6789`

**Remediation:** Review if this is a secret; use env vars if so

---

## Conclusion

Scan completed with 1057 total findings: 75 critical issue(s) requiring immediate attention; 968 warning(s) that should be reviewed; 14 informational finding(s). Address critical issues before deployment.
