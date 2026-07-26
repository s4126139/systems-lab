# Architecture Decisions

This directory stores Architecture Decision Records (ADRs). An ADR captures a
decision whose reasoning should survive longer than the current implementation.

## When to write an ADR

Write one when a decision:

- changes a component or data boundary;
- selects one consistency, retry, persistence, or security model over another;
- introduces a dependency that will be expensive to replace;
- constrains later phases;
- accepts a meaningful limitation or risk.

Do not write an ADR for a trivial naming choice or an easily reversible local
detail.

## Lifecycle

1. Copy [the ADR template](../templates/ADR.md).
2. Name it `NNNN-short-decision-title.md`.
3. Set the status to `Proposed`.
4. Record context, options, the decision, and consequences.
5. Change the status to `Accepted`, `Rejected`, `Superseded`, or `Deprecated`.
6. If superseded, link both ADRs.

## Decision index

| ADR | Status | Decision | Phase |
|---|---|---|---|
| — | — | No decisions recorded yet | — |
