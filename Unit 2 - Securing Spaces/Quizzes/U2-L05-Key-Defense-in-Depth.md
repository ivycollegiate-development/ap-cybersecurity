# Homework Quiz Answer Key — Unit 2

U2 L5 - Key: Homework Quiz Defense in Depth (Unit 2)

Homework Quiz Answer Key — Unit 2

These are the answers to U2 L5 — Homework Quiz: Defense in Depth. 10 points, 2 per question. Give credit for the reasoning, not the vocabulary — the target skill this unit keeps failing is a student naming a control without saying what it actually prevents.

## Q. List the three layers of defense-in-depth and give one example control for each.

A. The three layers are physical, technical (network/system), and organizational (policy/people/process). Example for each: physical — locked server room door, mantrap, badge reader, bollards. Technical — firewall, network segmentation, EDR, MFA, encryption at rest. Organizational — security policy, background checks, access reviews, incident response plan, security awareness training. Students who give only two layers, or three controls that are all technical, have not answered the question — the point of the model is that the layers are different in kind, not three versions of the same control.

## Q. A detective control finds an intrusion after it happens. Explain how it differs from a preventative control, and give one example of each.

A. A preventative control acts before the attack and removes the opportunity — the event never occurs. A detective control acts during or after and produces a record or an alert that the attack is happening, so response can begin. Examples: preventative — a mantrap between two locked doors, MFA on remote access, a badge reader that locks the door on failed reads. Detective — motion sensors, door contact sensors, badge access logs, CCTV with monitoring, NIDS. The important distinction to credit explicitly: detection without response is not a control, it is a notification. And a detective control that nobody watches is equivalent to no control at all.

## Q. The "castle" analogy says a single strong wall is weaker than several weak layers. Explain why that is true in one or two sentences.

A. Because an attacker only has to defeat one layer in a single-wall design, and a defender has to build and maintain it perfectly. With several layers, the attacker must find and defeat every layer in sequence, and each layer buys detection time and forces a second decision. The compounding effect is why a perimeter-only defense (firewall at the edge, nothing behind it) is brittle: one misconfiguration is a total loss, while the same misconfiguration in a layered design is one finding among several. Credit the student for identifying either the "defender must be perfect, attacker needs only one gap" asymmetry or the time-bought-by-detection point.

## Q. Name a corrective control and a detective control for the same physical space, such as a server room.

A. Accept any defensible pair as long as the student states what each one actually does and that they are different functions. Corrective: replacing a failed door lock, patching a vulnerable system, revoking a badge that was used during an incident, restoring a corrupted file from backup, disabling a port that was found open. Detective: a door contact sensor that alarms on forced entry, a failed-login alert, motion detection in the server room, badge log review, a camera covering the door. Watch for the common wrong answer: a camera listed as corrective. A camera does not stop anything, it records — that is the whole point of the previous question, and a student who misses it has not transferred the concept.

## Q. Why is it impossible to reduce risk to zero with technical controls alone?

A. Because risk is a function of the threat, the vulnerability, and the impact, and technical controls can only act on one of the three at a time and only within their own layer. A firewall cannot change who has a key, a camera cannot lower the value of what is stolen, and no product can eliminate human error — social engineering works precisely because the human being is not a technical control. The residual risk left after technical controls are all in place has to be carried by the organization: policies, training, background checks, insurance, and accepted risk. Full elimination would also require perfect operation forever, and controls degrade as staff change, configurations drift, and new attack methods appear. This question is the bridge to Unit 2's risk register work — the register exists precisely to record residual risk and name who accepts it.
