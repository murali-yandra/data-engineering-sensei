#!/usr/bin/env python3
"""Record session outcomes into progress/ so the next session starts with work, not re-orientation.

The progress files follow the schemas in CONTRIBUTING section 16. Editing fifteen markdown
files by hand at the end of a session is slow and drifts out of format, which is how a
tracker quietly stops being trustworthy. This script does the bookkeeping instead.

One rule is enforced rather than suggested: closing a weakness requires evidence. A tracker
that lets you mark things done because the candidate read an explanation manufactures exactly
the false confidence this skill exists to prevent.

Examples:
    python scripts/update_progress.py show
    python scripts/update_progress.py session --type drill --mode sql-drill-mode \
        --topic "window functions" --score 3/5 --next "redo Q4 with ROW_NUMBER"
    python scripts/update_progress.py weakness add --area SQL \
        --weakness "reaches for GROUP BY where a window is needed" --severity High \
        --evidence "eval drill 2, wrong grain" --repair "practice/sql/window-functions.md 13-19" \
        --exit-test "top-N-per-group with tie-break, unaided"
    python scripts/update_progress.py weakness close WR-001 --evidence "passed exit test 2026-09-02"
    python scripts/update_progress.py state --set "Current module=SQL" --set "Current difficulty=medium"
    python scripts/update_progress.py next --task "3 dedup drills" --mode sql-drill-mode \
        --why "dedup was the failure in the last mock" --exit-criteria "all 3 correct first try"
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROGRESS = REPO / "progress"

CURRENT_STATE = PROGRESS / "CURRENT_STATE.md"
SESSION_LOG = PROGRESS / "SESSION_LOG.md"
WEAKNESS_REGISTER = PROGRESS / "WEAKNESS_REGISTER.md"
NEXT_STEPS = PROGRESS / "NEXT_STEPS.md"

PLACEHOLDER_ROW = re.compile(r"^\|\s*WR-001\s*\|(\s*\|)+\s*open\s*\|\s*$")


def today() -> str:
    return dt.date.today().isoformat()


def read(path: Path) -> str:
    if not path.exists():
        sys.exit(f"error: {path.relative_to(REPO)} is missing. Is this the skill repo root?")
    return path.read_text(encoding="utf-8")


# --------------------------------------------------------------------------- helpers

def set_field(text: str, heading: str, key: str, value: str) -> str:
    """Set `key:` inside the first fenced text block under `heading`."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip().lower() == heading.lower())
    except StopIteration:
        return text
    in_block = False
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped.startswith("```"):
            if in_block:
                break
            in_block = True
            continue
        if in_block and stripped.lower().startswith(f"{key.lower()}:"):
            lines[i] = f"{key}: {value}".rstrip()
            return "\n".join(lines) + "\n"
        if lines[i].startswith("## ") and not in_block:
            break
    return text


def append_to_section(text: str, heading: str, block: str) -> str:
    """Append `block` at the end of the named section, replacing an empty placeholder."""
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip().lower() == heading.lower())
    except StopIteration:
        return text.rstrip() + f"\n\n{heading}\n\n{block}\n"
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
               len(lines))
    body = lines[start + 1:end]
    # drop "nothing recorded yet" style placeholders and bare list dashes
    body = [l for l in body
            if l.strip() not in {"-", ""} and "no sessions recorded yet" not in l.lower()]
    body = (body + [""]) if body else []
    return "\n".join(lines[:start + 1] + [""] + body + [block, ""] + lines[end:]).rstrip() + "\n"


def next_weakness_id(text: str) -> str:
    """Next free ID, ignoring the empty seed row the template ships with."""
    used = [
        int(m.group(1))
        for line in text.splitlines()
        if (m := re.match(r"\|\s*WR-(\d+)\s*\|", line)) and not PLACEHOLDER_ROW.match(line)
    ]
    return f"WR-{(max(used) + 1) if used else 1:03d}"


