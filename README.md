# Systems Lab

`systems-lab` is a build-to-understand monorepo. Its long-term 60-week roadmap
explores networking, backend and storage fundamentals, AI services, containers,
and deployment systems.

> Current status: **Week 1 complete.** The repository includes a minimal HTTP/1.1
> server built directly on TCP sockets, with request-line parsing, response
> serialization, a health route, and 10 automated tests. See
> [PROGRESS.md](PROGRESS.md) and the [HTTP server notes](01-networking/http-server/README.md).
> Later roadmap milestones are planned work, not implemented platform features.

## Long-term destination

```text
Developer
   │
   │ kai deploy
   ▼
CLI ──► Control Plane API
             │
             ├── Project and deployment database
             ├── Scheduler
             ├── Service registry
             └── Job queue
                      │
                      ▼
              Deployment Agent
                      │
              Container runtime
                      │
        ┌─────────────┴─────────────┐
        │                           │
   Normal web app              AI/RAG service
        │                           │
        └────────── Gateway ────────┘
                      │
                   Users

Logs ── Metrics ── Traces ── Dashboard
```

The eventual Kai Cloud capstone is intended to:

- create users, projects, and deployments;
- deploy a Docker image to a suitable node;
- expose an endpoint through a gateway;
- health-check and restart workloads;
- provide basic logs, metrics, and traces;
- run background jobs;
- inject environment variables;
- retain deployment versions and roll back;
- deploy a RAG application from a template.

It is a learning and portfolio platform, not a replacement for AWS or
Kubernetes.

## Start here

1. Read [ROADMAP.md](ROADMAP.md) for the complete 60-week path and phase gates.
2. Read [docs/WORKFLOW.md](docs/WORKFLOW.md) for the Sunday working rhythm.
3. Open [PROGRESS.md](PROGRESS.md) before and after every session.
4. At the start of a week, copy the
   [weekly plan template](docs/templates/WEEKLY-PLAN.md) into that week's notes.
5. Create an implementation directory only when its phase actually begins.

## Principles

- Use one monorepo; do not split each lesson into a separate repository.
- Spend roughly 3–6 focused hours on one bounded build each Sunday.
- Treat the selected video as a starting point, not a line-by-line recipe.
- The third week of every cycle must include an extension beyond the tutorial.
- The fourth week is for tests, refactoring, benchmarks, documentation, and
  integration.
- Do not cross a phase gate until the current system can be explained and
  demonstrated.
- Every component must state how it will contribute to Kai Cloud.
- Optimize for depth of understanding and explanation, not technology count.

## Repository shape

The repository contains the shared roadmap and progress documents plus the
first implemented networking milestone. Future component folders will be added
as those milestones begin.

```text
systems-lab/
├── README.md
├── ROADMAP.md
├── PROGRESS.md
├── docs/
│   ├── WORKFLOW.md
│   ├── architecture/
│   ├── diagrams/
│   ├── decisions/
│   └── templates/
│
├── 01-networking/
├── 02-gateway/
├── 03-storage/
├── 04-backend/
├── 05-reliability/
├── 06-ai-foundations/
├── 07-ai-systems/
├── 08-cloud-primitives/
└── 09-capstone/
    └── kai-cloud/
```

## Five milestones

| Milestone | Week | Demonstrable system |
|---|---:|---|
| 1 | 12 | HTTP server + gateway + mini Redis |
| 2 | 24 | Backend + PostgreSQL + queue + observability + Docker |
| 3 | 36 | Mini Transformer + model API + evaluated RAG system |
| 4 | 48 | Container runtime + deployment agent + scheduler + recovery |
| 5 | 60 | Kai Cloud deploying and operating an AI/RAG application |

The learning path is deliberately continuous:

```text
Bytes
→ HTTP
→ backend
→ storage
→ distributed components
→ AI model
→ AI service
→ container
→ orchestration
→ AI cloud platform
```

## Repository documents

| Document | Purpose |
|---|---|
| [ROADMAP.md](ROADMAP.md) | The 60-week plan, phase gates, and milestones |
| [PROGRESS.md](PROGRESS.md) | The single source of truth for progress |
| [docs/WORKFLOW.md](docs/WORKFLOW.md) | How to run a four-week cycle and a Sunday session |
| [docs/architecture/README.md](docs/architecture/README.md) | Target architecture and system evolution |
| [docs/diagrams/README.md](docs/diagrams/README.md) | Diagram conventions and index |
| [docs/decisions/README.md](docs/decisions/README.md) | Architecture decision log |
| [docs/templates/](docs/templates/) | Weekly plan, component README, and ADR templates |

## Explicitly out of scope for v1

- billing and multi-region operation;
- a custom TLS implementation;
- a new distributed consensus protocol;
- production-grade multi-tenant security;
- a distributed database;
- complex autoscaling;
- a custom GPU scheduler.

## Origin

The initial plan came from
[Sunday Build Pick](https://chatgpt.com/s/t_6a64bf08a9888191a2411d503ed6fd11)
and has been normalized into documents that can be maintained directly in this
repository.
