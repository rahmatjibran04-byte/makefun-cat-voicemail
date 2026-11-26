#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, as recorded by a cat, to /output/entry.txt.
Deterministic: no network, no randomness, no reading of outside files.
"""

import os

ENTRY = (
    "You've reached Biscuit. I knocked the phone off the table, "
    "so this is your voicemail. Leave a message. I'll sit on it."
)

# The gate: /output/entry.txt must be UTF-8 text of 1-120 characters,
# not only whitespace. Refuse to write anything that would fail it.
MAX_CHARS = 120


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise ValueError(
            f"entry is {len(ENTRY)} chars; gate requires 1-{MAX_CHARS} "
            "non-whitespace characters"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
