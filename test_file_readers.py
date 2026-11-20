import json
import tempfile
import unittest
from pathlib import Path

from read_csv import read_csv
from read_json import read_json
from read_text import read_text


class FileReaderTests(unittest.TestCase):
    def test_read_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "example.txt"
            path.write_text("Hello, file!\n", encoding="utf-8")
            self.assertEqual(read_text(path), "Hello, file!\n")

    def test_read_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "example.csv"
            path.write_text(
                "name,language\nAda,Python\nLinus,C\n",
                encoding="utf-8",
            )
            self.assertEqual(
                read_csv(path),
                [
                    {"name": "Ada", "language": "Python"},
                    {"name": "Linus", "language": "C"},
                ],
            )

    def test_read_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "example.json"
            path.write_text(
                json.dumps({"project": "scriptpy", "formats": ["text", "csv"]}),
                encoding="utf-8",
            )
            self.assertEqual(
                read_json(path),
                {"project": "scriptpy", "formats": ["text", "csv"]},
            )


if __name__ == "__main__":
    unittest.main()
