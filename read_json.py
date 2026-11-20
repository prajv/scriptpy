"""Read JSON data from a file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def read_json(path: str | Path, encoding: str = "utf-8") -> Any:
    """Return the decoded JSON value from a file."""
    with Path(path).open("r", encoding=encoding) as json_file:
        return json.load(json_file)


def main() -> None:
    parser = argparse.ArgumentParser(description="Pretty-print a JSON file")
    parser.add_argument("path", help="path to the JSON file")
    parser.add_argument("--encoding", default="utf-8", help="text encoding")
    args = parser.parse_args()
    json.dump(read_json(args.path, args.encoding), sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
