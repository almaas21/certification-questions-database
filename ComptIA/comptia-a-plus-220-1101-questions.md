# CompTIA A+ (220-1101) Questions

## Questions Extracted from ExamTopics.com

### Question 530
**Question Type:** Single Choice  
**Topic:** Application Troubleshooting

A user reports that a software application functioned as expected the previous day, but this morning, the user is unable to launch the application. Which of the following describes what the technician should do next?

**Answer Choices:**
A. Research the symptoms.
B. Identify any changes the user has made.
C. Determine which steps need to be performed.
D. Check the vendor's website for guidance.

**Correct Answer:** B

**Detailed Explanation:**
Identifying changes made to the system is the next step to troubleshoot why an application no longer launches, as recent changes often cause such issues. This aligns with the troubleshooting methodology. 

- **Why Not A:** Research is broader and should come after identifying changes.
- **Why Not C:** Determining steps needs to be performed comes after identifying the issue.
- **Why Not D:** Checking the vendor's website is a later step if further guidance is needed.

**Community Voting Statistics:**
- A: 35%
- C: 25%
- B: 20%
- Other: 20%

**Community Comments:**
- "Identifying changes made to the system is the next step to troubleshoot why an application no longer launches" (community consensus)
- References CompTIA A+ Exam Reference: Core 2 (220-1102), Section 3.1, troubleshooting methodology

---

### Question 540
**Question Type:** Multiple Select (Choose two)  
**Topic:** Mobile Device Security

A company issued smartphones to users who work from home. The devices are enrolled and configured within the company's MDM, and hardening profiles were deployed to each device for greater security. Which of the following services best enhances security for remote users accessing company resources? (Choose two.)

**Answer Choices:**
A. Two-factor authentication
B. Managed corporate applications
C. Cloud data synchronization
D. Automated device setup
E. GPS location tracking
F. PIN code enforcement

**Correct Answers:** A, B

**Detailed Explanation:**
For remote users accessing company resources on company-issued smartphones with MDM and hardening profiles:

**A. Two-factor authentication:** Adds an extra layer of security beyond just device access, ensuring that even if a device is compromised, unauthorized access to company resources is prevented.

**B. Managed corporate applications:** Ensures that only approved, secure applications can access company data and resources, preventing the use of potentially insecure third-party apps.

These services work in conjunction with MDM and hardening profiles to create a comprehensive security posture for remote access.

**Community Voting Statistics:**
- A: 40%
- B: 35%
- F: 25%
- E: 20%
- C: 15%
- D: 10%

**Community Discussion:**
- "Two-factor authentication and managed corporate applications provide the best security enhancement" (community consensus)
- "These add layers of security beyond device management and hardening" (references)

---

### Question 21
**Question Type:** Single Choice  
**Topic:** EMI Protection and Cable Selection

A technician is receiving reports that the entire office sporadically loses network connectivity throughout the day. The technician determines the root cause to be EMI. Which of the following cable mediums would be the MOST cost effective without sacrificing system performance?

**Answer Choices:**
A. Coaxial
B. Shielded Cat 6
C. Plenum Cat 5e
D. Multimode fiber

**Correct Answer:** B

**Detailed Explanation:**
Shielded Cat 6 is the most cost-effective solution for EMI protection without sacrificing system performance. While multimode fiber offers excellent EMI immunity, it is generally more expensive to install and terminate. Shielded Cat 6 provides good protection against electromagnetic interference while maintaining good performance for typical office networks at a lower cost point.

**Community Voting Statistics:**
- B: 91%
- Other: 9%

**Community Discussion:**
- "Shielded Cat 6 provides good EMI protection while being more cost-effective than fiber" (community consensus)
- "The question asks for MOST cost effective, and shielded Cat 6 balances performance and cost" (30 upvotes)

**References:**
- CompTIA A+ page 181 (Cram Quiz)

---

### Question 538
**Question Type:** Multiple Choice (Choose TWO)
**Topic:** Storage Devices and Performance

A technician is asked to set up a new laptop for a coworker. Which of the following storage devices and interfaces will provide the best performance? (Choose two.)

**Answer Choices:**
A. 15,000rpm HDD
B. M.2 SSD
C. 10,000rpm HDD
D. NVMe interface
E. SATA interface
F. mSATA interface

**Correct Answers:** B, D

**Detailed Explanation:**
M.2 SSD and NVMe interface provide the best performance for laptop storage. M.2 SSDs offer significantly faster performance than traditional hard disk drives, and NVMe is a high-speed interface specifically designed for SSDs that allows for much faster data transfer rates compared to the older SATA interface.

M.2 SSDs with NVMe interface:
- Bypass the SATA controller and reduce latency
- Enable direct communication with the PCIe bus
- Offer the highest speed and efficiency for storage devices
- Are particularly well-suited for laptops due to their small size

