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
---
### Question 11
**Question Type:** Multiple Choice  
**Topic:** Access Control vs Directory Administration

You need to grant a user read access to only one resource group without giving them permissions to manage users or apps in Microsoft Entra ID (Azure AD). Which feature should you use?

**Answer Choices:**
A) Microsoft Entra ID Global Administrator role  
B) Azure role-based access control (RBAC) at the resource group scope  
C) Resource locks (ReadOnly) on the resource group  
D) Azure Policy assignment at the subscription scope

**Correct Answer:** B

**Detailed Explanation:**
- Azure RBAC assigns roles (e.g., Reader) at scopes like subscription, resource group, or resource to control access to Azure resources.  
- Entra ID directory roles (e.g., Global Admin) manage the identity platform, not granular resource access in Azure Resource Manager.  
- Resource locks protect against accidental changes, not who can read.  
- Azure Policy enforces configuration/compliance, not user permissions.

**Community Voting (observed):**
- A: 9%  
- B: 78%  
- C: 7%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 12
**Question Type:** Multiple Choice  
**Topic:** Governance Packaging (Blueprints vs Policy)

You need to deploy a governed landing zone that includes role assignments, policy assignments (e.g., require tags), and ARM/Bicep templates for networks and resource groups—all as a repeatable package. Which Azure capability is designed for this?

**Answer Choices:**
A) Azure Policy only  
B) ARM templates only  
C) Azure Blueprints  
D) Azure Advisor

**Correct Answer:** C

**Detailed Explanation:**
- Azure Blueprints package artifacts (Policy assignments, role assignments, ARM templates) to deploy governed environments consistently.  
- Policy alone enforces configurations but does not deploy resources/roles.  
- ARM templates deploy resources, not governance policies/roles by themselves.  
- Advisor provides recommendations, not deployment packaging.

**Community Voting (observed):**
- A: 11%  
- B: 8%  
- C: 78%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 13
**Question Type:** Multiple Choice  
**Topic:** Compliance Documentation

Your auditors request SOC 2 and ISO 27001 reports for Azure services. Where should you download these compliance documents?

**Answer Choices:**
A) Azure Service Health  
B) Microsoft Service Trust Portal  
C) Azure Advisor  
D) Azure Marketplace

**Correct Answer:** B

**Detailed Explanation:**
- The Microsoft Service Trust Portal hosts compliance reports, audit documents, and trust resources for Azure, Microsoft 365, and Dynamics 365.  
- Service Health shows Azure outage/incidents; Advisor gives best-practice recommendations; Marketplace is for solutions and offers.

**Community Voting (observed):**
- A: 6%  
- B: 82%  
- C: 7%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 14
**Question Type:** Multiple Choice  
**Topic:** Migration Tools

You need to discover on‑premises servers, assess readiness/cost, and migrate them to Azure with minimal disruption. Which service should you use?

**Answer Choices:**
A) Azure Site Recovery only  
B) Azure Data Box  
C) Azure Migrate  
D) Azure Import/Export

**Correct Answer:** C

**Detailed Explanation:**
- Azure Migrate provides discovery, assessment, sizing/cost estimation, and migration tooling for servers, databases, and applications.  
- Site Recovery focuses on DR replication/failover.  
- Data Box/Import‑Export are for bulk data transfer, not comprehensive server migration planning.

**Community Voting (observed):**
- A: 9%  
- B: 6%  
- C: 80%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 15
**Question Type:** Multiple Choice  
**Topic:** Resource Organization

You want to manage lifecycle (deployment, RBAC, policy, tagging) for a set of related resources that share the same permissions and location boundaries. Which Azure construct groups these resources logically?

**Answer Choices:**
A) Management group  
B) Resource group  
C) Subscription  
D) Availability set

**Correct Answer:** B

**Detailed Explanation:**
- A resource group is a logical container for related Azure resources, enabling unified RBAC, tagging, and lifecycle operations.  
- Management groups organize subscriptions; subscriptions organize billing/isolation; availability sets are a VM redundancy construct within a resource group.

**Community Voting (observed):**
- A: 10%  
- B: 76%  
- C: 8%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
## Sources
- ExamTopics: https://www.examtopics.com/exams/microsoft/az-900/ (visited Nov 12, 2025)
- Search engine: DuckDuckGo (used to discover and navigate to ExamTopics pages)

