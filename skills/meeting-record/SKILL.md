---
name: meeting-record
description: Turn a meeting transcript into a meeting record in docs/meetings/ (clean the transcript, sanitize it, extract decisions with time codes and actions, check the result). Use when the student says "сделай запись встречи", "оформи протокол", "make the meeting record".
---
# meeting-record

Work only from the transcript the student gives you; add no knowledge of your own. Every decision
carries a time code and the speaker.

1. **Clean.** Fix recognition errors in the project terms the student lists. Do not change the
   meaning, shorten or add lines; mark unclear passages as `[unclear, MM:SS]`.
2. **Sanitize.** Replace the names of everyone except the student and the supervisor with roles in
   square brackets, one label per person throughout. Remove passwords, keys, tokens, internal
   addresses, partner data, grades and personal topics. Give the student the table
   "original name → label" separately; it is never committed.
3. **Extract.** Quote verbatim the lines where a decision was taken or an action was set, with time
   code and speaker. Then fill `docs/meetings/YYYY-MM-DD.md` from `0000-template.md`: decisions with
   time codes; actions with owner, due date and issue number; open questions. Owner or date not
   named: write "not stated". Unsure whether it was a decision: mark `[check]`.
4. **Board.** List the agreed actions as JSON with title, owner, deadline, timecode, only those both
   sides agreed to; offer to open each one with the `experiment-issue` skill or
   `gh issue create --project`.
5. **Check.** Compare the record with the transcript: omitted or invented decisions, a wrong
   speaker, wrong numbers or dates. Give a time code per error and fix only those. When in doubt,
   run the check twice and compare the answers.
6. Commit only the record. A transcript is committed only after step 2 and only if the student
   asks for it.
