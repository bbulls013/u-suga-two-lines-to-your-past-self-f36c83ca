#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry generator.

Writes the two-line warning to /output/entry.txt (the graded artifact)
and to entry.txt beside this script, byte for byte the same text.
The output is fully deterministic: no randomness, no clock, no I/O
beyond the two fixed writes.
"""

import os
import sys

WARNING_LINE = (
    "Don't wave off your father's cough on the drive home that Christmas "
    "- turn the car around and take him to the hospital."
)
REASON_LINE = (
    "It was pneumonia, and he never came home from that ward, so your "
    "last words to him were a joke about the traffic."
)

ENTRY_TEXT = WARNING_LINE + "\n" + REASON_LINE + "\n"


def build_entry() -> str:
    """Return the entry text: exactly two lines, one warning, one reason."""
    lines = ENTRY_TEXT.splitlines()
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no blank lines allowed"
    # Each line is one sentence: the warning names one concrete moment,
    # the second line traces what changed because of it.
    assert WARNING_LINE.endswith(".") and REASON_LINE.endswith(".")
    assert ENTRY_TEXT.encode("utf-8").decode("utf-8") == ENTRY_TEXT
    return ENTRY_TEXT


def write_entry(text: str, paths) -> None:
    for path in paths:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)


def main() -> int:
    text = build_entry()
    if not 1 <= len(text) <= 280:
        print(f"entry out of gate: {len(text)} chars", file=sys.stderr)
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    write_entry(text, ["/output/entry.txt", os.path.join(here, "entry.txt")])
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