def touch_state(fields: dict[str, str]) -> None:
    text = read(CURRENT_STATE)
    text = set_field(text, "## Snapshot", "Last updated", today())
    for key, value in fields.items():
        text = set_field(text, "## Snapshot", key, value)
        text = set_field(text, "## Active Focus", key, value)
    CURRENT_STATE.write_text(text, encoding="utf-8")


# --------------------------------------------------------------------------- commands

def cmd_show(_args: argparse.Namespace) -> int:
    state = read(CURRENT_STATE)
    snapshot = re.search(r"## Snapshot\s*```text\n(.*?)```", state, re.DOTALL)
    print("=== Current state ===")
    print((snapshot.group(1).rstrip() if snapshot else "(no snapshot)"))

    register = read(WEAKNESS_REGISTER)
    rows = [l for l in register.splitlines()
            if l.startswith("| WR-") and not PLACEHOLDER_ROW.match(l)]
    open_rows = [r for r in rows if r.rstrip().rstrip("|").rstrip().endswith("open")]
    print(f"\n=== Weaknesses: {len(open_rows)} open / {len(rows)} tracked ===")
    for row in open_rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        print(f"  {cells[0]} [{cells[3] or '?'}] {cells[1]}: {cells[2]}")

    nxt = re.search(r"## Immediate Task\s*```text\n(.*?)```", read(NEXT_STEPS), re.DOTALL)
    print("\n=== Next task ===")
    print((nxt.group(1).rstrip() if nxt else "(none set)"))
    return 0


def cmd_session(args: argparse.Namespace) -> int:
    entry = "\n".join([
        "```text",
        f"Date: {args.date or today()}",
        f"Session type: {args.type}",
        f"Mode: {args.mode or ''}",
        f"Topic: {args.topic or ''}",
        f"Candidate output: {args.output or ''}",
        f"Score: {args.score or ''}",
        f"Feedback summary: {args.feedback or ''}",
        f"Weaknesses found: {'; '.join(args.weakness) if args.weakness else ''}",
        f"Evidence created: {'; '.join(args.evidence) if args.evidence else ''}",
        f"Next task: {args.next or ''}",
        "```",
    ])
    SESSION_LOG.write_text(append_to_section(read(SESSION_LOG), "## Log", entry),
                           encoding="utf-8")

    fields = {}
    if args.mode:
        fields["Current mode"] = args.mode
    if args.topic:
        fields["Current module"] = args.topic
        fields["Primary focus"] = args.topic
    touch_state(fields)

    if args.evidence:
        state = read(CURRENT_STATE)
        for item in args.evidence:
            state = append_to_section(state, "## Completed Evidence",
                                      f"- {today()}: {item}")
        CURRENT_STATE.write_text(state, encoding="utf-8")

    if args.next:
        nxt = set_field(read(NEXT_STEPS), "## Immediate Task", "Task", args.next)
        NEXT_STEPS.write_text(nxt, encoding="utf-8")

    print(f"Logged session to progress/SESSION_LOG.md and refreshed CURRENT_STATE.md.")
    if not args.next:
        print("note: no --next given. Every session should end with a concrete next action.")
    return 0


def cmd_weakness(args: argparse.Namespace) -> int:
    text = read(WEAKNESS_REGISTER)

    if args.weakness_command == "add":
        wid = next_weakness_id(text)
        row = (f"| {wid} | {args.area} | {args.weakness} | {args.severity} "
               f"| {args.evidence} | {args.repair or ''} | {args.exit_test or ''} | open |")
        lines = text.splitlines()
        # replace the empty seed row the first time, otherwise append after the last row
        seed = next((i for i, l in enumerate(lines) if PLACEHOLDER_ROW.match(l)), None)
        if seed is not None:
            lines[seed] = row
        else:
            last = max(i for i, l in enumerate(lines) if l.startswith("| WR-"))
            lines.insert(last + 1, row)
        WEAKNESS_REGISTER.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Added {wid} ({args.severity}): {args.area} - {args.weakness}")
        return 0

    # close
    wid = args.id.upper()
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {wid} |"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells[-1] == "closed":
                print(f"{wid} is already closed.")
                return 0
            cells[-1] = "closed"
            cells[4] = f"{cells[4]}; closed {today()}: {args.evidence}".lstrip("; ")
            lines[i] = "| " + " | ".join(cells) + " |"
            WEAKNESS_REGISTER.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"Closed {wid} on evidence: {args.evidence}")
            return 0
    sys.exit(f"error: {wid} not found in progress/WEAKNESS_REGISTER.md")


