import json

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, average_precision_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from app import ROOT, load_data


def evaluate(df):
    numeric = ["Account_Age_Days", "Daily_Usage_Mins"]
    categorical = ["Login_Frequency"]
    x = df[numeric + categorical]
    y = df.Churn
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y)
    preprocessing = ColumnTransformer([
        ("numeric", StandardScaler(), numeric),
        ("categorical", OneHotEncoder(handle_unknown="ignore", drop="first"), categorical),
    ])
    model = make_pipeline(preprocessing, LogisticRegression(max_iter=1000))
    model.fit(x_train, y_train)
    probability = model.predict_proba(x_test)[:, 1]
    predicted = (probability >= 0.5).astype(int)
    return {
        "train_rows": len(x_train), "test_rows": len(x_test),
        "threshold": 0.5, "test_prevalence": float(y_test.mean()),
        "majority_baseline_accuracy": float(max(y_test.mean(), 1-y_test.mean())),
        "accuracy": accuracy_score(y_test, predicted),
        "precision": precision_score(y_test, predicted, zero_division=0),
        "recall": recall_score(y_test, predicted, zero_division=0),
        "roc_auc": roc_auc_score(y_test, probability),
        "average_precision": average_precision_score(y_test, probability),
        "confusion_matrix": confusion_matrix(y_test, predicted, labels=[0,1]).tolist(),
        "limitation": "Synthetic cross-sectional classification; no prospective validation. Behaviour may have been measured after churn."
    }


if __name__ == "__main__":
    print(json.dumps(evaluate(load_data(ROOT / "data" / "train.csv")), indent=2))
