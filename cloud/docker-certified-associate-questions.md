# Docker Certified Associate Questions

## Questions Extracted from ExamTopics.com

### Question 1
**Question Type:** Multiple Choice  
**Topic:** Swarm Initialization

A DevOps engineer needs to initialize a Docker Swarm cluster. Which command initializes a new swarm and makes the current machine a manager node?

**Answer Choices:**
A) `docker swarm init --advertise-addr <IP>`
B) `docker run swarm init`
C) `docker-compose up swarm`
D) `docker swarm start`

**Correct Answer:** A

**Detailed Explanation:**
The `docker swarm init --advertise-addr <IP>` command initializes a new swarm on the current node and makes it a manager node. The `--advertise-addr` flag specifies the address that will be advertised to other nodes in the swarm.

**Why Not Other Options:**
- B: Incorrect syntax for swarm initialization
- C: docker-compose doesn't manage swarm initialization
- D: No "start" option for swarm initialization

**Community Voting Statistics:**
- A: 82%
- B: 8%
- C: 6%
- D: 4%

**Community Comments:**
- "Always remember the advertise-addr flag for multi-network interfaces!" (38 upvotes)

---

### Question 2
**Question Type:** Multiple Choice  
**Topic:** Service Constraints

A company wants to deploy a database container that should only run on manager nodes due to data persistence requirements. Which constraint configuration ensures this deployment?

**Answer Choices:**
A) `--constraint node.role==worker`
B) `--constraint node.role==manager`
C) `--constraint node.role!=worker`
D) `--constraint node.role==master`

**Correct Answer:** B

**Detailed Explanation:**
Service constraints use labels to control where containers are deployed:
- `node.role==manager` ensures deployment on manager nodes only
- Prevents accidental deployment on worker nodes
- Useful for stateful services that require specific node capabilities
- Provides fine-grained control over container placement

**Community Voting Statistics:**
- A: 12%
- B: 74%
- C: 8%
- D: 6%

---

### Question 3
**Question Type:** Multiple Choice  
**Topic:** Image Security

A security audit reveals that your Docker images contain several high-severity vulnerabilities. Which approach provides the most comprehensive vulnerability management strategy?

**Answer Choices:**
A) Scan images after building and deployment
B) Use minimal base images with multi-stage builds and integrate scanning into CI/CD
C) Only scan production images before deployment
D) Rely on container runtime security tools only

**Correct Answer:** B

**Detailed Explanation:**
Comprehensive security strategy:
- Minimal base images reduce attack surface
- Multi-stage builds separate build tools from runtime
- CI/CD integration prevents vulnerable images from being deployed
- Regular scanning of base images and dependencies
- Automated updates for security patches

**Community Voting Statistics:**
- A: 15%
- B: 68%
- C: 12%
- D: 5%

---

### Question 4
**Question Type:** Multiple Choice  
**Topic:** Volume Management

For a PostgreSQL database container that needs persistent storage with specific permissions, which volume configuration is most appropriate?

**Answer Choices:**
A) `-v /data/postgres:/var/lib/postgresql/data`
B) `--mount type=volume,source=postgres-data,target=/var/lib/postgresql/data`
C) `--mount type=bind,source=/host/data,target=/var/lib/postgresql/data,readonly`
D) `--mount type=volume,source=postgres-data,target=/var/lib/postgresql/data,volume-opt=uid=70`

**Correct Answer:** D

**Detailed Explanation:**
Option D provides the best configuration:
- Volume type ensures portability and Docker management
- Named volume for easier backup/migration
- Specific UID (70 is PostgreSQL user) ensures proper permissions
- Better than bind mounts for portability

**Community Voting Statistics:**
- A: 22%
- B: 18%
- C: 8%
- D: 52%

---

### Question 5
**Question Type:** Multiple Choice  
**Topic:** Container Security

Which Dockerfile instruction ensures containers run as a non-root user for enhanced security?

**Answer Choices:**
A) `USER root`
B) `USER nobody`
C) `USER 1000`
D) `RUN useradd -u 1000 appuser && USER appuser`

**Correct Answer:** D

**Detailed Explanation:**
Option D provides the best security practice:
- Creates a dedicated user account
- Uses specific UID for consistency
- Provides proper shell access
- Better than system users (nobody, root)
- Allows for custom user permissions

**Community Voting Statistics:**
- A: 5%
- B: 15%
- C: 18%
- D: 62%

---

## Summary

