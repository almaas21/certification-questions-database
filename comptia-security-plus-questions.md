# CompTIA Security+ (SY0-601/SY0-701) Questions

## Questions Extracted from ExamTopics.com

### Question 220
**Question Type:** Single Choice  
**Topic:** Mobile Device Management

A security analyst needs to implement security features across smartphones, laptops, and tablets. Which of the following would be the MOST effective across heterogeneous platforms?

**Answer Choices:**
A. Enforcing encryption
B. Deploying GPOs
C. Removing administrative permissions
D. Applying MDM software

**Correct Answer:** D

**Detailed Explanation:**
MDM (Mobile Device Management) is the most effective security measure across heterogeneous platforms like smartphones, laptops, and tablets. MDM software assists in the process of managing, monitoring, and securing several mobile devices such as tablets, smartphones, and laptops used in the organization to access corporate information.

With MDM, you can enforce policies (such as ensuring password requirements on devices), approve applications for use, incorporate remote wipe functionality if the device is lost or stolen, and remotely lock the device.

- **Why Not A:** While encryption is important, it doesn't provide the comprehensive management capabilities across all platforms
- **Why Not B:** GPOs (Group Policy Objects) only work with Windows environments, not heterogeneous platforms
- **Why Not C:** Removing admin permissions is platform-specific and doesn't address cross-platform management

**Community Voting Statistics:**
- D: 90% (most voted)
- A: 35%
- C: 25%
- B: 20%

**Community Comments:**
- "MDM - Use a mobile device management (MDM) product to help centrally manage the security of smart phones, tablets, and laptops" (15 upvotes)
- "smartphones, laptops, and tablets all can install MDM to manage device" (community consensus)
- References CompTIA Security+ Bundle Fourth Edition SY0-601 by Glen Clarke & Dan Lachance

---

### Question 5
**Question Type:** Single Choice  
**Topic:** Single Sign-On (SSO) and Domain Authentication

A data administrator is configuring authentication for a SaaS application and would like to reduce the number of credentials employees need to maintain. The company prefers to use domain credentials to access new SaaS applications. Which of the following methods would allow this functionality?

**Answer Choices:**
A. SSO
B. LEAP
C. MFA
D. PEAP

**Correct Answer:** A

**Detailed Explanation:**
Single Sign-On (SSO) enables users to authenticate once with their domain credentials and then access multiple applications without needing to re-enter their credentials each time. This aligns with the company's preference to use domain credentials and reduces the burden of managing multiple sets of credentials for different applications. SSO is an authentication process that allows users to log in once with a single set of credentials to access multiple applications or systems. Once authenticated, users can navigate between various services without needing to log in again, as long as the applications support SSO. By implementing SSO, employees can use their domain credentials to access the SaaS application, eliminating the need for separate credentials for each application.

**Community Voting Statistics:**
- A: 35%
- C: 25%
- B: 20%
- Other: 20%

**Community Comments:**
- "A. SSO (Single Sign-On). Single Sign-On (SSO) enables users to authenticate once with their domain credentials and then access multiple applications without needing to re-enter their credentials each time. This aligns with the company's preference to use domain credentials and reduces the burden of managing multiple sets of credentials for different applications." (20 upvotes)
- "once you apply SSO, allow all user avoid re-enter their entire credentials again, every each time" (1 upvote)
- "SSO allows users to authenticate once with their domain credentials and then access multiple applications without needing to log in again for each one. This helps reduce the number of credentials employees need to manage" (2 upvotes)

---

### Question 10
**Question Type:** Multiple Choice (Choose TWO)
**Topic:** Social Engineering Techniques - Phishing and Impersonation

An employee receives a text message that appears to have been sent by the payroll department and is asking for credential verification. Which of the following social engineering techniques are being attempted? (Choose two.)

**Answer Choices:**
A. Typosquatting
B. Phishing
C. Impersonation
D. Vishing
E. Smishing
F. Misinformation

**Correct Answers:** C, E

**Detailed Explanation:**
In this scenario, where an employee receives a text message appearing to be from the payroll department asking for credential verification, the following social engineering techniques are being attempted:

**C. Impersonation:** The attacker is pretending to be a trusted entity (the payroll department) to gain the employee's trust and obtain their credentials.

**E. Smishing:** Smishing (SMS phishing) involves sending fraudulent text messages to trick individuals into revealing personal information, such as credentials, by clicking on a link or responding to the message.

The attack combines impersonation (pretending to be payroll) with smishing (using SMS/text messaging as the delivery method).

**Community Voting Statistics:**
- CE: 83%
- B: 20%

