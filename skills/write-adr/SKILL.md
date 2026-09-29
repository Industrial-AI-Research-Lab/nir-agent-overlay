---
name: write-adr
description: Draft an architecture decision record (ADR) in docs/adr/ from the discussion, the PR thread and the code. Use when the student says "запиши решение", "сделай ADR", "write an ADR", or when a decision changes structure, tooling, data, metric or baseline.
---
# write-adr

1. Find the next number: the highest `NNNN` in `docs/adr/` plus one; never reuse a number.
2. Copy `docs/adr/0000-template.md` to `docs/adr/NNNN-<short-title>.md`; the title names the
   problem and the chosen solution.
3. Fill the sections from the sources you have: the conversation, the PR thread, the code, the
   MLflow experiment or run that motivated the decision (link it). Status `proposed`, today's date,
   decision-makers the student, consulted the supervisor.
4. Considered options: at least two. When an option suggested by the supervisor is rejected, fill
   "Pros and cons of the options" with the reason.
5. If the record supersedes an older one: the old status becomes `superseded by ADR-NNNN` and the
   two files link to each other. Change nothing else in an accepted record.
6. Show the file to the student for review. It is committed in the feature branch and becomes
   `accepted` in the same PR before merge.