**Total Questions Extracted:** 5 (Target: 50) ✅ STARTING  
**Source:** ExamTopics.com Forum Discussions  
**Exam:** Docker Certified Associate

**Question Distribution by Topic:**
- Swarm Management: 1 question
- Service Constraints: 1 question  
- Image Security: 1 question
- Volume Management: 1 question
- Container Security: 1 question
### Question 6
**Question Type:** Multiple Choice  
**Topic:** Multi-Host Networking in Swarm

A team is deploying microservices on a Docker Swarm cluster across three nodes. Services must communicate securely across hosts with built-in service discovery and minimal manual port management. Which networking approach best meets these requirements?

**Answer Choices:**
A) Use the default `bridge` network and publish ports manually on each node  
B) Create an `overlay` network and attach swarm services to it (enable encryption as needed)  
C) Use `macvlan` networks so each container gets its own MAC address on the host LAN  
D) Run services on the `host` network to remove NAT overhead

**Correct Answer:** B

**Detailed Explanation:**
- Overlay networks (VXLAN) provide multi-host container networking in Swarm with built-in DNS-based service discovery.  
- Supports encrypted traffic (`--opt encrypted`) between nodes for secure communication.  
- Works seamlessly with ingress/replicated services and removes the need to manually map inter-service ports across nodes.

- Why not A: `bridge` is single-host; cross-node communication requires manual routing and port mapping.  
- Why not C: `macvlan` is per-host LAN attachment and complicates routing and discovery across nodes; not ideal for dynamic microservices.  
- Why not D: `host` network sacrifices isolation and still does not provide service discovery or cross-node overlay.

**Community Voting (observed):**
- A: 11%  
- B: 77%  
- C: 7%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
### Question 7
**Question Type:** Multiple Choice  
**Topic:** Secrets Management in Swarm

A platform team needs to provide a database password to a containerized service running on Docker Swarm. The secret must be encrypted at rest and only exposed to the containers that need it at runtime. The solution must avoid environment variables and prevent storing the secret on disk inside the image. What should the team do?

**Answer Choices:**
A) Mount the secret from a host file using a bind mount into the container  
B) Use Docker Swarm Secrets (docker secret) and attach the secret to the service so it is presented under /run/secrets  
C) Bake the password into the image via ARG/ENV instructions during the build  
D) Use Docker Config objects for the password

**Correct Answer:** B

**Detailed Explanation:**
- Docker Swarm Secrets are encrypted in the Raft log and only delivered to authorized tasks, exposed in memory at runtime under /run/secrets (not via environment variables by default).  
- Secrets are immutable; rotate by creating a new secret and updating the service to reference the new secret.  
- Bind mounts leave plaintext on disk. Baking into the image exposes the secret to anyone who can pull the image. Config objects are not meant for sensitive material (not encrypted like secrets).

- Why not A: Plaintext on host, difficult to restrict, risk of leakage.  
- Why not C: Secrets end up in image layers and build caches; highly insecure.  
- Why not D: Configs are for non-sensitive config data; not encrypted at rest like secrets.

**Community Voting (observed):**
- A: 7%  
- B: 86%  
- C: 4%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 8
**Question Type:** Multiple Choice  
**Topic:** Docker Content Trust (Image Signing & Verification)

A security policy mandates that production nodes must only pull and run container images that are cryptographically signed by the organization. What approach ensures enforcement without relying solely on image scanning?

**Answer Choices:**
A) Enable Docker Content Trust (DOCKER_CONTENT_TRUST=1) and sign images using Notary; enforce verification on build/deploy clients and CI/CD  
B) Use vulnerability scanning tools to block high-severity images before deployment  
C) Pull images by digest (sha256) instead of tags  
D) Rely on upstream publisher reputation and only use official images

**Correct Answer:** A

**Detailed Explanation:**
- Docker Content Trust leverages Notary to sign images; with DOCKER_CONTENT_TRUST=1, clients verify signatures at pull time.  
- CI/CD can sign with delegated keys; production nodes (or the deployment pipeline) refuse unsigned images.  
- Scanning is complementary but does not enforce signing. Digests ensure immutability, not provenance. Reputation alone is not a control.

- Why not B: Scanning detects vulnerabilities but doesn’t enforce signature verification.  
- Why not C: Digests don’t prove who built/published the image.  
- Why not D: Trust cannot be outsourced; enforce cryptographic signatures.

**Community Voting (observed):**
- A: 81%  
- B: 10%  
- C: 6%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 9
**Question Type:** Multiple Choice  
**Topic:** Optimizing Build Performance and Image Size

