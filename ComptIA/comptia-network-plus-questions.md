# CompTIA Network+ (N10-008/N10-009) Questions

## Questions Extracted from ExamTopics.com

### Question 56
**Question Type:** Single Choice  
**Topic:** Network Performance and Duplex Settings

A network engineer is investigating reports of poor network performance. Upon reviewing a device configuration, the engineer finds that duplex settings are mismatched on both ends. Which of the following would be the MOST likely result of this finding?

**Answer Choices:**
A. Increased CRC errors
B. Increased giants and runts
C. Increased switching loops
D. Increased device temperature

**Correct Answer:** A

**Detailed Explanation:**
A duplex mismatch will usually generate excessive CRC errors. The different duplex settings on both ends of a connection can cause a mismatch in the flow control (sending data at different speed), leading data collisions. These collisions can result in corrupted data and increase the number of CRC errors.

According to the official CompTIA Network+ 008 Student Guide (Lesson 12, page 291): "A runt is a frame that is smaller than the minimum size (64 bytes for Ethernet). A runt frame is usually caused by a collision. In a switched environment, collisions should only be experienced on an interface connected to a legacy hub device and there is a duplex mismatch in the interface configuration."

**Community Voting Statistics:**
- A: 93%
- Other: 7%

**Community Comments:**
- "A mismatch will usually generate excessive CRC errors. Mismatch = ERROR" (12 upvotes)
- "The different duplex settings on both ends can cause a mismatch in the flow control, leading to data collisions" (7 upvotes)

---

### Question 57
**Question Type:** Single Choice  
**Topic:** Network Troubleshooting and ARP Tables

A network administrator is troubleshooting connectivity issues in a network segment. When examining the ARP table on a workstation, the administrator notices several entries with incomplete MAC addresses. Which of the following is the MOST likely cause of this condition?

**Answer Choices:**
A. Network congestion
B. IP address conflicts
C. Incomplete ARP resolution process
D. Faulty network cable

**Correct Answer:** C

**Detailed Explanation:**
Incomplete MAC addresses in the ARP table typically indicate that the ARP resolution process is still in progress or has failed. The workstation is attempting to resolve IP addresses to MAC addresses but has not yet received responses or the responses are incomplete.

This is a normal part of network operation when new devices come online or when there are temporary network issues. The incomplete entries will be resolved once communication is established or will timeout and be removed.

**Community Discussion:** 0 comments

---

### Question 58
**Question Type:** Multiple Choice  
**Topic:** VLAN Configuration

A network technician needs to configure a switch port to allow only devices from VLAN 10 to communicate. Which of the following switchport modes should be configured?

**Answer Choices:**
A. Access
B. Trunk
C. Dynamic
D. Desirable

**Correct Answer:** A

**Detailed Explanation:**
An access port is configured to carry traffic for only one VLAN. When you set a switchport to access mode and assign it to VLAN 10, only devices in that VLAN will be able to communicate through that port. This is the appropriate configuration for end-user devices.

Trunk ports, on the other hand, are used to carry multiple VLANs between switches and are not suitable for single-VLAN access.

**Community Discussion:** 0 comments

---

### Question 59
**Question Type:** Multiple Choice  
**Topic:** Network Security and Firewalls

A company wants to block all incoming connections to their web server while still allowing the web server to make outbound connections. Which of the following firewall rules should be configured?

**Answer Choices:**
A. Allow inbound on port 80, deny outbound on all ports
B. Deny inbound on all ports, allow outbound on port 80
C. Allow outbound on all ports, deny inbound on all ports
D. Deny all traffic, allow only port 443

**Correct Answer:** C

**Detailed Explanation:**
To block all incoming connections while allowing the web server to make outbound connections, you should deny all inbound traffic and allow outbound traffic. This creates a secure perimeter where the server can initiate connections but cannot be directly accessed from external networks.

This is a common security configuration for servers that need to communicate with external services but should not be accessible from the internet.

**Community Discussion:** 0 comments

---

### Question 60
**Question Type:** Multiple Choice  
**Topic:** Network Protocols and Subnetting

A network administrator needs to subnet a /24 network to create 6 subnets. Which of the following subnet masks should be used?

**Answer Choices:**
A. 255.255.255.0
B. 255.255.255.224
C. 255.255.255.192
D. 255.255.255.240

**Correct Answer:** B

**Detailed Explanation:**
To create 6 subnets from a /24 network, you need to borrow 3 bits (2^3 = 8 subnets, which is more than the required 6). This results in a /27 subnet mask of 255.255.255.224.

With 5 bits remaining for host addresses (32 - 27 = 5), each subnet will have 2^5 - 2 = 30 usable host addresses, which is sufficient for most subnet requirements.

**Community Discussion:** 0 comments

---