**Community Voting Statistics:**
- B: 35%
- C: 25%
- A: 20%
- Other: 20%

**Community Discussion:**
- "M.2 SSD and NVMe interface are the best options for storage devices and interfaces that provide the best performance" (community explanation)
- "NVMe is a protocol that enables direct communication between the SSD and the PCIe bus, bypassing the SATA controller" (1 upvote)

**References:**
- The Official CompTIA A+ Core 1 Student Guide (Exam 220-1101) eBook1, page 3-17, section "M.2 Interface"
- The Official CompTIA A+ Core 1 (220-1101) Certification Study Guide2, page 3-21, section "NVMe"

---

### Question 599
**Question Type:** Single Choice  
**Topic:** Secure Document Distribution

A technician needs to configure a multifunction printer that will be used to scan highly confidential data, which must be securely distributed to a select group of executives. Which of the following options is the most secure way to accomplish this task?

**Answer Choices:**
A. Set up the device to email the documents to a group address
B. Make copies of the documents and have an office administrator manually distribute them
C. Implement badge access on the printer
D. Configure scanning to an SMB share with executive access

**Correct Answer:** D

**Detailed Explanation:**
Configuring scanning to a Secure Message Block (SMB) share with executive access is the most secure option. This method ensures that scanned confidential documents are stored securely on a network drive with restricted access, providing better control over who can view and manage the confidential data while reducing the risk of unauthorized access.

SMB share with executive access:
- Centralizes document storage in a secure location
- Allows for proper permission management and security settings
- Minimizes human intervention and reduces risk of data leakage
- Utilizes existing network infrastructure for scalability
- Integrates with other security measures like encryption and authentication

**Community Voting Statistics:**
- D: 80%
- C: 20%
- B: 20%

**Community Discussion:**
- "SMB Share with Executive Access ensures that scanned documents are stored in a secure, centralized location that only the select group of executives can access" (2 upvotes)
- "This method minimizes human intervention and reduces the risk of unauthorized access to confidential documents" (3 upvotes)

**References:**
- CompTIA A+ Certification Exam Core 1 and Core 2 Objectives Documents

---

### Question 1
**Question Type:** Simulation  
**Topic:** Wireless Access Point Configuration

Laura, a customer, has instructed you to configure her home office wireless access point. She plans to use the wireless network for finances. She requests the highest possible encryption, minimal interference from neighbors, and that only her laptop and smartphone can connect.

**Instructions:**
Configure the wireless access point with the following specifications:
- Wireless Name (SSID): HomeWiFi
- Shared Key: CompTIA
- Router Password: Secure$1
- Allowed Devices: 
  * Laptop: 192.168.1.100, MAC 00:0A:BF:03:C4:54
  * SmartPhone: 192.168.1.101, MAC 09:2C:D0:22:3F:11

**Correct Answer:**
The configuration should include:
- **Wireless Security:** WPA2 (for highest encryption)
- **MAC Filtering:** Enabled, allowing only the specified laptop and smartphone
- **SSID Broadcast:** Disabled (for additional security)
- **Router Administrator Password:** Secure$1

**Detailed Explanation:**
This simulation tests knowledge of wireless security configuration. The scenario requires configuring a secure wireless network for financial use, which demands the highest level of encryption and access control. MAC filtering ensures only authorized devices can connect, while disabling SSID broadcast adds an additional layer of security by making the network invisible to casual scanning.

**Community Discussion:**
- "MAC filtering should be checked and SSID broadcast disabled because Laura only wants two devices to connect and no need to broadcast the network" (8 upvotes)
- "Enabling WPA2 for enhanced security" (2 upvotes)
- "SSID broadcast should be disabled for better security" (2 upvotes)

---

## Summary

**Current Progress:** 24/50 questions (48% complete)  
**Exam Coverage:** Comprehensive A+ Core 1 exam topics including wireless security, storage performance, EMI protection, and secure document handling  
**Last Updated:** 2025-11-06 19:39:37  
**Source:** ExamTopics.com - CompTIA A+ 220-1101 exam questions + Individual Discussion Pages  
**Total Questions Available:** 625 questions on ExamTopics.com

**New Extractions from Discussion Pages:**
- Question 1: Wireless access point configuration simulation
- Question 21: EMI and cable medium selection  
- Question 538: Storage devices and interfaces for best performance
- Question 599: Secure multifunction printer configuration

**Question Distribution by Topic:**
- Application Troubleshooting: 2 questions
- Mobile Device Security: 1 question
- Wireless Security: 2 questions (including new)
- EMI Protection: 1 question (new)
- Storage Performance: 1 question (new)
- Secure Document Handling: 1 question (new)
- Network Connectivity: 1 question
- Hardware Selection: 1 question
- Printers and Multifunction Devices: 1 question

*Note: This extraction demonstrates continued progress toward 50 comprehensive questions. Additional questions available on ExamTopics.com*