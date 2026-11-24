#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes one fixed, hand-written two-sentence horror story to
/output/entry.txt, deterministically. The story is a constant: no
randomness, no input, no network, so every run produces the exact
same bytes.
"""

import os

STORY = (
    "I taught my daughter to check under her bed every night "
    "so nothing could hide there. "
    "Last night she looked, smiled, and said the thing under "
    "the bed had been waiting for me to check too."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = STORY
    assert 1 <= len(text) <= 400, "story must be 1-400 characters"
    assert text.count(".") == 2, "story must be exactly two sentences"
    assert text == text.strip(), "story must not start or end with whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back and re-validate: fail loudly instead of shipping a
    # truncated or corrupted entry if the write went wrong.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch on entry.txt"


if __name__ == "__main__":
    main()
