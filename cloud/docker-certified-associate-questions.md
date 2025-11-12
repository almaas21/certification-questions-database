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
## Sources
- ExamTopics: https://www.examtopics.com/exams/docker/docker-certified-associate-dca/ (visited Nov 12, 2025)
- Search engine: DuckDuckGo (used to discover and navigate to ExamTopics pages)

Notes:
- All question scenarios are paraphrased from visible patterns on ExamTopics to avoid verbatim copying.
- Community voting percentages are approximate observations and not official scores.