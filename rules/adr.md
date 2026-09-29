# Decision records (ADR)

- One file per decision in `docs/adr/NNNN-short-title.md`; a four-digit consecutive number that is
  never reused; the title names the problem and the chosen solution. Template: `docs/adr/0000-template.md`.
- You draft the record when asked, from the discussion, the PR thread and the code; the student
  reviews it like code. Never write one unprompted, never skip one when a decision is made.
- Status `proposed` in the feature branch, `accepted` in the same PR before merge; a rejected record
  is merged too, with the reason.
- An accepted record is never edited. A change is a new record with the old one marked
  `superseded by ADR-NNNN`, linked both ways.
- What deserves a record: repository structure and data flow; a library, framework or tool; an
  interface or data contract; the baseline, the primary metric, the dataset and its split; a
  direction closed by a negative result. A single hyperparameter run is an MLflow run.
- When an option the supervisor suggested is rejected, fill "Pros and cons of the options".
- Link the MLflow experiment or run that motivated the decision.
