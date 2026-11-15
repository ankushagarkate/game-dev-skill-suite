#!/usr/bin/env python3
"""Validate Antigravity SKILL.md frontmatter, line limits, and relative links."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / ".agents" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\((references/[^)]+|assets/[^)]+|scripts/[^)]+)\)")


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) > 500:
        errors.append(f"{skill_dir.name}: SKILL.md has {len(lines)} lines (max 500)")

    if not text.startswith("---\n"):
        errors.append(f"{skill_dir.name}: missing YAML frontmatter opening '---'")
        return errors

    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        errors.append(f"{skill_dir.name}: missing YAML frontmatter closing '---'")
        return errors

    frontmatter = text[4:end_idx]
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

    if not name_match:
        errors.append(f"{skill_dir.name}: missing 'name' in frontmatter")
    else:
        name = name_match.group(1).strip().strip("'\"")
        if len(name) > 64 or not NAME_RE.match(name):
            errors.append(f"{skill_dir.name}: invalid kebab-case name '{name}'")
        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: folder name does not match frontmatter name '{name}'")

    if not desc_match or len(desc_match.group(1).strip()) < 20:
        errors.append(f"{skill_dir.name}: missing or too short 'description' in frontmatter")

    for rel_path in LINK_RE.findall(text):
        target = skill_dir / rel_path
        if not target.exists():
            errors.append(f"{skill_dir.name}: broken link '{rel_path}'")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"Skills directory not found: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    if not skill_dirs:
        print("No skill directories found.", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for sdir in skill_dirs:
        all_errors.extend(validate_skill(sdir))

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for err in all_errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} Antigravity skills successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