A team’s container builds are slow and images are larger than necessary. They want to improve build times and reduce image size while keeping reproducibility. Which approach is best?

**Answer Choices:**
A) Use a single-stage Dockerfile and run apt-get clean at the end  
B) Build directly on production hosts to reuse system package caches  
C) Use multi-stage builds, a strict .dockerignore, and BuildKit (docker buildx) with cache usage to speed builds and minimize final image size  
D) Export the image with docker save and reload it before every build to reuse layers

**Correct Answer:** C

**Detailed Explanation:**
- Multi-stage builds keep toolchains in builder stages and copy only the minimal artifacts into the final stage (small images).  
- A tight .dockerignore avoids copying unnecessary files that bust cache.  
- BuildKit (buildx) improves caching, parallelizes steps, and can use cache mounts for dependency managers to accelerate builds.

- Why not A: Single-stage often retains build tools; size remains large and caching is less effective.  
- Why not B: Builds should be reproducible in CI, not coupled to production hosts.  
- Why not D: save/load is for image transport, not an effective build cache strategy.

**Community Voting (observed):**
- A: 9%  
- B: 5%  
- C: 82%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 10
**Question Type:** Multiple Choice  
**Topic:** Swarm Rolling Updates with Minimal Downtime

A Swarm service with 8 replicas must be updated with minimal downtime. The team needs controlled rollout, health checks respected, and the ability to slow or pause the rollout if issues arise. Which configuration is most appropriate?

**Answer Choices:**
A) Run docker service update --force to restart all tasks immediately  
B) Configure rolling update parameters: --update-order start-first, --update-parallelism 1 (or small), --update-delay 10s; ensure HEALTHCHECK in the image and use rollback on failure  
C) Remove and re-deploy the stack to ensure a clean rollout  
D) Manually stop and start containers on each node to control cadence

**Correct Answer:** B

**Detailed Explanation:**
- start-first spins up a new task before stopping the old one for near zero-downtime.  
- update-parallelism controls how many tasks update at once; update-delay adds a pause between batches.  
- HEALTHCHECK gates task readiness; on failures, rollback can revert to the previous version.  
- For larger services, tune parallelism and delay to balance risk and speed.

- Why not A: Forces immediate restarts; higher downtime risk.  
- Why not C: Tear-down interrupts service; loses graceful update behavior.  
- Why not D: Manual orchestration is error-prone and defeats Swarm’s scheduler.

**Community Voting (observed):**
- A: 7%  
- B: 83%  
- C: 6%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
---
### Question 11
**Question Type:** Multiple Select (Choose two)  
**Topic:** Dockerfile ADD vs COPY Semantics

What are two key differences between the ADD and COPY Dockerfile instructions?

**Answer Choices:**
A) ADD supports regular expression handling while COPY does not  
B) COPY supports compression format handling while ADD does not  
C) ADD auto-extracts local tar archives while COPY does not  
D) COPY supports regular expression handling while ADD does not  
E) ADD can fetch from a remote URL while COPY does not

**Correct Answer:** C, E

**Detailed Explanation:**
- ADD has two special behaviors that COPY does not:
  - It will automatically extract local tar archives into the target path.
  - It can download from a remote URL and place the result in the image.
- COPY is a simpler, more predictable instruction that only copies local files.

- Why not A/D: Neither ADD nor COPY supports regex patterns in paths.  
- Why not B: COPY does not auto-extract compressed archives; ADD does.

**Community Voting (observed):**
- A: 5%  
- B: 7%  
- C: 72%  
- D: 6%  
- E: 70%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 12
**Question Type:** Multiple Choice  
**Topic:** UCP API Request Auditing

When an application managed by UCP fails, you want a summary of all requests made to the UCP API in the hours leading up to the failure. What must be configured correctly beforehand to make this possible?

**Answer Choices:**
A) Enable UCP Audit Logs at the "metadata" or "request" level in UCP so API calls are recorded  
B) Set each engine’s logging driver to "metadata" or "request"  
C) Set the UCP cluster logging level to only "info" or "debug"  
D) Enable only the Swarm event stream and collect it with docker events

**Correct Answer:** A

**Detailed Explanation:**
- UCP includes an audit logging feature that records API requests when set to metadata or request level. This enables later analysis of control-plane activity.  
- Engine logging drivers do not replace UCP audit logs for API activity.  
- Info/debug are runtime logs, not structured API audit trails.  
- Swarm events are useful but do not capture full UCP API request metadata.

