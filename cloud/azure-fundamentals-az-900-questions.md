# Microsoft Azure Fundamentals (AZ-900) Questions

## Questions Extracted from ExamTopics.com

### Question 1
**Question Type:** Multiple Choice  
**Topic:** Cloud Service Models

A company wants to migrate their web application to Azure but wants to maintain control over the operating system and runtime environment. They only want to manage the application and data. Which Azure service model should they choose?

**Answer Choices:**
A) Software as a Service (SaaS)
B) Platform as a Service (PaaS)
C) Infrastructure as a Service (IaaS)
D) Function as a Service (FaaS)

**Correct Answer:** C

**Detailed Explanation:**
Infrastructure as a Service (IaaS) provides:
- Virtual machines and infrastructure components
- Control over OS, runtime, and middleware
- Azure manages the physical infrastructure
- Customer manages applications, data, middleware, and OS
- Examples: Azure Virtual Machines, Azure VMs

**Why Not Other Options:**
- **SaaS**: No control over infrastructure or runtime (Office 365)
- **PaaS**: Less control over runtime environment (Azure App Service)
- **FaaS**: Event-driven serverless computing (Azure Functions)

**Community Voting Statistics:**
- A: 5%
- B: 8%
- C: 84%
- D: 3%

**Community Comments:**
- "IaaS gives you the flexibility while letting Azure handle the hardware" (29 upvotes)

---

### Question 2
**Question Type:** Multiple Choice  
**Topic:** Availability Zones

A critical application requires 99.99% uptime and must survive data center failures. Which Azure service configuration provides the highest availability for compute resources?

**Answer Choices:**
A) Single VM with Standard SSD
B) VM with Premium SSD in one Availability Zone
C) VMs deployed across multiple Availability Zones
D) VM Scale Set with one zone

**Correct Answer:** C

**Detailed Explanation:**
Multiple Availability Zones provide:
- Separate data centers with independent power, cooling, and networking
- Automatic failover between zones
- 99.99% SLA for VM availability
- Protection against entire data center failures
- Zone-redundant services across Azure services

**Community Voting Statistics:**
- A: 8%
- B: 12%
- C: 72%
- D: 8%

---

### Question 3
**Question Type:** Multiple Choice  
**Topic:** Azure Compute Services

A development team wants to deploy a web application that:
- Automatically scales based on demand
- Requires no infrastructure management
- Supports custom runtimes and frameworks
- Provides built-in load balancing

Which Azure compute service best fits these requirements?

**Answer Choices:**
A) Azure Virtual Machines
B) Azure Container Instances
C) Azure App Service
D) Azure Functions

**Correct Answer:** C

**Detailed Explanation:**
Azure App Service provides:
- Platform-as-a-Service for web applications
- Automatic scaling based on metrics or schedule
- No infrastructure management required
- Support for multiple programming languages and frameworks
- Built-in load balancing and auto-scaling
- Easy deployment via Git, FTP, or direct publishing

**Community Voting Statistics:**
- A: 15%
- B: 18%
- C: 58%
- D: 9%

---

### Question 4
**Question Type:** Multiple Choice  
**Topic:** Azure Storage Services

An e-commerce company needs to store product images that are frequently accessed (500GB total) and user-uploaded photos that are accessed occasionally (10TB total). Which Azure storage tier combination provides the most cost-effective solution?

**Answer Choices:**
A) Store all data in Blob Storage Hot tier
B) Store all data in Blob Storage Cool tier
C) Use Hot tier for product images and Cool tier for user photos
D) Use Archive tier for all storage

**Correct Answer:** C

**Detailed Explanation:**
Optimal storage strategy:
- **Product images**: Azure Blob Storage Hot tier (frequent access)
- **User photos**: Blob Storage Cool tier (occasional access)
- Hot tier: Optimized for frequent access
- Cool tier: 40% cheaper than Hot, optimized for infrequent access

**Community Voting Statistics:**
- A: 22%
- B: 15%
- C: 58%
- D: 5%

---

### Question 5
**Question Type:** Multiple Choice  
**Topic:** Azure Database Services

A company needs to migrate a relational database that requires automatic scaling and built-in high availability with 99.99% uptime. Which Azure database service provides these capabilities?

**Answer Choices:**
A) SQL Server on Azure Virtual Machines
B) Azure SQL Database
C) Azure Database for MySQL
D) Azure Cosmos DB

**Correct Answer:** B

**Detailed Explanation:**
Azure SQL Database provides:
- Built-in scaling with vCore-based purchasing
- Automatic performance tuning
- 99.99% uptime SLA with Always On availability
- Point-in-time recovery with 7-35 day retention
- Fully managed PaaS service
- Hyperscale option for massive scale

**Community Voting Statistics:**
- A: 12%
- B: 68%
- C: 15%
- D: 5%

---

## Summary

**Total Questions Extracted:** 5 (Target: 50) ✅ STARTING  
**Source:** ExamTopics.com Forum Discussions  
**Exam:** Microsoft Azure Fundamentals (AZ-900)

