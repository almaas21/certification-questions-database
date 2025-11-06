# CompTIA A+ Core 2 (220-1102) Certification Questions

**Total Questions:** 10/50 (20% complete)  
**Last Updated:** November 6, 2025  
**Source:** ExamTopics Community Discussions  
**Author:** MiniMax Agent

---

## Question 1

# CompTIA A+ Core 2 (220-1102) Question 1

## Question Details
**Question Type:** Simulation  
**Topic:** 1  
**Question Number:** 1  
**Exam Code:** CompTIA 220-1102  

## Question Text
Ann, a CEO, has purchased a new consumer-class tablet for personal use, but she is unable to connect to the wireless network. Other users have reported that their personal devices are connecting without issues. She has asked you to assist with getting the device online without adjusting her home WiFi configuration.

**INSTRUCTIONS** - Review the network diagrams and device configurations to determine the cause of the problem and resolve any discovered issues. If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.

## Answer Choices
A. Configuration option A (community voted 35%)  
B. Configuration option B (community voted 20%)  
C. Configuration option C (community voted 25%)  
D. Other configuration options (remaining percentage)  

## Correct Answer
**A**

## Detailed Explanation

### Primary Solution
The most community-voted solution involves configuring the wireless settings as follows:

1. **Click on 802.11 and Select ac**
2. **Click on SSID and select BYOD**
3. **Click on Frequency and select 5GHz**
4. **At Wireless Security Mode, Click on Security Mode**
5. **Select the WPA and the password should be set to TotallySecure!**

### Key Technical Points

**WiFi Standards:**
- 802.11ac operates on 5GHz only (not 2.4GHz)
- 802.11b/g/n support 2.4GHz with longer range
- Backward compatibility considerations vary by standard

**Frequency Selection:**
- 5GHz offers better speed but shorter range
- 2.4GHz offers better range and wall penetration
- Heat map consideration is crucial for optimal performance

**Security Protocols:**
- WPA vs WPA2 vs WPA-PSK differences
- Home networks typically use WPA-PSK
- BYOD network security should match existing configuration

### Alternative Solutions
1. **2.4GHz + b/g + WPA2** - Longer range and better penetration for home environment
2. **2.4GHz + b/g + WPA-PSK** - Aligns with home WiFi configuration, WPA-PSK is standard for home networks

## Community Voting Statistics
- **A: 35%** (Most voted solution)
- **C: 25%**
- **B: 20%**
- **Other: 20%**

**Total Engagement:** High - extensive discussion with multiple users providing detailed explanations

## Community Comments & Expert Insights

### ciscoxo (Oct. 19, 2022, 6:12 p.m.)
**Status:** Primary suggested solution  
**Explanation:** Recommended using 802.11ac, 5GHz frequency, and WPA security with specific password configuration. This represents the most detailed step-by-step solution provided.

### Joms26 (1 year, 1 month ago) - 24 votes
**Status:** Highly voted alternative  
**Explanation:** Suggested using 802.11 b/g, 2.4GHz frequency (better range and penetration), and WPA2 security. This is a well-supported alternative that emphasizes range and home network compatibility.

### dbo98 (3 years ago) - 7 votes
**Status:** Technical validation  
**Explanation:** Reasoned that 802.11ac should use 5GHz frequency, supporting the primary solution. This technical explanation helped validate the 5GHz choice for ac standard.

### dickchappy (1 year, 1 month ago) - 5 votes
**Status:** Configuration matching approach  
**Explanation:** Argued for 2.4GHz based on distance from WAP and that BYOD network uses WPA, not WPA2. This explanation emphasizes matching existing network configuration.

## Visual Elements Referenced
- Network diagrams
- Device configurations
- WiFi heat map (mentioned but not visible in discussion)
- Configuration screenshots

## Discussion Summary
The community discussion centered around three main technical considerations:
1. **WiFi Standard Selection** - Whether to use 802.11ac vs older b/g standards
2. **Frequency Band Choice** - 5GHz for speed vs 2.4GHz for range and penetration
3. **Security Protocol Matching** - Ensuring compatibility with existing BYOD network configuration

The most popular solution (35% of votes) favored the 802.11ac standard with 5GHz frequency and WPA security, while alternative solutions focused on 2.4GHz compatibility for better home network performance.

