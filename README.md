# Codex Teach Profile Skills

This repository contains two Codex skills for personalized, stepwise learning:

- `teach`: a course workspace skill for mission-driven lessons, resources, learning records, and reviewable lesson artifacts.
- `learner-profile-teach`: a companion profile skill that reads a stable learner model before teaching, asks for learner self-explanation after each substantial lesson, and performs a five-lesson review before proposing profile updates.

The skills are designed to work together:

```text
learner-profile-teach -> stable learner model
teach -> current course execution
external notes app -> durable notes and review material
```

## Install

Copy both skill folders into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/teach "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/learner-profile-teach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installation if your environment does not reload skills automatically.

## Personalize

Before using `learner-profile-teach`, edit:

- `skills/learner-profile-teach/references/global-profile.md`
- `skills/learner-profile-teach/references/research-workflow.md`
- `skills/learner-profile-teach/references/cognition-and-planning.md`

Keep the files concise. Store stable cross-course patterns there, not lesson-by-lesson notes.

## Recommended Use

Ask:

```text
Use $learner-profile-teach and $teach to teach me <topic>.
```

At the end of each substantial lesson, the assistant should ask you to explain the concept in your own words, transfer it to a real scenario, and name what is still unclear. After every five substantial lessons, it should decide whether a profile update proposal is warranted.

## Privacy

This public package contains templates only. Replace placeholder examples with your own information locally. Do not commit personal learner profiles, private research details, note-vault paths, or project-specific data unless you intend them to be public.

