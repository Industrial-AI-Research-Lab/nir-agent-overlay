# nir-agent-overlay

[Русская версия](README.ru.md)

Shared instructions, rules and skills for LLM assistants in the lab's student research projects (NIR). A project connects the overlay as a submodule pinned to a tag; a rule fixed here reaches every project on its next version bump.

## What is inside

- [AGENTS.md](AGENTS.md) — the shared instructions; a project imports them.
- [rules/](rules) — one topic per file: python-style, experiments-mlflow, adr, commits, pr, security.
- [skills/](skills) — write-adr, experiment-issue, meeting-record, pr-describe; pre-ship and review are copied from the lab skill set, see [skills/VENDORED.md](skills/VENDORED.md).
- [hooks/settings.json](hooks/settings.json) — a fragment for the project's `.claude/settings.json`: deny reading `.env`, run `make check` on Stop while the working tree is dirty.

## Connecting

From the [project template](https://github.com/Industrial-AI-Research-Lab/nir-project-template): `make overlay` (the version is pinned in the Makefile). By hand:

```bash
git submodule add https://github.com/Industrial-AI-Research-Lab/nir-agent-overlay.git .agents/overlay
git -C .agents/overlay checkout v0.1.0
mkdir -p .claude/rules && ln -s ../../.agents/overlay/rules .claude/rules/overlay
printf '\n@.agents/overlay/AGENTS.md\n' >> CLAUDE.md
git add .gitmodules .agents/overlay .claude/rules/overlay CLAUDE.md
```

Clone a project with `--recurse-submodules`, otherwise the overlay folder stays empty. Windows without symlink rights: skip the link and import the rules file by file in CLAUDE.md, `@.agents/overlay/rules/<name>.md`. A skill becomes visible to Claude Code through a symlink `.claude/skills/<name>` → `../../.agents/overlay/skills/<name>`.

## Which agent reads what

| Agent | Reads | How to connect the overlay |
|---|---|---|
| Claude Code | CLAUDE.md, `.claude/rules/`, `.claude/skills/` | `@.agents/overlay/AGENTS.md` in CLAUDE.md; the symlink `.claude/rules/overlay`; skills by symlink |
| Codex | AGENTS.md | a line in the project's AGENTS.md: "Also follow `.agents/overlay/AGENTS.md` and `.agents/overlay/rules/`" |
| Cursor | AGENTS.md, `.cursor/rules/` | the same line; or copy the rules into `.cursor/rules/` as `.mdc` files |
| GitHub Copilot | AGENTS.md, CLAUDE.md, `.github/copilot-instructions.md` | the same line in AGENTS.md |

## Versions

Tags `vMAJOR.MINOR.PATCH`, history in [CHANGELOG.md](CHANGELOG.md). A project moves to a new version through a PR: switch the submodule to the new tag on a `chore/...` branch.

## Before connecting an overlay you did not write

Read the source of every file, not only its rendering; look for commands in hooks and skills that send anything outside the repository; pin a tag or a commit; keep a LICENSE at the root.

## Licence

MIT.
