# Unit 3 Vocabulary Reference — All Flashcard Sets

**Consolidated reference for U3 L1–L20. Create physical or digital flashcards for each set.**

---

## Flashcard Set 1: Network Vulnerabilities (U3 L1 HW — Due Nov 16)

| Term | Definition | CED LO |
|------|------------|--------|
| Vulnerability | A weakness in a system that can be exploited by a threat | 3.1.A |
| Attack Vector | The path or method an attacker uses to exploit a vulnerability | 3.1.A |
| OSI Layer 2 (Data Link) | MAC addressing, switching, ARP, Ethernet frames | 3.1.B |
| OSI Layer 3 (Network) | IP addressing, routing, ICMP, packet forwarding | 3.1.B |
| OSI Layer 4 (Transport) | TCP/UDP, ports, sessions, connection state | 3.1.B |
| Interception | Attacker captures/monitors traffic (sniffing, ARP spoofing) | 3.1.B |
| Disruption | Attacker denies service (DoS/DDoS, MAC flooding) | 3.1.B |
| Redirection | Attacker diverts traffic (DNS poisoning, BGP hijack) | 3.1.B |
| Infiltration | Attacker gains unauthorized access (exploits, credential theft) | 3.1.B |

---

## Flashcard Set 2: Wireless Security (U3 L4 HW — Due Nov 23)

| Term | Definition | CED LO |
|------|------------|--------|
| WPA3 | Wi-Fi Protected Access 3 — SAE, forward secrecy, no PSK brute-force | 3.2.C |
| WPA2 | Wi-Fi Protected Access 2 — AES-CCMP, 4-way handshake, vulnerable to KRACK | 3.2.C |
| 802.1X | Port-based network access control — EAP over RADIUS | 3.2.C |
| RADIUS | Remote Authentication Dial-In User Service — AAA server | 3.2.C |
| EAP | Extensible Authentication Protocol — framework for auth methods | 3.2.C |
| SSID | Service Set Identifier — network name | 3.2.C |
| MAC Filtering | Allowlist/blocklist by MAC address — bypassable but raises bar | 3.2.C |
| Evil Twin | Rogue AP mimicking legitimate SSID — credential harvest | 3.2.A |
| SAE | Simultaneous Authentication of Equals — WPA3 handshake, no offline attack | 3.2.C |
| Forward Secrecy | Session keys not compromised even if long-term key is later | 3.2.C |

---

## Flashcard Set 3: Risk Assessment (U3 L6 HW — Due Nov 24)

| Term | Definition | CED LO |
|------|------------|--------|
| Likelihood | Probability a threat exploits a vulnerability (Very Low–Very High) | 3.1.C |
| Impact | Magnitude of harm if exploit occurs (Very Low–Very High) | 3.1.C |
| Risk Matrix | 5×5 grid mapping likelihood × impact → risk level | 3.1.C |
| Risk Register | Structured table: Asset, Threat, Vulnerability, Likelihood, Impact, Score, Mitigation | 3.1.C |
| Mitigation | Control that reduces likelihood or impact | 3.1.C |
| Residual Risk | Risk remaining after mitigation applied | 3.1.C |
| Risk Appetite | Amount of risk organization is willing to accept | 3.1.C |
| Qualitative Assessment | Risk rated by categories (Low/Med/High) — subjective | 3.1.C |
| Quantitative Assessment | Risk calculated in monetary terms (ALE = SLE × ARO) | 3.1.C |

---

## Flashcard Set 4: Segmentation & Zero Trust (U3 L11–L13)

| Term | Definition | CED LO |
|------|------------|--------|
| VLAN | Virtual LAN — logical broadcast domain on same physical switch | 3.3.A |
| DMZ | Demilitarized Zone — semi-trusted zone for public-facing servers | 3.3.A |
| Screened Subnet | DMZ with dual firewalls (external + internal) | 3.3.A |
| Blast Radius | Scope of damage from a compromise — segmentation limits this | 3.3.B |
| East-West Traffic | Traffic between internal segments (lateral movement path) | 3.3.B |
| North-South Traffic | Traffic between internal and external (internet) | 3.3.B |
| Zero Trust | "Never trust, always verify" — continuous verification, least privilege | 3.3.C |
| Microsegmentation | Per-workload/device isolation — beyond VLANs | 3.3.C |
| Least Privilege | Minimum access necessary — default deny | 3.3.C |
| Continuous Verification | AuthZ/AuthN at every request, not just login | 3.3.C |
| Assume Breach | Design as if attacker already inside | 3.3.C |