### Question 61
**Question Type:** Multiple Choice  
**Topic:** Wireless Network Security

Which of the following wireless security protocols provides the strongest encryption and should be the preferred choice for securing a wireless network?

**Answer Choices:**
A. WEP
B. WPA
C. WPA2
D. WPA3

**Correct Answer:** D

**Detailed Explanation:**
WPA3 is the most secure wireless security protocol available. It provides stronger encryption than WPA2 and includes additional security features such as:

- Enhanced protection against offline password guessing attacks
- Forward secrecy to protect past traffic even if the password is compromised
- Individualized data encryption for each user on a network

WPA3 should be the preferred choice for all new wireless network deployments.

**Community Discussion:** 0 comments

---

### Question 62
**Question Type:** Multiple Choice  
**Topic:** Network Equipment and Cabling

A network technician needs to connect two switches using fiber optic cable. Which of the following fiber optic connectors should be used for this connection?

**Answer Choices:**
A. RJ-45
B. LC
C. BNC
D. VGA

**Correct Answer:** B

**Detailed Explanation:**
LC (Lucent Connector) is the most commonly used fiber optic connector for switch-to-switch connections. It's a small form-factor connector that provides reliable, high-performance connectivity and is widely supported by modern network equipment.

Other fiber optic connector types include ST, SC, and FC, but LC is the current standard for most enterprise equipment.

**Community Discussion:** 0 comments

---

### Question 63
**Question Type:** Multiple Choice  
**Topic:** Network Monitoring and SNMP

A network administrator wants to monitor network traffic on a core switch. Which of the following protocols should be configured to collect traffic statistics?

**Answer Choices:**
A. SMTP
B. SNMP
C. SSH
D. Telnet

**Correct Answer:** B

**Detailed Explanation:**
SNMP (Simple Network Management Protocol) is used to monitor and manage network devices. It allows network administrators to collect statistics, monitor performance, and receive alerts from network equipment.

SNMP works by having network devices respond to queries from an SNMP manager, which can then analyze the data and provide insights into network performance and health.

**Community Discussion:** 0 comments

---

### Question 64
**Question Type:** Multiple Choice  
**Topic:** Routing Protocols

Which of the following routing protocols is classified as a link-state routing protocol?

**Answer Choices:**
A. RIP
B. OSPF
C. EIGRP
D. BGP

**Correct Answer:** B

**Detailed Explanation:**
OSPF (Open Shortest Path First) is a link-state routing protocol. Link-state protocols work by having each router share information about its directly connected networks with all other routers in the routing domain.

This allows each router to build a complete map of the network topology and calculate the best paths to all destinations using Dijkstra's algorithm.

**Community Discussion:** 0 comments

---

### Question 65
**Question Type:** Multiple Choice  
**Topic:** Network Segmentation

A company wants to separate their guest wireless network from their corporate network to prevent unauthorized access to corporate resources. Which of the following network design techniques should be implemented?

**Answer Choices:**
A. VLAN segmentation
B. MAC address filtering
C. Port security
D. Network address translation

**Correct Answer:** A

**Detailed Explanation:**
VLAN segmentation is the most effective way to separate networks and prevent unauthorized access. By placing the guest wireless network in a separate VLAN, you can:

- Isolate guest traffic from corporate traffic
- Apply different security policies to each VLAN
- Prevent broadcast traffic from crossing between networks
- Implement specific routing rules for inter-VLAN communication

This provides strong network isolation while allowing controlled access where needed.

**Community Discussion:** 0 comments

---

### Question 66
**Question Type:** Multiple Choice  
**Topic:** DNS and Domain Services

A user reports that they cannot access a website using its domain name, but they can access it using the IP address. Which of the following network services is most likely causing this issue?

**Answer Choices:**
A. DHCP
B. DNS
C. NAT
D. ARP

**Correct Answer:** B

**Detailed Explanation:**
DNS (Domain Name System) is responsible for translating domain names (like www.example.com) into IP addresses. If a user can access a website by IP address but not by domain name, it indicates a problem with DNS resolution.

This could be caused by:
- DNS server being unavailable or misconfigured
- DNS cache corruption
- DNS records not propagating properly
- Firewall blocking DNS traffic

**Community Discussion:** 0 comments

---

### Question 67
**Question Type:** Multiple Choice  
**Topic:** Network Address Assignment

A network administrator needs to configure IP addresses for a small office network. Which of the following private IP address ranges should be used?

**Answer Choices:**
A. 192.168.0.0/16
B. 10.0.0.0/8
C. 172.16.0.0/12
D. All of the above

**Correct Answer:** D

**Detailed Explanation:**
All three IP address ranges are valid private IP address ranges as defined by RFC 1918:

