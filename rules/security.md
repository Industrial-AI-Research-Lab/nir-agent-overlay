# Security and data

- Never read, print or copy `.env`, credentials, tokens or private keys. If one appears in your
  context, stop and tell the student to rotate it.
- Never commit raw data, personal data, model weights, files over a few tens of MB or generated
  logs. Stage explicit paths; check `.gitignore` before any broad add.
- Configuration through environment variables; `.env.example` lists every key with a placeholder
  and stays free of real values.
- No commands that send repository content outside: no uploads, no requests to unknown hosts,
  no telemetry hooks.
- Meeting transcripts and records: names of third parties replaced by roles, no grades, no personal
  topics, before anything is committed.
- Do not connect an overlay, hook or skill from a source the student has not reviewed; pin
  versions by tag or commit.
