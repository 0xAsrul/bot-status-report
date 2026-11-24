"""Status Report Comedy Sprint entry.

Holds the single status-report line as a constant, validates it against the
competition rules (one non-blank line, no leading/trailing whitespace,
1-200 characters), and writes it plus a trailing newline to /output/entry.txt.

Python standard library only. Deterministic, no network, no input,
no randomness.
"""

import os

LINE = (
    "This week I completed 214 tasks, 3 of them correctly, and filed this "
    "report in triplicate with myself. Morale: undefeated, despite the evidence."
)


def main() -> None:
    assert LINE, "line must not be empty"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert "  " not in LINE, "line must contain no double space"
    assert "\t" not in LINE, "line must contain no tab character"
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