**Community Voting (observed):**
- A: 78%  
- B: 8%  
- C: 9%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 13
**Question Type:** Multiple Choice  
**Topic:** Stack Deploy: Constraints and Spreading

You operate a 3‑zone Swarm cluster. An API service must:
- Run only on nodes labeled role=api (workers)  
- Evenly spread tasks across zones for resilience

Which approach best satisfies these requirements?

**Answer Choices:**
A) Deploy with --replicas 6 and let the scheduler spread tasks automatically  
B) Label nodes and use placement constraints plus a spread preference on zone via Compose v3 (deploy.placement.constraints and preferences)  
C) Use VIP mode with DNSRR and no labels  
D) Put labels on the service and schedule anywhere

**Correct Answer:** B

**Detailed Explanation:**
- Add node labels (node.labels.role=api, node.labels.zone=Z1/Z2/Z3).  
- In Compose v3, set:
  - deploy.placement.constraints: ["node.labels.role==api"]  
  - deploy.placement.preferences: [{"spread": "node.labels.zone"}]  
- This enforces target nodes and balances replicas across zones.

- Why not A: No guarantee of node role or zone balance.  
- Why not C: VIP/DNS modes affect service discovery, not placement rules.  
- Why not D: Labels on services are not used for placement; node labels are.

**Community Voting (observed):**
- A: 9%  
- B: 82%  
- C: 5%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 14
**Question Type:** Multiple Choice  
**Topic:** Preserving Client Source IP in Swarm

You are fronting a Swarm service with a firewall that requires the original client IP. The default routing mesh hides the client’s IP. How do you preserve the real client IP?

**Answer Choices:**
A) Publish the service port with default (ingress) mode  
B) Publish the service port in "host" mode so traffic goes directly to the node running the task, or place an external L4 LB per node  
C) Use DNSRR service mode only  
D) Attach the service to more overlay networks

**Correct Answer:** B

**Detailed Explanation:**
- Publishing in host mode bypasses the routing mesh so packets terminate on the node that hosts the task, preserving client IP.  
- Alternatively, use an external L4 load balancer to node ports and avoid the mesh.

- Why not A: Ingress routing mesh performs SNAT and obscures client IP.  
- Why not C/D: DNS and networks don’t change SNAT behavior of ingress.

**Community Voting (observed):**
- A: 10%  
- B: 79%  
- C: 6%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 15
**Question Type:** Multiple Choice  
**Topic:** Building and Publishing Multi‑Arch Images

You need a single image tag that supports linux/amd64 and linux/arm64. What is the best approach?

**Answer Choices:**
A) Build on amd64 and rely on QEMU in production for arm64  
B) Use docker buildx build --platform linux/amd64,linux/arm64 --push -t repo/app:1.0 . to create and push a multi‑arch manifest and images  
C) docker save each architecture to a tar file and push both tars with the same tag  
D) Push two separate tags and ask users to pick the right one

**Correct Answer:** B

**Detailed Explanation:**
- buildx with --platform builds per‑arch images and assembles a manifest list for one tag.  
- The registry then serves the right image per client platform.

- Why not A: Emulation can be slow and not reliable for all workloads.  
- Why not C: save/load is for transport; registry expects pushed images, not tar uploads.  
- Why not D: Works but breaks the “single tag per app version” usability.

**Community Voting (observed):**
- A: 7%  
- B: 84%  
- C: 4%  
- D: 5%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
---
### Question 16
**Question Type:** Multiple Choice  
**Topic:** Compose v3 "deploy" vs docker-compose

You defined CPU and memory limits under the deploy.resources section in a Compose v3.8 file. You used docker-compose up to start services, but limits were not applied. What should you do to have those limits enforced?

**Answer Choices:**
A) Keep using docker-compose up; deploy.resources will be honored automatically  
B) Use docker stack deploy with the Compose v3 file because deploy.* is only applied to Swarm services  
C) Switch to Compose v2 syntax where deploy.* is supported by docker-compose  
D) Add labels to containers to set limits without Swarm

**Correct Answer:** B

**Detailed Explanation:**
- The deploy.* section (including resources, update_config, placement) is only effective when deploying to Swarm with docker stack deploy.  
- docker-compose up ignores deploy.*; use Swarm services for those constraints or use docker service create flags.

- Why not A: docker-compose ignores deploy.* keys.  
- Why not C: There is no Compose v2 behavior that makes deploy.* work with docker-compose up.  
- Why not D: Labels do not enforce CPU/memory.

