# Documentation Guide

The documentation has four jobs:

1. keep the 60-week direction visible;
2. make each weekly build reproducible;
3. capture architecture reasoning and limitations;
4. provide evidence that the current phase gate has been met.

## Map

| Location | Contents |
|---|---|
| [../ROADMAP.md](../ROADMAP.md) | The complete learning path |
| [../PROGRESS.md](../PROGRESS.md) | Current status and weekly tracker |
| [WORKFLOW.md](WORKFLOW.md) | Session rhythm and Definition of Done |
| [architecture/](architecture/) | Target architecture and major system views |
| [diagrams/](diagrams/) | Diagram index and conventions |
| [decisions/](decisions/) | Architecture Decision Records |
| [templates/](templates/) | Reusable documentation templates |

## What belongs where?

- Put stable project orientation in the root `README.md`.
- Put time-ordered plans and gates in `ROADMAP.md`.
- Put changing status, blockers, and evidence in `PROGRESS.md`.
- Put a component-specific explanation in that component's own `README.md`.
- Put a long-lived architecture trade-off in an ADR.
- Put diagrams near the document that explains them, then index them in
  `docs/diagrams/README.md`.

## Documentation rule

A document should explain the system in the author's own words. Links and videos
may support the explanation, but they do not replace it.
