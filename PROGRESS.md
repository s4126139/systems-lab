# Progress

This file is the single source of truth for progress through `systems-lab`.

## Current position

| Field | Value |
|---|---|
| Status | Week 0 — repository setup |
| Phase | Preparation |
| Next build | Week 1 — TCP server and HTTP response |
| Next phase gate | Gate 1 after Week 4 |
| Blocker | None |
| Last updated | 2026-07-26 |

## Week 0 — Repository setup

- [x] Define the Kai Cloud destination.
- [x] Normalize the 60-week roadmap.
- [x] Define the workflow and Definition of Done.
- [x] Create templates for weekly plans, component READMEs, and ADRs.
- [ ] Select the video and exact scope for Week 1.

## 60-week tracker

### Phase 1 — HTTP and networking

- [ ] W01 — TCP server and HTTP response
- [ ] W02 — HTTP request parser and router
- [ ] W03 — File server, POST, and concurrency
- [ ] W04 — Logging, tests, and benchmark

### Phase 2 — Gateway, proxy, and traffic control

- [ ] W05 — Reverse proxy
- [ ] W06 — Load balancer
- [ ] W07 — Rate limiter and health check
- [ ] W08 — Mini API gateway

### Phase 3 — Storage, cache, and database internals

- [ ] W09 — In-memory key-value store
- [ ] W10 — Persistence
- [ ] W11 — TTL and eviction
- [ ] W12 — Mini Redis server

### Phase 4 — Structured backend development

- [ ] W13 — FastAPI service
- [ ] W14 — PostgreSQL
- [ ] W15 — Authentication
- [ ] W16 — Integrated backend

### Phase 5 — Queues, reliability, and observability

- [ ] W17 — Task queue
- [ ] W18 — Retry and idempotency
- [ ] W19 — Scheduler and dead-letter queue
- [ ] W20 — Document-processing pipeline
- [ ] W21 — Structured logging
- [ ] W22 — Metrics
- [ ] W23 — Distributed tracing
- [ ] W24 — Docker Compose and CI

### Phase 6 — AI from foundations

- [ ] W25 — Scalar autograd engine
- [ ] W26 — Small tensor system and MLP
- [ ] W27 — Tokenizer
- [ ] W28 — Character language model
- [ ] W29 — Self-attention
- [ ] W30 — Mini Transformer
- [ ] W31 — Training system
- [ ] W32 — Model-serving API

### Phase 7 — Applied AI and RAG

- [ ] W33 — Embeddings pipeline
- [ ] W34 — Vector search
- [ ] W35 — RAG service
- [ ] W36 — RAG evaluation

### Phase 8 — Containers and Linux primitives

- [ ] W37 — Process isolation
- [ ] W38 — Resource limits
- [ ] W39 — Root filesystem and image layers
- [ ] W40 — Mini container runtime

### Phase 9 — Orchestration primitives

- [ ] W41 — Mini image registry
- [ ] W42 — Deployment agent
- [ ] W43 — Service discovery
- [ ] W44 — Scheduler
- [ ] W45 — Health check and restart
- [ ] W46 — Rolling deployment
- [ ] W47 — Config and secrets
- [ ] W48 — Persistent storage

### Phase 10 — Kai Cloud capstone

- [ ] W49 — Control plane and CLI skeleton
- [ ] W50 — User, project, and deployment state
- [ ] W51 — End-to-end deployment
- [ ] W52 — Routing and domain
- [ ] W53 — Logs dashboard
- [ ] W54 — Metrics and traces dashboard
- [ ] W55 — AI application template
- [ ] W56 — Deploy a RAG service
- [ ] W57 — Background jobs
- [ ] W58 — Versioning and rollback
- [ ] W59 — Security and load testing
- [ ] W60 — Demo, docs, and benchmark

## Milestone review

| Milestone | Week | Status | Demo/evidence |
|---|---:|---|---|
| HTTP + gateway + storage | 12 | Not started | — |
| Backend + reliability | 24 | Not started | — |
| AI foundations + RAG | 36 | Not started | — |
| Containers + orchestration | 48 | Not started | — |
| Kai Cloud | 60 | Not started | — |

## Open blockers and decisions

| Date | Issue | Impact | Next action |
|---|---|---|---|
| — | None | — | — |

## Update rules

After every Sunday session:

1. update **Current position**;
2. mark a week complete only after its Definition of Done is met;
3. link its component README, diagram, benchmark, or demo;
4. record a blocker precisely when the build is incomplete;
5. create and link an ADR when a meaningful architecture trade-off appears.
