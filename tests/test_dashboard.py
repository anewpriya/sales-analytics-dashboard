import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from app import ROOT, create_app, load_data, snapshot
from evaluate_model import evaluate


@pytest.fixture
def data():
    return load_data(ROOT / "data" / "train.csv")


def test_original_metrics(data):
    result = snapshot(data)
    assert result["metrics"] == dict(total_customers=2000, churned_customers=737,
                                     active_customers=1263, churn_rate=36.85)
    assert result["comparison"]["active"]["avg_daily_usage_mins"] == 47.7
    assert result["comparison"]["churned"]["avg_daily_usage_mins"] == 16.4


def test_segments(data):
    result = snapshot(data)
    for groups in result["segments"].values():
        assert sum(g["total_customers"] for g in groups) == len(data)
        assert sum(g["churned_customers"] for g in groups) == int(data.Churn.sum())


def test_api(data):
    client = create_app(data).test_client()
    assert client.get("/").status_code == 200
    assert client.get("/api/health").json["total_records"] == 2000
    for endpoint in ["dashboard", "metrics", "comparison", "insights", "segments"]:
        assert client.get("/api/" + endpoint).status_code == 200
    daily = client.get("/api/dashboard?login=Daily").json
    assert daily["metrics"]["total_customers"] == int((data.Login_Frequency == "Daily").sum())
    assert client.get("/api/dashboard?login=invalid").status_code == 400
    assert "Email" not in client.get("/api/dashboard").get_data(as_text=True)


def test_empty_group(data):
    result = snapshot(data.iloc[:0])
    assert result["metrics"]["churn_rate"] is None
    assert result["comparison"]["active"]["avg_daily_usage_mins"] is None


def test_model(data):
    result = evaluate(data)
    assert result["train_rows"] == 1600
    assert result["test_rows"] == 400
    assert 0 <= result["roc_auc"] <= 1
    assert sum(map(sum, result["confusion_matrix"])) == 400
