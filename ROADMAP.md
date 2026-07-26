# 60-Week Roadmap

This roadmap moves from bytes and sockets to a small AI cloud platform. Each row
is one Sunday build. Every four weeks form a learn → extend → consolidate cycle.

Progress is tracked in [PROGRESS.md](PROGRESS.md).

## Phase 1 — HTTP and networking

**Weeks 1–4 · Planned location:** `01-networking/http-server/`

| Week | Build | Required outcome |
|---:|---|---|
| 1 | TCP server and HTTP response | Accept a connection, read bytes, and return `200 OK` |
| 2 | HTTP request parser and router | Parse method, path, headers, and body |
| 3 | File server, POST, and concurrency | Serve files, accept POST, and handle multiple clients |
| 4 | Logging, tests, and benchmark | Complete the first HTTP server |

**Gate 1**

- Explain when a TCP connection opens and closes.
- Explain the roles of `\r\n` and `Content-Length`.
- Describe how a router maps a URL to a handler.
- Demonstrate what happens when two clients connect concurrently.

## Phase 2 — Gateway, proxy, and traffic control

**Weeks 5–8 · Planned location:** `02-gateway/`

| Week | Build | Required outcome |
|---:|---|---|
| 5 | Reverse proxy | Forward a request to one backend |
| 6 | Load balancer | Distribute requests across multiple backends |
| 7 | Rate limiter and health check | Limit traffic and exclude dead backends |
| 8 | Mini API gateway | Routing, logs, retries, and load balancing |

**Gate 2**

- Two backends both receive traffic.
- Requests still succeed when one backend dies.
- Excess requests receive `429`.
- Every request has a request ID and recorded duration.

## Phase 3 — Storage, cache, and database internals

**Weeks 9–12 · Planned location:** `03-storage/`

| Week | Build | Required outcome |
|---:|---|---|
| 9 | In-memory key-value store | `SET`, `GET`, `DELETE`, and `EXISTS` |
| 10 | Persistence | Write-ahead log and snapshot |
| 11 | TTL and eviction | Expiring keys and a memory limit |
| 12 | Mini Redis server | RESP parser and TCP clients |

**Gate 3**

- Data survives a restart.
- Keys expire automatically.
- Two clients can connect concurrently.
- A failure path covers a corrupted log.
- Explain the difference between memory, disk, cache, and database.

### Milestone 1

```text
HTTP server + gateway + mini Redis
```

## Phase 4 — Structured backend development

**Weeks 13–16 · Planned location:** `04-backend/project-service/`

| Week | Build | Required outcome |
|---:|---|---|
| 13 | FastAPI service | API validation and error handling |
| 14 | PostgreSQL | Schema, queries, migrations, and transactions |
| 15 | Authentication | Users, password hashing, and access tokens |
| 16 | Integrated backend | API + PostgreSQL + cache + gateway |

**Gate 4**

- Real data is stored in PostgreSQL.
- Authentication, unit tests, and integration tests exist.
- At least one query is cached.
- The service runs behind the gateway.
- No password or secret is stored in source code.

## Phase 5 — Queues, reliability, and observability

**Weeks 17–24 · Planned location:** `05-reliability/`

| Week | Build | Required outcome |
|---:|---|---|
| 17 | Task queue | A producer submits jobs and a worker consumes them |
| 18 | Retry and idempotency | Failed jobs retry without duplicate effects |
| 19 | Scheduler and dead-letter queue | Scheduled jobs and retained failures |
| 20 | Document-processing pipeline | Upload → queue → process → result |
| 21 | Structured logging | JSON logs and correlation IDs |
| 22 | Metrics | Request count, latency, and error rate |
| 23 | Distributed tracing | Follow one request across services |
| 24 | Docker Compose and CI | Start the complete stack with one command |

**Gate 5**

- Identify which services are running.
- Find failed jobs and their retry counts.
- See where a request spends its time.
- Read average latency and error rate.
- Start the integrated stack by following its documentation.

### Milestone 2

```text
Backend + PostgreSQL + queue + observability + Docker
```

## Phase 6 — AI from foundations

**Weeks 25–32 · Planned location:** `06-ai-foundations/`

| Week | Build | Required outcome |
|---:|---|---|
| 25 | Scalar autograd engine | `Value`, operation graph, and backward pass |
| 26 | Small tensor system and MLP | Layers, activations, and optimizer |
| 27 | Tokenizer | Character tokenizer and simple BPE |
| 28 | Character language model | Predict the next character |
| 29 | Self-attention | Query, key, value, and causal mask |
| 30 | Mini Transformer | Embedding, attention, MLP, and residual paths |
| 31 | Training system | Dataset, batching, checkpoints, and evaluation |
| 32 | Model-serving API | Load a model, run inference, and stream output |

**Gate 6**

- Explain a computational graph and backward pass.
- Distinguish a token from a word.
- Explain the weighted combination produced by attention.
- Explain how a causal mask prevents looking into the future.
- Distinguish training from inference.

