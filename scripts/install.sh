#!/usr/bin/env sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
codex_home=${CODEX_HOME:-"$HOME/.codex"}
skills_dir="$codex_home/skills"
timestamp=$(date +%Y%m%d-%H%M%S)

mkdir -p "$skills_dir"

for skill in teach learner-profile-teach; do
  source_dir="$repo_root/skills/$skill"
  target_dir="$skills_dir/$skill"

  if [ ! -d "$source_dir" ]; then
    echo "Missing skill directory: $source_dir" >&2
    exit 1
  fi

  if [ -e "$target_dir" ]; then
    backup_dir="$target_dir.backup-$timestamp"
    mv "$target_dir" "$backup_dir"
    echo "Backed up existing $skill -> $backup_dir"
  fi

  cp -R "$source_dir" "$target_dir"
  echo "Installed $skill -> $target_dir"
done

echo "Done. Restart Codex if skills are not reloaded automatically."
