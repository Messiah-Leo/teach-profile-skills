# Obsidian Integration

Use this reference when writing durable learning material into the user's
Obsidian vault.

## Vault And Folders

Default vault resolution:

```text
explicit user path -> --vault argument -> OBSIDIAN_VAULT or OBSIDIAN_VAULT_PATH -> ~/Documents/Coffers
```

Default learning folder:

```text
Skills/<topic>/
```

Stable learner profile source:

```text
Self/learner-profile/
```

Profile update proposals:

```text
Self/learner-profile/proposals/
```

Base dashboard files:

```text
Categories/Base/Codex Learning.base
Categories/Base/Codex Concepts.base
Categories/Base/Codex Profile Proposals.base
Categories/Base/Codex Review Queue.base
```

## Artifact Split

- Course index: course mission, links, status, and review queue.
- Lesson note: one substantial lesson or derivation step.
- Concept card: one durable concept, definition, confusion, and mastery signal.
- Derivation note: physical constraint, model, method, assumptions, validation.
- Stage review: multi-lesson review and next-step decision.
- Profile proposal: stable cross-course update candidate, never a silent update.
- Daily summary: short pointer from the daily note into durable course notes.

## Writing Rule

Every Obsidian learning note should have:

1. YAML properties from `obsidian-properties-schema.md`.
2. Links required by `obsidian-linking-policy.md`.
3. Concise recall-oriented body text.
4. CLI validation from `validation.md` when the CLI is available.

Properties hold atomic searchable data. Body text holds explanations.
