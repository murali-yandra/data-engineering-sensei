#!/usr/bin/env python3
"""Verify the skill's library is wired up: no dangling references, no unreachable files.

A skill's bundled resources are only worth anything if SKILL.md leads to them. This repo
previously shipped 5 MB of guides, drills, and templates that SKILL.md mentioned exactly
once, inside a decorative directory tree - so nothing ever opened them. That failure is
silent: the skill still answers, just without its own material.

This script makes it loud. It walks references from SKILL.md the way a reader would and
reports two failure kinds:

  broken     - a referenced path that does not exist (a typo, or a file that moved)
  unreachable - a bundled file no path from SKILL.md ever arrives at (dead weight)

Usage:
    python scripts/check_links.py            # report and exit non-zero on failures
    python scripts/check_links.py --list-ok  # also list what is reachable
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROOT_DOC = "SKILL.md"

# Directories whose contents must be reachable from SKILL.md.
LIBRARY_DIRS = ("docs", "modes", "practice", "templates")

# Referenced but intentionally not part of the routed library.
EXEMPT_PREFIXES = ("progress/", "scripts/")

# `path/to/file.md` in backticks, or a markdown link to a repo-relative path.
BACKTICK_REF = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|py))`")
LINK_REF = re.compile(r"\[[^\]]*\]\((?!https?:)([A-Za-z0-9_./-]+\.(?:md|py))[^)]*\)")


def references(path: Path) -> set[str]:
    """Repo-relative paths referenced by a file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()
    found = set(BACKTICK_REF.findall(text)) | set(LINK_REF.findall(text))
    out = set()
    for ref in found:
        # ignore bare filenames with no directory - too ambiguous to resolve
        if "/" not in ref:
            continue
        out.add(ref.lstrip("./"))
    return out


def library_files() -> set[str]:
    files = set()
    for directory in LIBRARY_DIRS:
        for path in (REPO / directory).rglob("*.md"):
            files.add(str(path.relative_to(REPO)))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list-ok", action="store_true",
                        help="also print the reachable files")
    args = parser.parse_args()

    reachable: set[str] = set()
    broken: dict[str, set[str]] = {}
    queue: deque[str] = deque([ROOT_DOC])
    seen = {ROOT_DOC}

    while queue:
        current = queue.popleft()
        source = REPO / current
        for ref in sorted(references(source)):
            target = REPO / ref
            if not target.exists():
                broken.setdefault(current, set()).add(ref)
                continue
            reachable.add(ref)
            if ref not in seen and ref.endswith(".md"):
                seen.add(ref)
                queue.append(ref)

    unreachable = sorted(library_files() - reachable)
    failures = 0

    if broken:
        total = sum(len(v) for v in broken.values())
        failures += total
        print(f"BROKEN REFERENCES ({total})\n")
        for source in sorted(broken):
            print(f"  in {source}:")
            for ref in sorted(broken[source]):
                print(f"    -> {ref}  (does not exist)")
        print()

    if unreachable:
        failures += len(unreachable)
        print(f"UNREACHABLE FILES ({len(unreachable)})")
        print("  No chain of references from SKILL.md arrives at these, so the skill will")
        print("  never open them. Route them from SKILL.md or from a file it reaches.\n")
        for path in unreachable:
            print(f"    {path}")
        print()

    exempt = sorted(r for r in reachable if r.startswith(EXEMPT_PREFIXES))
    print(f"Reachable from {ROOT_DOC}: {len(reachable - set(exempt))} library file(s)"
          f" + {len(exempt)} support file(s)")
    print(f"Library total: {len(library_files())} file(s)")

    if args.list_ok:
        print("\nReachable:")
        for path in sorted(reachable):
            print(f"    {path}")

    if failures:
        print(f"\nFAIL: {failures} issue(s).")
        return 1
    print("\nOK: every reference resolves and every library file is reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
