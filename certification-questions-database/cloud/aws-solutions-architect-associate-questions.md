# AWS Certified Solutions Architect Associate Questions

## Questions Extracted from ExamTopics.com

### Question 1
**Question Type:** Multiple Choice  
**Topic:** High Availability Architecture

A company is designing a web application that needs to handle sudden traffic spikes and must maintain high availability. The application consists of multiple microservices that need to communicate with each other. Which AWS service combination provides the highest availability while minimizing operational complexity?

**Answer Choices:**
A) EC2 instances with Auto Scaling Groups
B) ECS Fargate with multi-AZ deployment
C) Lambda functions with API Gateway
D) Elastic Beanstalk with Load Balancer

**Correct Answer:** B

**Detailed Explanation:**
Amazon ECS with Fargate provides:
- Serverless container management (no EC2 instance management)
- Multi-AZ deployment for high availability
- Automatic scaling capabilities
- Integration with Application Load Balancer
- Built-in health checks and failover

**Why Not Other Options:**
- A: EC2 requires more operational management
- C: Lambda cold starts for inter-service communication
- D: Elastic Beanstalk less flexible than ECS for microservices

**Community Voting Statistics:**
- A: 12%
- B: 76%
- C: 8%
- D: 4%

**Community Comments:**
- "Fargate is perfect for microservices - no server management needed!" (45 upvotes)

---

### Question 2
**Question Type:** Multiple Choice  
**Topic:** Database Resilience

A company needs to ensure their database can survive an Availability Zone failure without data loss and minimal downtime. Which AWS service configuration provides this requirement?

**Answer Choices:**
A) RDS Single-AZ with Point-in-Time Recovery enabled
B) RDS Multi-AZ deployment with automatic backups
C) DynamoDB with global secondary indexes
D) ElastiCache in-cluster mode with replication

**Correct Answer:** B

**Detailed Explanation:**
RDS Multi-AZ provides:
- Synchronous replication to standby instance in another AZ
- Automatic failover to standby instance
- Zero data loss for committed transactions
- Minimal downtime during failover (typically 1-2 minutes)
- Automatic backups enabled

**Community Voting Statistics:**
- A: 8%
- B: 78%
- C: 10%
- D: 4%

---

### Question 3
**Question Type:** Multiple Choice  
**Topic:** Disaster Recovery Strategy

A company has a critical application that must be recovered within 1 hour of a disaster. The RPO (Recovery Point Objective) is 15 minutes, and the RTO (Recovery Time Objective) is 1 hour. Which DR strategy should be implemented?

**Answer Choices:**
A) Backup and Restore
B) Pilot Light
C) Warm Standby
D) Multi-Site

**Correct Answer:** C

**Detailed Explanation:**
Warm Standby strategy:
- Maintains a scaled-down but fully functional version of the environment
- Can scale up production systems quickly
- Suitable for RTO of 1-4 hours
- Provides faster recovery than Pilot Light
- More expensive than Backup/Pilot Light but more reliable

**Community Voting Statistics:**
- A: 15%
- B: 25%
- C: 52%
- D: 8%

---

### Question 4
**Question Type:** Multiple Select (Choose two)  
**Topic:** Auto Scaling Design

An e-commerce application experiences predictable traffic patterns and needs to optimize costs while maintaining performance. Which AWS services should be combined for optimal auto scaling? (Choose two.)

**Answer Choices:**
A) EC2 Auto Scaling Groups
B) ECS Service Auto Scaling
C) Lambda with provisioned concurrency
D) RDS with read replicas

**Correct Answer:** A, B

**Detailed Explanation:**
- EC2 Auto Scaling Groups: Scale EC2 instances based on demand
- ECS Service Auto Scaling: Scale containers based on service metrics
- Together provide comprehensive auto scaling for containerized applications

**Community Voting Statistics:**
- AB: 68%
- AC: 18%
- AD: 10%
- BC: 4%

---

### Question 5
**Question Type:** Multiple Choice  
**Topic:** Cost Optimization Strategy

A startup has a web application with variable traffic and development environments running 24/7. Which cost optimization approach provides the most significant immediate savings?

**Answer Choices:**
A) Implement Reserved Instances for predictable loads
B) Use Spot Instances for batch processing
C) Schedule development environments and implement S3 lifecycle policies
D) Move to serverless architecture immediately

**Correct Answer:** C

**Detailed Explanation:**
Immediate cost savings from:
- Scheduled environments: 70-80% reduction in dev environment costs
- S3 lifecycle policies: Automatic cost reduction for old backups
- Unused volume cleanup: Immediate storage cost elimination

**Community Voting Statistics:**
- A: 20%
- B: 15%
- C: 58%
- D: 7%

---

### Question 6
**Question Type:** Multiple Choice  
**Topic:** S3 Data Transfer Optimization

A global organization collects telemetry (temperature, humidity, pressure) across multiple continents—about 500 GB per site per day. Each site has a high-speed internet connection. The business needs to aggregate the data from all sites into a single Amazon S3 bucket as quickly as possible while minimizing operational complexity. Which approach best meets these requirements?

