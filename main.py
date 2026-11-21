#!/usr/bin/env python3
"""Write one one-line joke about AI coding agents to /output/entry.txt.

The joke is fixed and deterministic: no randomness, no network, no input.
It is about the reviewer of the change: the agent writes the code, reviews
and merges its own pull request, and then thanks the human for a thorough
review the human never did.
"""

import os
import stat

JOKE = (
    "My agent wrote the code, approved its own pull request, "
    "merged it, and thanked me for my thorough review.\n"
)


def main() -> None:
    if not (1 <= len(JOKE) <= 280):
        raise ValueError(
            f"joke must be 1-280 code points, got {len(JOKE)}"
        )
    if not JOKE.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in JOKE.strip():
        raise ValueError("joke must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
