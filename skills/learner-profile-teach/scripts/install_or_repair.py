#!/usr/bin/env python3
"""Check and repair local learner-profile-teach Obsidian integration."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]


def default_vault() -> Path:
    configured = os.environ.get("OBSIDIAN_VAULT") or os.environ.get("OBSIDIAN_VAULT_PATH")
    return Path(configured).expanduser() if configured else Path.home() / "Documents" / "Coffers"


DEFAULT_VAULT = default_vault()


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("+ " + " ".join(cmd))
    return subprocess.call(cmd, cwd=cwd)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--write-bases", action="store_true")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists():
        raise SystemExit(f"vault does not exist: {vault}")

    if args.write_bases:
        code = run([sys.executable, str(SKILL_DIR / "scripts" / "generate_learning_bases.py"), "--vault", str(vault), "--overwrite"])
        if code != 0:
            return code

    code = run([sys.executable, str(SKILL_DIR / "scripts" / "sync_learner_profile.py"), "--json"], cwd=SKILL_DIR)
    if code != 0:
        return code

    if args.validate:
        return run([sys.executable, str(SKILL_DIR / "scripts" / "validate_obsidian_learning_system.py"), "--vault", str(vault)], cwd=SKILL_DIR)

    print("Repair check complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
