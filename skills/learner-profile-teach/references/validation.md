# Validation

Use this reference before declaring Obsidian learning-system work complete.

## Skill Files

- `SKILL.md` exists and has valid frontmatter.
- Required references exist.
- Required templates exist.
- Scripts compile with `python3 -m py_compile`.

## Obsidian CLI

```bash
command -v obsidian
obsidian version
```

## Profile Sync

```bash
cd ~/.codex/skills/learner-profile-teach
python3 scripts/sync_learner_profile.py --json
```

Continue only on `status: ok`. If confidence is `medium`, mention that remote
Obsidian Sync completion cannot be proven.

## Note Validation

For each important written note:

- File exists.
- YAML properties are present.
- `type`, `status`, `tags`, and `summary` are present.
- Lessons link to course index and at least one concept when applicable.
- Profile proposals link to evidence notes or blocks.
- `obsidian read path="..."` succeeds.
- `obsidian links path="..." total` is nonzero for connected notes.

## Bases Validation

```bash
cd /path/to/Obsidian/Vault
obsidian bases
obsidian base:query path="Categories/Base/Codex Learning.base" view="All lessons"
```

Empty query results are acceptable when no matching notes exist; syntax or
command errors are not.