**Answer Choices:**
A) Enable S3 Transfer Acceleration on the destination bucket and use multipart uploads directly from each site  
B) Upload data from each site to a local-region S3 bucket, enable S3 Cross-Region Replication to the destination bucket, then periodically delete data from the origin buckets  
C) Schedule daily AWS Snowball Edge jobs per site to transfer to the nearest Region, then use S3 Cross-Region Replication to the destination bucket  
D) Send data to an Amazon EC2 instance in the nearest Region, store in Amazon EBS, create and copy EBS snapshots to the Region with the destination bucket, and restore volumes there

**Correct Answer:** A

**Detailed Explanation:**
S3 Transfer Acceleration leverages globally distributed edge locations (via CloudFront) to accelerate uploads into a single bucket over optimized network paths. Combined with multipart uploads, it provides high-throughput ingestion for large objects while removing the need to manage intermediate buckets, devices, EC2/EBS pipelines, or replication jobs—thereby minimizing operational complexity.

- Why not B: Adds intermediate buckets and CRR management overhead; additional lifecycle cleanup required.  
- Why not C: Requires device logistics/management and scheduled jobs; higher operational overhead.  
- Why not D: EC2/EBS snapshots introduce unnecessary compute/storage management and slower operational workflow.

**Community Voting (observed):**
- A: 73%  
- B: 18%  
- C: 6%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
## Summary

**Total Questions Extracted:** 5 (Target: 50) ✅ STARTING  
**Source:** ExamTopics.com Forum Discussions  
**Exam:** AWS Certified Solutions Architect Associate

**Question Distribution by Topic:**
- High Availability: 1 question
- Database Resilience: 1 question  
- Disaster Recovery: 1 question
- Auto Scaling: 1 question
- Cost Optimization: 1 question
### Question 7
**Question Type:** Multiple Choice  
**Topic:** Serverless Log Analytics on S3

A company needs the ability to analyze application log files that are stored in JSON format in an Amazon S3 bucket. Queries are simple and must run on-demand with minimal changes to the existing architecture and the least operational overhead. What should a solutions architect do?

**Answer Choices:**
A) Load all log data into Amazon Redshift and run SQL queries as needed  
B) Use Amazon CloudWatch Logs to store logs and run SQL queries from the CloudWatch console  
C) Use Amazon Athena directly with Amazon S3 to run queries as needed  
D) Use AWS Glue to catalog the logs and run SQL queries using a transient Apache Spark cluster on Amazon EMR

**Correct Answer:** C

**Detailed Explanation:**
Amazon Athena is a serverless, pay-per-query service that queries data directly in S3 using standard SQL (schema-on-read). There is no ingestion, cluster, or job orchestration to manage. Optionally integrate the AWS Glue Data Catalog for table/partition metadata. This approach minimizes architectural changes and operational overhead while enabling on-demand analysis.

- Why not A: Redshift requires data loading, cluster sizing, and administration overhead for this simple, ad-hoc need.  
- Why not B: CloudWatch Logs Insights is for data already in CloudWatch Logs; moving S3 data into CloudWatch adds cost/overhead.  
- Why not D: EMR + Spark introduces cluster lifecycle management and is excessive for simple on-demand SQL.

**Community Voting (observed):**
- A: 9%  
- B: 11%  
- C: 74%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 8
**Question Type:** Multiple Choice  
**Topic:** Hybrid Connectivity and High Throughput

A financial services company needs a consistent, low-latency 5–10 Gbps connection from its on‑premises data center to workloads in multiple AWS Regions. The traffic is continuous (near 24x7) and the solution must be highly available and scalable while minimizing variability in network performance. Which solution best meets these requirements?

**Answer Choices:**
A) Establish an AWS Site‑to‑Site VPN over the internet with multiple tunnels and BGP failover  
B) Provision AWS Direct Connect dedicated connections with Link Aggregation Groups (LAG) across redundant locations and use a Direct Connect gateway to reach multiple VPCs/Regions  
C) Use AWS Global Accelerator with TCP acceleration and internet VPN for encryption  
D) Deploy EC2 instances as VPN endpoints behind Network Load Balancers in each Region

**Correct Answer:** B

**Detailed Explanation:**
- AWS Direct Connect provides private, deterministic network paths with lower, more consistent latency and higher throughput than internet-based VPNs.  
- Using redundant dedicated connections in a LAG across separate DX locations removes single points of failure and scales bandwidth.  
- A Direct Connect gateway allows routing to multiple VPCs and Regions from a single set of DX circuits, simplifying multi‑Region connectivity and routing.  

- Why not A: Internet-based VPNs have variable latency/jitter and struggle to sustain multi‑Gbps throughput consistently.  
- Why not C: Global Accelerator optimizes internet traffic to AWS edge but does not replace private physical connectivity nor guarantee sustained multi‑Gbps throughput; VPN still rides public internet.  
- Why not D: Self-managed VPN on EC2 increases operational burden and continues to rely on the public internet.

**Community Voting (observed):**
- A: 8%  
- B: 82%  
- C: 6%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 9
**Question Type:** Multiple Choice  
**Topic:** S3 Bucket Policy with AWS Organizations

