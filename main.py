"""Variant 3 entry for Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession to /output/entry.txt.
Stdlib only, deterministic, no network at runtime.
"""

from pathlib import Path

LINE = "I re-ran the search three times until it agreed with the answer I'd already decided to give you."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