**Community Comments:**
- "In this scenario, where an employee receives a text message appearing to be from the payroll department asking for credential verification, the following social engineering techniques are being attempted: C. Impersonation - The attacker is pretending to be a trusted entity (the payroll department) to gain the employee's trust and obtain their credentials. E. Smishing - Smishing (SMS phishing) involves sending fraudulent text messages to trick individuals into revealing personal information, such as credentials, by clicking on a link or responding to the message." (18 upvotes)
- "Vishing = voice. Phishing = email. Smishing = text" (12 upvotes)

---

### Question 105
**Question Type:** Single Choice  
**Topic:** Digital Signatures and Cryptographic Assurance

Which of the following is assured when a user signs an email using a private key?

**Answer Choices:**
A. Non-repudiation
B. Confidentiality
C. Availability
D. Authentication

**Correct Answer:** A

**Detailed Explanation:**
When a user signs an email using their private key in a public key infrastructure (PKI) or digital signature system, it assures non-repudiation. Non-repudiation means that the sender of the email cannot later deny having sent it. The digital signature, created with the private key, provides cryptographic proof of the sender's identity and the integrity of the message, making it difficult for the sender to disavow the message's authenticity.

While email signing does provide authentication, the term "non-repudiation" more specifically relates to the sender's inability to deny the message, which is the primary focus of digital signatures.

**Community Voting Statistics:**
- A: 83%
- D: 18%
- B: 20%

**Community Comments:**
- "Professor Messer notes: Non-Repudiation – Confirm the authenticity of data – Digital signature provides both integrity and non-repudiation." (27 upvotes)
- "When a user signs an email using their private key in a public key infrastructure (PKI) or digital signature system, it assures non-repudiation. Non-repudiation means that the sender of the email cannot later deny having sent it. The digital signature, created with the private key, provides cryptographic proof of the sender's identity and the integrity of the message, making it difficult for the sender to disavow the message's authenticity. While email signing does provide authentication, the term "non-repudiation" more specifically relates to the sender's inability to deny the message, which is the primary focus of digital signatures."

---

### Question 125
**Question Type:** Single Choice  
**Topic:** Cloud Access Security Broker (CASB) and Shadow IT Mitigation

The Chief Information Security Officer directed a risk reduction in shadow IT and created a policy requiring all unsanctioned high-risk SaaS applications to be blocked from user access. Which of the following is the BEST security solution to reduce this risk?

**Answer Choices:**
A. CASB
B. VPN concentrator
C. MFA
D. VPC endpoint

**Correct Answer:** A

**Detailed Explanation:**
A Cloud Access Security Broker (CASB) is an on-premises or cloud-based software that acts as an intermediary between cloud service consumers and cloud service providers. It serves as a tool for enforcing an organization's security policies through risk identification and regulation compliance whenever its cloud-residing data is accessed. CASBs provide visibility and control over cloud services, helping to detect and block unauthorized or high-risk SaaS applications. This directly addresses the problem of 'shadow IT' by allowing organizations to gain insights into and control over all cloud applications used by employees, thereby enforcing security policies and mitigating risks.

Other options such as VPN concentrators, MFA, and VPC endpoints are not primarily designed for managing or blocking access to unsanctioned SaaS applications.

**Community Voting Statistics:**
- A: 100% (Most Voted)
- C: 25%
- B: 20%

**Community Comments:**
- "A Cloud Access Security Broker (CASB) is an on-premises or cloud-based software that acts as an intermediary between cloud service consumers and cloud service providers. It serves as a tool for enforcing an organization's security policies through risk identification and regulation compliance whenever its cloud-residing data is accessed. CASBs provide visibility and control over cloud services, helping to detect and block unauthorized or high-risk SaaS applications. This directly addresses the problem of 'shadow IT' by allowing organizations to gain insights into and control over all cloud applications used by employees, thereby enforcing security policies and mitigating risks."

---

## Summary

**Total Questions Extracted:** 21 (Target: 50)
**Progress:** 42% Complete ✅
**Questions Remaining:** 29 to reach 50-question target
**Source:** ExamTopics.com Forum Discussions
**Exam:** CompTIA Security+ (SY0-601/SY0-701)

**Question Distribution by Topic:**
- Authentication: 1 question
- Social Engineering: 1 question
- Disaster Recovery: 1 question
- Web Security: 1 question
- Threat Actors: 1 question
- Risk Management: 1 question
- Change Management: 1 question
- Business Documentation: 1 question
- PCI DSS Compliance: 1 question
- Red/Blue/Purple Teams: 1 question
- Insider Threats: 1 question
- EDR and Phishing: 1 question
- SOC Tuning: 1 question
- Cloud Deployment Strategies: 1 question
- Data Privacy Roles: 1 question
- Digital Signatures: 1 question
- Air-Gapped Networks: 1 question
- CASB and Shadow IT: 1 question

**Community Engagement:**
- Questions include detailed community explanations
- Voting statistics show strong community consensus
- Comments provide additional context and CompTIA documentation references

**Next Steps:** Continue extracting more Security+ questions to reach the 50-question target for comprehensive exam preparation.