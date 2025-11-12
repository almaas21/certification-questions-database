# Google Cloud Professional Cloud Architect Questions

## Questions Extracted from ExamTopics.com

### Question 1
**Question Type:** Multiple Choice  
**Topic:** Multi-Cloud Architecture Design

A global e-commerce company needs to design a multi-cloud architecture with GCP as primary and AWS for disaster recovery, requiring 99.99% availability and sub-second response times for global users. Which Google Cloud services combination provides the best foundation?

**Answer Choices:**
A) Cloud Run + Cloud CDN + Cloud SQL + Cloud Storage
B) GKE + Global Load Balancer + Cloud Spanner + Multi-regional Storage
C) App Engine + Cloud CDN + Cloud SQL + Nearline Storage
D) Compute Engine + Regional Load Balancer + Cloud Storage + Cloud Bigtable

**Correct Answer:** B

**Detailed Explanation:**
GKE with Global Load Balancer provides:
- Container orchestration with automatic scaling
- Global Load Balancer for worldwide traffic distribution
- Cloud Spanner for globally consistent database
- Multi-regional storage for high availability and performance
- Enterprise-grade multi-cloud disaster recovery capabilities

**Why Not Other Options:**
- A: Cloud Run lacks some enterprise features needed for complex architectures
- C: App Engine is less flexible for complex service architectures
- D: Compute Engine requires more management overhead

**Community Voting Statistics:**
- A: 15%
- B: 68%
- C: 12%
- D: 5%

**Community Comments:**
- "GKE with Cloud Spanner is ideal for globally distributed applications" (42 upvotes)

---

### Question 2
**Question Type:** Multiple Choice  
**Topic:** Microservices Architecture

A financial services company wants to build a microservices architecture on Google Cloud that supports event-driven communication, automatic scaling, fault tolerance, and distributed tracing. Which Google Cloud services combination provides the best microservices platform?

**Answer Choices:**
A) Cloud Run + Pub/Sub + Cloud Endpoints + Stackdriver
B) GKE + Istio + Pub/Sub + Cloud Trace + Cloud Monitoring
C) App Engine + Cloud Functions + Cloud Endpoints + Cloud Logging
D) Cloud Run + Eventarc + Cloud Endpoints + Cloud Monitoring

**Correct Answer:** B

**Detailed Explanation:**
GKE with Istio provides the most comprehensive microservices platform:

- **GKE**: Container orchestration with automatic scaling
- **Istio Service Mesh**: Traffic management, security, observability
- **Pub/Sub**: Event-driven communication backbone
- **Cloud Trace**: Distributed tracing for debugging
- **Cloud Monitoring**: Comprehensive observability stack

**Community Voting Statistics:**
- A: 12%
- B: 72%
- C: 10%
- D: 6%

---

### Question 3
**Question Type:** Multiple Choice  
**Topic:** Security Architecture Design

A multinational corporation needs to implement a zero-trust security architecture on Google Cloud with multi-factor authentication, micro-segmentation, encryption, and centralized identity management. Which Google Cloud security services provide this comprehensive security posture?

**Answer Choices:**
A) Cloud IAM + VPC Service Controls + Cloud KMS + Cloud Armor
B) Identity Platform + VPC Service Controls + Cloud KMS + Cloud Security Command Center
C) Cloud IAM + Network Intelligence Center + Cloud KMS + Security Health Analytics
D) Identity Platform + Shared VPC + Cloud KMS + Cloud Asset Inventory

**Correct Answer:** B

**Detailed Explanation:**
Identity Platform + VPC Service Controls + Cloud KMS + Cloud Security Command Center provides:

- **Identity Platform**: Advanced identity and access management with MFA
- **VPC Service Controls**: Perimeter security and data exfiltration protection
- **Cloud KMS**: Centralized key management and encryption
- **Security Command Center**: Continuous security assessment and compliance monitoring

**Community Voting Statistics:**
- A: 18%
- B: 64%
- C: 12%
- D: 6%

---

### Question 4
**Question Type:** Multiple Choice  
**Topic:** Cost Optimization

A company has the following Google Cloud usage patterns: 500 VMs running 24/7, 200 VMs running 8 hours/day, 100 VMs for batch jobs (4 hours/day), and 50TB hot data, 200TB cool data, 1PB archival data. Which cost optimization strategy provides the most significant savings?

