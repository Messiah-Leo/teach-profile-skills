# Gotchas

Record real failures as:

```text
Symptom -> Cause -> Correct handling
```

## Current Gotchas

- Sync script skipped -> cached `references/` may be stale -> run
  `scripts/sync_learner_profile.py` before reading profile references.
- `references/` edited as source -> changes are overwritten by sync -> edit
  `Self/learner-profile/` or write a proposal first.
- CLI missing -> Obsidian command line interface is disabled or PATH is wrong ->
  enable it in Obsidian settings and check `command -v obsidian`.
- CLI points to old app -> symlink targets an old bundle -> verify
  `obsidian version` and symlink target.
- Bases view empty -> notes lack expected tags/properties -> check
  `obsidian-properties-schema.md`.
- Backlinks empty -> notes were written without internal links -> apply
  `obsidian-linking-policy.md`.
- Profile updated after one lesson -> single evidence was overpromoted -> keep it
  course-local until repeated or explicitly confirmed.
- Long prose in properties -> properties become hard to query -> move prose to
  body and keep properties atomic.
- Conflict copy appears in profile folder -> sync may overwrite the wrong source
  -> stop and resolve conflicts before teaching.
