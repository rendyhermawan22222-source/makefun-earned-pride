#!/usr/bin/env python3
"""One Line of Earned Pride (make.fun).

Writes one quiet, earned moment of pride to /output/entry.txt: a lighthouse
keeper of forty years watches the new lamp blink on at dusk and, for the
first time, lets someone else keep the light. Concrete scene, one real
person, the effort felt in "forty years of climbing those stairs", and the
pride lands on the last words - no trophy, no podium, no graduation. One
line, well under the 240-character gate.
"""

import os

LINE = (
    "After forty years of climbing those stairs, the lighthouse keeper "
    "watched the new lamp blink on at dusk and, for the first time, let "
    "someone else keep the light."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 240, f"line is {len(line)} chars, gate needs 1-240"
    assert "\n" not in line, "the line must be a single line"
    assert line == LINE.strip(), "the line must not change when stripped"
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
