from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, request, send_from_directory

ROOT = Path(__file__).resolve().parents[1]
FEATURES = ["Account_Age_Days", "Login_Frequency", "Daily_Usage_Mins", "Churn"]
LOGIN = ["Daily", "Weekly", "Rarely"]


def load_data(path):
    df = pd.read_csv(path, usecols=FEATURES)
    if df.empty or df.isna().any().any():
        raise ValueError("Dataset is empty or contains missing values")
    if not df.Churn.isin([0, 1]).all() or not df.Login_Frequency.isin(LOGIN).all():
        raise ValueError("Invalid churn or login category")
    if (df[["Account_Age_Days", "Daily_Usage_Mins"]] < 0).any().any():
        raise ValueError("Negative tenure or usage")
    return df


def summarise(df):
    n = len(df)
    churned = int(df.Churn.sum())
    return dict(total_customers=n, churned_customers=churned,
                active_customers=n - churned,
                churn_rate=round(100 * churned / n, 2) if n else None)


def describe(df):
    def mean(col):
        return round(float(df[col].mean()), 1) if len(df) else None
    return dict(count=len(df), avg_account_age_days=mean("Account_Age_Days"),
                avg_daily_usage_mins=mean("Daily_Usage_Mins"),
                login_frequency={k: int((df.Login_Frequency == k).sum()) for k in LOGIN})


def compare(df):
    return {name: describe(df[df.Churn == label])
            for name, label in [("active", 0), ("churned", 1)]}


def segments(df):
    result = {}
    for key, column, bins, labels in [
        ("tenure", "Account_Age_Days", [-1, 90, 365, float("inf")], ["0–90 days", "91–365 days", "366+ days"]),
        ("usage", "Daily_Usage_Mins", [-1, 15, 30, 60, float("inf")], ["0–15 min", "16–30 min", "31–60 min", "61+ min"]),
    ]:
        groups = pd.cut(df[column], bins=bins, labels=labels)
        result[key] = [dict(label=label, **summarise(df[groups == label])) for label in labels]
    result["login"] = [dict(label=label, **summarise(df[df.Login_Frequency == label])) for label in LOGIN]
    return result


def snapshot(df):
    c = compare(df)
    a, b = c["active"], c["churned"]
    insights = []
    if a["count"] and b["count"]:
        gap = df[df.Churn == 0].Daily_Usage_Mins.mean() - df[df.Churn == 1].Daily_Usage_Mins.mean()
        insights.append(f"Active minus churned average daily usage: {gap:.1f} minutes.")
    insights.append("Observed associations do not establish causation or future churn risk.")
    return dict(metrics=summarise(df), comparison=c, segments=segments(df), insights=insights)


def create_app(data=None):
    app = Flask(__name__)
    df = load_data(ROOT / "data" / "train.csv") if data is None else data

    def selected():
        login = request.args.get("login", "all")
        if login != "all" and login not in LOGIN:
            return None
        return df if login == "all" else df[df.Login_Frequency == login]

    @app.get("/")
    def index():
        return send_from_directory(ROOT / "frontend", "index.html")

    @app.get("/<path:filename>")
    def assets(filename):
        return send_from_directory(ROOT / "frontend", filename)

    @app.get("/api/health")
    def health():
        return jsonify(status="ok", total_records=len(df))

    @app.get("/api/dashboard")
    @app.get("/api/metrics")
    @app.get("/api/comparison")
    @app.get("/api/insights")
    @app.get("/api/segments")
    def dashboard():
        subset = selected()
        if subset is None:
            return jsonify(error="Invalid login filter"), 400
        data = snapshot(subset)
        key = request.path.rsplit("/", 1)[-1]
        if key == "dashboard":
            return jsonify(data)
        if key == "insights":
            return jsonify(insights=data[key])
        return jsonify(data[key])

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