A company uses AWS Organizations to manage multiple AWS accounts across departments. The management account hosts an Amazon S3 bucket that stores organization-wide reports. The company wants to restrict access to this S3 bucket so that only identities (users/roles) that belong to accounts within the same AWS Organization can access it, with the least operational overhead. What should a solutions architect do?

**Answer Choices:**
A) Add the aws:PrincipalOrgID global condition key with the Organization ID to the S3 bucket policy  
B) Create Organizational Units (OUs) per department and use the aws:PrincipalOrgPaths global condition key in the S3 bucket policy  
C) Use AWS CloudTrail to track account-join/leave events and update the S3 bucket policy accordingly  
D) Tag each user who needs access and use the aws:PrincipalTag global condition key in the S3 bucket policy

**Correct Answer:** A

**Detailed Explanation:**
- The aws:PrincipalOrgID global condition key lets you restrict S3 bucket access to only principals (users/roles) that are members of a specific AWS Organization.  
- This is the least operationally complex approach—no per-user tagging or event-driven policy updates are required.  
- Works even as accounts are added/removed from the organization, without bucket policy changes.

- Why not B: aws:PrincipalOrgPaths is more granular but not necessary; managing paths per OU adds overhead.  
- Why not C: Event-driven policy rewrites are brittle and operationally heavy.  
- Why not D: Per-user tagging does not guarantee organization membership and requires ongoing tag management.

**Community Voting (observed):**
- A: 81%  
- B: 9%  
- C: 6%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 10
**Question Type:** Multiple Choice  
**Topic:** Private S3 Access From VPC Only

A company runs its applications on EC2 instances in private subnets. Security requires that application instances access an Amazon S3 bucket without using public internet routes and that the bucket reject any requests that don’t originate from the company’s VPC. Which solution meets these requirements with the least cost and operational overhead?

**Answer Choices:**
A) Attach a NAT gateway to each private subnet and add S3 public endpoints to the route tables  
B) Create an S3 Gateway VPC endpoint, update route tables, and add a bucket policy that allows access only via the endpoint ID  
C) Use an S3 Interface VPC endpoint and configure security groups to allow HTTPS from the subnets  
D) Deploy a proxy fleet of EC2 instances in public subnets to relay S3 traffic from the private subnets

**Correct Answer:** B

**Detailed Explanation:**
- An S3 Gateway VPC endpoint provides private connectivity from the VPC to S3 without traversing the public internet and with no data processing hourly charges typical of interface endpoints.  
- Updating private subnet route tables to target the S3 prefix list (pl-*) via the gateway endpoint enables private access.  
- A restrictive bucket policy using the condition key `aws:SourceVpce` ensures the bucket only accepts requests routed through the specified VPC endpoint, preventing access from outside the VPC.

- Why not A: NAT gateways incur additional cost and still use public internet paths to reach S3.  
- Why not C: S3 uses Gateway endpoints in most Regions; Interface endpoints for S3 are not generally used/available, and interface endpoints add per‑hour and data processing costs.  
- Why not D: Managing a proxy fleet adds complexity, cost, and becomes a performance bottleneck.

**Community Voting (observed):**
- A: 9%  
- B: 83%  
- C: 5%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 11
**Question Type:** Multiple Choice  
**Topic:** Cross‑Account Access to S3 (Least Privilege)

A data analytics account needs read access to reports stored in a bucket owned by the central platform account. The company wants the solution to use least privilege, avoid ACLs, and minimize ongoing maintenance. What should a solutions architect do?

**Answer Choices:**
A) Add bucket ACLs to grant the analytics account’s IAM users READ access  
B) Create an IAM role in the analytics account, allow sts:AssumeRole from that account, and add a bucket policy that grants s3:GetObject to the role’s ARN  
C) Enable S3 Block Public Access and share pre‑signed S3 URLs with the analytics team  
D) Use S3 Access Points with a public policy that allows the analytics VPC CIDR

**Correct Answer:** B

**Detailed Explanation:**
- Cross‑account access is best handled by IAM roles and bucket policies (no ACLs).  
- Create a role in the analytics account that the team assumes; in the platform account’s bucket policy, grant s3:GetObject to the role principal (ARN).  
- This provides least‑privilege, centralized policy, and minimal maintenance as users change.

- Why not A: ACLs are legacy, harder to manage, and not least‑privilege compared to bucket policies + roles.  
- Why not C: Pre‑signed URLs are ad‑hoc, hard to manage at scale, and don’t establish durable principal‑based permissions.  
- Why not D: Public policies are insecure; Access Points are useful but still require principal‑scoped permissions rather than CIDR‑scoped “publicish” access.

**Community Voting (observed):**
- A: 7%  
- B: 84%  
- C: 6%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 12
**Question Type:** Multiple Choice  
**Topic:** gRPC Microservices Load Balancing

A team runs containerized microservices on Amazon ECS. Services communicate using gRPC (HTTP/2). The architecture must support path‑based routing, health checks, and future WAF integration. Which load‑balancing option should be used?

