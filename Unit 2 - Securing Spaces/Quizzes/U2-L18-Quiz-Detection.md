# U2 L18 Quiz — Detection: Badge Log Anomaly, Video/Log Correlation, Alerting Threshold

**3 MCQ — 5 minutes — Tech day quiz format**

---

**1.** A badge log shows a single entry event at 22:47 for Employee ID 4829 at the server room door. The video footage for that corridor at 22:47 shows **no one at the door**. Which statement is **correct**?

A. The badge log is wrong; the employee did not enter  
B. The video is wrong; the employee entered but the camera missed them  
C. The badge log records *one badge event*; it cannot confirm how many people entered or whether the badge holder was the person who entered  
D. This is a system error; badge logs and video must always agree

**Answer: C** — A badge log records **credential presentations**, not people. It cannot detect tailgating, piggybacking, or a stolen/borrowed badge. The video showing no one means either (a) the badge holder entered alone but the camera angle missed them, or (b) someone else used their badge. The log alone cannot distinguish. (CED 2.4.A, 2.4.B)

---

**2.** An organization sets the following alerting threshold for its badge log system: **"Alert if any badge is used to enter the server room between 22:00 and 06:00."** The alert emails the facilities manager. At 03:12, a cleaning contractor badges in (authorized for night cleaning). The facilities manager receives the alert at 03:13, sees the contractor's name, and takes no action. Which requirement of **2.4.C** is **missing**?

A. The threshold is not specific enough  
B. The response is not a **named action with an owner**  
C. The threshold should not trigger for authorized personnel  
D. The alert should go to the security team, not facilities

**Answer: B** — 2.4.C requires: **a threshold (value someone chose) + a response (a named action with an owner).** "Email the facilities manager" is a notification, not an action. A compliant response: *"Alert on after-hours server room access → Night-shift security officer verifies identity via camera and confirms authorized work order within 10 minutes; if not confirmed, dispatch to floor."* (CED 2.4.C)

---

**3.** During a review, you find a badge log showing **four consecutive failed badge attempts** at the clean room door at 14:22, followed by a **successful entry** at 14:23 by Employee ID 7711. The video shows Employee 7711 entering alone. Which correlation finding is **most significant**?

A. The failed attempts indicate a malfunctioning reader  
B. The failed-then-success pattern suggests credential testing or a borrowed badge  
C. The time gap (1 minute) is too short for an attack  
D. Since the video shows the employee entering alone, no anomaly exists

**Answer: B** — **Failed-then-success** is a classic credential-testing or borrowed-badge indicator (CED 2.4.B). The video showing the employee alone does not rule out a borrowed badge — the employee could be the legitimate holder lending their badge. The pattern warrants investigation: was the badge shared? Was someone testing a cloned credential? The 1-minute gap is consistent with an attacker trying a cloned badge until it works.

---

**Answer Key:** 1-C, 2-B, 3-B