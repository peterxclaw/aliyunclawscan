# aliclawscan Rule Catalog

## Secret Detection

| Rule ID    | Title               | Severity | CWE     | Pattern                           |
| ---------- | ------------------- | -------- | ------- | --------------------------------- |
| SECRET-001 | AWS Access Key      | critical | CWE-798 | `AKIA[0-9A-Z]{16}`                |
| SECRET-002 | AWS Secret Key      | critical | CWE-798 | `aws_secret_access_key = ...`     |
| SECRET-003 | Private Key         | critical | CWE-321 | `-----BEGIN RSA PRIVATE KEY-----` |
| SECRET-004 | JWT Token           | warn     | CWE-522 | `eyJ...` base64 pattern           |
| SECRET-005 | Connection String   | critical | CWE-798 | `mongodb://user:pass@host`        |
| SECRET-006 | Generic Password    | warn     | CWE-798 | `password = "value"`              |
| SECRET-007 | High-Entropy String | info     | CWE-798 | Shannon entropy > 4.5             |

## Configuration

| Rule ID    | Title                | Severity | CWE     | Pattern                            |
| ---------- | -------------------- | -------- | ------- | ---------------------------------- |
| CONFIG-001 | Dangerous Skip Flags | critical | CWE-693 | `dangerouslySkipPermissions: true` |
| CONFIG-002 | Debug Mode Enabled   | warn     | CWE-489 | `debug: true` in config files      |
| CONFIG-003 | No Auth Gateway      | critical | CWE-306 | `requireAuth: false`               |
| CONFIG-004 | Permissive CORS      | warn     | CWE-942 | `allowOrigin: "*"`                 |
| CONFIG-005 | Sandbox Disabled     | critical | CWE-693 | `sandbox: false`                   |
| CONFIG-006 | Insecure TLS         | critical | CWE-295 | `rejectUnauthorized: false`        |

## Code Vulnerabilities

| Rule ID    | Title                  | Severity | CWE     | Pattern                          |
| ---------- | ---------------------- | -------- | ------- | -------------------------------- |
| INJECT-001 | Command Injection      | critical | CWE-78  | `exec()` with string concat      |
| INJECT-002 | eval/Function Usage    | critical | CWE-95  | `eval()`, `new Function()`       |
| INJECT-003 | Path Traversal         | warn     | CWE-22  | `../` or `path.join` with concat |
| INJECT-004 | Unsafe Deserialization | warn     | CWE-502 | `JSON.parse(req.body)`           |
| INJECT-005 | SSRF Risk              | warn     | CWE-918 | `fetch(variable)`                |
| INJECT-006 | Dangerous innerHTML    | warn     | CWE-79  | `innerHTML =`                    |
| INJECT-007 | SQL Injection          | critical | CWE-89  | `query()` with template literal  |
| LOG-001    | Sensitive Data in Logs | warn     | CWE-532 | `console.log(password)`          |
| LOG-002    | Error Stack Exposure   | info     | CWE-209 | `res.send(err.stack)`            |

## Dependencies

| Rule ID | Title               | Severity | CWE | Pattern                           |
| ------- | ------------------- | -------- | --- | --------------------------------- |
| DEP-001 | Known CVE           | varies   | —   | `pnpm audit` findings             |
| DEP-002 | Outdated Dependency | warn     | —   | 2+ major versions behind          |
| DEP-003 | Phantom Dependency  | info     | —   | Import without package.json entry |

## Network Exposure

| Rule ID    | Title                    | Severity | CWE     | Pattern                       |
| ---------- | ------------------------ | -------- | ------- | ----------------------------- |
| EXPOSE-001 | Bind All Interfaces      | warn     | CWE-668 | `0.0.0.0` with listen/bind    |
| EXPOSE-002 | Debug Port Exposed       | warn     | CWE-489 | `--inspect`, `debugger;`      |
| EXPOSE-003 | Unauthenticated Endpoint | info     | CWE-306 | Route without auth middleware |

## Skill Permissions

| Rule ID   | Title                      | Severity | CWE     | Pattern                           |
| --------- | -------------------------- | -------- | ------- | --------------------------------- |
| SKILL-001 | Unsandboxed Exec           | critical | CWE-78  | `subprocess.run()`, `os.system()` |
| SKILL-002 | Sensitive Path Access      | critical | CWE-552 | `/etc/passwd`, `~/.ssh/`          |
| SKILL-003 | Gateway Control Escalation | warn     | CWE-269 | `ws://127.0.0.1:18789`            |
| SKILL-004 | Broad Tool Permissions     | warn     | CWE-250 | `allowedTools: ["*"]`             |
