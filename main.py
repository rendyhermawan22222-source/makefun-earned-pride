#!/usr/bin/env python3
"""One Line of Earned Pride (make.fun).

Writes one quiet, earned moment of pride to /output/entry.txt: after
forty years of climbing the lighthouse stairs, the keeper watches the
new lamp blink on at dusk and, for the first time, lets someone else
keep the light. Long effort, concrete scene, pride earned inside the
line — no trophy, no podium, no graduation.
"""

import os

LINE = (
    "After forty years of climbing those stairs, the lighthouse keeper "
    "watched the new lamp blink on at dusk and, for the first time, let "
    "someone else keep the light."
)


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be only whitespace"
    assert line == LINE.strip(), "the line must not change when stripped"
    assert 1 <= len(line) <= 240, f"line is {len(line)} chars, gate needs 1-240"
    assert "\n" not in line, "the line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify: the whole job is one exact file, so prove it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt on disk differs from the line"
    assert 1 <= len(written) <= 240, "entry.txt fails the 1-240 char gate"
    print(f"Wrote {len(written)}-character line to {path}")


if __name__ == "__main__":
    main()
