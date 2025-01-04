# Cybersecurity Research on the Portuguese Market

## Motifs & Reasons for the Research

The primary motivation behind this research was to enhance the cybersecurity posture of systems within the Portuguese market. Specifically, the focus was on Portuguese MEO (a telco) routers which have a generic login page. These routers were exposed to the exterior network, posing a significant security risk. By identifying systems that utilize default credentials, we can highlight the significant security risks these configurations pose. The intent was not to exploit these systems maliciously but to draw attention to potential vulnerabilities that could be easily targeted by attackers. This research underscores the need for more robust security practices to protect against unauthorized access and data breaches.

## Goals of the Research

- **Identify Vulnerable Systems**: Using specific search queries on the Censys website, which is a search engine for internet-connected devices, we aimed to pinpoint MEO routers with publicly accessible IP addresses that might be vulnerable due to default credentials.
  
- **Conduct Basic Penetration Testing**: The research involved attempting to access the login pages of these MEO routers using basic default credentials to assess their security level. This step was crucial to prove the existence of vulnerabilities in a controlled manner.

- **Notification and Protection**: The ultimate goal was to gather contact information of system owners and notify them about the vulnerabilities. This action was intended to encourage immediate remediation, thereby preventing potential exploitation by malicious actors, especially since these routers were exposed to the exterior network.

## Vulnerabilities Used to Exploit the Systems

- **Default Credentials**: Many MEO routers, especially those with generic login pages, still use default usernames and passwords provided by manufacturers. This research exploited this vulnerability by attempting to log into these systems with known default credentials. 

  - **Why Default Credentials?**: Default credentials are often left unchanged due to oversight or lack of awareness about security best practices. They represent one of the simplest yet most effective entry points for cyber attackers. By demonstrating how easily these can be exploited, this research aimed to educate and prompt system administrators to update their security settings, particularly for routers exposed to external networks.

## OpSec Techniques Used

- **VPN Cascade**: Multiple layers of encryption and routing to obscure IP.
- **Virtual Machine (VM)**: Isolated environment for research activities.
- **Public Wi-Fi**: Used to mask geographical location.
- **No Website Login**: Avoided to prevent tracking via cookies or sessions.
- **Randomized MAC Address**: Changed to prevent hardware-based tracking.

These techniques ensured anonymity and security during the research.

## Success of the Operation

- **Positive Outcome**: Out of 23 machines tested, 1 was found to be vulnerable with weak credentials.
- **Location Identification**:
  - Used WiFi neighboring network analysis.
  - Combined with data from wigle.net for triangulation.
  - Managed to vaguely triangulate the location to Telheiras, Lisbon.
  - However, was unable to pinpoint the exact company.

- **Security of Other Machines**: 
  - The other 22 machines were secured with non-default passwords.
  
- **Methodology**: 
  - Only tested default credentials.
  - Did not use brute force methods, as this was not the goal of the research.

This research not only identifies immediate risks but also contributes to broader cybersecurity awareness and improvement within the Portuguese market.
