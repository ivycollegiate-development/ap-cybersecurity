# U6-L09: Ethics and Law — Taiwan's Personal Information Protection Act (PIPL)

**AP Cybersecurity — ICA 2026-27**  
**Date**: May 18, 2027 (Tue) | **Period**: 130 | **Duration**: 50 min  
**Type**: Legal/Ethical Frameworks | **Format**: Case Study + Discussion

---

## Learning Objectives

By the end of this lesson, students will be able to:
1. **Explain** Taiwan PIPL (Personal Information Protection Act) core principles and penalties
2. **Apply** PIPL to capstone project data handling (consent, retention, breach notification)
3. **Analyze** ethical dilemmas in vulnerability disclosure and penetration testing
4. **Articulate** a personal code of ethics for security practice

---

## Prerequisites

- Unit 1 LO 1.5 (Incident Response) — legal/regulatory considerations
- Unit 5 LO 5.4 (PKI) / LO 5.6 (Logging) — data protection in practice
- Career-Path-Research.md Part 5 (Taiwan Context) — read

---

## Materials

- PIPL summary handout (key articles: 8, 9, 10, 12, 15, 22, 27, 37)
- Case studies: (1) 2023 Taiwan hospital ransomware, (2) 2022 telecom data leak, (3) Bug bounty legal gray zone
- Ethical framework card: (ISC)² Code of Ethics, EC-Council Code of Ethics, Personal template

---

## Lesson Flow

| Time | Activity | Details |
|------|----------|---------|
| 0-5 | **Hook** | "You find a vuln in a Taiwan gov website. Do you report? Test? Publish? Sell? The law has opinions." |
| 5-15 | **PIPL Core** (10 min) | Teacher mini-lecture with handout:<br>**Scope**: "Personal data" = any identifiable info (Art 2)<br>**Principles** (Art 8): Lawful, specific, minimal, accurate, secure, retained only as needed<br>**Consent** (Art 9): Explicit, informed, revocable — exceptions (contract, legal duty, vital interest)<br>**Rights** (Art 10-12): Access, correction, deletion, restriction, portability, objection<br>**Security** (Art 15): Technical + organizational measures — encryption, access control, logging<br>**Breach Notification** (Art 12): Notify authority *and* subjects within 72 hrs if high risk<br>**Penalties** (Art 37-39): Admin fines up to NT$50M; criminal up to 5 yrs + NT$10M for intentional |
| 15-25 | **Capstone Application** (10 min) | In pairs, audit capstone against PIPL:<br>1. **What personal data** does your capstone process? (IP, email, auth logs, PII in test data)<br>2. **Lawful basis** for each? (Consent? Contract? Legitimate interest?)<br>3. **Retention policy** defined? (Art 8.5)<br>4. **Breach response** in runbook? (Art 12 — 72 hr clock)<br>5. **DPIA needed**? (Art 22 — systematic monitoring, sensitive data, large scale)<br>Record gaps in `compliance-gap-analysis.md` (portfolio `docs/`) |
| 25-35 | **Case Study: Vulnerability Disclosure Ethics** (10 min) | Read: "Student finds SQLi in university portal. Reports via email. No response 30 days. Posts PoC on GitHub."<br>Discuss:<br>- Legal: Unauthorized access? (Criminal Code Art 358-360)<br>- Ethical: (ISC)² Code — "Protect society, act honorably, provide diligent service"<br>- Responsible disclosure: CVD (Coordinated Vulnerability Disclosure) process<br>- Taiwan context: NCC/CCERT reporting channels, TWCERT/CC |
| 35-45 | **Personal Ethics Statement** (10 min) | Students draft 5-bullet personal code in `ethics-statement.md` (portfolio `docs/`):<br>1. I will [always/never] ______ when testing systems<br>2. I will handle data by ______<br>3. I will disclose vulnerabilities by ______<br>4. I will refuse requests to ______<br>5. I will continue learning by ______ |
| 45-50 | **Commit & Share** | `git add docs/compliance-gap-analysis.md docs/ethics-statement.md && git commit -m "Add ethics & compliance artifacts" && git push`<br>Volunteers share 1 bullet. Teacher: "This = Portfolio Section 6 material + interview differentiator." |

---

## Teacher Notes

- **PIPL updates**: 2022 amendment strengthened cross-border transfer, breach notification, DPIA
- **Taiwan Cyber Security Management Act** (2018) — critical infrastructure operators have extra duties
- **No legal advice** — frame as "awareness for practitioners"; refer to counsel for real incidents
- **Capstone connection**: Logging (LO 5.6) = PIPL Art 15 compliance evidence

---

## Differentiation

| Need | Adjustment |
|------|------------|
| Law Interest | Add: GDPR comparison (Art 33 breach = 72 hrs same); Taiwan adequacy decision status |
| Technical Focus | Emphasize: encryption, pseudonymization, access control as technical PIPL compliance |
| ELL | Provide PIPL summary in Chinese; key terms bilingual |

---

## Assessment

**Formative**: `compliance-gap-analysis.md` + `ethics-statement.md` committed — teacher reviews for PIPL article references, capstone specificity, ethics statement authenticity.

---

## Homework / Next Steps

- **Read**: Career-Path-Research.md Part 8 (Reflection Prompts) — answer for Portfolio Section 6
- **Portfolio**: Update Section 6 (Reflection) with ethics/compliance insights — due U6-L11
- **Prep**: U6-L10 (May 19) — OWASP Juice Shop debrief; bring capstone Lab 1 (Juice Shop) notes

---

*U6-L09 — Ethics and Law: Taiwan PIPL — May 18, 2027*