def cmd_state(args: argparse.Namespace) -> int:
    fields = {}
    for pair in args.set:
        if "=" not in pair:
            sys.exit(f"error: --set expects key=value, got {pair!r}")
        key, value = pair.split("=", 1)
        fields[key.strip()] = value.strip()
    touch_state(fields)
    print(f"Updated {len(fields)} field(s) in progress/CURRENT_STATE.md.")
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    text = read(NEXT_STEPS)
    for key, value in (("Task", args.task), ("Mode", args.mode),
                       ("Why it matters", args.why), ("Expected output", args.output),
                       ("Time box", args.timebox), ("Exit criteria", args.exit_criteria)):
        if value:
            text = set_field(text, "## Immediate Task", key, value)
    NEXT_STEPS.write_text(text, encoding="utf-8")
    print("Updated progress/NEXT_STEPS.md.")
    return 0


# --------------------------------------------------------------------------- cli

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("show", help="print current state, open weaknesses, and next task"
                   ).set_defaults(func=cmd_show)

    s = sub.add_parser("session", help="log a finished session")
    s.add_argument("--type", required=True,
                   help="drill, mock, review, tutor, roadmap, project-deep-dive, ...")
    s.add_argument("--mode", help="mode file used, e.g. sql-drill-mode")
    s.add_argument("--topic")
    s.add_argument("--output", help="what the candidate produced")
    s.add_argument("--score", help="e.g. 3/5")
    s.add_argument("--feedback")
    s.add_argument("--weakness", action="append", default=[])
    s.add_argument("--evidence", action="append", default=[])
    s.add_argument("--next", help="the next concrete action")
    s.add_argument("--date", help="defaults to today")
    s.set_defaults(func=cmd_session)

    w = sub.add_parser("weakness", help="add or close a tracked weakness")
    wsub = w.add_subparsers(dest="weakness_command", required=True)

    wa = wsub.add_parser("add")
    wa.add_argument("--area", required=True, help="SQL, Python, DSA, system design, ...")
    wa.add_argument("--weakness", required=True)
    wa.add_argument("--severity", required=True,
                    choices=["Critical", "High", "Medium", "Low"])
    wa.add_argument("--evidence", required=True,
                    help="what demonstrated it - a weakness without evidence is a guess")
    wa.add_argument("--repair", help="the drill that fixes it")
    wa.add_argument("--exit-test", dest="exit_test",
                    help="what the candidate must pass to close it")

    wc = wsub.add_parser("close")
    wc.add_argument("id", help="e.g. WR-001")
    wc.add_argument("--evidence", required=True,
                    help="the passed exit test. Reading an explanation is not evidence.")
    w.set_defaults(func=cmd_weakness)

    st = sub.add_parser("state", help="update CURRENT_STATE.md fields")
    st.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
    st.set_defaults(func=cmd_state)

    n = sub.add_parser("next", help="set the immediate next task")
    n.add_argument("--task", required=True)
    n.add_argument("--mode")
    n.add_argument("--why")
    n.add_argument("--output")
    n.add_argument("--timebox")
    n.add_argument("--exit-criteria", dest="exit_criteria")
    n.set_defaults(func=cmd_next)

    return parser


if __name__ == "__main__":
    ns = build_parser().parse_args()
    sys.exit(ns.func(ns))
