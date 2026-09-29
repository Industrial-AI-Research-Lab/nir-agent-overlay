# Vendored skills

Copies of skills from other lab repositories. The pin is the upstream commit sha in the `source:`
line of the frontmatter and in this table. Updating is manual: copy the new version, update the sha
here and in the frontmatter, carry over the "Project context" block.

| Skill | source | Copied | Local changes |
|---|---|---|---|
| `pre-ship` | `iairlab-skillset@858279254cff4370b3bebe858eb3e3eb29b8909d` (`development/review/pre-ship/SKILL.md`) | 2026-09-29 | `source:` in the frontmatter; "Project context" block at the end |
| `review` | `iairlab-skillset@858279254cff4370b3bebe858eb3e3eb29b8909d` (`development/review/review/SKILL.md`) | 2026-09-29 | `source:` in the frontmatter; "Project context" block at the end |

Update a copy (lab members with access to the source repository):

```bash
SHA=$(gh api repos/Industrial-AI-Research-Lab/iairlab-skillset/commits/main --jq .sha)
gh api repos/Industrial-AI-Research-Lab/iairlab-skillset/contents/development/review/pre-ship/SKILL.md \
  -H 'Accept: application/vnd.github.raw' > /tmp/pre-ship.md
# carry over `source: iairlab-skillset@$SHA` and the "Project context" block, update the table
```