- 10.0.0.0/8 (10.0.0.0 - 10.255.255.255)
- 172.16.0.0/12 (172.16.0.0 - 172.31.255.255)
- 192.168.0.0/16 (192.168.0.0 - 192.168.255.255)

The choice between these ranges depends on the size of the network and specific requirements. The /16 range is commonly used for small networks as it provides a good balance of address space and subnetting flexibility.

**Community Discussion:** 0 comments

---

### Question 68
**Question Type:** Multiple Choice  
**Topic:** Network Troubleshooting Methodology

When troubleshooting a network connectivity issue, which of the following should be the FIRST step in the troubleshooting process?

**Answer Choices:**
A. Test the solution
B. Establish a plan of action
C. Identify the problem
D. Document the findings

**Correct Answer:** C

**Detailed Explanation:**
The first step in any network troubleshooting process should be to identify the problem. This involves:

- Talking to the user to understand the symptoms
- Gathering information about when the problem started
- Determining the scope of the issue
- Identifying what works and what doesn't

Without a clear understanding of the problem, it's impossible to develop an effective solution plan or test potential fixes.

**Community Discussion:** 0 comments

---

### Question 69
**Question Type:** Multiple Choice  
**Topic:** Network Security and Authentication

Which of the following authentication methods provides the strongest security for network access?

**Answer Choices:**
A. Password-only authentication
B. Username and password
C. Multi-factor authentication (MFA)
D. Certificate-based authentication

**Correct Answer:** C

**Detailed Explanation:**
Multi-factor authentication (MFA) provides the strongest security because it requires users to provide two or more different types of authentication factors:

- Something you know (password)
- Something you have (smartphone, token)
- Something you are (biometric)

This makes it much more difficult for attackers to gain unauthorized access, even if they compromise one authentication factor.

**Community Discussion:** 0 comments

---

### Question 70
**Question Type:** Multiple Choice  
**Topic:** Network Convergence and Redundancy

A network administrator wants to ensure that if one network path fails, traffic will automatically reroute through an alternate path. Which of the following technologies should be implemented?

**Answer Choices:**
A. Port aggregation
B. Spanning Tree Protocol (STP)
C. Load balancing
D. Network redundancy

**Correct Answer:** D

**Detailed Explanation:**
Network redundancy involves having multiple paths between network devices so that if one path fails, traffic can automatically reroute through an alternate path. This can be achieved through:

- Multiple physical links between switches
- Redundant core switches
- Multiple internet connections
- Diverse routing paths

This provides fault tolerance and ensures network availability even when individual components fail.

**Community Discussion:** 0 comments

---

### Question 71
**Question Type:** Multiple Choice  
**Topic:** Network Documentation and Asset Management

When documenting a network infrastructure, which of the following information should be included for each network device?

**Answer Choices:**
A. IP addresses only
B. Physical location and connections
C. MAC addresses only
D. Vendor information only

**Correct Answer:** B

**Detailed Explanation:**
Comprehensive network documentation should include:

- Physical location of the device
- Network connections and cabling
- IP addressing information
- Device configuration details
- Vendor and model information
- Asset tag numbers
- Installation dates
- Maintenance schedules

This information is crucial for troubleshooting, maintenance, and planning network expansions.

**Community Discussion:** 0 comments

---

### Question 72
**Question Type:** Multiple Choice  
**Topic:** Wireless Network Configuration

A wireless network is experiencing interference from a neighboring wireless network on the same channel. Which of the following should be done to resolve this issue?

**Answer Choices:**
A. Change to a non-overlapping channel
B. Increase the transmission power
C. Disable wireless security
D. Restart all wireless devices

**Correct Answer:** A

**Detailed Explanation:**
When experiencing interference from neighboring networks on the same channel, the best solution is to change to a non-overlapping channel. For 2.4 GHz networks, channels 1, 6, and 11 are non-overlapping.

For 5 GHz networks, there are more available non-overlapping channels. This reduces interference and improves wireless performance and reliability.

**Community Discussion:** 0 comments

---

### Question 73
**Question Type:** Multiple Choice  
**Topic:** Network Performance Optimization

A network administrator notices that file transfers are running slowly during business hours. Which of the following tools should be used to identify the bottleneck?

**Answer Choices:**
A. ping
B. traceroute
C. netstat
D. iperf

**Correct Answer:** D

**Detailed Explanation:**
iperf is a network performance testing tool that can measure bandwidth, throughput, and latency between two points on a network. It's specifically designed for network performance testing and can help identify bottlenecks by:

- Measuring actual throughput
- Testing different network paths
- Identifying latency issues
- Analyzing network performance under load

Tools like ping and traceroute are more suited for basic connectivity testing, while netstat shows network connections but doesn't measure performance.

**Community Discussion:** 0 comments

---

### Question 74
**Question Type:** Multiple Choice  
**Topic:** Network Security and Intrusion Prevention

