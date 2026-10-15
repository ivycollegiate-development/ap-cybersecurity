# U2 L9 Quiz: Physical Control Matching (from L08 Case Studies)

**Name:** ______________________________    **Date:** _______________    **Score:** ____ / 4

> **Instructions:** For each case study from Friday's lesson (RSA SecurID 2011, Snowden 2013, Stuxnet, Taichung water utility), identify the vulnerability exploited and the single most cost-effective physical control that would have prevented or limited the incident. Choose the BEST answer from the catalog.

---

### 1. RSA SecurID, 2011
An outsourced contractor with legitimate credentials was compromised via an APT campaign, leading to replacement of every deployed SecurID token. The contractor had broad, unscoped access.

**Vulnerability exploited:**
A. Weak password policy on the contractor's account
B. **Contractor access was administered but not scoped (excessive privileges, no time-bound limits)**
C. Lack of multi-factor authentication on the VPN
D. Unencrypted token seed records on the server

**Most cost-effective physical control to prevent/limit:**
A. Biometric fingerprint reader on the server room ($12,000–30,000)
B. **Scoped badge access with least-privilege zoning and time-bounded credentials (policy + existing reader config — near-zero marginal cost)**
C. Mantrap at the data center entrance ($180,000–320,000)
D. 24/7 guard at the contractor entrance ($1.1M–1.7M/yr)

---

### 2. Snowden, 2013
A trusted insider with legitimate badge access and cleared credentials exfiltrated classified data over months. No alarm triggered because every access used valid credentials.

**Vulnerability exploited:**
A. Weak encryption on the data at rest
B. **System assumed a cleared insider would behave; no monitoring of access *patterns* (volume, hours, destinations)**
C. Lack of air-gapped networks
D. Insufficient background check depth

**Most cost-effective physical control to prevent/limit:**
A. Mantrap at every secure area ($180,000–320,000 each)
B. **Access control and alarm logging with automated anomaly review (included in readers or $30,000–80,000 for centralized logging + review policy)**
C. Biometric iris readers on all doors ($20,000–60,000 each)
D. Armed guards at every hallway intersection ($1.1M–1.7M/yr per guard)

---

### 3. Stuxnet
A worm arrived on USB drives carried by maintenance contractors, crossed an air gap physically, and targeted industrial control systems. The physical vector: four USB sticks and one maintenance contract.

**Vulnerability exploited:**
A. Unpatched Windows vulnerabilities on the OT network
B. **Air gap was crossed by a *device* carried in by someone with legitimate physical access — no control on what enters the boundary**
C. Weak network segmentation between IT and OT
D. Lack of antivirus on the engineering workstations

**Most cost-effective physical control to prevent/limit:**
A. Faraday cage around the centrifuge hall ($millions)
B. **Port-blocking policy + USB port locks on all engineering workstations + contractor device scan station at entry ($3,000–8,000 for locks + scanner)**
C. Biometric readers on the air-gapped network room ($20,000–60,000)
D. Mantrap at the facility perimeter ($180,000–320,000)

---

### 4. Taichung Water Utility (Composite)
A contractor entered a process-control area without a proper escort during typhoon-response operations. The facility's flood/power resilience systems were accessed by unauthorized personnel.

**Vulnerability exploited:**
A. Lack of water-leak detection in the server room
B. **No verification of *authority* at the process-area door — badge proved identity, not why the person was there**
C. Insufficient UPS capacity for the SCADA systems
D. No CCTV coverage of the pump house

**Most cost-effective physical control to prevent/limit:**
A. **Photo-badge check at a staffed gate / escort verification at the process-area door (negligible cost — policy and training)**
B. Mantrap at the process-area entrance ($180,000–320,000)
C. 4K low-light CCTV on every approach ($18,000–45,000 per camera)
D. Biometric face readers on the process-area doors ($20,000–60,000 each)

---

## Answer Key

| Question | Vulnerability | Control | Rationale |
|----------|---------------|---------|-----------|
| 1 | **B** — access administered but not scoped | **B** — scoped badge access / least privilege (policy fix) | Cost follows asset value. The token seeds were the crown jewels; the fix is narrowing who can reach them, not buying a $30K fingerprint reader for a door the contractor already opened with a valid badge. |
| 2 | **B** — no monitoring of access *patterns* | **B** — access logging + anomaly review | Snowden used valid credentials validly. Detection controls that watch for *pattern* (unusual volume, hours, destinations) are what would have caught it. Logging is cheap; 24/7 guards are not. |
| 3 | **B** — device carried across air gap by authorized person | **B** — USB port locks + contractor device scan | Stuxnet started *inside* the boundary. The cheapest fix is preventing the vector (USB) at the entry point, not hardening the room the vector already reached. |
| 4 | **B** — badge proves identity, not authority | **A** — escort verification / photo-badge check | The contractor had a valid badge. A mantrap or biometric reader would have admitted them anyway. The failure was *authorization*, not *authentication* — a human check is the right layer. |

---

## Scoring
- **4/4** — Mastery: You distinguish authentication vs. authorization, and match control cost to actual failure mode
- **3/4** — Proficient: Minor confusion on one case (usually #2 or #3)
- **2/4** — Developing: Tendency to over-buy impressive controls (biometrics, mantraps) where policy/logging/escort would work
- **0–1/4** — Needs review: Re-read the control catalog and the three questions (asset, construction vs. attention, cheapest real fix)

**Teacher note:** This quiz is graded on the *reasoning*, not just the letter. If a student picks a different control but correctly justifies it with cost/asset/failure-mode reasoning, award full credit.