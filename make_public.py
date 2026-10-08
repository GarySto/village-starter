"""Step 10: a public-safe copy of the data. Never publish the private file.
Run:  py make_public.py   -> writes public/village_data.json"""
import json
from pathlib import Path


def make_public(data):
    pub = dict(data)
    pub["requests"] = [{"id": r["id"], "from": r["from"], "title": "A decision for the owner"}
                       for r in data.get("requests", [])]
    pub["fields"] = {k: round(v / 50) * 50 for k, v in data["fields"].items()}
    return pub


if __name__ == "__main__":
    data = json.loads(Path("village/village_data.json").read_text(encoding="utf-8"))
    Path("public").mkdir(exist_ok=True)
    Path("public/village_data.json").write_text(json.dumps(make_public(data)), encoding="utf-8")
    print("Wrote public/village_data.json - check it before you publish it")
