import json
from app import ROOT, load_data, snapshot

if __name__ == "__main__":
    print(json.dumps(snapshot(load_data(ROOT / "data" / "train.csv")), indent=2))
