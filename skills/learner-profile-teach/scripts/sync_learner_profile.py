#!/usr/bin/env python3
"""Sync the Obsidian learner profile source into the local Codex skill cache."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path


REQUIRED_FILES = [
    "global-profile.md",
    "research-workflow.md",
    "cognition-and-planning.md",
]

CONFLICT_MARKERS = [
    "conflict",
    "conflicted copy",
    "sync-conflict",
    "冲突",
]


def skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def config_path() -> Path:
    return skill_dir() / "local-sync-config.json"


def load_config() -> dict:
    path = config_path()
    if not path.exists():
        raise RuntimeError(f"missing config: {path}")
    with path.open("r", encoding="utf-8") as handle:
        config = json.load(handle)

    missing = [
        key
        for key in ("vault_path", "profile_source", "codex_references")
        if not config.get(key)
    ]
    if missing:
        raise RuntimeError(f"config missing required keys: {', '.join(missing)}")
    return config


def wake_obsidian(vault_path: Path) -> bool:
    if sys.platform != "darwin":
        return False
    try:
        subprocess.run(
            ["open", "-a", "Obsidian", str(vault_path)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return True
    except OSError:
        return False


def find_conflicts(profile_dir: Path) -> list[str]:
    conflicts: list[str] = []
    for path in profile_dir.rglob("*"):
        if not path.is_file():
            continue
        name = path.name.lower()
        if any(marker.lower() in name for marker in CONFLICT_MARKERS):
            conflicts.append(str(path.relative_to(profile_dir)))
    return conflicts


def snapshot(paths: list[Path]) -> dict[str, tuple[int, int]]:
    return {str(path): (path.stat().st_mtime_ns, path.stat().st_size) for path in paths}


def wait_for_stability(paths: list[Path], checks: int, delay: float) -> bool:
    previous = snapshot(paths)
    for _ in range(checks):
        time.sleep(delay)
        current = snapshot(paths)
        if current != previous:
            previous = current
            continue
    return snapshot(paths) == previous


def sync(config: dict, *, wait_seconds: float) -> dict:
    vault_path = Path(config["vault_path"]).expanduser().resolve()
    profile_source = config["profile_source"]
    profile_dir = (vault_path / profile_source).resolve()
    references_dir = Path(config["codex_references"]).expanduser().resolve()

    wake_attempted = wake_obsidian(vault_path)

    if not vault_path.exists():
        raise RuntimeError(f"vault path does not exist: {vault_path}")
    if not profile_dir.exists():
        raise RuntimeError(f"profile source does not exist: {profile_dir}")

    source_files = [profile_dir / name for name in REQUIRED_FILES]
    missing = [path.name for path in source_files if not path.exists()]
    if missing:
        raise RuntimeError(f"missing required source files: {', '.join(missing)}")

    conflicts = find_conflicts(profile_dir)
    if conflicts:
        raise RuntimeError("conflict files detected: " + ", ".join(conflicts))

    checks = 2
    delay = max(wait_seconds / checks, 0.1)
    stable = wait_for_stability(source_files, checks=checks, delay=delay)
    if not stable:
        raise RuntimeError("profile files did not become stable during the wait window")

    references_dir.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for source in source_files:
        target = references_dir / source.name
        shutil.copy2(source, target)
        copied.append(source.name)

    return {
        "status": "ok",
        "confidence": "high" if wake_attempted and stable else "medium",
        "copied": copied,
        "source": str(profile_dir),
        "destination": str(references_dir),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument(
        "--wait-seconds",
        type=float,
        default=2.0,
        help="seconds to wait while checking source file stability",
    )
    args = parser.parse_args()

    try:
        result = sync(load_config(), wait_seconds=args.wait_seconds)
        exit_code = 0
    except Exception as exc:  # noqa: BLE001 - CLI should report any sync blocker.
        result = {"status": "low", "confidence": "low", "error": str(exc), "copied": []}
        exit_code = 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"STATUS={result['status']}")
        print(f"CONFIDENCE={result['confidence']}")
        if result.get("copied"):
            print("COPIED=" + ",".join(result["copied"]))
        if result.get("error"):
            print("ERROR=" + result["error"])
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
