# Contributing

Thanks for improving `teach-profile-skills`.

## Good Contributions

- Clearer teaching protocols.
- Better templates for lesson review or profile update proposals.
- Safer privacy guidance.
- Installation and documentation fixes.
- Small examples that show the split between profile memory and course-local
  evidence.

## Design Rules

- Keep stable learner profile files separate from course workspace files.
- Do not encourage silent profile updates.
- Do not store lesson-by-lesson notes in global profile references.
- Prefer concise, reusable instructions over broad personality descriptions.
- Avoid committing private learner data, client data, note-vault paths, API
  tokens, or local machine details.

## Development Workflow

1. Edit the relevant skill, reference, template, or doc.
2. Run a basic repository check:

   ```bash
   git status --short
   git ls-files | sort
   ```

3. Install the skills into a local Codex environment.
4. Start a test chat with:

   ```text
   Use $learner-profile-teach and $teach to teach me one small topic.
   ```

5. Confirm that Codex loads the profile layer before teaching and keeps
   course-local evidence out of the stable profile.

## Pull Requests

In a pull request, include:

- what changed,
- why it helps,
- any privacy or profile-update behavior affected,
- how you tested the change.
