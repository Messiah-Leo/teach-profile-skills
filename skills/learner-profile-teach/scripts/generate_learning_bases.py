#!/usr/bin/env python3
"""Generate Obsidian Bases for the Codex learning system."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


def default_vault() -> Path:
    configured = os.environ.get("OBSIDIAN_VAULT") or os.environ.get("OBSIDIAN_VAULT_PATH")
    return Path(configured).expanduser() if configured else Path.home() / "Documents" / "Coffers"


DEFAULT_VAULT = default_vault()

BASES = {
    "Codex Learning.base": """filters:
  and:
    - file.hasTag("codex/lesson")
    - '!file.path.contains("Templates")'
    - '!file.path.contains("_setup/")'
    - '!file.path.contains("/templates/")'
properties:
  file.name:
    displayName: Lesson
  note.course:
    displayName: Course
  note.lesson_index:
    displayName: Index
  note.status:
    displayName: Status
  note.summary:
    displayName: Summary
  note.difficulty_type:
    displayName: Difficulty
  note.transfer_context:
    displayName: Transfer
  note.profile_candidate:
    displayName: Profile Candidate
  note.evidence_level:
    displayName: Evidence
  note.updated:
    displayName: Updated
views:
  - type: table
    name: All lessons
    order:
      - file.name
      - course
      - lesson_index
      - status
      - summary
      - difficulty_type
      - transfer_context
      - profile_candidate
      - evidence_level
      - updated
    sort:
      - property: updated
        direction: DESC
      - property: file.name
        direction: ASC
    columnSize:
      file.name: 260
      note.course: 220
      note.summary: 360
  - type: table
    name: Needs review
    filters:
      and:
        - 'status == "needs-review"'
    order:
      - file.name
      - course
      - summary
      - difficulty_type
      - updated
  - type: table
    name: Profile candidates
    filters:
      and:
        - "profile_candidate == true"
    order:
      - file.name
      - course
      - summary
      - evidence_level
      - updated
  - type: table
    name: By difficulty type
    groupBy:
      property: note.difficulty_type
      direction: ASC
    order:
      - file.name
      - course
      - difficulty_type
      - summary
  - type: table
    name: By transfer context
    groupBy:
      property: note.transfer_context
      direction: ASC
    order:
      - file.name
      - course
      - transfer_context
      - summary
""",
    "Codex Concepts.base": """filters:
  and:
    - file.hasTag("codex/concept")
    - '!file.path.contains("Templates")'
    - '!file.path.contains("_setup/")'
    - '!file.path.contains("/templates/")'
properties:
  file.name:
    displayName: Concept Note
  note.concept:
    displayName: Concept
  note.status:
    displayName: Status
  note.summary:
    displayName: Definition
  note.common_confusion:
    displayName: Common Confusion
  note.domain_context:
    displayName: Domain
  note.mastery_signal:
    displayName: Mastery Signal
  note.updated:
    displayName: Updated
views:
  - type: table
    name: All concepts
    order:
      - file.name
      - concept
      - status
      - summary
      - common_confusion
      - domain_context
      - mastery_signal
      - updated
    sort:
      - property: file.name
        direction: ASC
    columnSize:
      file.name: 240
      note.summary: 360
      note.common_confusion: 300
  - type: table
    name: Immature concepts
    filters:
      and:
        - 'status != "reviewed"'
    order:
      - file.name
      - concept
      - summary
      - mastery_signal
  - type: table
    name: Confusion map inputs
    order:
      - file.name
      - concept
      - common_confusion
      - related_lessons
""",
    "Codex Profile Proposals.base": """filters:
  and:
    - file.hasTag("codex/profile-proposal")
    - '!file.path.contains("Templates")'
    - '!file.path.contains("_setup/")'
    - '!file.path.contains("/templates/")'
properties:
  file.name:
    displayName: Proposal
  note.status:
    displayName: Status
  note.target_file:
    displayName: Target
  note.summary:
    displayName: Summary
  note.evidence_level:
    displayName: Evidence
  note.profile_area:
    displayName: Profile Area
  note.requires_confirmation:
    displayName: Requires Confirmation
  note.updated:
    displayName: Updated
views:
  - type: table
    name: Pending proposals
    filters:
      and:
        - 'status == "pending"'
    order:
      - file.name
      - target_file
      - summary
      - evidence_level
      - profile_area
      - requires_confirmation
      - updated
    sort:
      - property: updated
        direction: DESC
  - type: table
    name: Accepted proposals
    filters:
      and:
        - 'status == "accepted"'
    order:
      - file.name
      - target_file
      - summary
      - updated
  - type: table
    name: Rejected proposals
    filters:
      and:
        - 'status == "rejected"'
    order:
      - file.name
      - target_file
      - summary
      - updated
""",
    "Codex Review Queue.base": """filters:
  and:
    - '!file.path.contains("Templates")'
    - '!file.path.contains("_setup/")'
    - '!file.path.contains("/templates/")'
    - or:
        - file.hasTag("codex/lesson")
        - file.hasTag("codex/review")
        - file.hasTag("codex/profile-proposal")
properties:
  file.name:
    displayName: Note
  note.type:
    displayName: Type
  note.status:
    displayName: Status
  note.course:
    displayName: Course
  note.summary:
    displayName: Summary
  note.profile_candidate:
    displayName: Profile Candidate
  note.updated:
    displayName: Updated
views:
  - type: table
    name: Needs review
    filters:
      and:
        - 'status == "needs-review"'
    order:
      - file.name
      - type
      - course
      - summary
      - updated
  - type: table
    name: Pending self-explanation
    filters:
      and:
        - 'status == "active"'
        - file.hasTag("codex/lesson")
    order:
      - file.name
      - course
      - summary
      - updated
  - type: table
    name: Recent learning notes
    order:
      - file.name
      - type
      - status
      - course
      - summary
      - updated
    sort:
      - property: updated
        direction: DESC
      - property: file.name
        direction: ASC
""",
}


def generate(vault: Path, overwrite: bool) -> list[Path]:
    base_dir = vault / "Categories" / "Base"
    base_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for name, content in BASES.items():
        path = base_dir / name
        if path.exists() and not overwrite:
            continue
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=str(DEFAULT_VAULT))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists():
        raise SystemExit(f"vault does not exist: {vault}")
    written = generate(vault, args.overwrite)
    for path in written:
        print(path)
    if not written:
        print("No base files changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
