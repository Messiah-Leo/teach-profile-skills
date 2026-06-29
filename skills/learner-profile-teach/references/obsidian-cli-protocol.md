# Obsidian CLI Protocol

Prefer the `obsidian` CLI for Obsidian automation when available. Fall back to
filesystem writes only when the CLI is missing or a command does not support the
needed action.

## Availability Check

```bash
command -v obsidian
obsidian version
```

Any recent Obsidian CLI that supports `read`, `search`, `links`,
`backlinks`, and `base:query` is acceptable.

## Common Commands

Run commands from the vault root when possible:

```bash
cd /path/to/Obsidian/Vault
obsidian read path="Self/learner-profile/global-profile.md"
obsidian search query="[profile_candidate:true]"
obsidian backlinks path="Skills/Course/0001-lesson.md" counts
obsidian links path="Skills/Course/0001-lesson.md" total
obsidian bases
obsidian base:query path="Categories/Base/Codex Learning.base"
obsidian daily:append content="- [[Lesson]]: one-line summary"
```

## Backend Order

1. `obsidian` CLI for read, search, backlinks, links, Bases, daily note, and
   verification.
2. Direct filesystem writes for deterministic note generation.
3. `obsidian://` URI links for opening notes or searches in the UI.

## Safety

- Do not use `obsidian delete`, `history:restore`, plugin installation, or
  plugin disable/enable commands unless the user explicitly asks.
- Verify writes with `obsidian read` or `obsidian file`.
- Verify link structure with `obsidian links` and `obsidian backlinks` when the
  note should be connected.
