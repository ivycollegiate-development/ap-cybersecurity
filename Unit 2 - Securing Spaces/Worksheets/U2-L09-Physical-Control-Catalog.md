# U2 L9: Physical Control Catalog (with costs and failure modes)

Name: ______________________________    Date: _______________

Every control here has a price range and a failure mode. The failure mode is not a footnote — it is the reason two controls at the same price are not interchangeable. Costs are planning figures in NT$ for a mid-size school or small office, installed or per year, and are deliberately rounded. Read the CED codes so you can place each control against tomorrow's matching worksheet.

## Access controls — locks

| Control | Cost (NT$) | Failure mode | CED |
| ------- | ---------- | ------------ | --- |
| Pin tumbler lock, standard | 800 – 2,000 per cylinder | Picks and shims in seconds with a rake or a bump key; no record of who entered | 2.3.A |
| Single-cylinder deadbolt | 2,000 – 4,500 | A long screwdriver and 30 seconds beats most residential-grade deadbolts; the door frame is weaker than the bolt | 2.3.A |
| Mortise lock set | 6,000 – 14,000 installed | Better than a surface bolt because the mechanism is inside the door, but still open to frame failure and forced entry | 2.3.A |
| Electronic keypad lock | 6,000 – 15,000 installed | If the code is shared, the log records a number that identifies nobody — shared codes destroy the audit trail the device exists to create | 2.3.A |
| Magnetic lock, fail-safe | 8,000 – 18,000 installed | Releases on power loss; an attacker who cuts power walks in, and it is on the inside of the frame where it is reachable | 2.3.A |
| Magnetic lock, fail-secure | 9,000 – 20,000 installed | Locks on power loss — a fire is now a security event and emergency egress may be blocked; requires a monitored fire panel | 2.3.A |
| Anti-shim door wrap | 4,000 – 10,000 installed | Only protects the gap it covers; the hinges and the frame are still attack surface | 2.3.A |

## Access controls — readers and credentials

| Control | Cost (NT$) | Failure mode | CED |
| ------- | ---------- | ------------ | --- |
| Proximity badge reader, 125 kHz legacy | 1,500 – 3,500 per door | The card transmits a fixed code with no challenge, so it is clonable in seconds with a commercial cloner; the most common weakness in older systems | 2.3.A |
| Smart card / EMV reader (13.56 MHz) | 4,000 – 9,000 per door | Far harder to clone, but a compromised backend can still issue a valid card to an attacker; cost moves from hardware to identity management | 2.3.A |
| Mobile / NFC credential | 2,000 – 6,000 per door plus server cost | No card to lose, but it inherits the phone's own security — an unlocked phone handed over is a valid badge | 2.3.A |
| Biometric reader, fingerprint | 12,000 – 30,000 installed | Defeated by a gelatin or silicone replica of a finger; can be configured to fail open or fail closed, and fail open makes any sensor weakness a full bypass | 2.3.A |
| Biometric reader, face or iris | 20,000 – 60,000 installed | Face recognition accepted photographs or masks before modern liveness detection; iris resists this but costs more and has throughput problems at a busy door | 2.3.A |
| Mantrap / two-door vestibule | 180,000 – 320,000 installed | The only control on this sheet that makes tailgating physically impossible, because the inner door cannot release while two people are inside. It costs space, and a jammed or propped door defeats it entirely | 2.3.A |
| Turnstile or speed gate | 400,000 – 900,000 installed | Not a security control on its own; it needs a credential behind it or it is furniture | 2.3.A |

## Access controls — personnel

| Control | Cost (NT$) | Failure mode | CED |
| ------- | ---------- | ------------ | --- |
| Guard, single shift | 1,100,000 – 1,700,000 per year | The only control that evaluates intent rather than matching a credential — and the control most likely to be phoned in, dozed off, or socially engineered by someone in a legitimate uniform | 2.3.A |
| Guard booth, built | 250,000 – 600,000 | The booth is the control; an unstaffed booth is a locked door with a window, at a premium | 2.3.A |
| Receptionist-controlled entry | cost of staff time | Scales badly at volume and depends entirely on training and script discipline | 2.3.A |
| Photo-badge check at a staffed gate | negligible | Detective, not preventative — it catches a bad credential, it does not stop a determined person with a good one | 2.3.A |