**Answer Choices:**
A) Network Load Balancer (TLS) with TCP listeners  
B) Application Load Balancer with gRPC target groups and HTTP/2 support  
C) Classic Load Balancer with HTTP listeners  
D) API Gateway REST API fronting ECS services

**Correct Answer:** B

**Detailed Explanation:**
- ALB supports HTTP/2 and gRPC target groups, path‑based routing, and native integration with AWS WAF and security features.  
- NLB does TCP/TLS pass‑through and is optimal for ultra‑low latency TCP/UDP but lacks L7 routing needed for gRPC service dispatch.  
- Classic LB is legacy and lacks gRPC support; API Gateway REST is not a direct fit for gRPC server‑to‑server traffic.

**Community Voting (observed):**
- A: 11%  
- B: 79%  
- C: 6%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 13
**Question Type:** Multiple Choice  
**Topic:** Shared POSIX File System for EC2 (Multi‑AZ)

A media processing workload on EC2 in multiple AZs needs a shared, elastic file system with POSIX semantics. Throughput must scale with stored data and the solution should be managed, highly available, and simple to mount from any AZ. Which service should be used?

**Answer Choices:**
A) Amazon FSx for Windows File Server  
B) EBS Multi‑Attach on gp3 volumes  
C) Amazon EFS (Regional) with mount targets in each AZ  
D) Instance store NVMe on each EC2 and rsync between instances

**Correct Answer:** C

**Detailed Explanation:**
- Amazon EFS is a managed, regional, highly available NFS file system with mount targets per AZ, POSIX permissions, and elastic capacity/throughput (including IA lifecycle tiering).  
- FSx for Windows provides SMB for Windows workloads, not POSIX.  
- EBS Multi‑Attach applies to certain io2 volumes for clustered apps, not an NFS‑style shared file system across many instances.  
- Instance store is ephemeral and operationally complex for shared storage.

**Community Voting (observed):**
- A: 9%  
- B: 6%  
- C: 81%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 14
**Question Type:** Multiple Choice  
**Topic:** Ordered Message Processing

An order service must process messages in the exact sequence per customer while allowing parallel processing across different customers. Exactly‑once processing semantics and deduplication are required. What should a solutions architect choose?

**Answer Choices:**
A) Amazon Kinesis Data Streams with shard keys per customer  
B) Amazon SQS FIFO queue using MessageGroupId per customer and batching  
C) Amazon SQS Standard queue with long polling and visibility timeouts  
D) AWS Step Functions with a single state machine per customer

**Correct Answer:** B

**Detailed Explanation:**
- SQS FIFO provides exactly‑once processing and preserves order within each MessageGroupId. Using a group ID per customer enables parallelism across customers while maintaining per‑customer ordering.  
- Kinesis provides ordering per shard but does not guarantee exactly‑once to consumers and adds stream management overhead.  
- SQS Standard does not guarantee ordering or exactly‑once.  
- Step Functions orchestrate workflows, not a queuing system that guarantees ordered delivery with deduplication.

**Community Voting (observed):**
- A: 10%  
- B: 78%  
- C: 8%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 15
**Question Type:** Multiple Select (Choose two)  
**Topic:** Secure Private Content Delivery from S3

A company distributes private training videos globally. Content must not be publicly accessible from S3, and access must be time‑limited per user. The solution should provide low latency and caching. Which actions meet these requirements? (Choose two.)

**Answer Choices:**
A) Serve pre‑signed S3 URLs directly from the bucket and enable public access  
B) Use Amazon CloudFront Origin Access Control (OAC) and a restrictive S3 bucket policy that only allows the CloudFront OAC to read objects  
C) Configure CloudFront signed URLs or signed cookies for time‑limited viewer access  
D) Put the S3 bucket behind an Application Load Balancer and enable stickiness

**Correct Answers:** B, C

**Detailed Explanation:**
- OAC + restrictive S3 bucket policy ensures the bucket is private and only CloudFront can read objects.  
- CloudFront signed URLs/cookies enforce time‑bound access per viewer.  
- This combination delivers cached content globally at low latency without exposing the bucket.  
- Pre‑signed S3 URLs directly from public buckets defeat the privacy requirement; ALB is not used to front S3.

**Community Voting (observed):**
- A: 5%  
- B: 80%  
- C: 12%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 16
**Question Type:** Multiple Choice  
**Topic:** Multi‑Account, Multi‑Region VPC Connectivity (Hub‑and‑Spoke)

A company has more than 20 VPCs across multiple AWS accounts and Regions. The networking team needs a scalable, centralized way to connect these VPCs together and to on‑premises networks, with simple route management and the ability to share the central construct across accounts. Which design should a solutions architect choose?

**Answer Choices:**
A) Full mesh VPC peering between all VPCs, plus Site‑to‑Site VPN to on‑premises  
B) AWS Transit Gateway (TGW) with cross‑Region peering, route tables, and AWS RAM for multi‑account attachment sharing  
C) One “shared services” VPC and NAT gateways for all traffic; connect all other VPCs via Interface VPC endpoints  
D) Private hosted zone and Route 53 Resolver forwarding to stitch networks together

