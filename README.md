# Codex Teach Profile Skills

Personalized learning skills for Codex. This package combines a course
workspace skill with a stable learner-profile layer so Codex can teach across
multiple sessions without turning every lesson note into permanent profile
memory.

## About

`teach-profile-skills` is for people who use Codex as a long-running learning
partner. It gives Codex two coordinated skills:

- `teach`: manages one learning workspace at a time, including the mission,
  resources, lesson artifacts, reusable references, glossary terms, and learning
  records.
- `learner-profile-teach`: loads stable learner preferences before teaching,
  adapts explanations to durable goals and work contexts, and reviews evidence
  after five substantial lessons before proposing profile updates.

The core idea is a clean separation:

```text
learner-profile-teach -> stable cross-course learner model
teach -> current course execution and lesson evidence
external notes app -> durable review notes when requested
```

This keeps the learner profile useful without letting temporary moods, one-off
topics, or private project details become global memory by accident.

## What's Included

```text
skills/
  teach/
    SKILL.md
    *-FORMAT.md
  learner-profile-teach/
    SKILL.md
    agents/openai.yaml
    references/
    templates/
docs/
  INSTALL.md
  CUSTOMIZATION.md
  REPOSITORY_METADATA.md
```

## Install

Use the installer:

```bash
./scripts/install.sh
```

Or copy the skills manually:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/teach "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/learner-profile-teach "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex after installation if your environment does not reload skills
automatically.

For more detail, see [docs/INSTALL.md](docs/INSTALL.md).

## Personalize

Before using `learner-profile-teach`, copy the package locally and edit:

- `skills/learner-profile-teach/references/global-profile.md`
- `skills/learner-profile-teach/references/research-workflow.md`
- `skills/learner-profile-teach/references/cognition-and-planning.md`

Keep these files concise. Store stable cross-course patterns there, not
lesson-by-lesson notes.

For guidance, see [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md).

## Recommended Use

Ask Codex:

```text
Use $learner-profile-teach and $teach to teach me <topic>.
```

At the end of each substantial lesson, Codex should ask you to:

1. explain the core concept in your own words,
2. transfer it to a personal research, engineering, management, planning, or
   life scenario,
3. name one unclear, uncertain, or disputable point.

After every five substantial lessons, Codex should review the recent lesson
evidence and decide whether a profile update proposal is warranted.

## Safety And Privacy

This public package contains templates only. Replace placeholder examples with
your own information locally. Do not commit personal learner profiles, private
research details, note-vault paths, client data, or project-specific secrets
unless you intend them to be public.

## Repository About Metadata

GitHub's right-side About panel is repository metadata, not a normal markdown
section. Suggested values are in
[docs/REPOSITORY_METADATA.md](docs/REPOSITORY_METADATA.md).

## Contributing

Issues and pull requests are welcome. Please keep the split between stable
profile memory and course-local evidence clear. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
