# Threat Model Template — Capstone Project

**Project**: [Lab Name / Extension Title]  
**Student**: _________________________  
**Date**: _________________________  
**Lab Repo**: _________________________

---

## 1. System Overview

### 1.1 Architecture Diagram
```
[Draw ASCII/text diagram here showing:]
- Components (services, databases, APIs, frontends)
- Data flows (arrows with protocol/port)
- Trust boundaries (dashed lines: e.g., Internet | DMZ | Internal)
- External dependencies (3rd party APIs, auth providers)
```

**Example**:
```
┌─────────────┐     HTTPS/443      ┌──────────────┐
│   Client    │ ──────────────────▶ │  Web App     │
│  (Browser)  │ ◀────────────────── │  (Nginx +    │
└─────────────┘     JSON/REST       │   Flask)     │
                                      └──────┬───────┘
                                             │ SQL/5432
                                             ▼
                                      ┌──────────────┐
                                      │  PostgreSQL  │
                                      │  (User DB)   │
                                      └──────────────┘
```
*Trust Boundaries*: 
- `Internet` ────── (TLS) ────── `Web App`
- `Web App` ────── (Internal VPC) ────── `Database`

### 1.2 Data Flow Description
| Flow | Source | Destination | Protocol | Data Classification |
|------|--------|-------------|----------|---------------------|
| 1 | Client | Web App | HTTPS | Public / Auth tokens |
| 2 | Web App | Database | PostgreSQL | PII, Credentials (hashed) |
| 3 | Web App | External API | HTTPS | Non-sensitive metadata |

### 1.3 Trust Boundaries
| Boundary | Description | Controls |
|----------|-------------|----------|
| Internet → Web App | Public-facing attack surface | WAF, Rate limiting, TLS 1.2+ |
| Web App → Database | Internal data access | Parameterized queries, Least priv DB user |
| Web App → External API | 3rd party integration | API key rotation, Timeout/retry logic |

---

## 2. Asset Inventory

| Asset ID | Asset Name | Type | Classification | Owner | Location |
|----------|------------|------|----------------|-------|----------|
| A1 | User credentials (hashed) | Data | Confidential | App | PostgreSQL |
| A2 | Session tokens | Data | Confidential | App | Redis / Cookie |
| A3 | Application source code | Code | Proprietary | Team | GitHub |
| A4 | API keys (external) | Secret | Restricted | Team | Env vars / Vault |
| A5 | Audit logs | Data | Internal | App | File / SIEM |

---

## 3. STRIDE Analysis

**Instructions**: List each identified threat. Use additional rows as needed.

| Threat ID | Threat Description | STRIDE Category | Likelihood (H/M/L) | Impact (H/M/L) | Risk Score | Mitigation | Residual Risk |
|-----------|-------------------|-----------------|-------------------|----------------|------------|------------|---------------|
| T1 | SQL injection in search endpoint | Tampering, Elevation | H | H | 9 | Parameterized queries; input validation; WAF rules | L |
| T2 | XSS via user profile field | Tampering, Info Disclosure | M | H | 6 | Output encoding; CSP headers; sanitize on input | L |
| T3 | Weak session tokens predictable | Spoofing, Info Disclosure | M | H | 6 | Cryptographically secure RNG; HttpOnly; Secure flags | L |
| T4 | Brute-force login | Spoofing | H | M | 6 | Rate limiting; account lockout; MFA | L |
| T5 | Insecure deserialization | Tampering, Remote Exec | L | H | 4 | Avoid custom serialization; validate schema | L |
| T6 | Exposed debug endpoints | Info Disclosure | M | M | 4 | Remove in prod; feature flags; auth required | L |
| T7 | Hardcoded secrets in repo | Info Disclosure | L | H | 3 | Git hooks (gitleaks); env vars; vault | L |
| T8 | Missing audit logging | Repudiation | M | M | 4 | Structured logs; immutable storage; alerting | L |
| T9 | | | | | | | |
| T10 | | | | | | | |

**STRIDE Categories Reference**:
- **S**poofing: Impersonating another entity
- **T**ampering: Modifying data/code
- **R**epudiation: Denying actions (no audit trail)
- **I**nformation Disclosure: Exposing data
- **D**enial of Service: Making service unavailable
- **E**levation of Privilege: Gaining unauthorized access

**Risk Score**: Likelihood × Impact (H=3, M=2, L=1) → 1–9 scale

---

## 4. Risk Prioritization (Top 3)

| Rank | Threat ID | Justification (why top) | Mitigation Summary | Residual Risk (H/M/L) | Acceptance |
|------|-----------|------------------------|-------------------|----------------------|------------|
| 1 | | | | | ☐ Accept ☐ Mitigate ☐ Transfer |
| 2 | | | | | ☐ Accept ☐ Mitigate ☐ Transfer |
| 3 | | | | | ☐ Accept ☐ Mitigate ☐ Transfer |

---

## 5. Assumptions & Out of Scope

| Assumption | Validation Method |
|------------|-------------------|
| TLS termination at load balancer | Verify config |
| Database not directly internet-accessible | Network scan |
| Users have modern browsers (CSP support) | Analytics data |

**Out of Scope**:
- Physical security of hosting infrastructure
- Supply chain attacks on dependencies (beyond basic scanning)
- Insider threats with privileged access

---

## 6. References

- [ ] STRIDE methodology (Microsoft)
- [ ] OWASP Top 10 2021
- [ ] Course Curriculum Framework Units 5.1–5.6
- [ ] Lab-specific documentation: _________________________

---

*Submit as `THREAT_MODEL.md` in your capstone branch by Mar 31, 8:00 AM.*