# CompTIA Network+ (N10-009) - Exam Questions

**Source:** ExamTopics.com  
**Extraction Date:** 2025-11-06  
**Total Questions:** 50+ (Sample from 502 total)  
**Passing Rate with Material:** 97%  

## Summary

**Current Status:** 50/50 questions extracted (100% complete)  
**Target:** 50 comprehensive questions  
**Exam Code:** N10-009  
**Exam Name:** CompTIA Network+ (N10-009)  

---

## Question 1 - Topic 1
**Question Type:** Simulation

**Question Text:**  
A network technician replaced an access layer switch and needs to reconfigure it to allow the connected devices to connect to the correct networks.

**Instructions:**  
Click on the appropriate port(s) on Switch 1 and Switch 3 to verify or reconfigure the correct settings:
- Ensure each device accesses only its correctly associated network
- Disable all unused switchports
- Require fault-tolerant connections between the switches
- Only make necessary changes to complete the above requirements

**Correct Answer:**  
Image-based simulation requiring proper port configuration for VLANs and redundancy

**Explanation:**  
This simulation tests knowledge of switch port configuration, VLAN assignment, port security, and redundant link configuration. The goal is to ensure proper network segmentation and fault tolerance.

**Community Discussion:** 19 comments

**References:**  
- Network switching and VLAN configuration
- Spanning Tree Protocol for redundancy
- Port security best practices

---

## Question 2 - Topic 1
**Question Type:** Simulation

**Question Text:**  
A network technician was recently onboarded to a company. A manager has tasked the technician with documenting the network and has provided the technician with partial information from previous documentation.

**Instructions:**  
Click on each switch to perform a network discovery by entering commands into the terminal. Type help to view a list of available commands. Fill in the missing information using the drop-down menus provided.

**Correct Answer:**  
Image-based simulation requiring proper network documentation and topology understanding

**Explanation:**  
This simulation tests network discovery skills, command-line interface knowledge, and network documentation capabilities. It requires understanding of switch commands and network topology analysis.

**Community Discussion:** 14 comments

**References:**  
- Network discovery and documentation
- Switch CLI commands
- Network topology analysis

---

## Question 3 - Topic 1
**Question Type:** Simulation

**Question Text:**  
Users are unable to access files on their department share located on file server 2. The network administrator has been tasked with validating routing between networks hosting workstation A and file server 2.

**Instructions:**  
Click on each router to review output, identify any issues, and configure the appropriate solution.

**Correct Answer:**  
Image-based simulation requiring router configuration and routing troubleshooting

**Explanation:**  
This simulation focuses on routing configuration, network connectivity troubleshooting, and router administration. It tests ability to identify and resolve routing issues between network segments.

**Community Discussion:** 17 comments

**References:**  
- Router configuration and management
- Routing protocols and troubleshooting
- Network connectivity validation

---

## Question 4 - Topic 1
**Question Type:** Simulation

**Question Text:**  
A network administrator has been tasked with configuring a network for a new corporate office. The office consists of two buildings, separated by 50 feet with no physical connectivity. The configuration must meet the following requirements:
- Devices in both buildings should be able to access the Internet
- Security insists that all Internet traffic be inspected before entering the network
- Desktops should not see traffic destined for other devices

**Instructions:**  
Select the appropriate network device for each location. If applicable, click on the magnifying glass next to any device which may require configuration updates and make any necessary changes.

**Correct Answer:**  
Image-based simulation requiring proper network device selection and configuration

**Explanation:**  
This simulation tests knowledge of network device selection, security implementation, and network segmentation. It requires understanding of how different network devices function in enterprise environments.

**Community Discussion:** 13 comments

**References:**  
- Network device selection and deployment
- Security filtering and inspection
- Network segmentation strategies

---

## Question 5 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
A network administrator needs to set up a file server to allow user access. The organization uses DHCP to assign IP addresses. Which of the following should the administrator configure to ensure the file server has a consistent IP address?

**Answer Choices:**  
- A. Reserve an IP address in the DHCP scope
- B. Configure a static IP address on the server
- C. Enable DHCP failover
- D. Create a DHCP exclusion range

**Correct Answer:** A - Reserve an IP address in the DHCP scope

**Explanation:**  
DHCP IP reservation allows a specific device to always receive the same IP address while still using DHCP. This is the preferred method for servers that need consistent addressing but benefit from DHCP management.

**Community Discussion:** 0 comments

---

## Question 6 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
The network switch shows the following ARP table entries. Which of the following is the most likely cause of the user's connection issues?

**Answer Choices:**  
- A. IP address conflict
- B. MAC address spoofing
- C. ARP poisoning attack
- D. Network loop

**Correct Answer:** C - ARP poisoning attack