The model must remain small enough for personal hardware. Explanatory value is
more important than generated-text quality.

## Phase 7 — Applied AI and RAG

**Weeks 33–36 · Planned location:** `07-ai-systems/rag-platform/`

| Week | Build | Required outcome |
|---:|---|---|
| 33 | Embeddings pipeline | Convert text into vectors |
| 34 | Vector search | Similarity search and metadata filtering |
| 35 | RAG service | Ingest, chunk, retrieve, and generate |
| 36 | RAG evaluation | Retrieval metrics, answer quality, and latency |

**Gate 7**

- Answers include source references.
- An evaluation question set exists.
- At least two chunk sizes are compared.
- Retrieval failures are recorded.
- Identify whether embedding, retrieval, or generation is the bottleneck.

### Milestone 3

```text
Mini Transformer + model API + evaluated RAG system
```

## Phase 8 — Containers and Linux primitives

**Weeks 37–40 · Planned location:** `08-cloud-primitives/container-runtime/`

| Week | Build | Required outcome |
|---:|---|---|
| 37 | Process isolation | Processes, environments, and namespaces |
| 38 | Resource limits | CPU and memory limits with cgroups |
| 39 | Root filesystem and image layers | Build a filesystem for a container |
| 40 | Mini container runtime | `run`, `stop`, `list`, and `logs` |

**Gate 8**

- Create an isolated process.
- Limit memory.
- Mount a separate filesystem.
- Capture stdout/stderr and retain state.
- Clean up resources after the process exits.

The custom runtime is for learning only. It must not run untrusted
Internet-facing workloads.

## Phase 9 — Orchestration primitives

**Weeks 41–48 · Planned location:** `08-cloud-primitives/`

| Week | Build | Required outcome |
|---:|---|---|
| 41 | Mini image registry | Push, pull, manifests, and blobs |
| 42 | Deployment agent | Receive a command and run a container |
| 43 | Service discovery | Find addresses for healthy services |
| 44 | Scheduler | Select a node using CPU and RAM |
| 45 | Health check and restart | Recover a dead process automatically |
| 46 | Rolling deployment | Replace a version without stopping everything |
| 47 | Config and secrets | Inject configuration at runtime |
| 48 | Persistent storage | Volumes, backup, and a two-node demo |

**Gate 9**

- A control plane deploys a container to one of two local nodes or VMs.
- An agent restarts a dead container.
- A rolling deployment replaces the old version gradually.
- The system can roll back to an earlier version.

### Milestone 4

```text
Container runtime + deployment agent + scheduler + recovery
```

## Phase 10 — Kai Cloud capstone

**Weeks 49–60 · Planned location:** `09-capstone/kai-cloud/`

| Week | Build | Required outcome |
|---:|---|---|
| 49 | Control plane and CLI skeleton | The `kai` CLI communicates with the API |
| 50 | User, project, and deployment state | Authentication and project management |
| 51 | End-to-end deployment | CLI → scheduler → agent → container |
| 52 | Routing and domain | Gateway routes to the correct app |
| 53 | Logs dashboard | Browse logs by project and deployment |
| 54 | Metrics and traces dashboard | CPU, RAM, latency, and error rate |
| 55 | AI application template | Template for a model or RAG service |
| 56 | Deploy a RAG service | One-click AI application deployment |
| 57 | Background jobs | Ingestion and indexing workers |
| 58 | Versioning and rollback | Deployment history |
| 59 | Security and load testing | Quotas, validation, and resource limits |
| 60 | Demo, docs, and benchmark | Complete portfolio presentation |

**Gate 10**

- A new user can deploy the demo by following the documentation.
- A web app and a RAG app use the same platform path.
- The dashboard shows health, logs, and basic metrics.
- A failure demo proves restart and rollback.
- Benchmarks, limitations, and trade-offs are explicit.

### Milestone 5

```text
Kai Cloud: deploy and operate an AI/RAG application
```

## Kai Cloud v1 scope

### Required

- Create a user and project.
- Deploy a Docker image.
- Select a node.
- Provide an endpoint.
- Health-check and restart automatically.
- Provide basic logs and metrics.
- Inject environment variables.
- Retain deployment versions and roll back.
- Deploy a RAG template.

### Deliberately excluded

- Billing and multi-region operation.
- A custom TLS implementation.
- A new distributed consensus protocol.
- Production-grade multi-tenant security.
- A distributed database.
- Complex autoscaling.
- A custom GPU scheduler.

## Adjusting the roadmap

The roadmap is a direction, not a hard deadline. If a gate is not satisfied:

1. remain in the current phase;
2. record the blocker and evidence in `PROGRESS.md`;
3. reduce the scope of the next build;
4. move on only when the gate can be explained and demonstrated.

Never make up time by dropping tests, documentation, or the explanation of what
was learned.
