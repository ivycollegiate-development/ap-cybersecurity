AP Cybersecurity — Unit 1 · U1 L11 (Sep 16, Wed)

# Passenger returning from DEF CON 34 spoofs Delta Wi-Fi network while in flight using pentest tool
By Tom's Hardware — Aug 11, 2026

Delta Flight 591 between Las Vegas, Nevada, and Atlanta, Georgia was carrying some passengers from the recently concluded DEF CON 34 hacking conference, and an attendee apparently didn't want to let the fun stay in Vegas. A passenger reportedly "jammed" the plane's Wi-Fi signal. That hacker then created their own Wi-Fi hotspot called "Delta WiFi Fast" that routed to a phishing website that harvested the Google credentials of any passenger who attempted to log in.

The pilots on the flight told the ground crew to alert corporate security as someone was tampering with in-flight Wi-Fi through ACARS, the digital communications systems airliners use for air-to-ground text communications. "Hey, alert corporate security. We have a passenger onboard that has created a scam Wi-Fi called 'Delta WiFi Fast.' We believe they are trying to scam the other passengers," the pilots said in their first message. They followed this up 17 minutes later with, "No information as of now. We have a bunch of passengers that were at a cybersecurity conference in Las Vegas. They were able to jam our Wi-Fi and broadcast their signal."

While the exact details are unclear as the incident is still under investigation, the attacker (or prankster) apparently used a Wi-Fi Pineapple penetration testing device to launch Wi-Fi deauthentication attacks and then created an evil twin that other passengers could log into instead. This fake log-in page could have been used to harvest usernames, passwords, and other credentials. The plane was reportedly met at the gate by the authorities, although it's unclear if any arrests were made.

Most in-flight Wi-Fi networks are unsecured, so a determined hacker could potentially use it for cyberattacks on their fellow passengers. Creating an "evil twin" network does not carry the same alarm, scandal, and potential lawsuit that a public network or device named "bomb" would on a flight, but it could still land you in hot water.

"Jamming" or interfering with in-flight Wi-Fi (or any Wi-Fi network, for that matter) is prohibited by the FCC, while the phishing log-in page could constitute wire fraud or identity theft. The passenger who created the fake in-flight Wi-Fi is also using social engineering, especially as more airlines adopt in-flight Wi-Fi and more passengers expect it.

Despite the potential threat to passengers' cybersecurity, Delta reassured flyers that the safety of the flight was never threatened in any way. "Safety of flight was never in question, and no aircraft operating systems were affected. We are fully investigating to gather a complete set of facts, which will take time," a Delta spokesperson told View From the Wing. "We will partner with federal law enforcement and aviation regulators to ensure the incident is thoroughly investigated. We thank our crew for their professionalism and our customers for their understanding."

---
Source: Tom's Hardware, Aug 11 2026. Original: tomshardware.com — "Passenger returning from DEF CON 34 spoofs Delta Wi-Fi network while in flight using pentest tool"