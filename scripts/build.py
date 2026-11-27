"""Build the standalone HTML using only Python's standard library."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data/tools.json"
TEMPLATE_PATH = ROOT / "src/template.html"
OUTPUT_PATH = ROOT / "index.html"

REQUIRED = ("name", "cat", "api", "os", "load", "tier", "desc", "connect", "note", "task", "url")
OPTIONAL = {"stars": int, "hot": bool}


def load_catalog():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    validate(data)
    return data


def validate(data):
    if not data:
        raise ValueError("The catalog must not be empty")
    if len({item.get("name") for item in data}) != len(data):
        raise ValueError("Tool names must be unique")
    for item in data:
        name = item.get("name", "?")
        for field in REQUIRED:
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"{name}: missing nonempty string field {field}")
        unknown = set(item) - set(REQUIRED) - set(OPTIONAL)
        if unknown:
            raise ValueError(f"{name}: unexpected fields {sorted(unknown)}")
        for field, kind in OPTIONAL.items():
            if field in item and not isinstance(item[field], kind):
                raise ValueError(f"{name}: {field} must be {kind.__name__}")
        if item.get("stars", 0) < 0:
            raise ValueError(f"{name}: stars must not be negative")
        if item.get("hot") and not item.get("stars"):
            raise ValueError(f"{name}: hot entries need a star count")
        if not item["url"].startswith("https://"):
            raise ValueError(f"{name}: source links must use HTTPS")


def render(data):
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if template.count("__DATA__") != 1:
        raise ValueError("Expected one __DATA__ placeholder")
    # Escape angle brackets so catalog text cannot terminate the script tag.
    serialized = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")
    return template.replace("__DATA__", serialized)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check tracked HTML without modifying it")
    args = parser.parse_args()

    data = load_catalog()
    result = render(data)
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != result:
            raise SystemExit("index.html is stale; run python scripts/build.py")
        print(f"Catalog validation and reproducible build check passed ({len(data)} tools)")
    else:
        OUTPUT_PATH.write_text(result, encoding="utf-8")
        print(f"Built index.html with {len(data)} tools")


if __name__ == "__main__":
    main()