Which of the following security devices is designed to inspect network traffic in real-time and block malicious traffic?

**Answer Choices:**
A. Switch
B. Hub
C. Intrusion Detection/Prevention System (IDS/IPS)
D. Load balancer

**Correct Answer:** C

**Detailed Explanation:**
An Intrusion Detection/Prevention System (IDS/IPS) is specifically designed to monitor network traffic for suspicious activity and take action to block malicious traffic:

- IDS: Detects and alerts on suspicious traffic
- IPS: Detects, alerts, and actively blocks malicious traffic

These systems use signature-based detection, anomaly detection, and behavioral analysis to identify and respond to security threats in real-time.

**Community Discussion:** 0 comments

---

### Question 75
**Question Type:** Multiple Choice  
**Topic:** Network Management and Monitoring

A network administrator wants to receive alerts when network devices go offline. Which of the following protocols should be configured?

**Answer Choices:**
A. SMTP
B. SNMP Traps
C. SSH
D. DNS

**Correct Answer:** B

**Detailed Explanation:**
SNMP Traps are used to send asynchronous notifications from network devices to a network management system. When configured, network devices can send alerts when:

- Interfaces go up or down
- Devices become unreachable
- Threshold conditions are met
- Security events occur

This provides real-time monitoring and alerting capabilities for network administrators.

**Community Discussion:** 0 comments

---

### Question 76
**Question Type:** Multiple Choice  
**Topic:** Network Implementation and Planning

A company is planning to implement a new network infrastructure. Which of the following should be considered FIRST in the planning process?

**Answer Choices:**
A. Budget constraints
B. Business requirements
C. Equipment vendor selection
D. Installation timeline

**Correct Answer:** B

**Detailed Explanation:**
Business requirements should be the first consideration in network planning because they determine all other decisions:

- Number of users and devices
- Required performance and capacity
- Security and compliance needs
- Application requirements
- Growth projections

Once business requirements are understood, you can then select appropriate technologies, vendors, and solutions that meet those requirements within budget and timeline constraints.

**Community Discussion:** 0 comments

---

### Question 77
**Question Type:** Multiple Choice  
**Topic:** Network Cabling and Physical Layer

When terminating network cables, which of the following tools is essential for creating proper connections?

**Answer Choices:**
A. Wire strippers
B. Cable tester
C. Punch down tool
D. All of the above

**Correct Answer:** D

**Detailed Explanation:**
Proper network cable termination requires multiple tools:

- Wire strippers: To remove cable jacket and expose individual wires
- Punch down tool: To terminate wires into keystone modules or patch panels
- Cable tester: To verify proper termination and test for continuity

Each tool serves a specific purpose in ensuring reliable, professional-quality cable installations.

**Community Discussion:** 0 comments

---

### Question 78
**Question Type:** Multiple Choice  
**Topic:** Network Security and Access Control

A company wants to implement a system that allows employees to access company resources from personal devices while maintaining security. Which of the following should be implemented?

**Answer Choices:**
A. BYOD (Bring Your Own Device) policy with MDM
B. VLAN segmentation only
C. Firewall rules only
D. Guest network access

**Correct Answer:** A

**Detailed Explanation:**
BYOD (Bring Your Own Device) policies combined with Mobile Device Management (MDM) provide the best approach for secure personal device access:

- Clear policies for acceptable use
- Device registration and approval process
- Security requirements (encryption, passwords, etc.)
- Remote wipe capabilities for lost/stolen devices
- Network access control integration

This ensures security while allowing the flexibility and productivity benefits of personal device use.

**Community Discussion:** 0 comments

---

### Question 79
**Question Type:** Multiple Choice  
**Topic:** Network Standards and Protocols

Which of the following IEEE standards defines Ethernet specifications for wired networks?

**Answer Choices:**
A. 802.11
B. 802.3
C. 802.1Q
D. 802.15

**Correct Answer:** B

**Detailed Explanation:**
IEEE 802.3 is the standard that defines Ethernet specifications for wired networks. This standard covers:

- Physical layer specifications
- MAC layer protocols
- Different Ethernet speeds (10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps, etc.)
- Auto-negotiation protocols
- Full-duplex operation

Other 802 standards cover different networking technologies:
- 802.11: Wireless LAN (WiFi)
- 802.1Q: VLAN tagging
- 802.15: Wireless PAN (Bluetooth)

**Community Discussion:** 0 comments

---

### Question 80
**Question Type:** Multiple Choice  
**Topic:** Network Troubleshooting and Connectivity

A user reports that they cannot reach the internet, but other users on the same network can. Which of the following should be the first troubleshooting step?

**Answer Choices:**
A. Check the user's default gateway configuration
B. Replace the network cable
C. Restart the user's computer
D. Check the user's IP address configuration

