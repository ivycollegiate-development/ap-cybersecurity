AP Cybersecurity — Unit 1 · Period 9 (Wed, Sep 16)   Name: ______________   Date: ______________

# Mitigation Toolkit — Public Wi-Fi & Wireless Protections

Reference sheet for protecting yourself (and your data) on public networks.

## The Problem

Public Wi-Fi networks (coffeeshops, airports, hotels) are shared. Anyone on the same network can:
- **Sniff** your traffic (view unencrypted data)
- **Spoof** a legitimate hotspot (evil twin / rogue AP)
- **Intercept** login credentials, emails, messages

## Protection Layer 1: Encryption

| Tool | What it does | Why it matters |
|------|-------------|----------------|
| **HTTPS** | Encrypts communication between your browser and the website | Even if someone sniffs the network, they can't read your traffic to HTTPS sites |
| **VPN** | Creates an encrypted tunnel from your device to a VPN server | All traffic is encrypted — your ISP, the coffee shop, and attackers on the same network see only encrypted data |
| **End-to-end encryption** | Messages encrypted from sender to recipient (WhatsApp, Signal, iMessage) | The service provider itself can't read your messages |

**But:** HTTPS only protects the browser. A VPN protects ALL apps on your device.

## Protection Layer 2: Connection Hygiene

| Practice | How to do it |
|----------|-------------|
| **No auto-connect** | Turn off "auto-join" and "ask to join networks" on your device |
| **Verify the network** | Ask the staff what their exact Wi-Fi name is before connecting |
| **Forget networks** | Don't keep coffee-shop Wi-Fi in your saved networks list |
| **Turn off sharing** | Disable file sharing, AirDrop, and printer sharing when on public Wi-Fi |

## Protection Layer 3: Authentication

| Tool | What it stops |
|------|--------------|
| **Password manager** | Auto-fills credentials only on the real site — won't fill on a phishing page |
| **Multi-factor authentication (MFA)** | Even if an attacker steals your password, they can't log in without the second factor |
| **Hardware security key** | Physical key required for login — phishing-resistant |

## Quick Decision Chart

| Situation | Tool to use |
|-----------|------------|
| Browsing on public Wi-Fi | HTTPS + VPN |
| Logging into email on coffee-shop Wi-Fi | HTTPS + MFA + password manager |
| Someone hands you a USB drive | Don't plug it in |
| Your phone asks "Join this network?" | Say no unless you asked for it |

## Key Takeaway

**VPN + HTTPS + MFA** covers most risks on public Wi-Fi. But the cheapest protection is **don't auto-connect** and **verify the network name** — the Delta flight evil twin attack (Aug 2026) worked because passengers clicked "Delta WiFi Fast" without checking.