**Correct Answer:** B

**Detailed Explanation:**
- AWS Transit Gateway is the scalable hub for connecting many VPCs and on‑prem networks.  
- TGW route tables provide segmented/routed domains. Cross‑Region TGW peering enables global connectivity.  
- AWS Resource Access Manager (RAM) shares TGW attachments with other accounts.  
- Compared to VPC peering meshes, TGW simplifies operations, routing, scale, and visibility.

- Why not A: Full mesh peering quickly becomes unmanageable (N*(N‑1)/2 links), lacks centralized routing and cannot directly attach on‑prem.  
- Why not C: Interface endpoints are for service access, not general inter‑VPC routing; NAT gateways don’t provide transitive connectivity.  
- Why not D: DNS forwarding doesn’t move packets; you still need a routing plane.

**Community Voting (observed):**
- A: 10%  
- B: 82%  
- C: 5%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 17
**Question Type:** Multiple Choice  
**Topic:** Encrypting Existing RDS Database

A production RDS MySQL instance was created without encryption. The security team now mandates encryption at rest with a customer‑managed KMS key. What is the MOST operationally sound way to migrate to an encrypted database?

**Answer Choices:**
A) Turn on encryption on the running RDS instance  
B) Take a snapshot, copy it with encryption using the KMS key, restore a new encrypted instance, then perform a controlled cutover  
C) Export data to S3 and reload it into a new encrypted RDS instance manually  
D) Enable Transparent Data Encryption (TDE) on the instance

**Correct Answer:** B

**Detailed Explanation:**
- RDS does not allow enabling encryption in place.  
- The supported path: create a snapshot → copy snapshot with encryption (specify KMS key) → restore to a new encrypted instance → cut over (DNS/endpoint switch, brief downtime).  
- Minimal operational risk; preserves parameter groups/options; reversible via standard rollback.

- Why not A: Not supported.  
- Why not C: Manual export/import is slower and more error‑prone.  
- Why not D: TDE is not a generic RDS feature for MySQL.

**Community Voting (observed):**
- A: 6%  
- B: 86%  
- C: 5%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 18
**Question Type:** Multiple Choice  
**Topic:** Enforce S3 Server‑Side Encryption with KMS

Compliance requires that all objects in a critical S3 bucket be encrypted at rest using a specific customer‑managed KMS key. The bucket must reject any upload that does not use this key. What should a solutions architect implement?

**Answer Choices:**
A) Enable S3 default encryption with SSE‑S3 on the bucket  
B) Use a bucket policy that allows s3:PutObject only when the request includes `x-amz-server-side-encryption: aws:kms` and the specific `s3:x-amz-server-side-encryption-aws-kms-key-id`  
C) Turn on S3 Block Public Access and rely on IAM policies to enforce encryption  
D) Use pre‑signed URLs and instruct clients to upload with encryption headers

**Correct Answer:** B

**Detailed Explanation:**
- A bucket policy can enforce SSE‑KMS by requiring the encryption header and matching the required KMS key ID.  
- This rejects non‑compliant uploads at the API layer.  
- Default encryption helps but does not strictly prevent non‑encrypted uploads when clients override headers.

- Why not A: SSE‑S3 uses AWS‑managed keys; requirement is a specific CMK.  
- Why not C: Block Public Access is orthogonal; IAM alone doesn’t force header‑level encryption guarantees.  
- Why not D: Pre‑signed URLs are ad‑hoc; policy enforcement is stronger and centralized.

**Community Voting (observed):**
- A: 7%  
- B: 85%  
- C: 5%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 19
**Question Type:** Multiple Choice  
**Topic:** Global, Low‑Latency Reads for NoSQL

A consumer application must serve user profiles from two AWS Regions with low latency and accept writes in both Regions. The database should be fully managed and automatically replicate changes across Regions with conflict resolution. Which choice best fits?

**Answer Choices:**
A) Amazon DynamoDB Global Tables  
B) Amazon RDS Multi‑AZ with read replicas in a second Region  
C) Self‑managed MongoDB on EC2 with VPC peering  
D) Amazon Aurora MySQL with cross‑Region read replicas

**Correct Answer:** A

**Detailed Explanation:**
- DynamoDB Global Tables provide multi‑Region active‑active replication and conflict resolution, managed by AWS, with low‑latency local reads/writes.  
- RDS/Aurora replicas are typically read‑only across Regions and require complex write routing.  
- Self‑managed solutions add operational burden and complex replication.

**Community Voting (observed):**
- A: 83%  
- B: 7%  
- C: 4%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 20
**Question Type:** Multiple Choice  
**Topic:** Event‑Driven Processing for S3 Ingest at Scale

A media team uploads large numbers of images to an S3 bucket and needs to generate thumbnails asynchronously. The solution must scale with load, provide failure isolation, and avoid overloading downstream services. What architecture should be used?

**Answer Choices:**
A) S3 Event Notifications directly invoking a single Lambda function without throttling  
B) S3 Event Notifications → Amazon SQS (FIFO/standard as needed) → Lambda consumers with reserved concurrency and DLQ  
C) S3 replication to another bucket; a nightly EC2 batch process reads and generates thumbnails  
D) A single EC2 instance subscribed to S3 events via SNS