**Correct Answer:** D

**Detailed Explanation:**
When troubleshooting connectivity issues, the first step should be to check the user's IP address configuration. This includes:

- Verifying the user has a valid IP address
- Confirming the subnet mask is correct
- Checking the default gateway is reachable
- Ensuring DNS servers are accessible

Without a proper IP configuration, the user cannot communicate on the network or access internet resources.

**Community Discussion:** 0 comments

---

## Question 1 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Fundamentals

Which of the following is the primary purpose of a network switch?

**Answer Choices:**
A. Connect different network segments
B. Provide DHCP services
C. Route traffic between networks
D. Translate between protocols

**Correct Answer:** A

**Detailed Explanation:**
The primary purpose of a network switch is to connect devices within the same network segment and forward traffic based on MAC addresses. Switches operate at Layer 2 of the OSI model and make forwarding decisions based on hardware addresses.

**Community Discussion:** 0 comments

---

## Question 2 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Protocols

Which network protocol is used to automatically assign IP addresses to devices on a network?

**Answer Choices:**
A. DNS
B. DHCP
C. ARP
D. ICMP

**Correct Answer:** B

**Detailed Explanation:**
DHCP (Dynamic Host Configuration Protocol) is used to automatically assign IP addresses, subnet masks, default gateways, and DNS servers to network devices. This eliminates the need for manual IP address configuration.

**Community Discussion:** 0 comments

---

## Question 3 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Security

Which of the following is the most secure wireless encryption protocol?

**Answer Choices:**
A. WEP
B. WPA
C. WPA2
D. WPA3

**Correct Answer:** D

**Detailed Explanation:**
WPA3 is the most secure wireless encryption protocol available. It provides enhanced security features including protection against offline password guessing attacks and individual data encryption for each user.

**Community Discussion:** 0 comments

---

## Question 4 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Troubleshooting

A user reports slow network performance. Which of the following tools would be most useful for diagnosing the issue?

**Answer Choices:**
A. nslookup
B. tracert
C. ping
D. iperf

**Correct Answer:** D

**Detailed Explanation:**
iperf is a network performance testing tool that measures bandwidth and throughput. It's specifically designed for network performance analysis and can help identify bottlenecks and measure actual network performance.

**Community Discussion:** 0 comments

---

## Question 5 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Infrastructure

What is the main advantage of using fiber optic cable over copper cable for network connections?

**Answer Choices:**
A. Lower cost
B. Longer distance capability
C. Easier installation
D. Better electromagnetic interference resistance

**Correct Answer:** B

**Detailed Explanation:**
Fiber optic cable can carry signals over much longer distances than copper cable without signal degradation. This makes it ideal for backbone connections and long-distance network links.

**Community Discussion:** 0 comments

---

## Question 6 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Protocols

Which protocol is used to resolve IP addresses to MAC addresses on a local network?

**Answer Choices:**
A. DNS
B. DHCP
C. ARP
D. RARP

**Correct Answer:** C

**Detailed Explanation:**
ARP (Address Resolution Protocol) is used to resolve IP addresses to MAC addresses on a local network. When a device wants to communicate with another device on the same network, it uses ARP to find the MAC address corresponding to the IP address.

**Community Discussion:** 0 comments

---

## Question 7 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Topology

In a star network topology, where are the network devices connected?

**Answer Choices:**
A. Directly to each other
B. Through a central hub or switch
C. In a ring formation
D. In a mesh configuration

**Correct Answer:** B

**Detailed Explanation:**
In a star topology, all network devices connect to a central device such as a hub, switch, or router. This central device manages all network communications and provides a central point for network management and troubleshooting.

**Community Discussion:** 0 comments

---

## Question 8 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Security

What is the purpose of a firewall in a network environment?

**Answer Choices:**
A. Provide wireless connectivity
B. Monitor and control network traffic based on security rules
C. Assign IP addresses automatically
D. Route traffic between networks

**Correct Answer:** B

**Detailed Explanation:**
A firewall monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, such as the internet.

**Community Discussion:** 0 comments

---

## Question 9 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Standards

What does the "1000" in 1000BASE-T refer to?

**Answer Choices:**
A. Cable length in meters
B. Maximum number of devices
C. Data transmission speed in Mbps
D. Number of copper pairs

**Correct Answer:** C

**Detailed Explanation:**
The "1000" in 1000BASE-T refers to 1000 Mbps (1 Gbps) data transmission speed. The "T" indicates twisted pair cable, making this the standard for gigabit Ethernet over copper twisted pair cables.

**Community Discussion:** 0 comments

---

## Question 10 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Management

Which of the following is a common tool used for network monitoring and management?

**Answer Choices:**
A. Wireshark
B. Putty
C. CuteFTP
D. VLC Media Player

