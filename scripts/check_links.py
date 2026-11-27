"""Check every source link in the catalog. Standard library only.

Exit code 0 when no link is broken; 1 when at least one 404/410/5xx or
connection failure is found. 403/429 responses are reported as "blocked"
warnings because many sites reject non-browser clients or rate-limit CI.
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/tools.json"
TIMEOUT = 15
WORKERS = 8
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 "
    "agent-capability-atlas-link-check"
)
# Hosts that deliberately reject non-browser clients; a 403 is expected.
KNOWN_BLOCKED = {"docs.opencv.org"}
BLOCKED_CODES = {403, 429}


def fetch(url, method):
    request = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        return response.status


def check(item):
    url = item["url"]
    host = urllib.parse.urlparse(url).hostname or ""
    last_error = ""
    for attempt in range(2):
        for method in ("HEAD", "GET"):
            try:
                return item, fetch(url, method), ""
            except urllib.error.HTTPError as error:
                last_error = f"HTTP {error.code}"
                if method == "HEAD" and error.code in (403, 405, 429):
                    continue
                if error.code in BLOCKED_CODES:
                    return item, error.code, "blocked by site"
                if error.code < 500 or attempt == 1:
                    return item, error.code, last_error
            except Exception as error:  # noqa: BLE001 - report any transport failure
                last_error = f"{type(error).__name__}: {error}"
                if method == "HEAD":
                    continue
    return item, None, last_error


def classify(status, host):
    if status is None:
        return "broken"
    if status in BLOCKED_CODES:
        return "ok" if host in KNOWN_BLOCKED else "blocked"
    if 200 <= status < 400:
        return "ok"
    return "broken"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, data))

    rows = []
    for item, status, detail in results:
        host = urllib.parse.urlparse(item["url"]).hostname or ""
        state = classify(status, host)
        rows.append((state, item, status, detail))

    order = {"broken": 0, "blocked": 1, "ok": 2}
    rows.sort(key=lambda row: (order[row[0]], row[1]["name"]))
    broken = [row for row in rows if row[0] == "broken"]
    blocked = [row for row in rows if row[0] == "blocked"]
    ok = len(rows) - len(broken) - len(blocked)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print("# Link check\n")
    print(f"Checked {len(rows)} source links at {stamp}.")
    print(f"**{ok} reachable · {len(blocked)} blocked · {len(broken)} broken**\n")
    if broken or blocked:
        print("| State | Tool | Link | Detail |")
        print("| --- | --- | --- | --- |")
        for state, item, status, detail in broken + blocked:
            label = "❌ broken" if state == "broken" else "⚠️ blocked"
            code = f"HTTP {status}" if status else detail
            print(f"| {label} | {item['name']} | {item['url']} | {code} |")
        print()
    if not broken:
        print("No broken links." if blocked else "All links responded.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
