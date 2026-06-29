#!/usr/bin/env python3
"""Create a Codex learning note in an Obsidian vault."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import shutil
import subprocess
from pathlib import Path


def default_vault() -> Path:
    configured = os.environ.get("OBSIDIAN_VAULT") or os.environ.get("OBSIDIAN_VAULT_PATH")
    return Path(configured).expanduser() if configured else Path.home() / "Documents" / "Coffers"


DEFAULT_VAULT = default_vault()
KIND_TAGS = {
    "course-index": "codex/course",
    "lesson": "codex/lesson",
    "concept-card": "codex/concept",
    "derivation": "codex/derivation",
    "stage-review": "codex/review",
    "profile-update-proposal": "codex/profile-proposal",
}


def slugify(text: str) -> str:
    text = text.strip()
    text = re.sub(r"[\\/:*?\"<>|#^[\\]]+", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:80] or "codex-note"


def yaml_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def yaml_block(data: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {yaml_scalar(item)}")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines)


def body_for(kind: str, title: str, course: str, concepts: list[str]) -> str:
    concept_links = "\n".join(f"  - [[{c}]]" for c in concepts) or "  -"
    if kind == "lesson":
        return f"""# {title}

## Core Question

-

## Minimal Terms

-

## Definition

-

## Common Confusion

-

## Small Example

-

## Domain Transfer

-

## Self-Explanation Prompt

1. Explain the core concept in your own words.
2. Transfer it to one research, engineering, management, planning, or life scenario.
3. Name one unclear, uncertain, or disputable point.

## Evidence

User self-explanation:  ^evidence-{dt.date.today().strftime('%Y%m%d')}-001

## Links

- Course: [[{course}]]
- Concepts:
{concept_links}
"""
    if kind == "concept-card":
        return f"""# {title}

## Definition

-

## What It Is Not

-

## Common Confusion

-

## Small Example

-

## Where It Appears

-

## Mastery Signal

-
"""
    if kind == "profile-update-proposal":
        return f"""# Profile Update Proposal: {title}

## Proposed Change

-

## Evidence

-

## Why This Is Cross-Course Useful

-

## Suggested Target File

-

## Exact Draft Text

```md

```

## Confirmation Needed

Ask the user to confirm before editing stable profile files.
"""
    return f"""# {title}

## Summary

-

## Links

- Course: [[{course}]]
- Concepts:
{concept_links}
"""


def build_note(args: argparse.Namespace) -> str:
    today = dt.date.today().isoformat()
    concepts = args.concept or []
    tag = KIND_TAGS[args.kind]
    data: dict[str, object] = {
        "type": args.kind,
        "status": args.status,
        "categories": ["[[Codex Learning]]"],
        "summary": args.summary,
        "created": today,
        "updated": today,
        "source_skill": ["teach", "learner-profile-teach"],
        "tags": [tag],
    }
    if args.course:
        data["course"] = f"[[{args.course}]]"
    if args.kind == "lesson":
        data["lesson_index"] = args.lesson_index
        data["key_question"] = args.key_question
        data["concepts"] = [f"[[{c}]]" for c in concepts]
        data["difficulty_type"] = args.difficulty_type or ["terminology"]
        data["transfer_context"] = args.transfer_context or ["research"]
        data["profile_candidate"] = args.profile_candidate
        data["evidence_level"] = args.evidence_level
    if args.kind == "concept-card":
        data["concept"] = args.title
        data["aliases"] = []
        data["common_confusion"] = args.common_confusion
        data["domain_context"] = args.transfer_context or ["research"]
        data["related_lessons"] = []
        data["mastery_signal"] = args.mastery_signal
    if args.kind == "profile-update-proposal":
        data["target_file"] = args.target_file
        data["evidence_level"] = args.evidence_level
        data["requires_confirmation"] = True
        data["lessons_reviewed"] = []
        data["profile_area"] = args.profile_area or ["teaching-preference"]
    return yaml_block(data) + "\n\n" + body_for(args.kind, args.title, args.course or args.title, concepts)


def note_path(args: argparse.Namespace) -> Path:
    vault = Path(args.vault).expanduser().resolve()
    if args.path:
        rel = Path(args.path)
    else:
        folder = Path(args.folder or f"Skills/{args.course or 'Codex Learning'}")
        rel = folder / f"{slugify(args.title)}.md"
    return vault / rel


def verify(path: Path, vault: Path) -> None:
    obsidian = shutil.which("obsidian")
    if not obsidian:
        return
    rel = path.relative_to(vault)
    subprocess.run([obsidian, "read", f"path={rel}"], cwd=vault, check=True, stdout=subprocess.DEVNULL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=sorted(KIND_TAGS), required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--folder")
    parser.add_argument("--path")
    parser.add_argument("--course")
    parser.add_argument("--summary", default="One-line summary.")
    parser.add_argument("--status", default="active")
    parser.add_argument("--lesson-index", type=int, default=1)
    parser.add_argument("--key-question", default="Central question.")
    parser.add_argument("--concept", action="append")
    parser.add_argument("--difficulty-type", action="append")
    parser.add_argument("--transfer-context", action="append")
    parser.add_argument("--profile-candidate", action="store_true")
    parser.add_argument("--evidence-level", default="lesson-local")
    parser.add_argument("--common-confusion", default="Most likely confusion.")
    parser.add_argument("--mastery-signal", default="What the user can do when stable.")
    parser.add_argument("--target-file", default="global-profile.md")
    parser.add_argument("--profile-area", action="append")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    path = note_path(args)
    content = build_note(args)
    if args.dry_run:
        print(content)
        return 0
    if path.exists() and not args.overwrite:
        raise SystemExit(f"refusing to overwrite existing note: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if args.verify:
        verify(path, Path(args.vault).expanduser().resolve())
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
