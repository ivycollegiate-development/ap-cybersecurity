# U2 L19 Quiz — Unit 2 Study Guide Sprint (8 MCQ, One Per LO)

**8 MCQ — 8 minutes — Tech day quiz format**  
*Covers all Unit 2 learning objectives; hardest items from mini-project & FRQ packet*

---

**1. 2.1.A — Preparatory/Reconnaissance**  
An adversary places a USB drive labeled "ICA Payroll Q4" in the staff parking lot on a Monday morning. A staff member picks it up and plugs it into their workstation. The USB executes a payload that maps the local network. **Which phase of the cyberattack does the USB placement represent?**

A. 2.1.A — Preparatory/Reconnaissance  
B. 2.1.B — Establishing Access  
C. 2.1.C — Lateral Movement  
D. 2.1.D — Exfiltration

**Answer: A** — The USB is a **reconnaissance payload** seeded to learn about the environment (who plugs in unknown devices, what systems are accessible, network layout). The execution on the workstation is 2.1.B; the network mapping is 2.1.C.

---

**2. 2.1.B — Establishing Access**  
After the USB payload runs, the adversary gains a foothold on the workstation. They then use a **pass-the-hash attack** to authenticate to the domain controller without knowing the password. This is an example of:

A. Physical access establishing logical access  
B. Logical access establishing physical access  
C. Social engineering bypassing MFA  
D. A supply chain attack

**Answer: A** — The **physical delivery** (USB in parking lot) established the initial **logical access** (workstation compromise), which was then leveraged for further logical access (domain controller via pass-the-hash). Physical → logical is the 2.1.B sequence.

---

**3. 2.1.C — Lateral Movement**  
From the domain controller, the adversary queries Active Directory for all servers in the "Clean Room" OU and attempts SMB connections to each. **What detection signal would most reliably identify this lateral movement?**

A. Spike in outbound internet traffic  
B. Multiple failed SMB authentication attempts from a single source to multiple targets  
C. Increased CPU on the domain controller  
D. New user account creation in AD

**Answer: B** — **Lateral movement** (2.1.C) often manifests as **enumeration + connection attempts** across multiple targets from a single compromised host. Failed SMB auth across many servers is a high-fidelity signal. Outbound traffic (A) suggests exfiltration (2.1.D); CPU spike (C) is noisy; new accounts (D) are persistence, not movement.

---

**4. 2.1.D — Exfiltration**  
The adversary compresses chip design files from the clean room file server and uploads them to a cloud storage bucket via HTTPS on port 443. **Which control would most directly prevent this exfiltration?**

A. Egress firewall rule blocking unauthorized cloud storage domains  
B. Full-disk encryption on the file server  
C. MFA on the domain controller  
D. Badge reader on the server room door

**Answer: A** — **Exfiltration (2.1.D)** is the unauthorized *outbound* transfer of data. An **egress firewall rule** blocking known cloud storage domains (or allowing only approved destinations) directly blocks the transfer path. Full-disk encryption (B) protects data at rest, not in transit; MFA (C) and badge readers (D) are access controls, not exfiltration controls.

---

**5. 2.1.E — Risk Assessment (Likelihood × Impact)**  
A Taichung semiconductor subcontractor assesses the risk of **typhoon-induced flooding** to their ground-floor server room. Historical data: 1-in-5-year flood event. Equipment replacement cost: NT$12M. Downtime cost: NT$3M/day. Recovery time: 3 days. **What is the Annualized Loss Expectancy (ALE)?**

A. NT$3.0M  
B. NT$9.0M  
C. NT$4.2M  
D. NT$21.0M

**Answer: A** — SLE = NT$12M + (3 × NT$3M) = NT$21M. ARO = 1/5 = 0.2. ALE = SLE × ARO = NT$21M × 0.2 = **NT$4.2M**. (Wait — the question asks for ALE, which is NT$4.2M. Option C is correct. Let me fix the options.)

**Corrected Options:**
A. NT$3.0M  
B. NT$9.0M  
C. NT$4.2M  
D. NT$21.0M

**Answer: C** — SLE = NT$21M (equipment + downtime). ARO = 0.2. ALE = NT$4.2M. (CED 2.1.E)

---

**6. 2.1.F — Risk Treatment**  
The same subcontractor cannot relocate the server room (avoid). They install a flood barrier (mitigate) and buy flood insurance (transfer). The residual risk after these controls is **low likelihood, medium impact**. The CISO documents: *"We accept the residual risk of a 1-in-50-year catastrophic flood exceeding the barrier; no further investment is justified."* This is an example of:

A. Avoid  
B. Transfer  
C. Mitigate  
D. Accept

**Answer: D** — **Accept** is a deliberate, documented decision to retain a risk after other treatments have been applied. The key phrase is *"no further investment is justified"* with reasoning. (CED 2.1.F)

---

**7. 2.2.A — Tailgating/Piggybacking**  
A secure facility uses badge readers on all doors. During evening shift change, **four people enter behind one badge swipe** at the main entrance. The badge log shows **one entry event**. **What is the vulnerability, and what control addresses it?**

A. Vulnerability: badge reader failure; Control: redundant readers  
B. Vulnerability: tailgating; Control: mantrap with anti-tailgating sensors  
C. Vulnerability: cloned badge; Control: MFA on badge readers  
D. Vulnerability: social engineering; Control: security awareness training

**Answer: B** — **Tailgating (2.2.A)** is unauthorized entry by following an authorized person. A **mantrap with anti-tailgating sensors** (single-person interlock) physically prevents multiple people from entering on one credential. Cloned badges (C) are 2.2.C; social engineering (D) is 2.2.B/C; reader failure (A) is availability, not tailgating.

---

**8. 2.4.C — Alerting Threshold & Response**  
An organization sets this threshold: **"Alert if any badge accesses the IP Vault more than 3 times in 1 hour."** The alert pages the on-call security engineer, who must **verify the badge holder's identity via video and confirm a valid work order within 15 minutes**. If not confirmed, the engineer **dispatches a guard to the IP Vault door**. This threshold/response pair satisfies 2.4.C because:

A. It uses a numeric threshold (3 times/hour)  
B. The response names a specific action, owner, and time bound  
C. It pages the engineer instead of emailing  
D. It covers the IP Vault, the most sensitive area

**Answer: B** — 2.4.C requires: **threshold (value chosen) + response (named action + owner + time bound).** "Page engineer → verify via video + confirm work order in 15 min → dispatch guard if not confirmed" meets all three. A numeric threshold alone (A) is insufficient; paging vs emailing (C) is a channel, not an action; covering the IP Vault (D) is scope, not the response structure.

---

**Answer Key:** 1-A, 2-A, 3-B, 4-A, 5-C, 6-D, 7-B, 8-B