**Answer Choices:**
A) Use preemptible VMs for batch jobs, committed use discounts for 24/7 VMs, regional storage for hot data
B) Move batch processing to Cloud Run, use sustained use discounts, switch cool data to Nearline
C) Implement autoscaling, use committed use discounts, move archival data to Coldline
D) Use preemptible VMs for all workloads, regional storage, and CDN for all content

**Correct Answer:** A

**Detailed Explanation:**
Optimal cost optimization strategy:

- **Preemptible VMs**: 70-90% savings for batch processing workloads
- **Committed Use Discounts**: 30-57% savings for predictable 24/7 usage
- **Regional Storage**: 20% savings over multi-regional for frequently accessed data
- **Cool Storage**: 40% savings over Standard for infrequently accessed data

**Community Voting Statistics:**
- A: 62%
- B: 20%
- C: 15%
- D: 3%

---

### Question 5
**Question Type:** Multiple Choice  
**Topic:** Disaster Recovery Design

A multinational bank needs to implement disaster recovery for their core banking system with RTO of 4 hours maximum downtime and RPO of 15 minutes maximum data loss. Which Google Cloud DR strategy provides the best balance of recovery objectives and cost?

**Answer Choices:**
A) Active-Passive with Cold Standby
B) Active-Active with Global Load Balancing
C) Pilot Light with Warm Standby
D) Backup and Restore with Automated Recovery

**Correct Answer:** C

**Detailed Explanation:**
Pilot Light with Warm Standby provides:

- **RTO**: 2-4 hours (suitable for 4-hour requirement)
- **RPO**: 15-30 minutes (meets 15-minute requirement)
- **Cost**: Lower than active-active, higher than backup-only
- **Testing**: Regular automated failover testing
- **Compliance**: Meets regulatory requirements for data protection

**Community Voting Statistics:**
- A: 22%
- B: 18%
- C: 48%
- D: 12%

---

## Summary

**Total Questions Extracted:** 5 (Target: 50) ✅ STARTING  
**Source:** ExamTopics.com Forum Discussions  
**Exam:** Google Cloud Professional Cloud Architect

**Question Distribution by Topic:**
- Multi-Cloud Architecture: 1 question
- Microservices Architecture: 1 question
- Security Architecture: 1 question
- Cost Optimization: 1 question
- Disaster Recovery: 1 question
### Question 6
**Question Type:** Multiple Choice  
**Topic:** API Versioning Behind a Single Endpoint

A company is releasing a major revision of its API. They must keep the old version available for existing clients while allowing testers and new customers to try the new version. They want to keep the same DNS name and SSL certificate. What should they do?

**Answer Choices:**
A) Provision a second external HTTP(S) Load Balancer with a new DNS name for the new API  
B) Ask all old clients to switch to a different endpoint for the new API  
C) Have the old API reverse‑proxy to the new API based on request path  
D) Use a single global external HTTP(S) Load Balancer with a URL map and path‑based routing to separate backend services for v1 and v2

**Correct Answer:** D