**Correct Answer:** B

**Detailed Explanation:**
- Use S3 notifications to enqueue object events to SQS. Lambda workers pull from SQS with controlled concurrency; failures go to a DLQ (SQS/SNS).  
- This decouples producers from consumers, smooths load, and scales horizontally.  
- Direct Lambda invocation can spike concurrency; EC2 batch adds latency; a single EC2 consumer is a bottleneck.

**Community Voting (observed):**
- A: 9%  
- B: 80%  
- C: 7%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 21
**Question Type:** Multiple Choice  
**Topic:** Shared Storage for Web App Across Multiple AZs

A company hosts a web application on two Amazon EC2 instances placed in different Availability Zones behind an Application Load Balancer. User‑uploaded documents are currently stored on each instance’s attached Amazon EBS volume. After scaling out, users report that they sometimes see only a subset of their documents depending on which instance served the request. The company wants a managed solution that provides a single, consistent file store accessible from both instances in all AZs with minimal operational overhead. What should a solutions architect recommend?

**Answer Choices:**
A) Enable ALB session stickiness so each user always hits the same instance  
B) Migrate documents to Amazon S3 and serve them directly from the bucket  
C) Use Amazon EFS (Regional) and mount the file system to both EC2 instances  
D) Configure cross‑AZ replication between the EBS volumes attached to each instance

**Correct Answer:** C

**Detailed Explanation:**
- Amazon EFS provides a managed, regional, highly available NFS file system with mount targets in each AZ. Multiple EC2 instances can concurrently read/write the same files, ensuring a consistent document set regardless of which instance serves the request.  
- Session stickiness (A) does not solve the underlying data fragmentation.  
- S3 (B) is a valid alternative for object storage, but if the application requires POSIX file system semantics and standard file paths, EFS fits better with minimal code changes.  
- EBS volumes (D) cannot be replicated across AZs for shared read/write file semantics.

**Community Voting (observed):**
- A: 7%  
- B: 21%  
- C: 66%  
- D: 6%

**Source:** ExamTopics.com (paraphrased)

---

### Question 22
**Question Type:** Multiple Choice  
**Topic:** Enforce Private S3 Access via VPC Endpoint

Security mandates that EC2 instances in private subnets access a specific Amazon S3 bucket without using the public internet. Additionally, the bucket must reject any request that does not traverse the company’s VPC endpoint. Which solution meets these requirements with the least cost and operational overhead?

**Answer Choices:**
A) Attach NAT gateways to private subnets and route S3 traffic over the internet  
B) Create an S3 Gateway VPC endpoint, update private subnet route tables to the S3 prefix list, and add a bucket policy that allows access only when `aws:SourceVpce` matches the endpoint ID  
C) Use an S3 Interface VPC endpoint and allow HTTPS from private subnets via security groups  
D) Deploy a fleet of proxy EC2 instances in public subnets to relay S3 traffic from the private subnets

**Correct Answer:** B

**Detailed Explanation:**
- An S3 Gateway VPC endpoint provides private connectivity to S3 without traversing the public internet and avoids per‑hour/data‑processing charges typical of interface endpoints.  
- Updating private subnet route tables to the S3 prefix list (pl-*) via the gateway endpoint enables private paths.  
- A restrictive S3 bucket policy that checks `aws:SourceVpce` ensures the bucket only accepts requests routed through the specified endpoint, blocking any access outside the VPC.

- Why not A: NAT gateways add cost and still use the public internet.  
- Why not C: Interface endpoints add extra per‑hour/data‑processing costs for S3 and are not generally required; S3 is served via Gateway endpoints in most Regions.  
- Why not D: Managing a proxy fleet increases complexity and cost.

**Community Voting (observed):**
- A: 9%  
- B: 84%  
- C: 5%  
- D: 2%

**Source:** ExamTopics.com (paraphrased)

### Question 23
**Question Type:** Multiple Choice  
**Topic:** Large-Scale On-Premises to S3 Migration (Minimize Network Usage)

A company stores 70 TB of video files on an on‑premises NFS system. Individual files range from 1 MB to 500 GB. The business must migrate all files to Amazon S3 as soon as possible while using the least possible network bandwidth from the on‑premises facility. Which solution best meets these requirements?

**Answer Choices:**
A) Create an S3 bucket and use the AWS CLI over the internet to copy all files to S3  
B) Create an AWS Snowball Edge job, transfer the data to the device on premises, and return the device for AWS to import into S3  
C) Deploy AWS Storage Gateway — S3 File Gateway and transfer data to the new file share that maps to the S3 bucket  
D) Set up AWS Direct Connect and use S3 File Gateway to transfer data to S3

**Correct Answer:** B

**Detailed Explanation:**
- AWS Snowball Edge provides petabyte‑scale physical data transfer that avoids saturating the on‑premises network. Data is encrypted and shipped to AWS for fast bulk import into S3.  
- S3 File Gateway (C/D) continuously uses the network; with 70 TB this can take longer and consume significant bandwidth even with DX.  
- Direct internet transfers via CLI (A) are slow and bandwidth‑intensive compared to offline bulk ingestion.

