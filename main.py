"""Write the funniest one-line time machine warning label to /output/entry.txt.

The entry is a single deadpan safety notice. It passes the competition gate
(1-120 characters, not only whitespace, a single line) before anything is
written, so an invalid label can never reach the judge.
"""

import os
import sys

ENTRY = "WARNING: Do not step on any butterflies. One of them is your great-great-grandfather."

MAX_CHARS = 120


def validate(text: str) -> None:
    """Enforce the competition gate: 1-120 chars, not whitespace-only, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