## Surveillance

| Control | Cost (NT$) | Failure mode | CED |
| ------- | ---------- | ------------ | --- |
| CCTV camera, 1080p IP | 6,000 – 15,000 each plus install | Resolution without coverage is useless; a camera pointed at the room misses the door and the approach, which is where the attacker is | 2.3.B |
| CCTV camera, 4K / low-light | 18,000 – 45,000 each | Costs more and still fails if the light is bad — lighting is the cheaper fix and often the only one that works | 2.3.B |
| NVR, 30-day retention, 4 cameras | 40,000 – 90,000 | 30 days of 4 Mbps footage is real storage, and footage deleted before an investigation is evidence that never existed. A camera with no retention policy is a decoration | 2.3.B |
| NVR, 90-day retention, 4 cameras | 120,000 – 260,000 | Buy the storage or do not claim the footage. Retention is the control most often skipped because it has no visible effect on the day it is installed | 2.3.B |
| Lighting upgrade at an entry | 3,000 – 15,000 | The cheapest row on this sheet and the highest-leverage one — adding light to an approach beats adding resolution to a camera pointed at a dark door | 2.3.B |
| Live monitoring service | 600,000 – 1,500,000 per year | Changes what cameras are for: recorded footage only helps after the fact, and an unmonitored camera is a filing cabinet of images | 2.3.B |
| Access control and alarm logging | included in readers, or 30,000 – 80,000 | Useless if nobody reviews the log; a badge log that is only pulled during an investigation has no deterrence value at all | 2.3.B, 2.4 |

## Environmental and monitoring

| Control | Cost (NT$) | Failure mode | CED |
| ------- | ---------- | ------------ | --- |
| Motion sensor, indoor | 1,200 – 3,000 | Detects movement, not identity — a custodian setting off an alarm every night is a control that gets disabled by the third week | 2.3.C |
| Door contact sensor | 800 – 2,500 per door | Only reports the door's state; on a propped door it reports closed if the contact is bypassed, and it needs a monitored panel behind it | 2.3.C |
| Glass-break and vibration sensor | 4,000 – 12,000 per window | Covers the glass only; a high window or a roof entry bypasses it entirely, which is why the approach matters | 2.3.C |
| Alarm panel, 8 zones, monitored | 30,000 – 90,000 plus monitoring | Unmonitored or unverified alarms get ignored, and a dispatch company that calls no one is a recorder, not a control | 2.3.C |
| Server closet environmental monitor | 8,000 – 25,000 | Temperature, humidity, and water leak in one box; nobody acts on the alert unless it pages someone | 2.3.C |
| UPS, 1 kVA | 25,000 – 60,000 | Buys minutes, not hours. A UPS is not a generator, and sizing it for the server closet rather than the whole building is a decision with consequences | 2.3.C |
| Generator, 20 kVA, installed | 400,000 – 900,000 | A generator without a tested automatic transfer switch and a fuel contract is a very expensive building ornament. The transfer switch is the control; the generator is the fuel | 2.3.C |
| Water-leak detection, raised floor | 6,000 – 18,000 | Server closets on a raised floor in a typhoon-and-flood environment are exactly the right place for this, and it is the control almost nobody has | 2.3.C |

## The three questions to ask about any row

1. **What asset is this protecting?** A NT$2,000,000 fingerprint reader on a supply closet holding NT$200 of paper is theater. Cost follows asset value and threat, not how impressive the control looks.
2. **Does it work by construction or by attention?** Mantraps, fail-secure locks, and retention policies work by construction. Guards, badge reviews, and camera monitoring work by attention, which means they are only as good as the person paying them.
3. **What is the cheapest thing that fixes the actual failure?** A dark approach needs NT$3,000 of lighting, not NT$30,000 of resolution. A shared keypad code needs a policy, not a new lock. Name the real failure before you price the fix.
