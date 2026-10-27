"""Build the standalone HTML using only Python's standard library."""
import argparse
import base64
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"name", "cat", "api", "os", "load", "tier", "desc", "connect", "note", "task", "url"}

def build():
    data = json.loads((ROOT / "data/tools.json").read_text(encoding="utf-8"))
    if not data or len({item["name"] for item in data}) != len(data):
        raise ValueError("Tool names must be unique and the catalog must not be empty")
    for item in data:
        if set(item) != FIELDS or not all(isinstance(v, str) and v.strip() for v in item.values()):
            raise ValueError("Each tool must have all required nonempty string fields")
        if not item["url"].startswith("https://"):
            raise ValueError("Source links must use HTTPS")
    template = (ROOT / "src/template.html").read_text(encoding="utf-8")
    for marker in ("__DATA__", "__INSTALLER_BASE64__"):
        if template.count(marker) != 1:
            raise ValueError(f"Expected one {marker} placeholder")
    payload = base64.b64encode((ROOT / "install-agent-starter.ps1").read_bytes()).decode("ascii")
    # Escape angle brackets so future catalog text cannot terminate the script tag.
    serialized = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(">", "\\u003e")
    return template.replace("__DATA__", serialized).replace("__INSTALLER_BASE64__", payload)

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
        print("Built index.html")
