# U3 L11: Network Segmentation — Diagram Template

**Date:** Nov 30 (Mon) — TECH DAY
**Topic:** 3.3 Network Segmentation — VLANs, Subnets, DMZs

---

## Instructions
Use this template for the in-class activity. Draw the segmentation for the small business scenario, then complete the water utility variant extension.

---

## Part 1: Small Business Network Diagram

**Scenario:** Small business with:
- Web server (public)
- Email server (public)
- Internal file server (private)
- 20 employee PCs
- 10 IoT cameras
- Guest Wi-Fi

**Draw your design below. Include:**
- DMZ for public servers
- Screened subnet (DMZ with dual firewalls)
- VLANs separating Staff / IoT / Guest
- Firewalls between segments
- Label all VLAN IDs, subnets, and firewall rule directions

```
┌─────────────────────────────────────────────────────────────────┐
│                         INTERNET                                 │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                    ┌─────▼─────┐
                    │  FIREWALL │  (NGFW / WAN interface)
                    └─────┬─────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
   ┌────▼────┐       ┌────▼────┐       ┌────▼────┐
   │  DMZ    │       │ STAFF   │       │  GUEST  │
   │ VLAN 10 │       │ VLAN 20 │       │ VLAN 30 │
   │         │       │         │       │         │
   │ Web Srv │       │ 20 PCs  │       │  Wi-Fi  │
   │ Email   │       │         │       │         │
   └────┬────┘       └────┬────┘       └────┬────┘
        │                 │                 │
        │          ┌──────▼──────┐          │
        │          │   INTERNAL  │          │
        │          │  FILE SRV   │          │
        │          │  VLAN 40    │          │
        │          └──────┬──────┘          │
        │                 │                 │
        │          ┌──────▼──────┐          │
        │          │    IoT      │          │
        └──────────│  VLAN 50    │──────────┘
                   │ (NO INET)   │
                   └─────────────┘
```

**Subnet Assignments (fill in):**

| VLAN | Name | Subnet (CIDR) | Gateway IP | DHCP Range |
|------|------|---------------|------------|------------|
| 10 | DMZ | | | N/A (static) |
| 20 | Staff | | | |
| 30 | Guest | | | |
| 40 | Internal File | | | N/A (static) |
| 50 | IoT | | | |

**Key Firewall Rules (source → dest, port, action):**

| # | Source | Dest | Port | Action | Notes |
|---|--------|------|------|--------|-------|
| 1 | Internet | DMZ Web | 80/443 | Allow | |
| 2 | Internet | DMZ Email | 25/587 | Allow | |
| 3 | DMZ | Internet | Any | Deny | No outbound from DMZ |
| 4 | Staff | DMZ | 80/443 | Allow | Web/email access |
| 5 | Staff | Internal File | 445/SMB | Allow | File access |
| 6 | Staff | IoT | Any | Deny | No camera access |
| 7 | Guest | Any Internal | Any | Deny | Internet only |
| 8 | IoT | Internet | Any | **Deny** | **CISA FIX — critical** |
| 9 | Any | Any | Any | Deny | Implicit default |

---

## Part 2: Water Utility Variant (Extension)

**Add to your diagram:**
- SCADA controller (chemical dosing)
- Chemical dosing pumps
- Water quality monitor
- Operator workstation

**Where do they go? (Answer: Their own OT VLAN with NO internet route — that's the CISA fix.)**

```
[Add OT VLAN to your diagram above]
```

| OT Component | VLAN | Internet Route? | Why? |
|--------------|------|-----------------|------|
| SCADA Controller | | | |
| Chemical Dosing Pumps | | | |
| Water Quality Monitor | | | |
| Operator Workstation | | | |

**Discussion Question:** *Why would a water utility have chemical controllers on the internet at all? What business pressure leads to this?*

---

## Part 3: Zero Trust Preview (U3 L13)

**Looking at your diagram above, identify:**

| Control | Castle-and-Moat (Perimeter) | Zero Trust (Per-Device) |
|---------|-----------------------------|-------------------------|
| Network boundary | Firewall at internet edge | |
| Internal trust | Trusted internal network | |
| Device authentication | None (IP-based) | |
| Microsegmentation | VLANs only | |
| Encryption | TLS at edge only | |
| Continuous verification | No | |

---

## Homework (Due 20:30)

**Complete the diagram if unfinished.** Answer: *"How does segmentation limit the damage from a compromised IoT device?"*

**Read CED excerpt on 3.3 Zero Trust** (1 page — provided separately).