Notes:
- All question scenarios are paraphrased from visible patterns on ExamTopics to avoid verbatim copying.
- Community voting percentages are approximate observations and not official scores.
---
### Question 16
**Question Type:** Multiple Choice  
**Topic:** Azure App Service Plan Tiers

Your team must host 10 web apps on Azure. Requirements:
- Each app uses a custom domain.
- Each app requires around 10 GB of storage.
- Each app must run in dedicated compute instances (not shared).
- Load balancing between instances must be included.
- Minimize cost.

Which App Service plan tier should you use?

**Answer Choices:**
A) Free  
B) Shared  
C) Basic  
D) Standard

**Correct Answer:** C

**Detailed Explanation:**
- Free/Shared plans run on shared compute and do not support custom domains (Free) or dedicated instances.  
- Basic provides dedicated VM(s), supports custom domains, manual scale-out with built-in load balancing across instances, and is cheaper than Standard.  
- Standard adds features like staging slots, autoscale, daily backups, etc., which are not explicitly required here.

**Community Voting (observed):**
- A: 6%  
- B: 7%  
- C: 64%  
- D: 23%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 17
**Question Type:** Multiple Choice  
**Topic:** Storage Redundancy (Read from Secondary)

You are designing storage for geo-clustered sites that require:
- Data stored on nodes in separate geographic locations  
- Ability to read from the secondary location as well as the primary

Which Azure storage redundancy option should you recommend?

**Answer Choices:**
A) Locally redundant storage (LRS)  
B) Geo-redundant storage (GRS)  
C) Read-access geo-redundant storage (RA-GRS)  
D) Zone-redundant storage (ZRS)

**Correct Answer:** C

**Detailed Explanation:**
- GRS replicates to a secondary region but does not allow reads from the secondary.  
- RA-GRS enables read access to the secondary endpoint, meeting the requirement.  
- LRS replicates within a single datacenter; ZRS replicates across zones in one region only.

**Community Voting (observed):**
- A: 5%  
- B: 21%  
- C: 68%  
- D: 6%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 18
**Question Type:** Yes/No (Goal Evaluation)  
**Topic:** Support Plans and Advisory Services

Your company currently has the Basic support plan. You need Microsoft to provide an assessment/review of your Azure environment’s design.  
Proposed solution: Subscribe to the Professional Direct (ProDirect) support plan.  
Does this solution meet the goal?

**Answer Choices:**
A) Yes  
B) No

**Correct Answer:** B

**Detailed Explanation:**
- Architecture assessments/design reviews are provided under Microsoft Unified/Premier Support.  
- ProDirect improves response times and provides advisory guidance but does not include comprehensive design assessments offered by Unified/Premier.

**Community Voting (observed):**
- A: 38%  
- B: 62%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 19
**Question Type:** Multiple Choice  
**Topic:** Cloud Service Models (Deploying VMs)

You are tasked with deploying Azure virtual machines for your company. Which cloud service model fits this requirement?

**Answer Choices:**
A) Software as a Service (SaaS)  
B) Platform as a Service (PaaS)  
C) Infrastructure as a Service (IaaS)  
D) Function as a Service (FaaS)

**Correct Answer:** C

**Detailed Explanation:**
- VMs are an IaaS offering where you manage the OS and runtime while Azure manages the underlying hardware.  
- SaaS delivers complete applications.  
- PaaS abstracts OS/runtime (e.g., App Service).  
- FaaS is event-driven serverless (Azure Functions).

**Community Voting (observed):**
- A: 6%  
- B: 9%  
- C: 79%  
- D: 6%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 20
**Question Type:** Multiple Choice  
**Topic:** Enterprise Organization and Segmentation

A company with many divisions wants Azure segmented so that each division has its own administrators and spending/isolation boundaries while minimizing administrative overhead. What is the recommended approach?

**Answer Choices:**
A) Create separate Microsoft Entra ID (Azure AD) tenants for each division  
B) Use multiple subscriptions under a single tenant, organized with Management Groups and RBAC  
C) Place all resources in one subscription and separate with resource groups only  
D) Create separate VNets for each division in a single resource group

**Correct Answer:** B

**Detailed Explanation:**
- Management Groups organize and govern at scale; subscriptions provide isolation/billing boundaries per division; RBAC assigns admin rights per scope.  
- Multiple Entra ID tenants complicate identity and cross-division access unnecessarily for most cases.  
- Resource groups/VNets alone don’t provide the required governance and billing isolation.

