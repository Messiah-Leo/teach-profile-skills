# Obsidian Bases

Use Bases to turn Codex-created learning notes into queryable views.

## Required Base Files

```text
Categories/Base/Codex Learning.base
Categories/Base/Codex Concepts.base
Categories/Base/Codex Profile Proposals.base
Categories/Base/Codex Review Queue.base
```

Generate or repair them with:

```bash
python3 scripts/generate_learning_bases.py
```

## Views

`Codex Learning.base` should include:

- `All lessons`
- `Needs review`
- `Profile candidates`
- `By difficulty type`
- `By transfer context`

`Codex Concepts.base` should include:

- `All concepts`
- `Immature concepts`
- `Confusion map inputs`

`Codex Profile Proposals.base` should include:

- `Pending proposals`
- `Accepted proposals`
- `Rejected proposals`

`Codex Review Queue.base` should include:

- `Needs review`
- `Pending self-explanation`
- `Recent learning notes`

## Query Examples

```bash
cd /path/to/Obsidian/Vault
obsidian bases
obsidian base:query path="Categories/Base/Codex Learning.base" view="All lessons"
```

If a Base is empty, first check whether notes have the expected tags and
properties from `obsidian-properties-schema.md`.

Note: `obsidian base:views` lists views for the active Base file only. For
scripted validation, prefer `base:query path="..." view="..."`.
