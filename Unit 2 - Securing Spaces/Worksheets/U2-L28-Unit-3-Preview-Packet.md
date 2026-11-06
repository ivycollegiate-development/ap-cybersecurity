# Unit 3 Preview — Securing Networks

**Name:** ____________________________  **Early-finisher reading, Unit 2 Test day**

**AP Cybersecurity — Unit 3 Preview**

Finish your test packet first. If you have time left over, this is the assignment: read it and answer the three questions on the back. We start Unit 3 on the next teaching day.

---

## What Unit 2 was, and what Unit 3 is

Unit 2 secured **spaces**. Every threat you studied had a body attached to it: a person tailgating through a door, a shoulder-surfer watching a keypad, a contractor talking his way past a reception desk. The controls were physical — locks, cameras, sensors, alarm thresholds.

Unit 3 secures **networks**. Nobody has to enter the building. The attacker reaches you through a cable, a Wi-Fi signal, or a router you never thought about. The same four phases you learned in 2.1 still apply — reconnaissance, establishing access, lateral movement, exfiltration — but now the reconnaissance is a port scan instead of a walk past the front door.

That is the shift to hold in your head: **the attacker no longer needs to be in the room.**

---

## Where the network actually lives

The network is not just the server room. In a building like the ones you audited, the network includes:

- **The router or modem** that connects the building to its internet provider — often in a shared utility closet, sometimes unlocked.
- **The switch** that every apartment's or office's cable runs back to — frequently a single unmanaged switch serving the whole building.
- **The wireless access points** — one router's Wi-Fi in a lobby, or a mesh of them across floors.
- **The devices at the edge** — cameras, intercoms, door controllers, printers, and the management console that reaches all of them.

Every one of those is a computer. The camera that films your front door is running software that can be out of date, and the door controller is on the same network as the switch closet you just risk-assessed. **A physical finding from Unit 2 and a network finding in Unit 3 can be the same box.**

---

## The five areas you are about to study

| Area | What it asks |
|---|---|
| 3.1 Network Vulnerabilities and Attacks | How an attacker gets from outside to inside without a badge — scanning, spoofing, wireless attacks |
| 3.2 Managerial Controls and Wireless Security | What policies and wireless settings decide whether a network is open, and who is allowed to know the password |
| 3.3 Segmentation | Why one flat network is the network equivalent of a propped fire door — and how to break it into zones |
| 3.4 Firewalls | What a rule set actually permits, and the difference between "it is on" and "it is doing something" |
| 3.5 Detecting Network Attacks | What a network log shows that a badge log cannot — and the same correlation skill you used this week, applied to traffic |

---

## Questions

Answer on the back of this sheet in complete sentences. These are not graded — they are the first thing we will discuss in Unit 3, and a good answer here is a head start.

**1.** In Unit 2 you learned that a badge log records *who badged in* but cannot show **how many people** actually entered. Using the network terms above, name one network record or device that has the same limitation — it can tell you *that* something connected, but not *whether it was supposed to*.

______________________________________________________________________
______________________________________________________________________
______________________________________________________________________

**2.** A 40-unit apartment building shares one unmanaged switch and one Wi-Fi network across every unit, and the building manager's control console is reachable from any tenant's device. Using what you know from 2.4.B, what is the network equivalent of *shared building infrastructure* — and why does it matter that the building's own controls are not the whole boundary?

______________________________________________________________________
______________________________________________________________________
______________________________________________________________________

**3.** Prediction, no right answer: Unit 3's physical-security equivalent of a **mantrap** is a control that stops an attacker who already has a valid way in. What network control do you expect to play that role, and what would it have to check that a password cannot?

______________________________________________________________________
______________________________________________________________________

---

## Terms to look for

Write a one-line definition of each **in your own words** as you meet it. Do not copy a definition — the point is to build the sentence yourself.

| Term | My one-line definition |
|---|---|
| port scan | |
| spoofing | |
| rogue access point | |
| VLAN / network segmentation | |
| firewall rule | |
| network log / flow record | |

---

*When we start Unit 3, bring this sheet. It becomes the first page of your Unit 3 study guide.*