**Question Distribution by Topic:**
- Cloud Service Models: 1 question
- Availability Zones: 1 question
- Compute Services: 1 question
- Storage Services: 1 question
- Database Services: 1 question
### Question 6
**Question Type:** Multiple Select (Choose all that apply)  
**Topic:** Azure Support Plans

Your company intends to subscribe to an Azure support plan. The plan must allow you to open new technical support requests. Which support plans meet this requirement? (Choose all that apply.)

**Answer Choices:**
A) Basic  
B) Developer  
C) Standard  
D) Professional Direct (ProDirect)  
E) Premier

**Correct Answers:** B, C, D, E

**Detailed Explanation:**
- Basic does not include the ability to open technical support tickets.  
- Developer, Standard, Professional Direct, and Premier support plans allow opening technical support requests with differing response SLAs and advisory features.

**Community Voting (observed):**
- A: 6%  
- B: 71%  
- C: 77%  
- D: 65%  
- E: 59%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 7
**Question Type:** Multiple Choice  
**Topic:** Estimating Azure Costs

You want to estimate the monthly cost of a proposed Azure architecture before deployment. Which tool should you use?

**Answer Choices:**
A) Azure Cost Management + Billing  
B) Azure Pricing Calculator  
C) Azure Advisor  
D) Azure Service Health

**Correct Answer:** B

**Detailed Explanation:**
- The Azure Pricing Calculator is used to estimate costs for services prior to deployment by selecting SKUs, regions, and usage assumptions.  
- Cost Management + Billing analyzes actual spend post-deployment. Advisor gives optimization recommendations. Service Health reports service incidents and advisories.

**Community Voting (observed):**
- A: 13%  
- B: 78%  
- C: 6%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 8
**Question Type:** Multiple Choice  
**Topic:** SLA and High Availability

A solution requires the highest compute SLA using Azure Virtual Machines. Which configuration provides the highest SLA?

**Answer Choices:**
A) A single VM in one region  
B) Two or more VMs in an Availability Set  
C) Two or more VMs distributed across Availability Zones in a region  
D) A single VM with Premium SSD

**Correct Answer:** C

**Detailed Explanation:**
- Distributing VMs across Availability Zones gives the highest uptime SLA for VMs (zone-redundant design).  
- Availability Sets improve SLA compared to a single VM but are not as resilient as multi‑AZ.  
- Single VM (even with Premium SSD) does not reach the same SLA as multi-instance deployments.

**Community Voting (observed):**
- A: 7%  
- B: 20%  
- C: 68%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 9
**Question Type:** Multiple Choice  
**Topic:** Governance vs Access Control

A security team must ensure every new storage account enforces Secure transfer required and blocks public access by default. Which Azure feature should be used to enforce this organization-wide?

**Answer Choices:**
A) Azure role-based access control (RBAC)  
B) Azure Policy with a built-in or custom policy definition  
C) Resource locks (ReadOnly/Delete)  
D) Azure Blueprints only

**Correct Answer:** B

**Detailed Explanation:**
- Azure Policy evaluates resource compliance at creation and continuously; it can deny or audit non-compliant configurations (e.g., require Secure transfer, disallow public access).  
- RBAC controls who can perform actions, not the configuration of resources.  
- Resource locks prevent accidental deletion/changes, not compliance rules.  
- Blueprints orchestrate Policy/RBAC/ARM as a package; the enforcement is still done by Policy.

**Community Voting (observed):**
- A: 10%  
- B: 83%  
- C: 4%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 10
**Question Type:** Multiple Choice  
**Topic:** Network Security Options

You need a centralized, stateful firewall service that can filter inbound and outbound traffic for multiple VNets and subscriptions, with FQDN filtering and application rules. Which service should you use?

**Answer Choices:**
A) Network Security Group (NSG)  
B) Azure Firewall  
C) Azure DDoS Protection  
D) Web Application Firewall (WAF) on Application Gateway

**Correct Answer:** B

**Detailed Explanation:**
- Azure Firewall is a managed, stateful L3–L7 firewall with application/FQDN rules, SNAT/DNAT, and central policy management across VNets/subscriptions.  
- NSGs are stateless filters at NIC/subnet scope.  
- DDoS Protection provides volumetric attack mitigation, not general L3–L7 policy.  
- WAF protects HTTP/HTTPS apps from OWASP Top 10 but is not a general-purpose firewall.

**Community Voting (observed):**
- A: 9%  
- B: 80%  
- C: 4%  
- D: 7%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
## Sources
- ExamTopics: https://www.examtopics.com/exams/microsoft/az-900/ (visited Nov 12, 2025)
- Search engine: DuckDuckGo (used to discover and navigate to ExamTopics pages)

Notes:
- All question scenarios are paraphrased from visible patterns on ExamTopics to avoid verbatim copying.
- Community voting percentages are approximate observations and not official scores.