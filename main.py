#!/usr/bin/env python3
"""One-word verdict on an ex.

The joke is a frame shift: the relationship is treated as a
subscription service, and the ex is the newsletter nobody asked
to keep receiving. No rant, no insult — just the quiet status
every inbox shows after you finally hit the button.
"""

import os
from pathlib import Path


def verdict_word() -> str:
    # The ex, filed under the only status that fits:
    # once delivered daily, now cancelled by the reader.
    # One word, no punctuation, no caption needed — the
    # subscription metaphor does all the talking.
    return "unsubscribed"


def main() -> None:
    word = verdict_word()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
