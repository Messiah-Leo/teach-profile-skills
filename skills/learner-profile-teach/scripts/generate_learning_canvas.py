#!/usr/bin/env python3
"""Generate a simple JSON Canvas map for a course folder."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def default_vault() -> Path:
    configured = os.environ.get("OBSIDIAN_VAULT") or os.environ.get("OBSIDIAN_VAULT_PATH")
    return Path(configured).expanduser() if configured else Path.home() / "Documents" / "Coffers"


DEFAULT_VAULT = default_vault()


def generate(vault: Path, folder: str, output: str) -> Path:
    course_dir = vault / folder
    if not course_dir.exists():
        raise SystemExit(f"course folder does not exist: {course_dir}")

    notes = sorted(path for path in course_dir.glob("*.md") if path.is_file())
    nodes = []
    edges = []
    x_step = 420
    for index, note in enumerate(notes):
        node_id = f"note-{index + 1}"
        rel = note.relative_to(vault).as_posix()
        nodes.append(
            {
                "id": node_id,
                "type": "file",
                "file": rel,
                "x": (index % 3) * x_step,
                "y": (index // 3) * 320,
                "width": 360,
                "height": 240,
            }
        )
        if index > 0:
            edges.append(
                {
                    "id": f"edge-{index}",
                    "fromNode": f"note-{index}",
                    "toNode": node_id,
                    "label": "next",
                }
            )
    canvas = {"nodes": nodes, "edges": edges}
    output_path = vault / output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(canvas, ensure_ascii=False, indent=2), encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--folder", required=True, help="course folder relative to vault root")
    parser.add_argument("--output", help="canvas path relative to vault root")
    args = parser.parse_args()

    output = args.output or f"{args.folder.rstrip('/')}/Course Map.canvas"
    path = generate(Path(args.vault).expanduser().resolve(), args.folder, output)
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
