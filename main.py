#!/usr/bin/env python3
"""The Printer Finally Answers — one line, in the printer's own voice.

Writes a single line of text (1-240 chars, UTF-8) to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = "You pressed print 14 times \u2014 I heard all 14, I am not ignoring you, I am out of cyan."


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
