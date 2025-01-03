# Security Analyst Scenario: Dealing with a DDoS Attack

## Scenario

You work as a security analyst for a travel agency that advertises sales and promotions on the company’s website. The employees of the company regularly access the company’s sales webpage to search for vacation packages their customers might like. 

One afternoon, you receive an automated alert from your monitoring system indicating a problem with the web server. You attempt to visit the company’s website, but you receive a connection timeout error message in your browser.

You use a packet sniffer to capture data packets in transit to and from the web server. You notice a large number of TCP SYN requests coming from an unfamiliar IP address. The web server appears to be overwhelmed by the volume of incoming traffic and is losing its ability to respond to the abnormally large number of SYN requests. You suspect the server is under attack by a malicious actor. 

You take the server offline temporarily so that the machine can recover and return to a normal operating status. You also configure the company’s firewall to block the IP address that was sending the abnormal number of SYN requests. You know that your IP blocking solution won’t last long, as an attacker can spoof other IP addresses to get around this block. You need to alert your manager about this problem quickly and discuss the next steps to stop this attacker and prevent this problem from happening again. You will need to be prepared to tell your boss about the type of attack you discovered and how it was affecting the web server and employees.

## Step-by-Step Instructions

1. **Confirm the Attack:**
   - Use tools like Wireshark or tcpdump to verify the presence of numerous TCP SYN packets from a single or multiple IP addresses.

2. **Document the Findings:**
   - Note the source IP addresses, the rate of SYN requests, and any patterns observed.

3. **Mitigate Immediate Impact:**
   - Temporarily take the server offline to stop the ongoing attack and allow recovery.
   - Add the offending IP address(es) to the firewall's block list.

4. **Prepare to Inform Management:**
   - **Identify the Attack Type:** Recognize this as a SYN flood, a subtype of DDoS attack where the attacker sends a succession of SYN requests to consume server resources.
   - **Impact Explanation:** Explain how the attack was preventing legitimate access to the website, potentially disrupting business operations and customer service.

5. **Plan for Future Prevention:**
   - Discuss implementing SYN cookies or other SYN flood protection mechanisms at the server or network level.
   - Consider upgrading DDoS protection with services like Cloudflare or AWS Shield.
   - Review and possibly strengthen the network infrastructure to handle such traffic spikes.

6. **Communication:**
   - Draft an email or schedule a meeting with your manager to:
     - Describe the incident, 
     - Explain the actions taken, 
     - Outline the impact on business operations, 
     - Propose preventive measures for the future.

7. **Follow-Up:**
   - Monitor the server post-recovery for any residual or new attack attempts.
   - Keep documentation updated with each incident for future reference and analysis.

8. **Training and Awareness:**
   - Suggest organizing a training session for the team on recognizing and responding to DDoS attacks.

By following these steps, you ensure not only immediate response but also lay groundwork for better security practices in the organization.