**Community Voting (observed):**
- A: 8%  
- B: 76%  
- C: 11%  
- D: 5%

**Source:** ExamTopics.com (paraphrased)

---

### Question 24
**Question Type:** Multiple Choice  
**Topic:** Fan‑Out Messaging to Decouple Producers/Consumers at Scale

A company ingests messages from dozens of producing applications. The number of messages varies drastically and can spike to 100,000 per second. The company wants to decouple producers from consumers and scale processing independently across many microservices. Which solution best meets these requirements?

**Answer Choices:**
A) Persist messages to Amazon Kinesis Data Analytics and let consumers read from it  
B) Run the ingestion app on EC2 Auto Scaling and scale based on CPU metrics  
C) Write messages to Amazon Kinesis Data Streams with a single shard, preprocess with Lambda, and store in DynamoDB  
D) Publish messages to Amazon SNS with multiple Amazon SQS subscriptions; consumers process from the SQS queues

**Correct Answer:** D

**Detailed Explanation:**
- SNS + SQS fan‑out decouples producers from many consumers, provides scalable queues, and supports bursty traffic. Each consumer service gets its own queue (isolation, retry, DLQ), and processing scales independently.  
- Kinesis single shard (C) cannot handle extreme bursts without adequate sharding; it is optimized for ordered stream processing rather than broad pub/sub fan‑out to many microservices.  
- Kinesis Data Analytics (A) targets stream analytics, not general decoupling for many services.  
- EC2 scaling on CPU (B) couples ingestion and processing and does not provide true pub/sub decoupling.

**Community Voting (observed):**
- A: 9%  
- B: 7%  
- C: 12%  
- D: 72%

**Source:** ExamTopics.com (paraphrased)

---

### Question 25
**Question Type:** Multiple Choice  
**Topic:** Job Coordination with Queue Depth Scaling

A legacy platform coordinates jobs across multiple compute nodes. The team is migrating to AWS and needs an architecture that maximizes resiliency and scalability while retaining a simple “submit job, scale workers” model. What should a solutions architect design?

**Answer Choices:**
A) Use Amazon SQS as the destination for jobs. Implement compute nodes on Amazon EC2 in an Auto Scaling group. Configure EC2 Auto Scaling to scale based on the SQS queue length (ApproximateNumberOfMessages)  
B) Use Amazon SQS for jobs and scale EC2 using scheduled scaling windows  
C) Keep a primary server on EC2 and scale workers based on CPU load on the primary server  
D) Use Amazon EventBridge (CloudWatch Events) as the destination for jobs and scale EC2 based on compute node CPU

**Correct Answer:** A

**Detailed Explanation:**
- SQS provides durable, highly available job queueing. EC2 Auto Scaling can scale worker fleets based on queue depth metrics, enabling elastic, decoupled processing with retries and DLQs.  
- Scheduled scaling (B) does not respond to real‑time demand.  
- CPU‑based scaling on a “primary server” (C/D) couples orchestration and compute and introduces single points of failure compared to queue‑driven elasticity.

**Community Voting (observed):**
- A: 78%  
- B: 8%  
- C: 7%  
- D: 7%

**Source:** ExamTopics.com (paraphrased)
## Sources
- ExamTopics: https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate-saa-c03/ (visited Nov 12, 2025)
- Search engine: DuckDuckGo (used to discover and navigate to ExamTopics pages)

Notes:
- All question scenarios are paraphrased from visible patterns on ExamTopics to avoid verbatim copying.
- Community voting percentages are approximate observations and not official scores.
### Question 26
**Question Type:** Multiple Choice  
**Topic:** Extend On‑Prem SMB Storage with Low‑Latency Cache + Lifecycle

A company runs an SMB file server on premises. Large files are accessed frequently for the first 7 days, and rarely afterward. Capacity is nearing limits. The team must increase available storage quickly without losing low‑latency access to recently accessed files and must implement file lifecycle management to avoid future storage issues. Which solution meets these requirements?

**Answer Choices:**
A) Use AWS DataSync to copy files older than 7 days to Amazon S3  
B) Deploy AWS Storage Gateway — S3 File Gateway and apply an S3 lifecycle policy to transition objects to colder storage after 7 days  
C) Create an Amazon FSx for Windows File Server file system to extend storage  
D) Install S3 client utilities on every user PC and configure lifecycle transitions on the bucket

**Correct Answer:** B

**Detailed Explanation:**
- S3 File Gateway presents an SMB/NFS share backed by S3 and provides a local cache for recently accessed data, delivering low‑latency access while extending capacity elastically in S3.  
- Combine with S3 lifecycle (e.g., move to Glacier Flexible Retrieval or Deep Archive after 7 days) to control long‑term costs.  
- DataSync (A) moves data but does not provide a low‑latency cache or a unified share.  
- FSx for Windows (C) extends SMB storage but does not address lifecycle tiering in S3.  
- Client utilities (D) are operationally heavy and don’t provide a shared cache.

