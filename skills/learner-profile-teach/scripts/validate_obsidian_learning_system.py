#!/usr/bin/env python3
"""Validate the Codex learner-profile and Obsidian learning-system setup."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def default_vault() -> Path:
    configured = os.environ.get("OBSIDIAN_VAULT") or os.environ.get("OBSIDIAN_VAULT_PATH")
    return Path(configured).expanduser() if configured else Path.home() / "Documents" / "Coffers"


DEFAULT_VAULT = default_vault()
SKILL_DIR = Path(__file__).resolve().parents[1]
REQUIRED_REFERENCES = [
    "global-profile.md",
    "teaching-protocol.md",
    "research-workflow.md",
    "cognition-and-planning.md",
    "update-protocol.md",
    "obsidian-integration.md",
    "obsidian-properties-schema.md",
    "obsidian-bases.md",
    "obsidian-linking-policy.md",
    "obsidian-cli-protocol.md",
    "validation.md",
    "gotchas.md",
    "routing.md",
]
REQUIRED_TEMPLATES = [
    "lesson-note.md",
    "concept-card.md",
    "derivation-note.md",
    "stage-review.md",
    "five-lesson-review.md",
    "profile-update-proposal.md",
    "course-index.md",
    "daily-learning-summary.md",
]
REQUIRED_BASES = [
    "Categories/Base/Codex Learning.base",
    "Categories/Base/Codex Concepts.base",
    "Categories/Base/Codex Profile Proposals.base",
    "Categories/Base/Codex Review Queue.base",
]


def run(cmd: list[str], cwd: Path | None = None) -> tuple[bool, str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode == 0, proc.stdout.strip()


def check_file(path: Path, label: str, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"missing {label}: {path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    check_file(vault, "vault", errors)
    check_file(SKILL_DIR / "SKILL.md", "skill file", errors)
    for name in REQUIRED_REFERENCES:
        check_file(SKILL_DIR / "references" / name, "reference", errors)
    for name in REQUIRED_TEMPLATES:
        check_file(SKILL_DIR / "templates" / name, "template", errors)
    for name in REQUIRED_BASES:
        check_file(vault / name, "base", errors)

    obsidian = shutil.which("obsidian")
    if not obsidian:
        errors.append("obsidian CLI not found on PATH")
    else:
        ok, output = run([obsidian, "version"], cwd=vault)
        if not ok:
            errors.append(f"obsidian version failed: {output}")

    sync_script = SKILL_DIR / "scripts" / "sync_learner_profile.py"
    if sync_script.exists():
        ok, output = run([sys.executable, str(sync_script), "--json"], cwd=SKILL_DIR)
        if not ok:
            errors.append(f"profile sync failed: {output}")
        else:
            try:
                result = json.loads(output)
                if result.get("status") != "ok":
                    errors.append(f"profile sync not ok: {output}")
            except json.JSONDecodeError:
                errors.append(f"profile sync did not return JSON: {output}")
    else:
        errors.append(f"missing sync script: {sync_script}")

    if obsidian and vault.exists():
        base_queries = {
            "Categories/Base/Codex Learning.base": "All lessons",
            "Categories/Base/Codex Concepts.base": "All concepts",
            "Categories/Base/Codex Profile Proposals.base": "Pending proposals",
            "Categories/Base/Codex Review Queue.base": "Recent learning notes",
        }
        for rel, view in base_queries.items():
            ok, output = run([obsidian, "base:query", f"path={rel}", f"view={view}", "format=json"], cwd=vault)
            if not ok:
                errors.append(f"base query failed for {rel}: {output}")
        ok, output = run([obsidian, "search", "query=[profile_candidate:true]"], cwd=vault)
        if not ok:
            warnings.append(f"profile candidate search failed: {output}")

    status = "ok" if not errors else "error"
    result = {"status": status, "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"STATUS={status}")
        for warning in warnings:
            print(f"WARNING={warning}")
        for error in errors:
            print(f"ERROR={error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
