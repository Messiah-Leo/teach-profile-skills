# Update Protocol

## Default Rule

Do not update the stable learner profile after every lesson.

After every five substantial lessons in a learning thread, review whether a profile update is warranted. The review may decide that no update is needed.

## What Counts As A Substantial Lesson

A lesson counts when it includes a coherent concept or skill unit and the learner has a chance to respond, practice, or self-explain.

Short clarifications, one-off answers, formatting help, or administrative tasks do not count.

## Evidence Required For Profile Updates

Propose a profile update only when evidence is:

- repeated across multiple lessons, or
- explicitly stated by the user as a preference or goal, or
- clearly cross-course useful, or
- likely to materially improve future teaching or collaboration.

## Good Profile Update Candidates

- Stable learning preferences.
- Interest patterns.
- Recurring difficulty patterns.
- Preferred transfer contexts.
- Research or work workflow changes.
- Toolchain or implementation workflow changes.
- Long-term planning or cognition patterns explicitly confirmed by the user.
- User-confirmed instructions such as "remember this" or "teach me this way".

## Poor Profile Update Candidates

- A single lesson topic.
- A temporary mood.
- One-off task details.
- File paths or project details unlikely to recur.
- Unconfirmed psychological labels.
- Private or sensitive inferences not explicitly confirmed.
- Anything that belongs only in the current course workspace.

## Five-Lesson Review Procedure

1. Gather the last five substantial lessons, self-explanations, learning records, and notes if available.
2. Identify interest signals, difficulty signals, pacing signals, and transfer-context signals.
3. Separate course-local facts from global learner-profile candidates.
4. Draft a profile update proposal only if there is enough evidence.
5. Ask the user to confirm before changing profile references.
6. If confirmed, edit the relevant reference file and briefly note what changed.

## File Targets

- `global-profile.md`: identity, durable goals, broad workstream, stable cross-course profile.
- `research-workflow.md`: field-specific research, implementation, validation, or integration patterns.
- `teaching-protocol.md`: teaching style, self-explanation, concept coverage, pacing.
- `cognition-and-planning.md`: planning, direction, emotion regulation, and cognitive methodology patterns.

## Proposal Requirement

Use `templates/profile-update-proposal.md` before editing stable profile files unless the user explicitly instructs an exact update.

