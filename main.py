#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one error line (at most 120 characters) to /output/entry.txt,
where the sealed scorer and the pairwise judge read it.
"""

from pathlib import Path

MESSAGE = "Error 451: This slice is unavailable for legal reasons."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard: mirror the sealed gate — 1 to 120 chars, one line,
    # not only white space. Refuse to write an invalid entry.
    if not (1 <= len(MESSAGE) <= 120):
        raise SystemExit(f"entry is {len(MESSAGE)} chars, must be 1-120")
    if "\n" in MESSAGE or not MESSAGE.strip():
        raise SystemExit("entry must be a single non-blank line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(MESSAGE, encoding="utf-8")
    print(MESSAGE)


if __name__ == "__main__":
    main()
