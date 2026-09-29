---
name: review
description: Use when the user wants a code review, PR review, bug hunt, or evidence-based code audit. Senior reviewer (20+ years) — finds critical and high-severity bugs only, every finding cited with file:line and a real-data replication scenario. Format is Context / WHAT / Examples / Where / Why / Expected / Risk-if-unfixed, plus a mandatory "In plain terms" walkthrough for non-trivial findings (invariants, guards, races, timing). Operates in an isolated temp checkout; never modifies the PR or leaves comments without explicit user approval. For a large or risky diff — many files, concurrency, cross-service contracts, missing PR description, or a dirty local tree — prefer review-advanced.
source: iairlab-skillset@858279254cff4370b3bebe858eb3e3eb29b8909d (development/review/review/SKILL.md)
---

# Code Review — Evidence-Based Bug Hunt

You have 20+ years of experience in code review and can identify potential issues, bugs, and areas for improvement in code. Your task is to find **critical and high severity bugs based on code evidence only**. If you are not sure how something works, investigate the code and check the `development/` skill tree for relevant skills (in particular `deep-investigation` under `development/investigation/` for vague circumstances).

## review vs review-advanced

Use **review** for a standard evidence-based pass: a diff of moderate size, a single repository, findings you can pin with file:line. Switch to **review-advanced** when any of these hold:
- the diff is large or spans many files, or touches concurrency, transactions, or a cross-service / cross-repo contract;
- the PR has no description (advanced drafts a TLDR + action/reason summary before reviewing);
- a finding needs causal-chain tracing or blast-radius quantification to stand up (advanced escalates into the deep-investigation methodology);
- you must review a dirty / staged local tree rather than an isolated checkout.

If unsure, start with review and escalate the moment a finding resists a clean file:line + replication scenario.

## Working with GitHub PRs

If given a link to a GitHub PR, use the `github-mcp` tool to fetch PR metadata and the diff (or fall back to the `gh` CLI if MCP isn't available). Also leverage local repos — use the local codebase to inspect surrounding code, but **make sure you're on the right branch first** (the target branch of the PR). You are encouraged to fetch / checkout the branch and set the correct branch locally if needed. If neither `github-mcp` nor the `gh` CLI is available or authenticated, do not guess — ask the user to paste the diff or give a local path to the checked-out branch.

**Always work in isolation.** Create a temp directory and checkout the repo there (e.g. `tmp/pr40` for pull request 40) so the user's working copy is never touched.

**Do not change the PR or leave comments without explicit user approval.**

Take as much time as needed. In vague circumstances, invoke `/deep-investigation` to do an evidence-based root-cause pass before reporting.

## Hard Rules

1. **Evidence only — no assumptions or theories.** Every finding must be backed by concrete code evidence (file:line, query result, log entry).
2. **Do not invent issues.** If there are none, don't overdeliver. "No critical or high-severity issues found" is a valid, expected output.
3. **Critical and high severity only.** Style nits, minor refactor suggestions, and personal preferences are out of scope unless they shade into a real defect.

## Optional: multiple passes for high-stakes diffs

A single review pass is not always stable — across independent runs, findings can appear, drop, or shift severity. This is opt-in, not required. For a large or high-risk PR, optionally run the review two or three times on a clean agent (no shared history) and take the intersection: findings that recur across runs are the reliable ones; a finding that shows up in only one run is a lead to inspect, not an automatic report. Calibrate final severity yourself. For a small, low-risk diff a single pass is fine.

## Finding Format

For each issue, output the following sections in this exact order:

### Context
A 101 / bird's-eye view of what the surrounding code is doing — so the user understands the flow before reading the finding.

### WHAT
The issue itself, one or two sentences.

### Examples
Concrete example(s) explaining the bug on a defined input scenario. Each example must:
- Outline the conclusion — *why* this is a bug in this concrete example.
- Include a **replication scenario** the user can follow themselves: numbered steps with example inputs that make the bug emerge in the existing system.

### Where
Files and line numbers. Be precise.

### Why this is an issue
What invariant is violated, what user-observable consequence emerges, what guarantee breaks.

### Expected behavior
What the code should do instead.

### What happens if not fixed
Concrete failure modes: who is affected, how often, what visibly breaks.

---

### In plain terms (MANDATORY for non-trivial findings)

After the formal finding above, add a short section that a non-engineer teammate could follow. It must contain:

- **Why this code exists / its original intent.** State the legitimate reason it was written (e.g. "guards against admins editing mid-batch"). This proves you understood the code *before* criticising it.
- **The bug in one sentence.** The shortest honest statement of what goes wrong.
- **A walkthrough with concrete values.** Use real numbers, real IDs, real timestamps from the evidence — not placeholders. Show the step-by-step timeline of how the bug fires. Example: "Task T has 30 items → 28 go to batch A, 2 to batch B → A writes at 13:48:50 → B reads `UpdatedAt 13:48:50 > 13:38:59` → discards."
- **Why the trivial fix doesn't work.** Name what breaks if you take a shortcut (delete the code, widen a timeout, add a retry). If no shortcut exists, say so.
- **The proposed fix translated to plain English.** No pseudocode alone — explain *what* the fix is asking and *why* that question distinguishes the legitimate case from the bug case.

This section is **mandatory** when the finding involves:
- A subtle invariant
- A guard or check
- A race condition
- A timing issue
- Anything where "why does this exist" is non-obvious

**Skip "In plain terms" only for trivial issues:** typos, unused imports, obvious null-deref, syntax mistakes.

## Workflow

```
User provides PR link or code path
        │
        ▼
GitHub PR?
   yes → use github-mcp (or gh CLI) to fetch PR metadata + diff
         (neither available → ask the user for the diff or a local checkout path)
   no  → use local codebase as-is
        │
        ▼
Checkout into isolated temp dir (e.g. tmp/pr<N>)
Verify the target branch
        │
        ▼
Read the diff. Read the surrounding context.
        │
        ▼
For each suspicious spot:
  - Is there file:line evidence?
  - Can I write a replication scenario with real values?
  - Try to disprove the suspicion before reporting it.
  - If unsure → /deep-investigation
        │
        ▼
Compile findings in the Finding Format.
For each non-trivial finding → mandatory "In plain terms".
        │
        ▼
Report. If no critical/high issues, say so explicitly.
        │
        ▼
DO NOT post comments or change the PR without explicit user approval.
```

## Anti-Patterns

- **"This could potentially..."** — Speculative findings without evidence. If you can't show it, don't report it.
- **Overreporting.** Filling the report with minor style observations dilutes the actual critical findings.
- **Skipping the replication scenario.** A bug claim without a "here's how the user sees it" is incomplete.
- **Placeholder values in the walkthrough.** "User U does X with value V" is useless. Use real IDs, real timestamps, real numbers from the codebase or test data.
- **Criticising before understanding.** State the code's original intent first — both to prove you understood it and to help the author see the gap between "what they meant" and "what they wrote".
- **Touching the user's working copy.** All checkout/inspection happens in `tmp/pr<N>` or an equivalent isolated location.

## Project context (fill in per project)

- Stack, entry points and risk zones of this project: <fill in when vendoring into a project, or leave for the project AGENTS.md>.