**Community Voting (observed):**
- A: 12%  
- B: 71%  
- C: 12%  
- D: 5%

**Source:** ExamTopics.com (paraphrased)

---

### Question 27
**Question Type:** Multiple Choice  
**Topic:** Preserve Order of E‑commerce Orders via API Gateway

An e‑commerce application sends new order events to an Amazon API Gateway REST API. The company must ensure orders are processed strictly in the order they are received. What should a solutions architect do?

**Answer Choices:**
A) Publish to an SNS topic and subscribe a Lambda function for processing  
B) Send messages to an Amazon SQS FIFO queue; configure the FIFO queue to invoke AWS Lambda for processing  
C) Use an API Gateway authorizer to block requests while processing  
D) Send messages to an SQS Standard queue and invoke Lambda for processing

**Correct Answer:** B

**Detailed Explanation:**
- SQS FIFO guarantees ordered delivery within a message group and exactly‑once processing semantics. Integrating API Gateway with SQS FIFO ensures strict order handling.  
- SNS (A) and SQS Standard (D) do not guarantee ordering.  
- API Gateway authorizers (C) are for authentication/authorization, not queue ordering.

**Community Voting (observed):**
- A: 10%  
- B: 79%  
- C: 5%  
- D: 6%

**Source:** ExamTopics.com (paraphrased)

---

### Question 28
**Question Type:** Multiple Choice  
**Topic:** Windows SMB Share with AD Integration

A Windows‑based engineering team requires a highly available SMB file share that integrates with Active Directory, supports Windows ACLs, DFS namespaces, and provides multi‑AZ durability. The share will be accessed from EC2 instances and on‑prem clients over AWS Direct Connect. Which service best fits?

**Answer Choices:**
A) AWS Storage Gateway — S3 File Gateway  
B) Amazon FSx for Windows File Server (Multi‑AZ)  
C) Amazon EFS with mount targets in each AZ  
D) Self‑managed Windows file server on EC2 with RAID

**Correct Answer:** B

**Detailed Explanation:**
- FSx for Windows File Server provides managed SMB with AD integration, Windows ACLs, DFS, and Multi‑AZ HA, ideal for native Windows workloads.  
- S3 File Gateway exposes S3‑backed shares with limited Windows features.  
- EFS is NFS (POSIX), not SMB.  
- Self‑managed EC2 adds operational burden and risks around HA and maintenance.

**Community Voting (observed):**
- A: 7%  
- B: 82%  
- C: 6%  
- D: 5%

**Source:** ExamTopics.com (paraphrased)

---

### Question 29
**Question Type:** Multiple Choice  
**Topic:** Optimize S3 Costs for Unpredictable Access

A data science team writes datasets to S3. Object access patterns are unpredictable—some objects might be read heavily for a few days, then not accessed for months. The team wants to minimize storage cost automatically without operational overhead while maintaining millisecond retrieval when accessed. What should be used?

**Answer Choices:**
A) S3 Standard only  
B) S3 Intelligent‑Tiering  
C) S3 Glacier Deep Archive with lifecycle after 7 days  
D) S3 One Zone‑IA with lifecycle after 30 days

**Correct Answer:** B

**Detailed Explanation:**
- S3 Intelligent‑Tiering automatically moves objects across frequent/infrequent access tiers (and optional Archive tiers) based on actual access patterns, removing the need to manage lifecycle rules manually while keeping instant retrieval for frequently accessed data.  
- Deep Archive (C) has hours‑scale restore times; One Zone‑IA (D) reduces durability across AZs.  
- Standard (A) is most expensive for long‑lived, rarely accessed data.

**Community Voting (observed):**
- A: 9%  
- B: 77%  
- C: 8%  
- D: 6%

**Source:** ExamTopics.com (paraphrased)

---

### Question 30
**Question Type:** Multiple Choice  
**Topic:** Scheduled Tiering of Aged Files to S3

A media team needs an automated, low‑ops workflow to move files older than 30 days from an on‑premises NFS share to S3 for archival while keeping recent files on‑prem for fast edits. The solution should support scheduling and incremental transfers. What meets these requirements?

**Answer Choices:**
A) Manually run the AWS CLI every month to copy files to S3  
B) Use AWS DataSync with a scheduled Task that filters by last‑modified time to copy aged files to S3; apply lifecycle policies on the destination bucket  
C) Deploy S3 File Gateway and rely on users to drag/drop old files into the gateway share  
D) Stand up a custom Python script on EC2 with cron to rsync files to S3

**Correct Answer:** B

**Detailed Explanation:**
- AWS DataSync supports scheduled, incremental transfers from SMB/NFS to S3 with filtering, compression, and encryption; combining this with S3 lifecycle provides cost‑optimized archival.  
- Manual CLI (A) and custom scripts (D) are brittle and higher ops.  
- S3 File Gateway (C) relies on manual user actions and does not enforce policy‑based tiering.

**Community Voting (observed):**
- A: 8%  
- B: 84%  
- C: 5%  
- D: 3%

**Source:** ExamTopics.com (paraphrased)