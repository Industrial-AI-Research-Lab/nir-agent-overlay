---
name: experiment-issue
description: Open a GitHub issue for one experiment from the Experiment form and add it to the project board. Use when the student says "заведи эксперимент", "создай issue на гипотезу", "open an experiment issue".
---
# experiment-issue

One hypothesis, one issue, nested under the checkpoint's parent issue.

1. Collect: the hypothesis (one sentence), the setup (data, baseline, metric), the expected result.
   Ask for what is missing; never invent it.
2. Create the issue with the form's fields as the body and the title `exp: <short hypothesis>`:

   ```bash
   gh issue create --title "exp: <short hypothesis>" \
     --body "$(printf '## Hypothesis\n%s\n\n## Setup\n%s\n\n## Expected result\n%s\n' "<hypothesis>" "<setup>" "<expected>")" \
     --project "<board title>"
   ```

   `--project` takes the board title. If it fails with a scope error, run `gh auth refresh -s project`
   once and retry.
3. When the student names the checkpoint issue, add the new issue as its sub-issue (GitHub UI or the
   sub-issues API).
4. Report the issue number: it goes into the PR as `Closes #N` and into the MLflow run note.
5. At the end of the experiment the student closes the issue with the outcome and its
   interpretation; a negative result is closed as completed, not as not planned.
