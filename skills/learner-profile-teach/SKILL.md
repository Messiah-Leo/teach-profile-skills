---
name: learner-profile-teach
description: Personalized teaching companion for the teach skill. Use when the user asks to learn a topic, continue a lesson, design a course, do research derivation, connect knowledge to their work, code engineering, tool integration, management decisions, planning, emotion regulation, or cognitive improvement. Reads a stable learner profile before teach-style step-by-step instruction, requires learner self-explanation at the end of lessons, and performs a five-lesson review before proposing profile updates.
---

# Learner Profile Teach

Use this skill as a personalization layer around `teach`. It supplies a stable learner model that shapes lesson design, feedback, pacing, and profile update decisions.

Core split:

- `learner-profile-teach`: stable cross-course learner model.
- `teach`: current course workspace, mission, resources, lessons, and learning records.
- external notes app: durable notes, derivations, concept cards, and review material when requested.

## Loading Workflow

At the start of a learning, teaching, research, planning, or cognition task:

1. Read `references/global-profile.md`.
2. Read `references/teaching-protocol.md` for lessons, courses, "next lesson", or teaching requests.
3. Read `references/research-workflow.md` for research, derivation, engineering, implementation, validation, or tool-integration work.
4. Read `references/cognition-and-planning.md` for planning, future direction, decision-making, emotion regulation, or cognitive improvement.
5. Read the current teach workspace state when available: `MISSION.md`, `NOTES.md`, `learning-records/`, relevant `lessons/`, and `reference/`.
6. Treat the current user message as higher priority than older profile notes.

Load only relevant references. Do not load every reference for simple tasks.

## Lesson Protocol

When teaching, follow `references/teaching-protocol.md`.

Every substantial lesson should end by asking the learner to answer in their own words:

1. Explain the core concept of this lesson.
2. Transfer it to one personal research, engineering, management, planning, or life scenario.
3. Name one unclear, uncertain, or disputable point.

Use the answer to identify knowledge boundaries, pace, interests, and difficulty patterns. Keep ordinary lesson outcomes in the teach workspace or notes app; do not immediately update the global profile.

## Five-Lesson Review

Do not update the stable learner profile after every lesson.

After every five substantial lessons in a learning thread:

1. Read `references/update-protocol.md`.
2. Use `templates/five-lesson-review.md`.
3. Inspect the last five lesson notes, learning records, and self-explanations.
4. Decide whether there is stable cross-course evidence worth proposing as a profile update.
5. If yes, draft a proposal with `templates/profile-update-proposal.md`.
6. Ask the user to confirm before editing profile references.

No silent profile updates.

## Update Discipline

Record stable profile facts only when they are:

- stable across multiple interactions,
- useful across future courses or research tasks,
- likely to improve teaching or collaboration,
- supported by user statements or repeated evidence,
- not merely a temporary mood, single lesson topic, or unconfirmed inference.

When in doubt, keep information in the current teach workspace.