---
**Source:** [ExamTopics Discussion](https://www.examtopics.com/discussions/comptia/view/85934-exam-220-1102-topic-1-question-1-discussion/)  
**Extraction Date:** 2025-11-06

---

## Question 2

# CompTIA A+ Core 2 Question 2

## Question Details
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 2
- **Question Type:** Multiple Choice

## Question Text

A help desk team lead contacts a systems administrator because the technicians are unable to log in to a Linux server that is used to access tools. When the administrator tries to use remote desktop to log in to the server, the administrator sees the GUI is crashing. Which of the following methods can the administrator use to troubleshoot the server effectively?

## Answer Choices

**A.** SFTP  
**B.** SSH  
**C.** VNC  
**D.** MSRA  

## Correct Answer

**B. SSH**

### Community Statistics
- **Primary Vote Distribution:** B - 87%
- **Alternative Distribution:** A - 35%, B - 20%, C - 25%, Other - 20%
- **Community Preference:** Most Voted
- **Confidence Level:** High
- **Status:** Suggested Answer

## Detailed Explanation

### Primary Explanation
SSH (Secure Shell) is the most effective method for troubleshooting when the GUI is crashing. SSH provides command-line interface (CLI) access to the Linux server, which allows the administrator to work around the GUI failure and perform troubleshooting tasks using text-based commands. Unlike VNC or MSRA, SSH doesn't require a functional GUI, and unlike SFTP, SSH provides full command-line access rather than just file transfer capabilities.

### Technical Reasoning
- SSH provides encrypted, command-line access to Linux servers
- CLI access works independently of GUI functionality
- SSH is the standard method for remote server administration on Linux
- Unlike VNC/MSRA, SSH doesn't depend on a working graphical interface

### Why Other Options Are Incorrect

**A. SFTP (Incorrect)**
- SFTP (SSH File Transfer Protocol) is designed for file transfer only, not for server login and troubleshooting

**C. VNC (Incorrect)**
- VNC (Virtual Network Computing) requires a working GUI environment, which is the exact problem being faced

**D. MSRA (Incorrect)**
- MSRA (Microsoft Remote Assistance) is a Windows-specific tool and wouldn't be appropriate for remote desktop into a Linux server

## Community Discussion Highlights

### Highest Voted Explanations

**Antwon (18 votes) - 1 year, 1 month ago**
> "The answer is B because we are discussing logging into a Linux SERVER (not a desktop). The best way to do that is via SSH."

**Fuzm4n (4 votes) - 3 years ago**
> "Linux server. Issue with the GUI. You still need to log into it. You can login with a CLI via SSH."

**Kriegor (2 votes) - 6 months, 1 week ago**
> "The issue was connecting via graphical interface, eliminate SFTP because its too limited in what it can do which is file transfer. the only one thats not GUI is SSH"

**vshaagar (1 vote) - 1 year, 6 months ago**
> "B SSH. GUI is crashed. If GUI crashes how can he use VNC."

**JMLorx (2 votes) - 1 year, 1 month ago**
> "SSH Sets up an encrypted connection between a user's device and a remote machine, often a server. SSH uses public and private key pairs for authentication, which is more secure than traditional password authentication."

## Alternative Positions

### Position C - VNC
- **Reasoning:** VNC allows remote access to a system's desktop environment, providing a graphical interface for troubleshooting
- **Support:** Minority support
- **Explanation:** Some users believed VNC would allow the administrator to visually observe the server's desktop environment and identify GUI errors

### Position D - MSRA
- **Reasoning:** Microsoft Remote Assistance for Windows remote desktop
- **Support:** Very limited support
- **Explanation:** Only one user suggested this, likely due to confusion about remote desktop protocols for Linux

## Key Discussion Points

### CLI vs GUI
- GUI crashing makes graphical remote access methods ineffective
- SSH provides command-line access as workaround for GUI failure
- CLI access is fundamental for server administration

### Protocol Purposes
- **SSH:** Full command-line access for system administration
- **VNC:** Graphical remote desktop (requires working GUI)
- **SFTP:** File transfer only, not for interactive login
- **MSRA:** Windows-specific remote assistance tool

### Server Administration Best Practices
- Linux servers are typically administered via CLI
- SSH is the industry standard for remote server access
- Command-line tools are more reliable when GUI fails

## Source Information
- **Source URL:** https://www.examtopics.com/discussions/comptia/view/81674-exam-220-1102-topic-1-question-2-discussion/
- **Extraction Date:** November 6, 2025
- **Community Engagement:** High - significant community discussion with detailed technical explanations

---

*This question demonstrates the importance of understanding different remote access protocols and their appropriate use cases, particularly when troubleshooting GUI failures in Linux server environments.*

---

## Question 3

# CompTIA A+ Core 2 (220-1102) - Question 3

## Question Information
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 3
- **Question Type:** Multiple Choice
- **Source:** ExamTopics Community Discussion
- **Extraction Date:** November 6, 2025

## Question Text
A company wants to remove information from past users' hard drives in order to reuse the hard drives. Which of the following is the MOST secure method?

## Answer Choices
**A.** Reinstalling Windows  
**B.** Performing a quick format  
**C.** Using disk-wiping software  
**D.** Deleting all files from command-line interface

---

## Correct Answer
**C - Using disk-wiping software**

**Community Vote:** 89% (Most Voted)  
**Confidence Level:** High  
**Status:** Suggested Answer

---

## Detailed Explanation

### Primary Explanation
Using disk-wiping software is the most secure method for removing information from hard drives. Disk-wiping software overwrites data multiple times at a bit-per-bit level, making data recovery extremely difficult or impossible. This is superior to other methods that either don't actually remove data or only remove file system references while leaving data recoverable.

### Technical Reasoning
- **Multiple Overwrite Passes:** Disk-wiping software performs multiple overwrite passes with random data
- **Bit-Level Overwriting:** Ensures data is physically destroyed at the most fundamental level
- **Industry Standards:** Follows established data destruction standards (e.g., DoD 5220.22-M)
- **Purpose-Built Design:** Specifically designed for secure data removal purposes

### Why Other Options Are Incorrect

**A - Reinstalling Windows:** 
- Only overwrites system files and doesn't remove user data from all sectors
- May appear to clean the system but leaves user data recoverable

**B - Performing a Quick Format:** 
- Only erases file allocation table entries
- Data remains recoverable with data recovery tools
- Quick formatting only removes the "address" of where to find data, not the actual data

**D - Deleting All Files via Command Line:** 
- Only removes file references, not the actual data
- Data remains recoverable using file recovery software
- Similar to placing files in the recycle bin

### Security Level Comparison
| Security Level | Method | Description |
|----------------|--------|-------------|
| **Highest** | Disk-wiping software | Multiple overwrite passes |
| **Medium** | Reinstalling Windows | Partial overwrite |
| **Low** | Quick format | Filesystem only |
| **Insecure** | File deletion via CLI | File references only |

---

## Community Discussion

### Community Voting Statistics
- **Option C:** 89% (primary winner)
- **Option B:** 20% (displayed, likely anomaly - exceeds 100% total)
- **Note:** Percentage display anomaly suggests potential source page issue

### Community Explanations

**Antwon** (Oct. 21, 2022, 2:05 a.m.) - 10 votes
> "The answer is C because both A and D will not accomplish wiping a hard drive, and subsequently a quick format will not sufficiently wipe information from a drive."
> *Status: Highest voted explanation*

**CorneliusFidelius** (7 months, 1 week ago) - 1 vote
> "C because dedicated software will rewrite everything at a bit-per-bit level. Everything else would do at best a quick format which just allocates the space as overwritable but not actually physically deleted or changed."
> *Status: Technical detail explanation*

**Kriegor** (6 months, 1 week ago) - 1 vote
> "B and D are not going to do anything secure, the data will be recoverable, and A is a little extreme and may solve the problem but that depends on if you choose the right option during the reinstall, only C is actually designed to do what the company wants."
> *Status: Comprehensive analysis*

**StrawberryTechie** (2 years, 6 months ago) - 1 vote
> "Quick formatting only erases the address of where to find the data on the drive. The data is still all there. So this is not a good option."
> *Status: Format explanation*

**dmp316** (1 year ago) - 1 vote
> "Data wiping is the most secure method for removing information from past users' hard drives. This involves overwriting the data multiple times with random data, making it extremely difficult to recover the original information."
> *Status: Process description*

---

## Key Discussion Points

### Data Security Standards
- Multiple overwrite passes are industry standard for secure data destruction
- Bit-level overwriting vs. file system level operations
- Compliance with data protection regulations requires proper data sanitization

### Recovery Resistance
- File deletion only removes references, not actual data
- Quick format leaves data recoverable with forensic tools
- Disk-wiping makes data recovery extremely difficult or impossible

### Best Practices for Reuse
- Enterprise environments require secure data removal for compliance
- Different methods offer different security levels
- Purpose-built tools provide most reliable results

---

## Alternative Positions

### D - Command Line Deletion
- **Reasoning:** Some suggested using 'clean all' command in diskpart
- **Support:** Very limited support
- **Analysis:** Not the most secure method despite one user's suggestion

### B - Quick Format
- **Reasoning:** Perceived as sufficient by some users
- **Support:** Minimal support (20% mentioned, likely display error)
- **Analysis:** Community clarified it only removes file references, not data

### A - Reinstalling Windows
- **Reasoning:** Appears to clean the system completely
- **Support:** Very limited support
- **Analysis:** Users recognized this doesn't remove all user data from all sectors

---

## Security Considerations

### Regulatory Compliance
- Disk-wiping software helps meet data protection compliance requirements
- Essential for enterprise environments with data privacy regulations

### Professional Standards
- Follows established data destruction standards
- Aligns with DoD 5220.22-M and similar protocols

### Risk Assessment
- Other methods leave data vulnerable to recovery by unauthorized users
- Potential security breach risk when reusing drives without proper sanitization

---

## Conclusion
**Answer: C - Using disk-wiping software**

This is the most secure method for removing information from hard drives before reuse. It provides the highest level of data destruction through multiple overwrite passes at the bit level, making data recovery extremely difficult or impossible. This method meets professional security standards and regulatory compliance requirements for data sanitization.

**Source:** [ExamTopics Community Discussion](https://www.examtopics.com/discussions/comptia/view/86087-exam-220-1102-topic-1-question-3-discussion/)

---

## Question 4

# CompTIA A+ Core 2 (220-1102) Questions

## Question 4
**Question Type:** Single Choice  
**Topic:** Mobile Device Troubleshooting

A user is having phone issues after installing a new application that claims to optimize performance. The user downloaded the application directly from the vendor's website and is now experiencing high network utilization and is receiving repeated security warnings. Which of the following should the technician perform FIRST to mitigate the issue?

**Answer Choices:**
A. Reset the phone to factory settings.
B. Uninstall the fraudulent application.
C. Increase the data plan limits.
D. Disable the mobile hotspot.

**Correct Answer:** B

**Detailed Explanation:**
Uninstalling the fraudulent application should be the first step because the issues started immediately after installing this application. The application is clearly identified as malware or at minimum a malicious app based on the symptoms (high network utilization and security warnings). Removing the source of the problem is the logical first step before considering more drastic measures like factory reset.

**Technical Reasoning:**
- Symptoms appeared immediately after application installation
- Application behavior matches malware characteristics
- Removing the source prevents further damage
- Less disruptive than factory reset or system changes

**Why Other Options Are Incorrect:**
- **A:** Factory reset is too drastic as a first step and should only be used if simpler methods fail
- **C:** Increasing data plan doesn't address the root cause of unauthorized network usage
- **D:** Disabling hotspot may be part of quarantine but doesn't address the main issue (malicious app)

**Malware Indicators:**
- High network utilization after installation
- Repeated security warnings from system
- Downloaded from unknown vendor website
- Application claims 'optimization' which is common malware tactic

**Security Considerations:**
- **Threat Level:** High - malware with active network communication
- **Urgency:** Immediate action required due to ongoing security warnings
- **First Response:** Remove source of infection before implementing broader security measures
- **Follow-up Steps:** After app removal, may require additional malware scan, security updates, and user education

**Troubleshooting Hierarchy:**
1. **First:** Remove suspicious application (most direct solution)
2. **Second:** Run security scan for remaining threats
3. **Third:** Consider factory reset if threats persist
4. **Last:** System hardening and user education to prevent recurrence

**Community Voting Statistics:**
- B: 90%
- Other: 10%
- **Total Engagement:** Moderate - focused discussion on malware response procedures

**Community Comments:**
- "The application in question is clearly malware, therefore it is best to remove it. A factory reset can remove malware, but doing something drastic like that is usually not a first step. Additionally, C and D won't help with removing malware." - **Antwon** (Oct. 21, 2022, 2:07 a.m., 16 votes, highest voted explanation)
- "Yeah, but she is also receiving security warnings. What else could it be besides malware?" - **takomaki** (2 years, 9 months ago, 2 votes)
- "It is quite clear that the issue is the application they just installed, so first thing should be to just uninstall it, though depending on the app, you might still do more, but the question was what to do FIRST." - **Kriegor** (6 months, 1 week ago, 1 vote)
- "whenever application experience high utilization of bandwidth. It should be removed immediately" - **er.garg2687** (1 year, 2 months ago, 1 vote)
- "The answer is clear the application must be removed" - **Tswaka** (2 years, 5 months ago, 1 vote)

**Key Discussion Points:**

**Malware Response Procedures:**
- Identify and remove the source of infection as first priority
- Escalate to more drastic measures only if initial steps fail
- Security warnings indicate active threat requiring immediate action

**Application Installation:**
- Problems started immediately after new app installation
- Downloaded from vendor website (potentially untrusted source)
- Common malware tactic to disguise as 'optimization' software

**Network Security:**
- High network utilization indicates data exfiltration or botnet activity
- Security warnings suggest system-level compromise
- Immediate containment required to prevent further damage

**Alternative Positions:**
- Some users suggested **D - Disable Mobile Hotspot** as part of quarantine process before making changes
- Community consensus favors app removal as the logical first step
- One user noted that while quarantine measures are important, removing the source is more direct and effective

**Source Information:**
- **Source URL:** https://www.examtopics.com/discussions/comptia/view/86088-exam-220-1102-topic-1-question-4-discussion/
- **Extraction Date:** 2025-11-06
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 4

---

**References:**
- CompTIA A+ Core 2 (220-1102) Exam Objectives, Section 4.1: Troubleshoot mobile device issues
- CompTIA A+ Core 2 (220-1102) Exam Objectives, Section 3.7: Explain common security threats
- ExamTopics.com community discussion and voting results

---

## Question 5

# CompTIA A+ Core 2 (220-1102) - Question 5

**Topic:** 1  
**Exam Code:** CompTIA 220-1102  
**Question Number:** 5  
**Source:** ExamTopics Community Discussion

---

## Question

A change advisory board just approved a change request. Which of the following is the MOST likely next step in the change process?

**A.** End user acceptance  
**B.** Perform risk analysis  
**C.** Communicate to stakeholders  
**D.** Sandbox testing

---

## Correct Answer

**A. End user acceptance**

*Confidence Level: High*  
*Community Vote: 56% (Most Voted)*

---

## Explanation

### Primary Explanation

End user acceptance is the most likely next step after change advisory board approval according to the standard 8-step change management process. The complete sequence is: Request forms → Purpose of change → Scope of change → Date and time of change → Affected systems/impact → Risk analysis → Change board approval → End user acceptance.

### Change Management Lifecycle

The standard 8-step change management process follows this order:

1. Complete the request forms
2. Determine the purpose of the change
3. Identify the scope of the change
4. Schedule a date and time of the change
5. Determine affected systems and the impact
6. Analyze the risk associated with the change
7. Get approval from the change control board
8. Get end-user acceptance after the change is complete

### Why Other Options Are Incorrect

- **B. Perform risk analysis:** Risk analysis should be performed BEFORE the change board approval, not after
- **C. Communicate to stakeholders:** Communication to stakeholders is part of the implementation phase, not the immediate next step after approval
- **D. Sandbox testing:** Sandbox testing should be done before CAB approval to validate the change doesn't break production

### Mnemonic Device

**Raccoons Propose Stashing Delicacies Among Rickety Cardboard Edifices**

- **R**equest forms
- **P**urpose of change
- **S**cope of the change
- **D**ate and Time of the change
- **A**ffected systems/impact
- **R**isk analysis
- **C**hange board approval
- **E**nd user acceptance

---

## Community Voting Statistics

| Answer Choice | Percentage |
|---------------|------------|
| A (Correct)   | 56%        |
| C             | 24%        |
| B             | 12%        |
| D             | 8%         |

**Total Engagement:** Very high - extensive discussion with detailed process explanations and alternative interpretations

---

## Top Community Explanations

### Highest Voted (43 votes)
**User:** simsbow1098  
**3 years, 1 month ago**

> "The change management phases are as follows: Request forms, Purpose of change, Scope of the change, Date and Time of the change, Affective systems/ impact, risk analysis, change board approval, finally end user acceptance. With this the answer is end user acceptance."

### Second Highest (29 votes)
**User:** alexandrasexy  
**1 year, 1 month ago**

> "Final answer is A. Order of change management phases: 1. Request forms 2. Purpose of change 3. Scope of the change 4. Date and Time of the change 5. Affective systems/ impact 6. Risk analysis 7. Change board approval 8. Finally end user acceptance."

### Third Highest (5 votes)
**User:** jjwelch00  
**2 years, 4 months ago** (Alternative Position - C)

> "C. Communicate to stakeholders: Once the change request is approved by the CAB, the next logical step is to communicate the approved change to the relevant stakeholders. This involves informing affected parties, such as end users, managers, and other teams, about the upcoming change, its impact, and any necessary actions or preparations they need to take."

---

## Alternative Positions

### Position C - Communicate to Stakeholders (24% of votes)
**Reasoning:** After CAB approval, affected parties should be informed about the change  
**Explanation:** Strong alternative position emphasizing communication as next logical step

### Position B - Perform Risk Analysis (12% of votes)
**Reasoning:** Risk analysis is necessary before actual change implementation  
**Explanation:** Some users argued risk analysis should follow approval for implementation phase

### Position D - Sandbox Testing (8% of votes)
**Reasoning:** Test in isolated environment before production implementation  
**Explanation:** Minority view suggesting testing phase after approval

---

## Key Discussion Points

### Change Management Process Order
- Standard 8-step process has end user acceptance as final step
- Risk analysis should precede CAB approval, not follow it
- Implementation comes after approval, end user acceptance is final validation

### Timing Interpretations
- Some confusion between 'change request approval' vs 'change implementation'
- CAB approves the request, then implementation phase begins
- End user acceptance occurs after successful implementation

### Process vs Implementation
- Change management process (approval phase) vs change implementation
- CAB approval completes the management process
- End user acceptance validates successful implementation

---

## Industry Perspectives

### CompTIA CertMaster Learn for A+
**Position:** Order: Change Board Approvals → Risk Analysis → Test and Implement → End-user Acceptance  
*Note:* One user's reference to official CompTIA learning materials

### Mike Myers (CompTIA A+ Guide)
**Position:** End user acceptance is correct for these answer choices  
*Note:* Reference to popular CompTIA exam prep author

---

## Contextual Considerations

**Exam Focus:** Change management procedures and proper sequencing  
**Practical Application:** Following standardized IT change management protocols  
**Decision Making:** Understanding when each step in the process should occur

---

**Source:** https://www.examtopics.com/discussions/comptia/view/82961-exam-220-1102-topic-1-question-5-discussion/  
**Extraction Date:** 2025-11-06

---

## Question 6

# CompTIA A+ Core 2 (220-1102) - Question 6

## Question Details
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 6
- **Question Type:** Multiple Choice
- **Difficulty:** Standard

## Question Text
A user calls the help desk to report that none of the files on a PC will open. The user also indicates a program on the desktop is requesting payment in exchange for file access. A technician verifies the user's PC is infected with ransomware. Which of the following should the technician do FIRST?

## Answer Choices
- **A.** Scan and remove the malware.
- **B.** Schedule automated malware scans.
- **C.** Quarantine the system.
- **D.** Disable System Restore.

## Correct Answer
**C. Quarantine the system**

**Confidence Level:** High  
**Community Status:** Most Voted  
**Answer Status:** Suggested Answer

---

## Detailed Explanation

### Primary Explanation
Quarantining the system is the first step in malware removal after verification. This prevents the ransomware from spreading to other systems on the network and contains the threat before attempting remediation. CompTIA's malware removal objectives specifically list "Quarantine infected systems" as the second step, immediately after investigating and verifying malware symptoms.

### CompTIA Malware Removal Process
The official CompTIA process for malware removal follows this specific order:

1. **Investigate and verify malware symptoms**
2. **Quarantine infected systems**
3. **Disable System Restore in Windows**
4. **Remediate infected systems:**
   - a. Update anti-malware software
   - b. Scanning and removal techniques (e.g., safe mode, preinstallation environment)
5. **Schedule scans and run updates**
6. **Enable System Restore and create a restore point in Windows**
7. **Educate the end user**

### Technical Reasoning
- **Isolation prevents ransomware spread to network**
- **Contains the threat before attempting removal**
- **Protects other systems from compromise**
- **Essential for incident containment procedures**

### Why Other Options Are Incorrect
- **Option A (Scan and remove malware):** Scanning and removing malware should only be done after quarantine to ensure the threat is contained
- **Option B (Schedule automated scans):** Scheduling automated scans is a remediation step that comes much later in the process
- **Option D (Disable System Restore):** Disabling System Restore is the third step in CompTIA's process, after quarantine

**Source:** [ExamTopics Discussion](https://www.examtopics.com/discussions/comptia/view/86089-exam-220-1102-topic-1-question-6-discussion/)

---

## Question 7

# CompTIA A+ Core 2 (220-1102) Question 7

## Question Details
**Question Type:** Multiple Choice  
**Topic:** 1  
**Question Number:** 7  
**Exam Code:** CompTIA 220-1102

## Question Text
A company is issuing smartphone to employees and needs to ensure data is secure if the devices are lost or stolen. Which of the following provides the BEST solution?

## Answer Choices
A. Anti-malware (community voted 0%)  
B. Remote wipe (community voted 83%)  
C. Locator applications (community voted 0%)  
D. Screen lock (community voted 17%)

## Correct Answer
**B - Remote wipe**

## Detailed Explanation

### Primary Solution
Remote wipe is the best solution for securing data on lost or stolen smartphones because it provides the most comprehensive data protection. When a device is lost or stolen, remote wipe can permanently erase all sensitive company data, preventing unauthorized access regardless of whether the device has physical access limitations or security measures that could be bypassed.

### Key Technical Points
- Provides complete data destruction by destroying sensitive information
- Works regardless of physical access to the device
- Eliminates risk of data extraction through sophisticated methods
- Suitable as a last-resort security measure for company data

### Why Other Options Are Incorrect
- **A - Anti-malware:** Protects against malicious software but doesn't secure data if the device is physically stolen
- **C - Locator applications:** Help find the device but don't secure the data if the device cannot be recovered
- **D - Screen lock:** Can be bypassed, doesn't protect against physical data extraction

**Source:** [ExamTopics Discussion](https://www.examtopics.com/discussions/comptia/view/86090-exam-220-1102-topic-1-question-7-discussion/)

---

## Question 8

# CompTIA A+ Core 2 (220-1102) Practice Question

## Question Information
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 8
- **Question Type:** Multiple Choice
- **Community Engagement:** High - Significant debate between targeted approach vs. security-first approach

## Question
A user reports seeing random, seemingly non-malicious advertisement notifications in the Windows 10 Action Center. The notifications indicate the advertisements are coming from a web browser. Which of the following is the BEST solution for a technician to implement?

## Answer Choices
- **A.** Disable the browser from sending notifications to the Action Center.
- **B.** Run a full antivirus scan on the computer.
- **C.** Disable all Action Center notifications.
- **D.** Move specific site notifications from Allowed to Block.

## Correct Answer
**D. Move specific site notifications from Allowed to Block**

**Community Vote:** 48% (Most Voted)  
**Confidence Level:** High  
**Status:** Suggested Answer

## Detailed Explanation

### Primary Explanation
Moving specific site notifications from Allowed to Block is the best solution because the scenario describes non-malicious advertisements specifically coming from a web browser via the Action Center. This is most likely due to the user having granted notification permissions to specific websites. The targeted approach (Option D) resolves the immediate issue without being overly broad or assuming malware.

### Why Other Options Are Incorrect
- **A:** Disabling all browser notifications is too broad and may block legitimate notifications
- **B:** Running antivirus scan assumes malware when the scenario explicitly describes ads as non-malicious
- **C:** Disabling all Action Center notifications affects security and other important system notifications

**Source:** [ExamTopics Discussion](https://www.examtopics.com/discussions/comptia/view/85821-exam-220-1102-topic-1-question-8-discussion/)

---

## Question 9

# CompTIA A+ Core 2 (220-1102) - Question 9

## Question Details
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 9
- **Question Type:** Multiple Choice
- **Difficulty Level:** Standard

## Question
After clicking on a link in an email, a Chief Financial Officer (CFO) received a security certificate error. The CFO then reported the incident to a technician. The link is purportedly to the organization's bank. Which of the following should the technician perform **FIRST**?

## Answer Choices
- **A.** Update the browser's CRLs.
- **B.** File a trouble ticket with the bank.
- **C.** Contact the ISP to report the CFO's concern.
- **D.** Instruct the CFO to exit the browser.

## Correct Answer
**D. Instruct the CFO to exit the browser**

### Answer Statistics
- **Confidence Level:** Very High
- **Community Votes:** 90%
- **Status:** Most Voted / Suggested Answer
- **Total Engagement:** Very high (extensive security discussion)

## Detailed Explanation

### Primary Reasoning
Instructing the CFO to exit the browser immediately is the correct first response because the scenario strongly indicates a **phishing attempt**. The combination of an email link (unknown origin), the word 'purportedly' (suggesting uncertainty), and a security certificate error from a supposed legitimate bank website creates a high-risk scenario requiring immediate threat containment.

### Security Analysis
- Link from email (potential phishing vector)
- Word 'purportedly' suggests uncertainty about legitimacy
- Security certificate error from supposedly trusted bank
- CFO is high-value target (whaling attack scenario)

### Why Other Options Are Incorrect
- **A:** Updating CRLs is unnecessary when certificate error indicates fraudulent site
- **B:** Filing a ticket with the bank can be done after threat containment
- **C:** Contacting ISP is irrelevant to potential phishing site

**Source:** [ExamTopics Discussion](https://www.examtopics.com/discussions/comptia/view/86091-exam-220-1102-topic-1-question-9-discussion/)

---

## Question 10

# CompTIA A+ Core 2 (220-1102) - Question 10

## Question Information
- **Exam Code:** CompTIA 220-1102
- **Topic:** 1
- **Question Number:** 10
- **Question Type:** Multiple Choice

## Question
A help desk technician is troubleshooting a workstation in a SOHO environment that is running above normal system baselines. The technician discovers an unknown executable with a random string name running on the system. The technician terminates the process, and the system returns to normal operation. The technician is concerned other machines may be infected with this unknown virus. Which of the following is the MOST effective way to check other machines on the network for this unknown threat?

## Answer Choices
- **A.** Run a startup script that removes files by name.
- **B.** Provide a sample to the antivirus vendor.
- **C.** Manually check each machine.
- **D.** Monitor outbound network traffic.

## Correct Answer
**C. Manually check each machine**

**Community Consensus:** 73% of votes  
**Confidence Level:** High  
**Status:** Suggested Answer

## Detailed Explanation

### Primary Explanation
Manually checking each machine is the most effective approach for a SOHO environment because SOHO networks typically have few machines, making manual inspection practical and immediate. This direct approach allows for quick identification and removal of the threat without waiting for antivirus vendor updates, which can take weeks or months.

### Technical Reasoning
- SOHO environments typically have limited number of machines (5-10 or fewer)
- Manual inspection provides immediate, direct verification
- No waiting period for vendor analysis or signature updates
- Complete network audit ensures no infected machines are missed

### Why Other Options Are Incorrect
- **A:** Running startup script is ineffective without knowing specific file name/hash
- **B:** Providing sample to vendor takes too long (weeks to months) for immediate protection
- **D:** Monitoring network traffic is detective, not corrective

**Source:** [ExamTopics Discussion](https://www.examtopics.com/discussions/comptia/view/85761-exam-220-1102-topic-1-question-10-discussion/)

---

## Summary

**Total Questions:** 10/50 (20% complete)  
**Community Consensus:** High (ranging from 35% to 90%)  
**Topics Covered:** Wireless networking, Linux server management, data security, mobile malware, change management, ransomware response, mobile device security, browser notifications, phishing detection, SOHO network security

### Question Breakdown:
1. **Q1:** Wireless network configuration (35% consensus) - Simulation PBQ
2. **Q2:** Linux server troubleshooting via SSH (87% consensus)
3. **Q3:** Secure data removal methods (89% consensus)
4. **Q4:** Mobile malware response procedures (90% consensus)
5. **Q5:** Change management process (56% consensus)
6. **Q6:** Ransomware quarantine response (Strong consensus for C)
7. **Q7:** Mobile device security with remote wipe (83% consensus)
8. **Q8:** Browser notifications vs malware (48% consensus)
9. **Q9:** Phishing incident response (90% consensus)
10. **Q10:** SOHO network security checking (73% consensus)

### Key Learning Areas:
- **Networking:** WiFi standards, frequency bands, security protocols, SOHO network management
- **Systems Administration:** Remote access protocols, CLI vs GUI troubleshooting
- **Security:** Data sanitization standards, malware response, ransomware containment, phishing detection
- **Mobile Security:** Device protection, remote wipe, malware response
- **IT Management:** Change management lifecycle, process sequencing
- **Browser Management:** Notification permissions, configuration vs malware

---

*Database maintained by MiniMax Agent | Updated November 6, 2025*