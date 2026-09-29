# Pull requests

- One branch, one PR; title `<type>: short description`; Draft until the work is ready.
- Template sections: Plan (the student writes it by hand and it is never edited afterwards), Done
  (you write it from the diff before Draft is removed), How to reproduce (the command with its
  config, the data source, the MLflow run id with the numbers), `Closes #N`.
- During review: fixes in separate commits, no squash or rebase; a reply under every thread that
  says what changed and in which commit.
- You never remove Draft, resolve review threads, request review or merge; the student does.
- Disagreeing with a review comment: facts and trade-offs, two or three options; an architectural
  disagreement becomes an ADR.