---

## Flashcard Set 5: Firewalls (U3 L15–L16)

| Term | Definition | CED LO |
|------|------------|--------|
| Packet-Filtering Firewall | Stateless — examines each packet in isolation (L3/L4) | 3.4.A |
| Stateful Firewall | Tracks connection state — allows return traffic automatically | 3.4.A |
| NGFW | Next-Gen Firewall — DPI, app awareness, IPS, TLS decryption | 3.4.A |
| ACL | Access Control List — ordered permit/deny rules | 3.4.B |
| Implicit Deny | Default action: deny all not explicitly permitted | 3.4.B |
| First-Match Wins | Rules processed top-down — order is critical | 3.4.B |
| Default-Deny | Secure posture: block everything, allow only needed | 3.4.B |
| Default-Allow | Insecure posture: allow everything, block known bad | 3.4.B |
| Dead Rule | Rule never matched due to earlier broader rule | 3.4.B |
| Overly Permissive | Rule allows more than necessary (e.g., Any→Any) | 3.4.B |

---

## Flashcard Set 6: Network Attack Detection (U3 L20)

| Term | Definition | CED LO |
|------|------------|--------|
| NIDS | Network Intrusion Detection System — monitor + alert (passive) | 3.5.A |
| NIPS | Network Intrusion Prevention System — monitor + block (inline) | 3.5.A |
| Signature-Based Detection | Matches known attack patterns (Snort/Suricata rules) | 3.5.A |
| Anomaly-Based Detection | Baselines normal behavior, flags deviations | 3.5.A |
| SIEM | Security Information & Event Management — collect, normalize, correlate, alert, dashboard | 3.5.B |
| Log Correlation | Linking related events across sources (time, pattern, threshold) | 3.5.B |
| Time-Based Correlation | Events within a time window | 3.5.B |
| Pattern-Based Correlation | Events matching attack sequence | 3.5.B |
| Threshold-Based Correlation | Count exceeds limit (e.g., 5 failed logins) | 3.5.B |
| Snort/Suricata | Open-source NIDS/NIPS rule engines | 3.5.A |
| Splunk/ELK/Wazuh | Commercial/open SIEM platforms | 3.5.B |

---

## Study Schedule Recommendation

| Week | Focus | Flashcard Sets |
|------|-------|----------------|
| Nov 16–22 | Network Vulnerabilities | Set 1 |
| Nov 23–29 | Wireless + Risk Assessment | Sets 2, 3 |
| Nov 30–Dec 6 | Segmentation + Firewalls | Sets 4, 5 |
| Dec 7–11 | Detection + Full Review | Sets 4, 5, 6 + all |

---

## Quiz/Test Coverage Map

| Assessment | Flashcard Sets Tested |
|------------|----------------------|
| U3 L1 Quiz (Nov 16) | Set 1 (partial) |
| U3 L3 Quiz (Nov 18) | Set 1 |
| U3 L5 Quiz (Nov 20) | Set 2 |
| U3 L6 Quiz (Nov 23) | Sets 2, 3 |
| U3 L7 Quiz (Nov 24) | Sets 1–3 |
| U3 L8 Quiz (Nov 25) | Set 2 |
| U3 L10 Quiz (Nov 27) | Set 4 (VLAN basics) |
| U3 L11 Quiz (Nov 30) | Set 4 |
| U3 L13 Quiz (Dec 2) | Set 4 (Zero Trust) |
| U3 L14 MCQ Sprint (Dec 3) | Sets 1–5 |
| U3 L15 Quiz (Dec 4) | Set 5 (firewall pre-read) |
| U3 L16 Quiz (Dec 7) | Set 5 |
| U3 L18 Test (Dec 9) | **ALL SETS 1–6** |
| U3 L20 Quiz (Dec 11) | Set 6 |