"""Read a text file with a UTF-8 encoding."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Return the complete contents of a text file."""
    return Path(path).read_text(encoding=encoding)


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a UTF-8 text file")
    parser.add_argument("path", help="path to the text file")
    parser.add_argument("--encoding", default="utf-8", help="text encoding")
    args = parser.parse_args()
    sys.stdout.write(read_text(args.path, args.encoding))


if __name__ == "__main__":
    main()
