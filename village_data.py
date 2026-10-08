"""Step 3: turn the activity log into village/village_data.json."""
import json
from datetime import datetime, timedelta
from pathlib import Path

LOG = Path("activity_log.jsonl")
OUT = Path("village/village_data.json")
BUILDING_FOR = {"writer": "workshop", "checker": "hall",
                "publisher": "site", "trader": "field"}

def recent_events(hours=48):
    cutoff = datetime.now() - timedelta(hours=hours)
    events = []
    if not LOG.exists():
        return events
    for line in LOG.read_text(encoding="utf-8").splitlines():
        e = json.loads(line)
        if datetime.strptime(e["ts"], "%Y-%m-%d %H:%M") >= cutoff:
            events.append({"time": e["ts"][11:], "from": "hall", "at": BUILDING_FOR.get(e["who"], "hall"),
                           "text": e["text"]})
    return events[-30:]

def build(pages, results):
    data = {"generated": datetime.now().isoformat(timespec="minutes"),
            "pages": pages, "events": recent_events(), "fields": results}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data), encoding="utf-8")

def main():
    build(pages=[{"title": "Home page", "url": "/", "views": 84}],
          results={"strategy_a": 120, "strategy_b": -40})

if __name__ == "__main__":
    main()
