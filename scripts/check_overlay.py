"""Sanity checks for the overlay: skill frontmatter, rule files, relative links. Stdlib only."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def main() -> int:
    errors: list[str] = []
    for skill in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
        path = skill / "SKILL.md"
        if not path.exists():
            errors.append(f"{skill.name}: SKILL.md missing")
            continue
        match = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
        if not match:
            errors.append(f"{path}: no frontmatter")
            continue
        front = match.group(1)
        name = re.search(r"^name:\s*(\S+)", front, re.M)
        if not name or name.group(1) != skill.name:
            errors.append(f"{path}: frontmatter name must be '{skill.name}'")
        if not re.search(r"^description:\s*\S", front, re.M):
            errors.append(f"{path}: description missing")
    for rule in sorted((ROOT / "rules").glob("*.md")):
        if len(rule.read_text(encoding="utf-8").strip()) < 80:
            errors.append(f"{rule}: too short to be a rule")
    for doc in sorted(ROOT.rglob("*.md")):
        if ".venv" in doc.parts:
            continue
        for target in LINK.findall(doc.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", target):
                continue
            if not (doc.parent / target).exists():
                errors.append(f"{doc}: broken link {target}")
    for error in errors:
        print(error)
    print("ok" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