**Correct Answer:** A

**Detailed Explanation:**
Wireshark is a popular network protocol analyzer that allows network administrators to capture and analyze network traffic. It's an essential tool for network troubleshooting, security analysis, and protocol development.

**Community Discussion:** 0 comments

---

## Question 11 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Infrastructure

Which of the following devices operates at Layer 3 of the OSI model?

**Answer Choices:**
A. Hub
B. Switch
C. Router
D. Bridge

**Correct Answer:** C

**Detailed Explanation:**
Routers operate at Layer 3 (Network layer) of the OSI model and make forwarding decisions based on IP addresses. They connect different networks and route traffic between them.

**Community Discussion:** 0 comments

---

## Question 12 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Protocols

Which of the following is a connectionless protocol?

**Answer Choices:**
A. TCP
B. UDP
C. ICMP
D. ARP

**Correct Answer:** B

**Detailed Explanation:**
UDP (User Datagram Protocol) is a connectionless protocol that sends data without establishing a connection first. It provides faster data transfer than TCP but with no guarantee of delivery or order.

**Community Discussion:** 0 comments

---

## Question 13 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Security

What is the purpose of a VLAN?

**Answer Choices:**
A. Increase network speed
B. Segment broadcast domains
C. Replace switches
D. Provide wireless access

**Correct Answer:** B

**Detailed Explanation:**
VLANs (Virtual Local Area Networks) are used to segment broadcast domains within a switched network. They allow network administrators to group devices logically regardless of their physical location.

**Community Discussion:** 0 comments

---

## Question 14 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Performance

Which of the following can cause network latency?

**Answer Choices:**
A. Distance
B. Network congestion
C. Processing delays
D. All of the above

**Correct Answer:** D

**Detailed Explanation:**
Network latency can be caused by various factors including physical distance between devices, network congestion, processing delays at routers and switches, and quality of the transmission medium.

**Community Discussion:** 0 comments

---

## Question 15 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Cabling

What is the maximum recommended length for a single Ethernet cable segment?

**Answer Choices:**
A. 50 meters
B. 100 meters
C. 150 meters
D. 200 meters

**Correct Answer:** B

**Detailed Explanation:**
The maximum recommended length for a single Ethernet cable segment (Category 5 or higher) is 100 meters. This includes 90 meters of solid cable in the wiring closet and 5 meters of patch cable at each end.

**Community Discussion:** 0 comments

---

## Question 16 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Addressing

Which of the following is a valid subnet mask?

**Answer Choices:**
A. 255.255.0.0
B. 255.0.255.0
C. 255.255.255.255
D. All of the above

**Correct Answer:** D

**Detailed Explanation:**
All of the listed options are technically valid subnet masks. A subnet mask must consist of consecutive 1s followed by consecutive 0s. 255.255.0.0 is /16, 255.0.255.0 is /8+8=16, and 255.255.255.255 is /32.

**Community Discussion:** 0 comments

---

## Question 17 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Management

Which protocol is used to centrally manage network devices?

**Answer Choices:**
A. HTTP
B. Telnet
C. SNMP
D. FTP

**Correct Answer:** C

**Detailed Explanation:**
SNMP (Simple Network Management Protocol) is the standard protocol for network management. It allows network administrators to monitor, configure, and troubleshoot network devices remotely.

**Community Discussion:** 0 comments

---

## Question 18 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Security

What is the purpose of port security on a switch?

**Answer Choices:**
A. Prevent unauthorized access to switch ports
B. Secure wireless connections
C. Protect against viruses
D. Encrypt network traffic

**Correct Answer:** A

**Detailed Explanation:**
Port security on a switch limits which MAC addresses can access a particular switch port. If an unauthorized MAC address is detected, the port can be shut down or restricted, preventing unauthorized devices from connecting to the network.

**Community Discussion:** 0 comments

---

## Question 19 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Routing

Which routing protocol uses the Bellman-Ford algorithm?

**Answer Choices:**
A. OSPF
B. EIGRP
C. RIP
D. BGP

**Correct Answer:** C

**Detailed Explanation:**
RIP (Routing Information Protocol) uses the Bellman-Ford distance vector algorithm to determine the best path to destination networks. It has a maximum hop count of 15, with 16 considered unreachable.

**Community Discussion:** 0 comments

---

## Question 20 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Infrastructure

What is the main difference between a hub and a switch?

**Answer Choices:**
A. Hubs are faster than switches
B. Switches operate at Layer 2, hubs at Layer 1
C. Hubs are more expensive
D. Switches can only connect two devices

**Correct Answer:** B

**Detailed Explanation:**
The main difference is that switches operate at Layer 2 (Data Link layer) and forward frames based on MAC addresses, while hubs operate at Layer 1 (Physical layer) and simply repeat signals to all ports.

