"""Read a CSV file as dictionaries."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Iterator


def read_csv(path: str | Path, encoding: str = "utf-8") -> list[dict[str, str]]:
    """Return CSV rows as dictionaries keyed by the header names."""
    with Path(path).open("r", encoding=encoding, newline="") as csv_file:
        return list(csv.DictReader(csv_file))


def iter_csv(path: str | Path, encoding: str = "utf-8") -> Iterator[dict[str, str]]:
    """Iterate over CSV rows, which is useful for large files."""
    with Path(path).open("r", encoding=encoding, newline="") as csv_file:
        yield from csv.DictReader(csv_file)


def main() -> None:
    parser = argparse.ArgumentParser(description="Print CSV rows as JSON")
    parser.add_argument("path", help="path to the CSV file")
    parser.add_argument("--encoding", default="utf-8", help="text encoding")
    args = parser.parse_args()
    json.dump(read_csv(args.path, args.encoding), sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
