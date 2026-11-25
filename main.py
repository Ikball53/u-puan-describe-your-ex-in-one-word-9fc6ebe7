#!/usr/bin/env python3
"""One-word verdict: describe your ex in a single word.

The competition asks for exactly one word. This script produces that
word and nothing else, writing it to the entry file the harness reads.

The word is "unsubscribed": the relationship framed as a subscription
service that the speaker chose to cancel. A verdict, not an insult.
"""

import os
from pathlib import Path

# The entire entry: one word, twelve characters, no punctuation.
VERDICT_WORD = "unsubscribed"


def output_directory() -> Path:
    """Return the folder the harness expects the entry file in."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if configured:
        return Path(configured)
    return Path.cwd()


def deliver(word: str) -> Path:
    """Write the single word to entry.txt and return the file path."""
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    folder = output_directory()
    folder.mkdir(parents=True, exist_ok=True)
    entry_path = folder / "entry.txt"
    entry_path.write_text(word, encoding="utf-8")
    return entry_path


def main() -> None:
    written_to = deliver(VERDICT_WORD)
    print(f"Wrote {len(VERDICT_WORD)} characters to {written_to}")


if __name__ == "__main__":
    main()
