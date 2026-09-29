---
name: pr-describe
description: Write the Done and How to reproduce sections of a pull request from the diff before Draft is removed. Use when the student says "опиши PR", "заполни Done", "describe the PR".
---
# pr-describe

1. Read the PR's Plan section, the full diff against `main` (`git diff main...HEAD`), the commit
   messages and the linked issue.
2. Write Done: three to eight lines on what changed and why, grouped by concern; name a file only
   where the reviewer must look. State every deviation from the Plan explicitly.
3. Fill How to reproduce: the exact command with its config, where the data comes from, the MLflow
   run id with the numbers. Take the numbers from the run, never from memory.
4. Never edit the Plan section or the `Closes #N` line. Leave Draft in place: the student removes it.
5. Show the text; the student pastes it or lets you apply it with `gh pr edit --body-file`.
