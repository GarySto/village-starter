"""Step 1: every automation calls log_activity() at its important moments.
Run this file on its own to add a few sample events."""
import json
from datetime import datetime


def log_activity(who, text, outcome="ok"):
    row = {"ts": datetime.now().strftime("%Y-%m-%d %H:%M"),
           "who": who, "text": text, "outcome": outcome}
    with open("activity_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


if __name__ == "__main__":
    log_activity("writer", "Drafted: how to build a village")
    log_activity("checker", "Checked the draft: no problems found")
    log_activity("publisher", "Published the article")
    log_activity("trader", "Closed a demo trade")
    print("Added 4 sample events to activity_log.jsonl")
