#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one joke about crypto and trading life to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, single line, not only whitespace.
"""

import os

JOKE = "Bought every dip until the dip bought me \u2014 now I'm the floor, and the group chat walks on me for support."

# Gate limit from the competition rules: 1-200 characters, single line.
# The gate counts characters, not bytes (the em dash is one character).
MAX_CHARS = 200


def validate(line):
    """Check the entry line against the gate; return its UTF-8 bytes."""
    if not line or line.strip() == "":
        raise SystemExit("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is over {MAX_CHARS} characters")
    return line.encode("utf-8")


def main():
    data = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