**Community Discussion:** 0 comments

---

## Question 21 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Protocols

Which protocol provides reliable, connection-oriented communication?

**Answer Choices:**
A. UDP
B. ICMP
C. TCP
D. ARP

**Correct Answer:** C

**Detailed Explanation:**
TCP (Transmission Control Protocol) provides reliable, connection-oriented communication. It establishes a connection before data transfer and ensures data is delivered correctly and in order.

**Community Discussion:** 0 comments

---

## Question 22 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Security

What is a common method to secure wireless networks?

**Answer Choices:**
A. MAC filtering only
B. WEP encryption only
C. WPA2 or WPA3 encryption with strong passwords
D. Open access with no security

**Correct Answer:** C

**Detailed Explanation:**
The most secure approach is to use WPA2 or WPA3 encryption with strong, unique passwords. MAC filtering alone is not sufficient security, and WEP is outdated and insecure.

**Community Discussion:** 0 comments

---

## Question 23 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Troubleshooting

Which command is used to test connectivity to a remote host?

**Answer Choices:**
A. ipconfig
B. ping
C. netstat
D. tracert

**Correct Answer:** B

**Detailed Explanation:**
The ping command is used to test connectivity to a remote host by sending ICMP echo request packets and waiting for echo reply packets. It helps determine if a host is reachable and measures round-trip time.

**Community Discussion:** 0 comments

---

## Question 24 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Standards

What does "802.11ac" refer to?

**Answer Choices:**
A. Ethernet standard
B. WiFi standard
C. Bluetooth standard
D. Cellular standard

**Correct Answer:** B

**Detailed Explanation:**
802.11ac is a WiFi standard that provides high-speed wireless networking in the 5 GHz band. It supports speeds up to several gigabits per second and is commonly known as WiFi 5.

**Community Discussion:** 0 comments

---

## Question 25 - Topic 1
**Question Type:** Multiple Choice  
**Topic:** Network Infrastructure

Which device is used to connect multiple networks together?

**Answer Choices:**
A. Hub
B. Switch
C. Router
D. Bridge

**Correct Answer:** C

**Detailed Explanation:**
A router is used to connect multiple networks together and route traffic between them. It operates at Layer 3 and makes forwarding decisions based on IP addresses.

**Community Discussion:** 0 comments

---

## Question 26 - Topic 1
**Question Type:** SIMULATION

**Question Text:**  
A network technician replaced an access layer switch and needs to reconfigure it to allow the connected devices to connect to the correct networks.  
INSTRUCTIONS: Click on the appropriate port(s) on Switch 1 and Switch 3 to verify or reconfigure the correct settings:  
- Ensure each device accesses only its correctly associated network.  
- Disable all unused switchports.  
- Require fault-tolerant connections between the switches.  
- Only make necessary changes to complete the above requirements.  
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

**Answer Choices:**  
*Simulation-based practical configuration task*

**Correct Answer:**  
*Visual solution provided showing the correct port configuration*

**Detailed Explanation:**  
This simulation tests the ability to configure VLANs, port security, and redundant connections in a switched network environment.

**Community Discussion:** 31 comments

---

## Question 27 - Topic 1
**Question Type:** SIMULATION

**Question Text:**  
A network technician was recently onboarded to a company. A manager has tasked the technician with documenting the network and has provided the technician with partial information from previous documentation.  
INSTRUCTIONS: Click on each switch to perform a network discovery by entering commands into the terminal. Type help to view a list of available commands.  
Fill in the missing information using the drop-down menus provided.  
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

**Answer Choices:**  
*Simulation-based network discovery and documentation task*

**Correct Answer:**  
*Visual solution provided showing the network documentation*

**Detailed Explanation:**  
This simulation tests the ability to use network discovery commands and properly document network infrastructure.

**Community Discussion:** 28 comments

---

## Question 28 - Topic 1
**Question Type:** SIMULATION

**Question Text:**  
Users are unable to access files on their department share located on file server 2. The network administrator has been tasked with validating routing between networks hosting workstation A and file server 2.  
INSTRUCTIONS: Click on each router to review output, identify any issues, and configure the appropriate solution.  
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

**Answer Choices:**  
*Simulation-based router configuration and troubleshooting*

**Correct Answer:**  
*Visual solution provided showing router configuration fixes*

**Detailed Explanation:**  
This simulation tests knowledge of routing protocols, network connectivity troubleshooting, and router configuration.

**Community Discussion:** 25 comments

---

## Question 29 - Topic 1
**Question Type:** SIMULATION

