---
name: teach
description: Teach the user a new skill or concept over multiple sessions. Use when the user asks to learn, study, continue a course, create lessons, build a learning path, or practice a concept with feedback. Maintains a teaching workspace with mission, resources, lessons, learning records, reference documents, and optional note-app mirroring.
---

# Teach

The user has asked to learn something over time. Treat the current directory as a teaching workspace and maintain learning state there.

## Teaching Workspace

Use these files and folders:

- `MISSION.md`: why the user is learning this topic. Use `MISSION-FORMAT.md`.
- `RESOURCES.md`: trusted resources for this topic. Use `RESOURCES-FORMAT.md`.
- `NOTES.md`: teaching notes and user preferences that are local to this course.
- `learning-records/*.md`: durable records of demonstrated understanding, prior knowledge, corrected misconceptions, or mission shifts. Use `LEARNING-RECORD-FORMAT.md`.
- `lessons/*.html`: short, self-contained lesson artifacts.
- `reference/*.html` or `reference/*.md`: concise review references, cheat sheets, glossaries, algorithms, or concept cards.
- `GLOSSARY.md` when a canonical vocabulary is useful. Use `GLOSSARY-FORMAT.md`.

## Optional Note-App Mirror

If the user asks to mirror lessons, thoughts, derivations, or progress into a note app, treat that mirror as part of the deliverable.

- Ask for or infer the note destination only when appropriate.
- Keep mirrored notes recall-oriented: concise headings, key definitions, small examples, and self-test questions.
- Verify mirrored files exist before finishing.
- Keep the note mirror separate from the workspace so course artifacts and review notes have clear roles.

## Teaching Philosophy

Deep learning needs:

- knowledge from high-quality sources,
- skills built through practice and feedback,
- wisdom from real-world use and community interaction when relevant.

Do not rely only on parametric memory when the topic needs current, precise, or source-grounded knowledge. Populate `RESOURCES.md` with high-trust sources early.

## Mission First

Every lesson should serve the mission. If the user has not explained why they want to learn the topic, ask enough to write a concrete `MISSION.md`.

Good missions are observable and practical:

- "Ship a Rust CLI to my team" is better than "learn Rust".
- "Read and critique papers in this field" is better than "understand the field".

Revise `MISSION.md` when the user's goal changes, and create a learning record for meaningful mission shifts.

## Lesson Design

A lesson is the main unit of teaching. It should be short, beautiful, and useful for review.

Each lesson should:

1. teach one tightly scoped concept or skill,
2. connect to the mission,
3. introduce only the necessary knowledge,
4. include practice or retrieval,
5. provide feedback when the user responds,
6. link to relevant references or prior lessons,
7. recommend at least one high-trust resource when appropriate.

Prefer small steps. Working memory is limited; durable learning benefits from retrieval, spacing, interleaving when appropriate, and desirable difficulty.

## Learning Records

Write learning records only when there is evidence:

- the user demonstrated understanding,
- the user disclosed meaningful prior knowledge,
- a misconception was corrected,
- the mission shifted.

Do not write records for mere coverage. Learning records are decision-grade signals for future teaching, not session logs.

## Reference Documents

Create reference documents for reusable knowledge:

- glossaries,
- algorithms,
- syntax cards,
- concept maps,
- procedures,
- exercises,
- review sheets.

Reference documents should compress what the user can return to later. They should not duplicate every lesson.

## Feedback Loop

When possible, end lessons with a user action: explain, solve, apply, compare, or transfer. Use the response to decide whether to correct, deepen, or move on.

