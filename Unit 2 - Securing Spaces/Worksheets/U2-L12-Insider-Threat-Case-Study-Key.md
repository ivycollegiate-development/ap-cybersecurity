# U2 L12: Detecting Physical Attacks — Insider Threat Case Study (ANSWER KEY)

**Teacher Use Only — Do Not Distribute**

---

## Detection Chain Reconstruction — Model Answers

| # | Detection Point | Control Type | Confidence | What Would Have Caught It Sooner? |
|---|-----------------|--------------|------------|-----------------------------------|
| 1 | **TSCM sweep** (routine physical sweep found the device) | **Detective** — periodic inspection detects existing compromise | **High** — physical discovery of the actual device | **Continuous RF monitoring / permanent TSCM sensors** — would alert the moment the device transmitted |
| 2 | **MAC address in network logs** (device's MAC appeared in DHCP/wireless logs) | **Detective** — log analysis reveals unauthorized device on network | **High** — MAC is hardware-unique, directly ties device to network | **Network Access Control (NAC) / 802.1X port authentication** — would reject unknown MAC at connection time (Day 1) |
| 3 | **Wife's ChatGPT history** (same MAC address pasted into ChatGPT two days earlier) | **Detective** — log review of AI assistant conversations | **Medium** — requires access to wife's account; OPSEC failure by suspect | **DLP / data exfiltration monitoring on AI chat platforms** — would flag sensitive technical data (MAC addresses) leaving the org |
| 4 | **Security footage** (suspect at executive room door 6× on separate days) | **Detective** — video surveillance review | **High** — direct visual evidence of presence | **Real-time video analytics / tailgating alerts** — would flag repeated visits to a restricted door by non-authorized personnel |
| 5 | **Covert camera** (installed behind TV after device found; caught him returning Oct 5) | **Detective** — targeted surveillance after incident detection | **High** — caught him in the act | **Not applicable** — this is a *response* control deployed *after* detection; earlier detection (rows 1–2) would have made this unnecessary |

---

## Analysis Questions — Model Answers

**1. Why did a crude bug take 48 hours and a routine sweep to find?**  
The device was *passive until transmitting* and physically small. No active monitoring existed on the TV's USB port (no port security, no USB device enumeration alerts). The executive conference room was not under continuous RF surveillance. The TSCM sweep was the *only* control checking for physical bugs — and it ran on a schedule, not continuously. The device exploited the gap between "physical access granted" and "next scheduled sweep."

**2. One control that would have detected it on Day 1:**  
**Network Access Control (NAC) with 802.1X on all wired ports** — the TV's USB port provided network connectivity (likely via the TV's built-in Ethernet/Wi-Fi). When the microcontroller connected, it would have requested a DHCP lease. NAC would have seen an unknown MAC, no valid certificate, and rejected the connection *immediately*, logging the event. The device would never have transmitted audio.

*Alternative acceptable answer:* **Continuous RF spectrum monitoring** in sensitive spaces — would detect the Wi-Fi transmission the moment the device powered on.

**3. Wiretapping vs. Espionage — burden of proof difference:**  
- **Wiretapping (18 U.S.C. § 2511):** Prosecution must prove the defendant *intentionally intercepted* oral/wire/electronic communications *without consent* of at least one party. No requirement to prove *who* benefited or *why*.  
- **Espionage (18 U.S.C. § 793/794):** Prosecution must prove the defendant acted *with intent or reason to believe* the information would be used to *injure the U.S. or advantage a foreign nation*. Requires proving *motive/beneficiary* — a much higher bar.

**4. Dual-use nature of AI in cybersecurity:**  
This case shows AI as both *attack enabler* (suspect used ChatGPT/GPT-4o to design the bug — "walked him through how to make it") and *defense multiplier* (OpenAI "used their models to understand the device and where it came from"). The same capability that helps a novice build a surveillance device also lets defenders reverse-engineer it from minimal evidence (MAC address, photos). The asymmetry: the attacker needed AI for *construction*; the defender used AI for *attribution and speed*. This mirrors the broader dynamic — AI lowers the floor for attacks but raises the ceiling for detection, *if* defenders deploy it intentionally.

---

## Exit Ticket — Model Answer

**Why did it take 48 hours? Name one Day-1 control.**  
The bug exploited the absence of continuous monitoring on a trusted port in a high-value room. The only physical detection was a *scheduled* TSCM sweep.  
**Day-1 control:** Network Access Control (802.1X) on the TV's network port — would have blocked the unknown device at first DHCP request, before any audio was captured.

---

## Grading Rubric (10 pts total)

| Component | Points | Criteria |
|-----------|--------|----------|
| Detection Chain Table (5 rows × 4 cols) | 5 | 1 pt per row: correct control type (2), reasonable confidence (1), plausible earlier control (2) |
| Analysis Q1 (why 48 hrs) | 1 | Mentions: no continuous monitoring, scheduled sweep only, trusted port gap |
| Analysis Q2 (Day-1 control) | 2 | NAC/802.1X or continuous RF monitoring + correct explanation |
| Analysis Q3 (wiretapping vs espionage) | 1 | Correctly distinguishes burden: wiretapping = act only; espionage = act + intent/beneficiary |
| Analysis Q4 (dual-use AI) | 1 | Identifies both attack-enabler and defense-multiplier roles with case specifics |

**Total: 10 pts**