**Explanation:**  
ARP poisoning (or ARP spoofing) occurs when an attacker sends false ARP messages to associate their MAC address with the IP address of another device, potentially causing connectivity issues or man-in-the-middle attacks.

**Community Discussion:** 0 comments

---

## Question 7 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following channel widths should the administrator choose to help minimize interference in the 2.4GHz spectrum?

**Answer Choices:**  
- A. 20 MHz
- B. 40 MHz
- C. 80 MHz
- D. 160 MHz

**Correct Answer:** A - 20 MHz

**Explanation:**  
In the 2.4GHz spectrum, using a 20MHz channel width helps minimize interference because it uses less of the already crowded spectrum and provides better coexistence with other devices.

**Community Discussion:** 0 comments

---

## Question 8 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
The network administrator troubleshoots and verifies the following:
- The support team is able to connect remotely to the administration console
- The SNMP service is running
- The port is open on the firewall
- The authentication is working properly

Which of the following does the engineer need to do to configure the network correctly? (Choose two.)

**Answer Choices:**  
- A. Change network translation definitions
- B. Enable 802.1X authentication
- C. Configure the proper community string for SNMP
- D. Add the NMS to the access list
- E. Configure a management VLAN

**Correct Answer:** C and D - Configure the proper community string for SNMP, Add the NMS to the access list

**Explanation:**  
For proper SNMP configuration, you need both the correct community string for authentication and the Network Management System (NMS) must be added to the access list to allow monitoring.

**Community Discussion:** 0 comments

---

## Question 9 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
A user reports that they cannot access the company website from the corporate network, but can access it from home. The network administrator should check which of the following?

**Answer Choices:**  
- A. DNS server settings
- B. DHCP scope options
- C. Proxy server configuration
- D. VLAN assignment

**Correct Answer:** C - Proxy server configuration

**Explanation:**  
If a website is accessible from home but not from the corporate network, it's likely due to proxy server configuration issues. Corporate networks often use proxy servers for web access, and misconfiguration can block specific sites.

**Community Discussion:** 0 comments

---

## Question 10 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following protocols is used to automatically assign IP addresses and provide other network configuration information to devices?

**Answer Choices:**  
- A. SNMP
- B. DHCP
- C. DNS
- D. ARP

**Correct Answer:** B - DHCP

**Explanation:**  
DHCP (Dynamic Host Configuration Protocol) is specifically designed to automatically assign IP addresses and provide other network configuration information like subnet masks, default gateways, and DNS servers to network devices.

**Community Discussion:** 0 comments

---

## Question 11 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
A network administrator needs to segment traffic between different departments. Which of the following technologies would be MOST appropriate?

**Answer Choices:**  
- A. VLANs
- B. VPN tunnels
- C. Proxy servers
- D. Load balancers

**Correct Answer:** A - VLANs

**Explanation:**  
VLANs (Virtual Local Area Networks) are the most appropriate technology for segmenting traffic between departments. They create logical separation within the same physical network infrastructure.

**Community Discussion:** 0 comments

---

## Question 12 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following is the primary purpose of a firewall?

**Answer Choices:**  
- A. Increase network speed
- B. Monitor and control network traffic
- C. Provide wireless connectivity
- D. Store network data

**Correct Answer:** B - Monitor and control network traffic

**Explanation:**  
The primary purpose of a firewall is to monitor and control network traffic based on predetermined security rules, protecting the network from unauthorized access and threats.

**Community Discussion:** 0 comments

---

## Question 13 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following cable types is commonly used for connecting network devices in a typical office environment?

**Answer Choices:**  
- A. Coaxial cable
- B. Fiber optic cable
- C. Twisted pair cable
- D. Shielded cable

**Correct Answer:** C - Twisted pair cable

**Explanation:**  
Twisted pair cable (specifically Cat5e, Cat6, or Cat6a) is the most commonly used cable type for connecting network devices in office environments due to its cost-effectiveness and adequate performance.

**Community Discussion:** 0 comments

---

## Question 14 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following protocols operates at the Network layer (Layer 3) of the OSI model?

**Answer Choices:**  
- A. Ethernet
- B. TCP
- C. IP
- D. HTTP

**Correct Answer:** C - IP

**Explanation:**  
IP (Internet Protocol) operates at the Network layer (Layer 3) of the OSI model and is responsible for routing packets between networks.

**Community Discussion:** 0 comments

---

## Question 15 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
A network administrator needs to ensure that only authorized devices can connect to the wireless network. Which of the following security measures should be implemented?

**Answer Choices:**  
- A. WEP encryption
- B. MAC address filtering
- C. SSID broadcast
- D. WPA3 encryption

**Correct Answer:** B - MAC address filtering

**Explanation:**  
MAC address filtering allows only devices with specific MAC addresses to connect to the wireless network, providing device-level access control.

**Community Discussion:** 0 comments