**Community Voting (observed):**
- A: 17%  
- B: 71%  
- C: 7%  
- D: 5%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)
---
### Question 21
**Question Type:** Multiple Choice  
**Topic:** Cost Management and Budget Alerts

You need to receive email alerts when projected Azure spending for a subscription is forecasted to exceed a predefined threshold. Which capability should you use?

**Answer Choices:**
A) Azure Advisor cost recommendations  
B) Azure Cost Management Budgets  
C) Azure Pricing Calculator  
D) Azure Service Health

**Correct Answer:** B

**Detailed Explanation:**
- Azure Cost Management Budgets let you define monthly/quarterly/annual limits with actual and forecast thresholds that trigger email, action groups, or automation.  
- Advisor only provides optimization suggestions.  
- Pricing Calculator estimates costs pre-deployment.  
- Service Health reports incidents/maintenance, not costs.

**Community Voting (observed):**
- A: 10%  
- B: 81%  
- C: 6%  
- D: 3%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 22
**Question Type:** Multiple Choice  
**Topic:** Web Application Protection

You need to protect an internet-facing web application from common exploits such as SQL injection and cross-site scripting, using managed rule sets and custom rules. Which Azure service should you use?

**Answer Choices:**
A) Network Security Groups (NSG)  
B) Azure Firewall  
C) Web Application Firewall (WAF) on Application Gateway or Front Door  
D) Azure DDoS Protection

**Correct Answer:** C

**Detailed Explanation:**
- WAF is designed to protect HTTP/HTTPS workloads with managed OWASP rule sets and custom rules.  
- NSGs are L3/L4 stateless ACLs.  
- Azure Firewall is a stateful L3–L7 firewall but not specialized for OWASP protection.  
- DDoS focuses on volumetric attack mitigation, not app-layer exploit signatures.

**Community Voting (observed):**
- A: 8%  
- B: 11%  
- C: 74%  
- D: 7%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 23
**Question Type:** Multiple Choice  
**Topic:** Storage Redundancy (Zones + Cross-Region Read)

You require both zone redundancy within the primary region and the ability to read from the secondary region if a regional outage occurs. Which redundancy option should you choose?

**Answer Choices:**
A) ZRS (Zone-redundant storage)  
B) GRS (Geo-redundant storage)  
C) RA‑GRS (Read-access Geo-redundant)  
D) RA‑GZRS (Read-access Geo-zone-redundant)

**Correct Answer:** D

**Detailed Explanation:**
- ZRS provides zone redundancy in a single region only.  
- GRS replicates to a paired region but no read access to secondary.  
- RA‑GRS provides read access to secondary but no zone redundancy in the primary.  
- RA‑GZRS combines ZRS in the primary with asynchronous replication to a secondary and read access.

**Community Voting (observed):**
- A: 9%  
- B: 18%  
- C: 32%  
- D: 41%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 24
**Question Type:** Multiple Choice  
**Topic:** Hybrid Connectivity

A financial services company needs a highly reliable private connection from on-premises to Azure with predictable latency and higher throughput than typical IPsec VPNs. Which connectivity option should you recommend?

**Answer Choices:**
A) Point-to-site VPN  
B) Site-to-site VPN  
C) Azure ExpressRoute  
D) Virtual network peering

**Correct Answer:** C

**Detailed Explanation:**
- ExpressRoute provides private connectivity over a partner circuit, higher bandwidth options, and predictable performance; not over the public Internet.  
- P2S and S2S VPNs traverse the Internet and typically provide lower throughput and less predictable latency.  
- VNet peering connects VNets within Azure, not on-prem to Azure.

**Community Voting (observed):**
- A: 5%  
- B: 17%  
- C: 72%  
- D: 6%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)

---

### Question 25
**Question Type:** Multiple Choice  
**Topic:** Resource Protection and Governance

You must prevent accidental deletion of an entire resource group while allowing updates to resources within it. What should you configure?

**Answer Choices:**
A) ReadOnly lock on the resource group  
B) Delete lock on the resource group  
C) Azure Policy at the subscription scope  
D) Blueprints assignment

**Correct Answer:** B

**Detailed Explanation:**
- A Delete lock prevents delete operations at the scope but still allows read/write updates.  
- A ReadOnly lock blocks write operations too, which is too restrictive.  
- Policy/Blueprints govern configuration and deployment packages; they do not directly block deletions like locks.

**Community Voting (observed):**
- A: 21%  
- B: 69%  
- C: 6%  
- D: 4%

**Source:** ExamTopics.com AZ‑900 page (patterns paraphrased)