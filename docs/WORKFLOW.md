# Working Method

The roadmap is completed in four-week cycles. Each Sunday has one bounded build
that should fit within 3–6 focused hours.

## Four-week cycle

| Week in cycle | Intent |
|---:|---|
| 1 | Learn the architecture and build the first version with video support |
| 2 | Build the next component with less dependence on the video |
| 3 | Add a feature that is not present in the tutorial |
| 4 | Test, refactor, benchmark, document, and integrate |

If the current phase gate is not met, the next session stays in that phase. The
calendar never has priority over understanding.

## A Sunday session

| Time | Activity |
|---|---|
| 0:00–0:20 | Read the goal and sketch the architecture |
| 0:20–1:10 | Watch only the relevant explanation and timestamps |
| 1:10–2:40 | Build independently; revisit the video only when blocked |
| 2:40–3:00 | Break and review the system flow |
| 3:00–4:00 | Complete the core component |
| 4:00–4:45 | Add the independent extension and tests |
| 4:45–5:15 | Update README, diagram, progress, and notes |
| 5:15–6:00 | Buffer or benchmark |

Finishing early is acceptable when the Definition of Done has been met.

## Before starting

1. Read the current row in `ROADMAP.md`.
2. Read the gate for the active phase.
3. Copy `docs/templates/WEEKLY-PLAN.md`.
4. Write one sentence for the problem and one sentence for the success signal.
5. Define what is explicitly out of scope.
6. Record the chosen video and only the timestamps relevant to the build.
7. Draw the expected request, data, or control flow before implementation.

## Definition of Done

A weekly build is complete only when all applicable items are true:

- [ ] The component runs by following its README.
- [ ] At least one happy-path test exists.
- [ ] At least one failure-path test exists.
- [ ] An architecture or sequence diagram exists.
- [ ] There is an extension beyond the selected video.
- [ ] `What I learned` is written in the author's own words.
- [ ] Known limitations are explicit.
- [ ] The work is recorded in a clear commit.
- [ ] `PROGRESS.md` is updated with evidence.

If an item genuinely does not apply, mark it `N/A` and explain why. Do not silently
remove it.

## Closing a session

1. Run the documented happy path.
2. Run the documented failure path.
3. Compare the result with the week's success signal.
4. Record observed behavior, not just intended behavior.
5. Update the component README and its diagram.
6. Record any meaningful trade-off as an ADR.
7. Update `PROGRESS.md`.
8. Decide whether the next week advances, repeats, or reduces scope.

## Phase-gate review

At the end of a phase, answer three questions:

1. **Explain:** Can the core mechanism be explained without the tutorial?
2. **Demonstrate:** Is there observable evidence for every gate criterion?
3. **Connect:** Is it clear how this component will be reused by Kai Cloud?

The phase advances only when all three answers are yes.

## Handling blockers

A useful blocker entry contains:

- the expected behavior;
- the observed behavior;
- the smallest reproducible case;
- what has already been tried;
- the next experiment;
- whether the roadmap or only the current build is affected.

Avoid vague entries such as “does not work” or “need more time.”

## Scope control

When a build exceeds one Sunday:

1. preserve the smallest end-to-end path;
2. defer optional protocols, optimizations, and UI;
3. keep one failure path and one measurable result;
4. carry the remaining work into the next Sunday;
5. do not start the next roadmap topic merely to stay on schedule.

## Repository discipline

- Keep all components in `systems-lab`.
- Create implementation folders only when they become active.
- Give each active component its own README and tests.
- Do not commit secrets, credentials, generated datasets, or large model files.
- Prefer a small, explained system over a large unexplained stack.
