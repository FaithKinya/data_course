#!/usr/bin/env python3
"""Parse PROGRESS.md and print completion summary."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PROGRESS_FILE = ROOT / "PROGRESS.md"


def parse_progress(text: str) -> tuple[list[str], list[str]]:
    done = []
    todo = []
    for line in text.splitlines():
        m_done = re.match(r"^- \[x\] (.+)$", line, re.IGNORECASE)
        m_todo = re.match(r"^- \[ \] (.+)$", line)
        if m_done:
            done.append(m_done.group(1).strip())
        elif m_todo:
            todo.append(m_todo.group(1).strip())
    return done, todo


def group_by_section(text: str) -> dict[str, tuple[int, int]]:
    sections: dict[str, tuple[int, int]] = {}
    current = "General"
    done_count = 0
    total = 0

    for line in text.splitlines():
        if line.startswith("## "):
            if total:
                sections[current] = (done_count, total)
            current = line[3:].strip()
            done_count = 0
            total = 0
        elif re.match(r"^- \[[ x]\]", line, re.IGNORECASE):
            total += 1
            if re.match(r"^- \[x\]", line, re.IGNORECASE):
                done_count += 1

    if total:
        sections[current] = (done_count, total)
    return sections


def main() -> int:
    if not PROGRESS_FILE.exists():
        print(f"Missing {PROGRESS_FILE}")
        return 1

    text = PROGRESS_FILE.read_text(encoding="utf-8")
    done, todo = parse_progress(text)
    total = len(done) + len(todo)
    pct = (len(done) / total * 100) if total else 0

    print("=" * 50)
    print("  Learn Data Engineering — Progress")
    print("=" * 50)
    print(f"\nOverall: {len(done)}/{total} ({pct:.1f}%)\n")

    for section, (d, t) in group_by_section(text).items():
        if t == 0:
            continue
        bar_len = 20
        filled = int(bar_len * d / t) if t else 0
        bar = "#" * filled + "-" * (bar_len - filled)
        print(f"  {section[:28]:28} [{bar}] {d}/{t}")

    if not done:
        print("\n>> Start here: docs/SETUP.md")
        print(">> Then: curriculum/phase-01-foundations/README.md")
    elif len(done) < 5:
        print("\n>> Keep going with Phase 1 lessons and exercises.")
    elif pct >= 100:
        print("\n>> Congratulations — course complete! Polish your capstone READMEs.")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
