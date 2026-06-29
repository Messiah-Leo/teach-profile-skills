# Install

## Requirements

- Codex with local skill support.
- A writable Codex home directory. By default this is `~/.codex`.
- Optional: Obsidian with a synced vault containing `Self/learner-profile/`.

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

## Configure Obsidian Profile Sync

After installing, create a machine-local config:

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/learner-profile-teach"
cp local-sync-config.example.json local-sync-config.json
```

Edit `local-sync-config.json`:

```json
{
  "vault_path": "/path/to/Obsidian/Vault",
  "profile_source": "Self/learner-profile",
  "codex_references": "/path/to/.codex/skills/learner-profile-teach/references"
}
```

Windows example:

```json
{
  "vault_path": "C:\\Users\\YOU\\Documents\\Coffers",
  "profile_source": "Self/learner-profile",
  "codex_references": "C:\\Users\\YOU\\.codex\\skills\\learner-profile-teach\\references"
}
```

macOS example:

```json
{
  "vault_path": "/Users/YOU/Documents/Coffers",
  "profile_source": "Self/learner-profile",
  "codex_references": "/Users/YOU/.codex/skills/learner-profile-teach/references"
}
```

Generate or repair Obsidian Bases and validate the setup:

```bash
python scripts/install_or_repair.py --write-bases --validate
```

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

If your personal learner profile lives in Obsidian, keep it there rather than
editing the installed `references/` cache directly. Re-run
`scripts/sync_learner_profile.py` after updating `Self/learner-profile/`.

## Verify

Start a new Codex chat and ask:

```text
Use $learner-profile-teach and $teach to teach me one small topic.
```

Codex should load the profile skill first, then use the teach skill to set or
continue a learning mission.

For a direct setup check:

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/learner-profile-teach"
python scripts/sync_learner_profile.py --json
python scripts/validate_obsidian_learning_system.py --json
```
