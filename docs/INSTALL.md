# Install

## Requirements

- Codex with local skill support.
- A writable Codex home directory. By default this is `~/.codex`.

## Quick Install

From the repository root:

```bash
./scripts/install.sh
```

The script copies both skill directories into:

```text
${CODEX_HOME:-$HOME/.codex}/skills
```

## Manual Install

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/teach "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/learner-profile-teach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex if it does not reload skills automatically.

## Update An Existing Install

Re-run the installer:

```bash
./scripts/install.sh
```

The installer replaces the installed copies of `teach` and
`learner-profile-teach` with the repository versions. Existing installed skill
directories are moved to timestamped backup folders next to the new install.
Review those backups if you personalized files inside the installed skill
directories.

## Verify

Start a new Codex chat and ask:

```text
Use $learner-profile-teach and $teach to teach me one small topic.
```

Codex should load the profile skill first, then use the teach skill to set or
continue a learning mission.
