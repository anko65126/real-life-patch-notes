"""Entry program for the 'Real-Life Patch Notes: The Comedy Changelog' make.fun bounty.

The entry is the funniest one-line patch note for a bug in real life, at
most 160 characters. The program writes exactly that one line to
/output/entry.txt (an optional first argument overrides the destination for
a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "v2.6.1: Fixed bug where Mondays arrived before the weekend had finished "
    "loading. Known issue: coffee now required to boot the human."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 160, f"entry must be 1-160 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
