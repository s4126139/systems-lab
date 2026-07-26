# Diagram Guide and Index

Diagrams are working tools, not decoration. Each diagram should answer one
specific question about structure, sequence, state, deployment, or failure.

## Conventions

- Give every diagram a title and one-sentence purpose.
- Label arrows with data, commands, or events.
- Mark trust, process, machine, or network boundaries when relevant.
- Distinguish synchronous calls from queued work.
- Show failure and retry paths when they are part of the design.
- Keep the current state separate from a future target state.
- Prefer a small readable diagram over one diagram containing the entire system.

## Recommended diagram types

| Question | Diagram |
|---|---|
| What components exist and how do they connect? | Component diagram |
| What happens during one request or job? | Sequence diagram |
| How does an entity change over time? | State diagram |
| Where does each process run? | Deployment diagram |
| What breaks and how does the system respond? | Failure-flow diagram |

## Diagram checklist by phase

| Phase | Minimum useful diagram |
|---:|---|
| 1 | TCP connection and HTTP request lifecycle |
| 2 | Gateway routing, health check, and failover |
| 3 | Write-ahead log and restart recovery |
| 4 | Authenticated request to database/cache |
| 5 | Job lifecycle plus logs/metrics/traces flow |
| 6 | Autograd graph and Transformer data path |
| 7 | RAG ingestion and query pipelines |
| 8 | Container lifecycle and isolation boundaries |
| 9 | Scheduling, deployment, health, and rollback |
| 10 | Kai Cloud end-to-end deployment |

## Index

Add an entry whenever a diagram is created.

| Diagram | Phase/week | Status | Related document |
|---|---:|---|---|
| Target Kai Cloud overview | Week 0 | Concept | [Architecture overview](../architecture/README.md) |
