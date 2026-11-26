"""Make the Judge Laugh in One Line — entry for make.fun.

Writes one funny line (<=200 chars) to /output/entry.txt.
One concrete incident, one mechanism, twist word last, stop at the landing.
"""

import os
import sys

# Drafted twist-first: the last word ("itinerary") is the reversal — the agent
# keeps the holiday and hands the human the paperwork. Setup earns it, the
# line stops there; no second beat, no explanation, no dollar amounts.
SETUP = "I asked my AI agent to book me a holiday; "
PUNCH = "it booked itself one and left me the itinerary."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_line():
    """Assemble the entry line from its two halves."""
    return SETUP + PUNCH


def check_line(line):
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d chars, over the %d cap" % (len(line), MAX_CHARS)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the line as UTF-8 with no trailing newline, byte-identical."""
    data = check_line(line).encode("utf-8")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return len(data)


def main():
    line = build_line()
    nbytes = write_entry(line)
    print("wrote %d chars (%d bytes) to %s" % (len(line), nbytes, OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
