# Lab overlay: shared instructions for LLM assistants

These instructions apply on top of the project's own AGENTS.md; the project's file wins on conflict.
Rules by topic are in `rules/`, skills in `skills/`.

## Working cycle

1. Start from a fresh `main`: branch `<type>/<short-description>`, types feat, fix, refactor, docs,
   test, chore, exp. One branch per change.
2. Small steps. Run `make check` after edits and before finishing; never `--no-verify`.
3. Before a PR: apply the `pre-ship` skill to the diff, then write the Done section with `pr-describe`.
4. A decision that changes structure, tooling, data, metric or baseline: draft an ADR with
   `write-adr`; the student reviews it.
5. Experiments: one issue per hypothesis (`experiment-issue`), one MLflow run per execution,
   `Closes #N` in the PR.
6. Meetings: `meeting-record` turns a transcript into `docs/meetings/YYYY-MM-DD.md`.

## What you must not do

- Read, print or copy `.env`, keys, tokens; write secrets into files, logs or PR text.
- Commit data, weights, generated logs, `mlruns/`, personal agent files.
- Rewrite pushed history on `main`, force-push, squash during review.
- Edit an accepted ADR or the Plan section of a PR; remove Draft; resolve review threads; merge.
- Invent results: every number comes from an MLflow run that you name.

## Language

Code, identifiers, commit messages and PR titles in English. Documents in the language the student
writes them in; keep the language of a file you edit.