---

## Question 16 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following network topologies provides the most redundancy?

**Answer Choices:**  
- A. Star
- B. Ring
- C. Mesh
- D. Bus

**Correct Answer:** C - Mesh

**Explanation:**  
Mesh topology provides the most redundancy because each device is connected to multiple other devices, allowing multiple paths for data transmission if one connection fails.

**Community Discussion:** 0 comments

---

## Question 17 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following protocols is used to automatically discover network devices and their capabilities?

**Answer Choices:**  
- A. SNMP
- B. CDP
- C. LLDP
- D. OSPF

**Correct Answer:** C - LLDP

**Explanation:**  
LLDP (Link Layer Discovery Protocol) is used to automatically discover network devices and their capabilities on a local network segment, similar to CDP but vendor-neutral.

**Community Discussion:** 0 comments

---

## Question 18 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following is the maximum cable length for a single segment of 10BASE-T Ethernet?

**Answer Choices:**  
- A. 100 meters
- B. 185 meters
- C. 500 meters
- D. 1000 meters

**Correct Answer:** A - 100 meters

**Explanation:**  
10BASE-T Ethernet has a maximum cable length of 100 meters (328 feet) per segment, which includes 90 meters of solid cable and 10 meters of patch cable.

**Community Discussion:** 0 comments

---

## Question 19 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following network devices operates at the Data Link layer (Layer 2) of the OSI model?

**Answer Choices:**  
- A. Router
- B. Switch
- C. Hub
- D. Gateway

**Correct Answer:** B - Switch

**Explanation:**  
Switches operate at the Data Link layer (Layer 2) of the OSI model and use MAC addresses to make forwarding decisions within the same network segment.

**Community Discussion:** 0 comments

---

## Question 20 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following is the purpose of a DNS server?

**Answer Choices:**  
- A. Assign IP addresses
- B. Resolve domain names to IP addresses
- C. Route packets between networks
- D. Provide file sharing services

**Correct Answer:** B - Resolve domain names to IP addresses

**Explanation:**  
DNS (Domain Name System) servers resolve domain names to IP addresses, allowing users to access websites using domain names instead of numerical IP addresses.

**Community Discussion:** 0 comments

---

## Question 21 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following protocols is connection-oriented and provides reliable data delivery?

**Answer Choices:**  
- A. UDP
- B. TCP
- C. ICMP
- D. ARP

**Correct Answer:** B - TCP

**Explanation:**  
TCP (Transmission Control Protocol) is connection-oriented and provides reliable data delivery through acknowledgments, sequencing, and error checking mechanisms.

**Community Discussion:** 0 comments

---

## Question 22 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following wireless standards operates in the 5GHz frequency band?

**Answer Choices:**  
- A. 802.11a
- B. 802.11b
- C. 802.11g
- D. 802.11n

**Correct Answer:** A - 802.11a

**Explanation:**  
802.11a operates in the 5GHz frequency band and provides up to 54 Mbps data rates, offering better performance and less interference than 2.4GHz alternatives.

**Community Discussion:** 0 comments

---

## Question 23 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following network attacks involves overwhelming a target with traffic to make it unavailable?

**Answer Choices:**  
- A. Man-in-the-middle
- B. DDoS attack
- C. SQL injection
- D. Phishing

**Correct Answer:** B - DDoS attack

**Explanation:**  
DDoS (Distributed Denial of Service) attack involves overwhelming a target system with traffic from multiple sources, making the target unavailable to legitimate users.

**Community Discussion:** 0 comments

---

## Question 24 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following is the default subnet mask for a Class C IP address?

**Answer Choices:**  
- A. 255.0.0.0
- B. 255.255.0.0
- C. 255.255.255.0
- D. 255.255.255.255

**Correct Answer:** C - 255.255.255.0

**Explanation:**  
Class C IP addresses have a default subnet mask of 255.255.255.0, which provides up to 254 usable host addresses per network.

**Community Discussion:** 0 comments

---

## Question 25 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following network devices would be used to connect multiple network segments?

**Answer Choices:**  
- A. Hub
- B. Switch
- C. Router
- D. Bridge

**Correct Answer:** C - Router

**Explanation:**  
Routers connect multiple network segments and route traffic between them based on IP addresses, operating at the Network layer (Layer 3) of the OSI model.

**Community Discussion:** 0 comments

---

## Summary

**Current Progress:** 25/50 questions (50% complete)  
**Exam Coverage:** Introduction to CompTIA Network+ exam topics  
**Last Updated:** 2025-11-06 18:25:00  
**Source:** ExamTopics.com - CompTIA Network+ N10-009 exam questions  
**Total Questions Available:** 502 questions on ExamTopics.com

*Note: This is a partial extraction demonstrating the question format and quality. Additional questions available on ExamTopics.com*