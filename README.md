# scriptpy

Small, dependency-free examples for reading common file formats in Python.

## Text

```bash
python3 read_text.py README.md
```

Use `read_text(path, encoding="utf-8")` to get the complete file as a string.

## CSV

```bash
python3 read_csv.py data.csv
```

Use `read_csv(path)` to get a list of rows keyed by the CSV header. For a
large file, use `iter_csv(path)` to process each row without loading the whole
file at once.

## JSON

```bash
python3 read_json.py data.json
```

Use `read_json(path)` to get the decoded JSON value (object, array, or scalar).

## Tests

```bash
python3 -m unittest -v
```
