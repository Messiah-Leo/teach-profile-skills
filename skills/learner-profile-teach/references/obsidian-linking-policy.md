# Obsidian Linking Policy

Use this reference before writing learning notes, concept cards, derivations,
stage reviews, or profile proposals.

## Minimum Links

Every note must avoid becoming an orphan.

Course index:

- Link to active lessons.
- Link to concept cards.
- Link to stage reviews.
- Link to pending profile proposals when relevant.

Lesson:

- Link to the course index.
- Link to every main concept card.
- Link to previous and next lesson when available.
- Link to related derivation notes when available.

Concept card:

- Link to lessons that use it.
- Link to confusing or adjacent concepts with an explicit relation label in the
  body, such as `Confused with: [[...]]`.
- Link to a domain context note when useful.

Derivation:

- Link to the course index.
- Link to model variables, assumptions, equations, or concept cards.
- Link to validation or implementation notes when available.

Stage review:

- Link to the reviewed lessons.
- Link to next-step lesson candidates.

Profile proposal:

- Link to evidence lessons.
- Link to exact self-explanation evidence blocks when available.
- Link to the target profile source file only as text path if direct linking
  would expose unstable local cache files.

## Evidence Blocks

For self-explanations or durable evidence, add a human-readable block id:

```md
User self-explanation: ... ^evidence-20260629-001
```

Reference it from profile proposals:

```md
Evidence: [[0003-lesson-title#^evidence-20260629-001]]
```

Block ids should use ASCII letters, digits, and hyphens.

## Graph Discipline

Graph links should express real learning structure, not decoration. Prefer links
that answer one of these questions:

- What course does this belong to?
- Which concept does this teach or depend on?
- Which evidence supports this proposal?
- Which note supersedes or corrects this one?
- Which validation signal closes the loop?
