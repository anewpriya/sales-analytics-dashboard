import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app import LOGIN, load_data, snapshot

if __name__ == "__main__":
    df = load_data(ROOT / "data" / "train.csv")
    data = {"all": snapshot(df)}
    data.update({login: snapshot(df[df.Login_Frequency == login]) for login in LOGIN})
    (ROOT / "demo" / "snapshot.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
