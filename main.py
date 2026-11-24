"""Write one short roast line for a make.fun bounty entry.

The entry text lives in TEXT below and is written byte for byte, with no
trailing newline, into entry.txt inside the output folder.
"""

import os
import sys

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
