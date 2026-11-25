import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app import LOGIN, load_data, snapshot


def test_public_snapshots():
    data = json.loads((ROOT / "demo" / "snapshot.json").read_text(encoding="utf-8"))
    df = load_data(ROOT / "data" / "train.csv")
    expected = {"all": snapshot(df)}
    expected.update({login: snapshot(df[df.Login_Frequency == login]) for login in LOGIN})
    assert data == expected
    assert sum(data[l]["metrics"]["total_customers"] for l in LOGIN) == len(df)
