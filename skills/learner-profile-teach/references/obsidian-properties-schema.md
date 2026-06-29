# Obsidian Properties Schema

Use these properties for Codex-created learning notes. Keep values short and
machine-readable; put complex explanations in the note body.

## Shared Properties

```yaml
---
type: lesson
status: active
categories:
  - "[[Codex Learning]]"
course: "[[Course Name]]"
summary: "One-line summary."
created: 2026-06-29
updated: 2026-06-29
source_skill:
  - teach
  - learner-profile-teach
tags:
  - codex/lesson
---
```

Use ISO dates. Use Obsidian links as quoted strings in properties.

## Status Values

- `active`: current and useful.
- `needs-review`: user should review or self-explain again.
- `reviewed`: reviewed and stable for now.
- `superseded`: replaced by a newer note.
- `pending`: waiting for user confirmation.
- `accepted`: confirmed and applied.
- `rejected`: explicitly not applied.

## Note Types

### Course Index

```yaml
type: course-index
status: active
categories:
  - "[[Codex Learning]]"
course: "[[Course Name]]"
summary: "Course purpose."
tags:
  - codex/course
```

### Lesson

```yaml
type: lesson
status: active
categories:
  - "[[Codex Learning]]"
course: "[[Course Name]]"
lesson_index: 1
summary: "What this lesson made usable."
key_question: "The central question."
concepts:
  - "[[Concept A]]"
difficulty_type:
  - terminology
transfer_context:
  - research
profile_candidate: false
evidence_level: lesson-local
tags:
  - codex/lesson
```

Allowed `difficulty_type` values:

- `terminology`
- `abstraction`
- `mathematical_form`
- `physical_mechanism`
- `engineering_implementation`
- `personal_transfer`
- `planning`

Allowed `transfer_context` values:

- `research`
- `engineering`
- `electromagnetics`
- `numerical_methods`
- `code`
- `tool_integration`
- `writing`
- `management`
- `planning`
- `life`

### Concept Card

```yaml
type: concept-card
status: active
categories:
  - "[[Codex Learning]]"
concept: "Concept name"
aliases:
  - "Alternate name"
summary: "One-line definition."
common_confusion: "Most likely confusion."
domain_context:
  - computational-electromagnetics
related_lessons:
  - "[[0001-example-lesson]]"
mastery_signal: "What the user can do when this is stable."
tags:
  - codex/concept
```

### Derivation Note

```yaml
type: derivation
status: active
categories:
  - "[[Codex Learning]]"
course: "[[Course Name]]"
summary: "What was derived."
concepts:
  - "[[Concept A]]"
validation_signal: "What would falsify or confirm this."
tags:
  - codex/derivation
```

### Stage Review

```yaml
type: stage-review
status: active
categories:
  - "[[Codex Learning]]"
course: "[[Course Name]]"
lessons_reviewed:
  - "[[Lesson 1]]"
profile_candidate: false
summary: "Review decision."
tags:
  - codex/review
```

### Profile Update Proposal

```yaml
type: profile-update-proposal
status: pending
categories:
  - "[[Codex Learning]]"
target_file: global-profile.md
evidence_level: repeated
requires_confirmation: true
lessons_reviewed:
  - "[[Lesson 1]]"
profile_area:
  - teaching-preference
summary: "What this proposal would update."
tags:
  - codex/profile-proposal
```

## Property Discipline

- Do not put paragraphs in properties.
- Do not store temporary moods as stable profile facts.
- Use `profile_candidate: true` only when evidence may matter beyond the
  current course.
- Use `requires_confirmation: true` for every profile proposal.
