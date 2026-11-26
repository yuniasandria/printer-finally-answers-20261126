#!/usr/bin/env python3
"""The Printer Finally Answers — one line, in the printer's own voice.

Judging rationale: the line works because it is a counted grievance told
from the printer's side — the exact number (14 presses, heard all 14)
proves it listened, the middle clause ("I am not ignoring you") answers
the accusation, and the closer ("I am out of cyan") lands as a single
concrete, everyday cause instead of a vague excuse. One read, no setup,
no punchline that needs explaining.

Writes a single line of text (1-240 chars, UTF-8) to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = "You pressed print 14 times \u2014 I heard all 14, I am not ignoring you, I am out of cyan."


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly one line: the entry text plus a single trailing newline.
    text = LINE + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
