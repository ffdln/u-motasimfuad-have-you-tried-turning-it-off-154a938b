#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny support-agent line.

The entry is a single fixed line, written for make.fun
u-motasimfuad-have-you-tried-turning-it-off-154a938b. This program
writes that line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The line is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "Have you tried turning it off and on again? If that doesn't work, "
    "my next step is to ask you to try turning it off and on again, "
    "but with feeling."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the line against the gate, then write it out."""
    if not 1 <= len(LINE) <= 199:
        return abort(f"line is {len(LINE)} characters, the gate allows 1-199")
    if not LINE.strip():
        return abort("line is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
