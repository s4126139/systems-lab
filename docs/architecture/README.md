# Architecture

This directory records stable views of the system as it evolves. It starts with
the destination and gains detailed documents only when a phase produces enough
evidence to make them useful.

## Target system

```text
Developer
   │
   ▼
CLI ─────────► Control Plane API
                    │
                    ├── Project and deployment state
                    ├── Scheduler
                    ├── Service registry
                    └── Job queue
                             │
                             ▼
                     Deployment Agent
                             │
                     Container runtime
                             │
                 ┌───────────┴───────────┐
                 │                       │
              Web app               AI/RAG service
                 │                       │
                 └──────── Gateway ──────┘
                             │
                           Users

Telemetry: logs + metrics + traces
```

## Major responsibilities

| Area | Responsibility | Roadmap origin |
|---|---|---|
| Gateway | Route, balance, rate-limit, and observe requests | Weeks 5–8 |
| Storage | Persist project, deployment, and application state | Weeks 9–16 |
| Reliability | Queue work, retry safely, schedule jobs | Weeks 17–20 |
| Observability | Explain system behavior through telemetry | Weeks 21–24 |
| AI serving | Train small models and expose inference/RAG APIs | Weeks 25–36 |
| Runtime | Isolate processes and control resources | Weeks 37–40 |
| Orchestration | Place, discover, recover, update, and roll back workloads | Weeks 41–48 |
| Control plane | Present one coherent deployment product | Weeks 49–60 |

## Evolution by milestone

### Milestone 1 — Request path

```text
Client → HTTP server → gateway → backend
                         │
                         └── mini Redis
```

The emphasis is bytes, protocols, routing, and basic persistence.

### Milestone 2 — Reliable backend

```text
Client → gateway → API → PostgreSQL
                    │
                    └→ queue → worker

Logs + metrics + traces observe the complete path.
```

The emphasis is service boundaries, reliable asynchronous work, and operational
visibility.

### Milestone 3 — AI system

```text
Documents → ingestion → embeddings → vector index
Question  → retrieval → prompt → model → answer + sources
```

The emphasis is model foundations, retrieval quality, evaluation, and serving.

### Milestone 4 — Workload platform

```text
Control plane → scheduler → deployment agent → container
                    │              │
                    └── registry   └── health/restart
```

The emphasis is isolation, placement, discovery, recovery, and safe updates.

### Milestone 5 — Kai Cloud

All prior paths become one product:

```text
kai deploy → control plane → scheduler → agent → runtime → gateway → users
```

## Architecture documentation policy

- Describe only behavior that exists or a clearly labeled target state.
- Separate the current architecture from the desired architecture.
- Link important trade-offs to an ADR.
- Update a diagram when a component boundary or data flow changes.
- Keep security and operational limitations visible.

## Planned documents

Create these when the relevant system exists:

| Document | Earliest useful phase |
|---|---:|
| HTTP request lifecycle | 1 |
| Gateway routing and failure handling | 2 |
| Persistence and recovery path | 3 |
| Backend data and authentication boundaries | 4 |
| Job lifecycle and delivery semantics | 5 |
| Telemetry signal flow | 5 |
| Training and inference paths | 6 |
| RAG ingestion and query paths | 7 |
| Container lifecycle | 8 |
| Deployment reconciliation loop | 9 |
| Kai Cloud end-to-end deployment | 10 |
