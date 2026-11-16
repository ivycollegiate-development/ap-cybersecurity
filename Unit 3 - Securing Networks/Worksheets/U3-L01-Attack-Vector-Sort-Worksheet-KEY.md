# U3 L1 — Attack Vector Sort & CISO First-Fix — ANSWER KEY

**Teacher copy — do not distribute. Formative worksheet, not a quiz: no score out of N. Mark Part A and Part B on whether the category, the layer and the reason hang together, not on matching the key word for word.**

## Part A — Six Vectors from the Taiwan Threat Brief

| # | Vector | Category | OSI layer | Model reason |
|---|--------|----------|-----------|--------------|
| 1 | Outdated Office IME binary abused as a loader | infiltration | L7 | A digitally signed program the user is expected to run executes attacker code on the workstation; nothing on the network looks wrong |
| 2 | ShadowPad remote-access tool | infiltration | L7 | It exists to give the attacker a keyboard on the victim machine — attacker is inside, using an application channel |
| 3 | Cobalt Strike | infiltration | L7 | Post-exploitation tooling; the intruder is already on the network and moving |
| 4 | CVE-2018-0824 (user → admin) | infiltration | host/OS — not an OSI layer | A Windows privilege-escalation flaw; OSI describes network layers, so the honest answer is "below the application layer, on the host". Accept "L7" only with that explanation |
| 5 | Unpatched internet-facing VPN appliance | infiltration | L7 | The VPN service is reachable from the internet; the flaw walks the attacker in through a service the company publishes on purpose |
| 6 | Default SNMP community string | interception | L7 | It does not break or move anything — it lets the attacker read device inventory and configuration that is not theirs |

**Q1.** Layer 7, Application. Accept: nearly every modern vector rides inside traffic the network is built to pass, so the perimeter has nothing to block. Rows 1, 2, 3 and 5 are all L7; a good answer also notes row 4 is a host/OS flaw rather than a network-layer one. Half credit if the student says "the top layer" without naming Application.

## Part B — Five More, Same Four Categories

| # | Vector | Category | OSI layer | Model reason |
|---|--------|----------|-----------|--------------|
| 7 | ARP poisoning on the office LAN | interception | L2 | Lies about which MAC address owns an IP, so frames come to the attacker. Accept **redirection** with an on-path justification — both are defensible |
| 8 | Packet capture on open café Wi-Fi | interception | L2 | Reads traffic that is not yours off the shared radio medium. Accept L1 (the radio itself) if argued |
| 9 | SYN flood | disruption | L4 | Exhausts the connection table; the service stops answering. Nothing is read, nothing is redirected |
| 10 | DNS cache poisoning | redirection | L7 | Rewrites the name-to-IP answer so users are sent to the attacker's address. Accept L3 if the student argues the destination address is the thing being changed |
| 11 | Wi-Fi deauthentication flood | disruption | L2 | Forges management frames that kick clients off the access point — availability only |

**Q2.** Rows 7 and 10. ARP poisoning lies inside the local network about which hardware address owns an IP; DNS cache poisoning lies about which IP a name resolves to, for every client using that resolver. Both leave packets flowing — they change the destination, which is why they are the quiet pair and why encryption plus DNSSEC/static ARP matter.

## Part C — The CISO Call

Any vector can be defended if the trade-off is real. Score the reasoning, not the choice. Strong default: the unpatched internet-facing VPN.

**3. Fix first.** Unpatched internet-facing VPN appliance — or default SNMP strings. Both are unauthenticated paths from outside into the network that holds the design data.

**4. Defund.** Must name a real sacrifice. Acceptable: the perimeter firewall refresh, the guest Wi-Fi upgrade, the IDS pilot, the endpoint refresh cycle, the second SIEM feed.

**5. Why this one.** Full credit needs three parts: (a) the layer/exposure — an L7 service published to the internet, reachable without a password; (b) the blast radius — the design repository sits behind that door, and a copied GDSII or mask layout cannot be recalled once it leaves; (c) the asymmetry — patching is cheap, the loss is permanent. Partial credit for "it is the most dangerous" with no layer or no blast radius.

**6. Risk accepted.** A specific residual, e.g. an insider or a signed binary slips past; DDoS still takes the customer portal down; DNS is still poisonable at the ISP. Reject "no risk" and reject restating the fix.

**7. Board sentence.** One sentence, no jargon, names the loss. Model: "One unpatched VPN is the difference between a design that stays ours and a design that is somebody else's."

## Part D — Exit Ticket

**8.** Interception. Nothing breaks, so nobody opens a ticket: disruption and redirection announce themselves with an outage or a wrong destination, and infiltration usually leaves authentication artifacts, but a successful interception looks exactly like normal traffic. Accept a defensible case for infiltration ("you only find out after the copy is gone") if the student explains why detection lags.

**Bonus.** Patch and manage the VPN with MFA and put it behind an EDR-monitored jump host; or move SNMP to v3 with authentication and an ACL. Also correct: remove the appliance from the internet entirely and require device posture before access.

## Marking note

Part A and Part B: 1 point per row for a category plus a layer plus a one-line reason that supports both. Part C: 4 points — choice (1), defunding (1), why (2, needs layer and blast radius). Part D: 1 point. Total 16. Convert to a completion check if the class is short on time.