**Question Text:**  
A network administrator has been tasked with configuring a network for a new corporate office. The office consists of two buildings, separated by 50 feet with no physical connectivity. The configuration must meet the following requirements:  
- Devices in both buildings should be able to access the Internet.  
- Security insists that all Internet traffic be inspected before entering the network.  
- Desktops should not see traffic destined for other devices.  
INSTRUCTIONS: Select the appropriate network device for each location. If applicable, click on the magnifying glass next to any device which may require configuration updates and make any necessary changes. Not all devices will be used, but all locations should be filled.  
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

**Answer Choices:**  
*Visual network topology and device selection*

**Correct Answer:**  
*Visual solution showing proper device placement and configuration*

**Detailed Explanation:**  
This simulation tests understanding of network security devices, Internet access configuration, and network segmentation.

**Community Discussion:** 22 comments

---

## Question 30 - Topic 1
**Question Type:** SIMULATION

**Question Text:**  
A network technician needs to resolve some issues with a customer's SOHO network. The customer reports that some of the devices are not connecting to the network, while others appear to work as intended.  
INSTRUCTIONS: Troubleshoot all the network components and review the cable test results by clicking on each device and cable. Type help in each terminal to view a list of available commands.  
Diagnose the appropriate component(s) by identifying any components with a problem and recommend a solution to correct each problem.  
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

**Answer Choices:**  
*Simulation-based SOHO network troubleshooting*

**Correct Answer:**  
*Visual solution showing identified problems and solutions*

**Detailed Explanation:**  
This simulation tests the ability to troubleshoot common SOHO network issues using proper diagnostic tools and methodologies.

**Community Discussion:** 19 comments

---

## Question 31 - Topic 1
**Question Type:** SIMULATION

**Question Text:**  
After a recent power outage, users are reporting performance issues accessing the application servers. Wireless users are also reporting intermittent Internet issues.  
INSTRUCTIONS: Click on each tab at the top of the screen. Select a widget to view information, then use the drop-down menus to answer the associated questions.  
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

**Answer Choices:**  
*Simulation-based performance monitoring and analysis*

**Correct Answer:**  
*Visual solution showing performance analysis and solutions*

**Detailed Explanation:**  
This simulation tests understanding of network performance monitoring, incident response, and problem analysis techniques.

**Community Discussion:** 16 comments

---

## Question 32 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following steps of the troubleshooting methodology would most likely include checking through each level of the OSI model after the problem has been identified?

**Answer Choices:**
A. Establish a theory.
B. Implement the solution.
C. Create a plan of action.
D. Verify functionality.

**Correct Answer:** A

**Detailed Explanation:**  
The "Establish a theory" step of the troubleshooting methodology involves testing theories about the cause of the problem. This is the most appropriate time to systematically check through each layer of the OSI model to identify where the issue might be occurring.

**Community Discussion:** Vote distribution: A: 70%, D: 26%, Other: 4%

---

## Question 33 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
While troubleshooting a VoIP handset connection, a technician's laptop is able to successfully connect to network resources using the same port. The technician needs to identify the port on the switch. Which of the following should the technician use to determine the switch and port?

**Answer Choices:**
A. LLDP
B. IKE
C. VLAN
D. netstat

**Correct Answer:** A

**Detailed Explanation:**  
LLDP (Link Layer Discovery Protocol) is used to identify network devices and their capabilities. This protocol allows devices to advertise information about themselves, including which switch port they are connected to.

**Community Discussion:** Vote distribution: A: 100%, C: 25%, B: 20%

---

## Question 34 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
A network administrator needs to set up a file server to allow user access. The organization uses DHCP to assign IP addresses. Which of the following is the best solution for the administrator to set up?

**Answer Choices:**
A. A separate scope for the file server using a /32 subnet
B. A reservation for the server based on the MAC address
C. A static IP address within the DHCP IP range
D. A SLAAC for the server

**Correct Answer:** B

**Detailed Explanation:**  
A DHCP reservation is the best solution because it ensures the file server always receives the same IP address while still using the DHCP infrastructure. This is more reliable and easier to manage than static configurations.

**Community Discussion:** Vote distribution: B: 100%, C: 25%, A: 20%

---

## Question 35 - Topic 1
**Question Type:** Multiple Choice

**Question Text:**  
Which of the following technologies are X.509 certificates most commonly associated with?

**Answer Choices:**
A. PKI
B. VLAN tagging
C. LDAP
D. MFA

**Correct Answer:** A

**Detailed Explanation:**  
X.509 certificates are digital certificates that are a fundamental component of Public Key Infrastructure (PKI). They are used to bind public keys to entities and are essential for secure communications, authentication, and digital signatures.

**Community Discussion:** Vote distribution: A: 100%, C: 25%, B: 20%

---

## Summary

**Current Progress:** 35/50 questions (70% complete)  
**Exam Coverage:** Introduction to CompTIA Network+ exam topics  
**Last Updated:** 2025-11-06 18:56:01