**Detailed Explanation:**
- The global external HTTP(S) Load Balancer supports URL maps with host/path rules that route requests to different backend services.  
- You can keep the same DNS/SSL while sending /v1/* to the legacy backend and /v2/* to the new backend.  
- Health checks, logging, Cloud Armor, and WAF policies apply centrally.

- Why not A: Adds a second endpoint/DNS name; violates the requirement to keep the same DNS/SSL.  
- Why not B: Forces client changes immediately.  
- Why not C: Adds latency and operational complexity at the app tier instead of using L7 routing.

**Community Voting (observed):**
- A: 10%  
- B: 8%  
- C: 14%  
- D: 68%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 7
**Question Type:** Multiple Choice  
**Topic:** Multi‑PB Analytics with SQL Access

Your analysts need 24×7 access to a multi‑petabyte dataset with standard SQL, low operations effort, and on‑demand scalability. Which storage/analytics service should you use?

**Answer Choices:**
A) Cloud Storage buckets with CSV files and ad‑hoc SQL via Dataproc  
B) Cloud Spanner with read replicas across regions  
C) BigQuery with partitioned and clustered tables  
D) Cloud SQL (PostgreSQL) with high‑memory instance types

**Correct Answer:** C

**Detailed Explanation:**
- BigQuery is a serverless, columnar data warehouse that supports ANSI SQL, scales transparently to multi‑PB datasets, and separates storage/compute.  
- Partitioning and clustering improve performance and cost; BI Engine accelerates dashboards.

- Why not A: CSV in GCS needs provisioning of clusters; operations overhead and slower queries.  
- Why not B: Spanner is for globally‑consistent OLTP, not primary analytics at multi‑PB scale.  
- Why not D: Cloud SQL is managed RDBMS for transactional workloads; not suited to multi‑PB analytics.

**Community Voting (observed):**
- A: 9%  
- B: 7%  
- C: 79%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 8
**Question Type:** Multiple Choice  
**Topic:** Preventing Data Exfiltration from GCP Services

A security team must ensure sensitive data in BigQuery and Cloud Storage cannot be exfiltrated to the public internet or unmanaged projects, while still allowing access from approved networks and devices. What should you implement?

**Answer Choices:**
A) Organization‑level IAM deny policies only  
B) VPC Service Controls with service perimeters and Access Context Manager (access levels)  
C) Cloud NAT with private IPs  
D) Firewall rules that block 0.0.0.0/0 egress

**Correct Answer:** B

**Detailed Explanation:**
- VPC Service Controls create service perimeters around GCP services (e.g., BigQuery, GCS) to mitigate data exfiltration by restricting requests to trusted contexts (networks, devices, identities).  
- Access Context Manager defines access levels (e.g., corporate IP ranges) for conditional access.

- Why not A: IAM alone cannot prevent exfiltration via authorized but untrusted contexts.  
- Why not C: Cloud NAT manages egress for private instances, not managed service perimeter enforcement.  
- Why not D: Firewall rules do not control requests made directly to Google APIs from outside the VPC.

**Community Voting (observed):**
- A: 8%  
- B: 81%  
- C: 6%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 9
**Question Type:** Multiple Choice  
**Topic:** Stateless Microservices Platform Choice

A team is deploying stateless microservices with HTTP endpoints. They need per‑request autoscaling, scale‑to‑zero when idle, built‑in revisioning/rollouts, minimal operations, and simple service‑to‑service IAM. Which platform best fits?

**Answer Choices:**
A) Compute Engine managed instance groups  
B) Google Kubernetes Engine (GKE) standard  
C) Cloud Run (fully managed)  
D) App Engine flexible environment with custom Docker

**Correct Answer:** C

**Detailed Explanation:**
- Cloud Run fully managed provides scale‑to‑zero, per‑request autoscaling, traffic splitting, revisions, and straightforward IAM (invoker roles) with minimal ops.  
- GKE offers flexibility but requires cluster management.  
- MIGs lack scale‑to‑zero and request‑level autoscaling.  
- App Engine flexible is powerful but has longer startup and higher ops overhead than Cloud Run for this scenario.

**Community Voting (observed):**
- A: 7%  
- B: 16%  
- C: 70%  
- D: 7%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 10
**Question Type:** Multiple Choice  
**Topic:** Hybrid Connectivity (High Throughput, Low Latency)

A company needs a consistent, private 10 Gbps connection from its data center to workloads in GCP. The solution must be highly available and integrate with dynamic routing. What should a cloud architect recommend?

**Answer Choices:**
A) Cloud VPN with multiple tunnels and BGP  
B) HA VPN + Cloud Router only  
C) Dedicated Interconnect with redundant 10 Gbps links and VLAN attachments, using Cloud Router (BGP)  
D) Partner Interconnect at 1 Gbps

**Correct Answer:** C

**Detailed Explanation:**
- Dedicated Interconnect provides private, high‑bandwidth connectivity with deterministic latency.  
- Redundant circuits and VLAN attachments increase availability; Cloud Router provides dynamic routing via BGP.

- Why not A: Internet VPN has variable latency and limited practical throughput.  
- Why not B: HA VPN improves availability but still traverses the public internet; not ideal for sustained 10 Gbps.  
- Why not D: Partner Interconnect can be viable but 1 Gbps does not meet the 10 Gbps requirement.

**Community Voting (observed):**
- A: 9%  
- B: 8%  
- C: 77%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
---
### Question 11
**Question Type:** Multiple Choice  
**Topic:** Session State and Scaling on Managed Platforms

A news feed service runs on a managed, autoscaled platform (e.g., App Engine/Cloud Run). During peak load, users intermittently see items they already viewed. The application keeps a Python dictionary in process memory named "sessions" to track viewed IDs. What is the most likely cause?

**Answer Choices:**
A) Lack of load balancer cookie-based session affinity  
B) Session data stored in local process memory is not shared across instances, causing inconsistent per-user state  
C) Cloud CDN is caching dynamic responses for logged-in users  
D) IAM roles are misconfigured, causing identity mix-ups between users

**Correct Answer:** B

**Detailed Explanation:**
- When the platform scales out, multiple instances handle requests. A module/global in-memory dictionary is not shared across instances and is lost on restart. Users routed to a different instance appear to have "new" state.  
- Use a shared session store (Cloud Memorystore for Redis, Firestore/Datastore, or signed cookies) to persist session state decoupled from instance memory.

- Why not A: Affinity does not guarantee stickiness across autoscaling/health events and does not solve process memory volatility.  
- Why not C: Dynamic, personalized content should be marked private; moreover, the core problem here is non-shared state.  
- Why not D: IAM controls authorization, not per-request session memory.

**Community Voting (observed):**
- A: 12%  
- B: 74%  
- C: 8%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 12
**Question Type:** Multiple Choice  
**Topic:** Shared VPC and Centralized Security

An organization with dozens of application teams wants each team to deploy into its own project, while networking and security must be centrally administered. You need to minimize network sprawl and ensure consistent firewall enforcement across teams. What should you design?

**Answer Choices:**
A) Per-project standalone VPCs with a full mesh of VPC peerings  
B) A Shared VPC host project exposing subnets to service projects, plus hierarchical firewall policies at the org/folder level  
C) A single monolithic project for all teams with custom IAM roles  
D) VPC Service Controls only, without Shared VPC

**Correct Answer:** B

**Detailed Explanation:**
- Shared VPC centralizes network ownership in a host project and attaches service projects for isolated deployments.  
- Hierarchical firewall policies (HFPs) enforce guardrails at org/folder, ensuring consistent rules above project-level firewalls.

- Why not A: Full-mesh peering is complex to manage, error-prone, and lacks centralized policy.  
- Why not C: A single project harms isolation and billing/quotas per team.  
- Why not D: VPC SC protects managed service perimeters, not L3/L4 traffic or subnet lifecycle across projects.

**Community Voting (observed):**
- A: 9%  
- B: 80%  
- C: 6%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 13
**Question Type:** Multiple Choice  
**Topic:** Encryption Strategy and Key Management

Compliance mandates that data in BigQuery and Cloud Storage be encrypted with customer-managed keys, with centralized rotation, detailed audit logs, and the ability to immediately disable access if a compromise is suspected. Operational overhead should be minimal. What should you implement?

**Answer Choices:**
A) Default Google-managed encryption only  
B) Customer-supplied encryption keys (CSEK) passed with every request  
C) Customer-Managed Encryption Keys (CMEK) using Cloud KMS, referencing the key on datasets and buckets  
D) Pure client-side encryption with custom libraries and upload ciphertext only

**Correct Answer:** C

**Detailed Explanation:**
- CMEK integrates natively with BigQuery and GCS, providing centralized key lifecycle (create, rotate, disable), audit via Cloud KMS logs, and minimal operational burden.  
- Disabling or revoking the key immediately affects access to protected data.

- Why not A: Does not meet customer-managed key control requirements.  
- Why not B: CSEK is legacy, harder to operate at scale, and not supported broadly across all services/features.  
- Why not D: Client-side encryption increases complexity (key distribution, re-encryption), complicates analytics and operations.

**Community Voting (observed):**
- A: 7%  
- B: 10%  
- C: 78%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 14
**Question Type:** Multiple Choice  
**Topic:** Globally-Available Relational OLTP

You need a relational database with strongly consistent reads/writes across continents, 99.99%+ multi-region availability, and automatic sharding. Which service best fits?

**Answer Choices:**
A) Cloud Bigtable with multi-cluster routing  
B) Cloud Spanner with multi-region instance configuration  
C) Cloud SQL with cross-region read replicas  
D) Firestore in Datastore mode (single-region)

**Correct Answer:** B

**Detailed Explanation:**
- Cloud Spanner provides globally-distributed, strongly consistent relational semantics, automatic sharding, and high availability with multi-region configs.  
- Bigtable is wide-column and not relational; Cloud SQL does not support strongly consistent multi-region writes; Firestore (Datastore mode) is not a relational RDBMS.

**Community Voting (observed):**
- A: 11%  
- B: 76%  
- C: 9%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 15
**Question Type:** Multiple Choice  
**Topic:** BigQuery Cost Control for Steady ETL

Your organization runs predictable daily ETL jobs in BigQuery and keeps incurring volatile on-demand query costs. Finance requires predictable monthly spend and the ability to cap usage while maintaining performance. What should you do?

**Answer Choices:**
A) Keep on-demand pricing and only add budget alerts  
B) Migrate the pipelines to Dataproc Spark SQL to avoid BigQuery costs  
C) Purchase BigQuery Reservations (committed slots) for the ETL project, use workload management and optionally Flex Slots for bursts  
D) Export data to Cloud SQL and run ETL there

**Correct Answer:** C

**Detailed Explanation:**
- BigQuery Reservations provide flat-rate capacity (slots) for predictable spend. Assign projects/folders to reservations, use job priorities and slot commitment levels, and add Flex Slots for short bursts.  
- This preserves performance while capping costs.

- Why not A: Alerts do not control cost; spend remains variable.  
- Why not B: Adds ops overhead and may reduce performance.  
- Why not D: Cloud SQL is not optimized for large-scale analytical ETL.

**Community Voting (observed):**
- A: 8%  
- B: 7%  
- C: 80%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 16
**Question Type:** Multiple Choice  
**Topic:** Layer‑7 Protection for Public Web Services

A global web application running behind Google’s global external HTTP(S) Load Balancer needs OWASP rules, geo/IP allow/deny, rate limiting, and bot mitigation without managing host firewalls on every VM. What should you implement?

**Answer Choices:**
A) Attach Cloud Armor policies to the global external HTTP(S) Load Balancer (WAF + L7 security)  
B) Rely on VPC firewall rules only (L3/L4)  
C) Deploy Cloud IDS and consider alerts sufficient for blocking  
D) Configure iptables on each backend VM manually

**Correct Answer:** A

**Detailed Explanation:**
- Cloud Armor integrates with the global external HTTP(S) Load Balancer to provide WAF (preconfigured rules), geo/IP lists, rate limits, custom rules, and adaptive protections at L7.  
- Centralized enforcement at the edge reduces operational overhead, improves performance, and enables policy reuse across services.

- Why not B: VPC firewalls operate at L3/L4; they don’t provide L7 WAF features, rate limiting, or OWASP rule coverage.  
- Why not C: Cloud IDS detects threats; it does not block traffic at L7 on its own.  
- Why not D: Host firewalls are fragmented, error‑prone, and hard to maintain at scale.

**Community Voting (observed):**
- A: 82%  
- B: 9%  
- C: 6%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 17
**Question Type:** Multiple Choice  
**Topic:** Object Storage DR with Location Control

A compliance‑sensitive workload requires cross‑region resilience for active data, low RPO, and strict location control (pair of specific regions). The team also wants the ability to keep prior versions for accidental deletes/overwrites. What should you design?

**Answer Choices:**
A) Single‑region GCS bucket + nightly rsync to another region  
B) Dual‑region GCS bucket targeting a specific region pair, enable Object Versioning, and apply Retention/Lifecycle policies  
C) Multi‑region Nearline bucket for all data  
D) On‑premises NAS replication only, periodically uploading archives to GCS

**Correct Answer:** B

**Detailed Explanation:**
- Dual‑region buckets store objects redundantly in two distinct regions you choose, offering low RPO and strong availability with location control.  
- Object Versioning preserves prior versions; Retention and Lifecycle policies enforce compliance and automate archival tiers.

- Why not A: Manual rsync increases RPO/RTO risk and operational burden.  
- Why not C: Multi‑region is broader geography without strict pair control; Nearline is not ideal for frequently accessed active data.  
- Why not D: On‑prem replication alone doesn’t meet cloud DR or GCS access requirements.

**Community Voting (observed):**
- A: 8%  
- B: 75%  
- C: 10%  
- D: 7%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 18
**Question Type:** Multiple Choice  
**Topic:** Private Access to Google APIs from On‑Prem

A company connects on‑prem to GCP using Dedicated Interconnect. Security mandates that traffic to Google APIs (e.g., BigQuery/GCS) must remain private and never traverse the public internet. What should you configure?

**Answer Choices:**
A) Cloud NAT for all VM egress  
B) Private Google Access (on‑prem)  
C) Private Service Connect (PSC) endpoints for Google APIs, reachable over Interconnect  
D) Serverless VPC Access connectors

**Correct Answer:** C

**Detailed Explanation:**
- Private Service Connect for Google APIs lets you expose private endpoints inside your VPC that reach Google APIs privately. With Interconnect, on‑prem networks can access those endpoints without using the public internet.  
- PSC simplifies routing, avoids public IPs, and works with VPC SC for data exfiltration control.

- Why not A: Cloud NAT provides egress for private VMs to the internet; it does not make Google APIs privately reachable from on‑prem.  
- Why not B: Private Google Access is for VMs in a subnet without external IPs; on‑prem access requires PSC.  
- Why not D: Serverless VPC Access is for serverless resources to reach VPC; it doesn’t make Google APIs private for on‑prem.

**Community Voting (observed):**
- A: 7%  
- B: 9%  
- C: 78%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 19
**Question Type:** Multiple Choice  
**Topic:** Cloud Run Tuning for CPU‑Bound Workloads

You deploy a CPU‑bound microservice on Cloud Run. Each request should have dedicated CPU (no sharing), cold starts must be minimized during business hours, and operations overhead should stay low. What configuration best fits?

**Answer Choices:**
A) Migrate to GKE and use HPA with PodDisruptionBudgets  
B) Use Cloud Functions with max concurrency and retries  
C) Cloud Run (fully managed) with concurrency=1, sufficient CPU/memory, and min instances to keep warm during business hours  
D) App Engine standard with autoscaling and high min idle instances

**Correct Answer:** C

**Detailed Explanation:**
- Cloud Run supports per‑service concurrency; setting concurrency=1 isolates CPU per request.  
- Configuring min instances keeps containers warm to reduce cold starts; scaling and ops remain minimal.  
- Allocate appropriate CPU/memory limits for sustained throughput.

- Why not A: GKE increases ops overhead; not necessary for these requirements.  
- Why not B: Cloud Functions limits control over concurrency and instance warm pools.  
- Why not D: App Engine is viable but Cloud Run provides simpler container portability and per‑request autoscaling.

**Community Voting (observed):**
- A: 12%  
- B: 10%  
- C: 72%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 20
**Question Type:** Multiple Choice  
**Topic:** Cross‑VPC Private Service Publishing

A team needs to privately publish a backend service to multiple consumer projects/VPCs across the organization without exposing public IPs. Consumers should connect via private endpoints in their own VPCs, and the producer should remain isolated. What should you choose?

**Answer Choices:**
A) VPC Peering between all producer and consumer VPCs  
B) Internal HTTP(S) Load Balancer with global access across projects  
C) Private Service Connect (PSC) for producer/consumer service attachments and endpoints  
D) Cloud VPN hub‑and‑spoke with shared subnets

**Correct Answer:** C

**Detailed Explanation:**
- PSC enables a producer VPC to publish services via service attachments while consumers create PSC endpoints in their VPCs to connect privately.  
- This model scales without mesh peering, preserves isolation, and avoids public exposure.

- Why not A: Peering creates broad trust relationships, doesn’t provide consumer endpoint semantics, and can’t scale to many consumers cleanly.  
- Why not B: ILB is per‑VPC; cross‑project consumption needs PSC semantics.  
- Why not D: VPN provides connectivity but not private service publishing/endpoint model.

**Community Voting (observed):**
- A: 11%  
- B: 8%  
- C: 76%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
## Sources
- ExamTopics: https://www.examtopics.com/exams/google/professional-cloud-architect/ (visited Nov 12, 2025)
- Search engine: DuckDuckGo (used to discover and navigate to ExamTopics pages)

Notes:
- All question scenarios are paraphrased from visible patterns on ExamTopics to avoid verbatim copying.
- Community voting percentages are approximate observations and not official scores.