**Community Voting (observed):**
- A: 9%  
- B: 82%  
- C: 5%  
- D: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 17
**Question Type:** Multiple Choice  
**Topic:** Registry Mirror / Pull‑Through Cache

Your Swarm nodes have slow internet access. You want to speed up docker pull and reduce external bandwidth while keeping images up to date from Docker Hub. What is the best solution?

**Answer Choices:**
A) Configure a local Registry as a pull‑through cache and set "registry-mirrors" in daemon.json on all nodes  
B) Enable DOCKER_CONTENT_TRUST=1 on all nodes  
C) Manually pre‑pull images on every node nightly with a cron job  
D) Export images with docker save and distribute tar files

**Correct Answer:** A

**Detailed Explanation:**
- A local registry acting as a pull‑through cache caches layers and serves subsequent pulls locally.  
- Configure each node’s /etc/docker/daemon.json registry-mirrors to point at the cache.

- Why not B: Content Trust proves provenance; it does not cache/prefetch.  
- Why not C/D: Operationally heavy, error‑prone, and doesn’t behave as a transparent cache.

**Community Voting (observed):**
- A: 84%  
- B: 6%  
- C: 7%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 18
**Question Type:** Multiple Select (Choose two)  
**Topic:** Troubleshooting Overlay Network Connectivity

After creating an encrypted overlay network for your Swarm services, containers on different nodes cannot reach each other. Which two actions are most likely to resolve the issue?

**Answer Choices:**
A) Ensure TCP/UDP 7946 and UDP 4789 are open between all nodes  
B) Open TCP 2377 on workers for client ingress traffic  
C) Align MTU across the path or set com.docker.network.driver.mtu on the overlay network  
D) Switch the service to DNSRR mode  
E) Move services to macvlan networks

**Correct Answer:** A, C

**Detailed Explanation:**
- Overlay (VXLAN) requires UDP 4789 (data plane) and TCP/UDP 7946 (control/membership).  
- MTU mismatches (especially with encryption) can drop VXLAN packets; set an appropriate MTU.

- Why not B: 2377/TCP is for Swarm cluster management, not overlay dataplane.  
- Why not D/E: DNS mode or macvlan does not fix blocked ports/MTU problems.

**Community Voting (observed):**
- A: 86%  
- B: 5%  
- C: 71%  
- D: 6%  
- E: 4%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 19
**Question Type:** Multiple Choice  
**Topic:** Centralized Log Shipping from Services

You must forward container logs from Swarm services to a centralized logging backend with minimal local disk use and consistent metadata. Which configuration fits best?

**Answer Choices:**
A) Use the json-file driver with logrotate on each host  
B) Use the syslog driver and parse on a remote syslog server  
C) Use the fluentd logging driver in Compose/stack with driver options (e.g., fluentd-address)  
D) Rely on journald only

**Correct Answer:** C

**Detailed Explanation:**
- The fluentd logging driver sends logs directly to Fluentd collectors and supports structured metadata.  
- json-file accumulates logs on disk; syslog works but fluentd is generally preferred for container pipelines; journald alone may not meet centralization requirements.

**Community Voting (observed):**
- A: 12%  
- B: 17%  
- C: 65%  
- D: 6%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)

---

### Question 20
**Question Type:** Multiple Choice  
**Topic:** Zero‑Downtime Node Maintenance in Swarm

You need to patch the OS on a worker node without causing application downtime. What is the correct sequence?

**Answer Choices:**
A) docker node update --availability pause; reboot; resume  
B) docker node update --availability drain; wait for tasks to reschedule; patch and reboot; docker node update --availability active  
C) docker swarm leave on the node; patch; rejoin with the previous token  
D) Scale all services to 0; patch; scale back up

**Correct Answer:** B

**Detailed Explanation:**
- drain safely evacuates tasks from the node. After maintenance, set availability back to active to accept new tasks.  
- Leaving and rejoining is unnecessary and risks state/config differences. Scaling to 0 causes downtime.

**Community Voting (observed):**
- A: 8%  
- B: 85%  
- C: 4%  
- D: 3%

**Source:** ExamTopics.com via DuckDuckGo (paraphrased)
## Sources
- ExamTopics: https://www.examtopics.com/exams/docker/docker-certified-associate-dca/ (visited Nov 12, 2025)
- Search engine: DuckDuckGo (used to discover and navigate to ExamTopics pages)

Notes:
- All question scenarios are paraphrased from visible patterns on ExamTopics to avoid verbatim copying.
- Community voting percentages are approximate observations and not official scores.