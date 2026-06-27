# About Codex Teach Profile Skills

`teach-profile-skills` is a small Codex skill package for personalized,
multi-session learning.

It exists because good teaching needs two kinds of memory:

- stable learner context that should carry across courses,
- course-local evidence that should stay tied to one learning mission.

The package keeps those layers separate.

## The Problem

A long-running learning assistant can easily overfit to recent conversations.
It may treat a temporary mood, a single difficult lesson, or a narrow project
detail as a permanent learner trait. It can also lose useful teaching context
between sessions if every course starts from scratch.

This repository provides a disciplined middle path:

- durable learner preferences live in `learner-profile-teach`,
- current course work lives in `teach`,
- profile updates require repeated evidence or explicit user confirmation.

## The Skills

### `teach`

The `teach` skill creates and maintains a course workspace. It helps Codex keep
track of:

- a concrete learning mission,
- trusted resources,
- lesson artifacts,
- reusable references,
- glossary terms,
- learning records backed by observed evidence.

### `learner-profile-teach`

The `learner-profile-teach` skill personalizes teaching before a lesson starts.
It reads stable profile references, applies the relevant teaching or research
workflow, and asks for self-explanation after substantial lessons.

After five substantial lessons, it reviews the evidence and proposes profile
updates only when the pattern is stable and useful across future work.

## Design Principles

- Keep stable profile memory separate from course-local notes.
- Prefer observed learning evidence over vague summaries.
- Ask the learner to self-explain before making strong inferences.
- Use high-trust sources when the topic needs precision.
- Do not silently write personal profile facts.

## Who This Is For

This package is useful if you want Codex to help with:

- learning a technical field over multiple sessions,
- building a course around a concrete mission,
- connecting concepts to research, engineering, planning, or management work,
- preserving useful teaching preferences without exposing private details,
- reviewing lesson evidence before updating a stable learner profile.

## What This Is Not

This is not a full learning management system. It is also not a memory database.
It is a lightweight set of Codex skill instructions and templates that make
teaching sessions more consistent, reviewable, and privacy-aware.
