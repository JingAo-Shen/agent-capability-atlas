"""Build the standalone HTML using only Python's standard library."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("name", "cat", "api", "os", "load", "tier", "desc", "connect", "note", "task", "url")
OPTIONAL = {"stars": int, "hot": bool}


def validate(data):
    if not data or len({item["name"] for item in data}) != len(data):
        raise ValueError("Tool names must be unique and the catalog must not be empty")
    for item in data:
        for field in REQUIRED:
            if field not in item or not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"{item.get('name', '?')}: missing nonempty string field {field}")
        for field, kind in OPTIONAL.items():
            if field in item and not isinstance(item[field], kind):
                raise ValueError(f"{item['name']}: {field} must be {kind.__name__}")
        unknown = set(item) - set(REQUIRED) - set(OPTIONAL)
        if unknown:
            raise ValueError(f"{item['name']}: unexpected fields {sorted(unknown)}")
        if not item["url"].startswith("https://"):
            raise ValueError("Source links must use HTTPS")


def build():
    data = json.loads((ROOT / "data/tools.json").read_text(encoding="utf-8"))
    validate(data)
    template = (ROOT / "src/template.html").read_text(encoding="utf-8")
    if template.count("__DATA__") != 1:
        raise ValueError("Expected one __DATA__ placeholder")
    # Escape angle brackets so catalog text cannot terminate the script tag.
    serialized = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")
    return template.replace("__DATA__", serialized)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check tracked HTML without modifying it")
    args = parser.parse_args()
    result = build()
    output = ROOT / "index.html"
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != result:
            raise SystemExit("index.html is stale; run python scripts/build.py")
        print("Catalog validation and reproducible build check passed")
    else:
        output.write_text(result, encoding="utf-8")
        print(f"Built index.html with {len(json.loads((ROOT / 'data/tools.json').read_text(encoding='utf-8')))} tools")
