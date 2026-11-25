# SaaS Retention Intelligence

A product analytics prototype for product, growth and customer success teams. Explore behavioural differences, segment churn and prioritise lifecycle experiments.

## Findings

| Metric | Synthetic sample |
| --- | ---: |
| Customers | 2,000 |
| Active | 1,263 |
| Churned | 737 |
| Churn proportion | 36.85% |
| Average daily usage (active / churned) | 47.7 / 16.4 min |

The observed usage gap is approximately 31.3 minutes/day. It is an association, not causal evidence or a validated future-risk predictor.

## Run locally

Python 3.10–3.12 recommended.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python backend/app.py
```

Open http://127.0.0.1:5000. The frontend uses React and Chart.js CDN assets (internet connection required).

```bash
python backend/analyze_data.py
python backend/evaluate_model.py
python -m pytest -q
```

## Architecture

React + Chart.js → same-origin Flask API → pandas → static CSV. The offline scikit-learn model is separate from the dashboard.

API: /api/health, /api/dashboard, /api/metrics, /api/comparison, /api/insights, /api/segments. Analytics accept an optional login filter (Daily, Weekly or Rarely).

## Product evidence

- [Product brief](docs/PRODUCT_BRIEF.md)
- [Case study](docs/CASE_STUDY.md)
- [Experiment plan](docs/EXPERIMENT_PLAN.md)
- [Data and model notes](docs/DATA_AND_MODEL.md)

## Limitations

Synthetic, cross-sectional data; original dataset URL and redistribution terms unverified. No live customer outcomes, longitudinal cohorts, real-time data, production deployment or prospective model validation. Public redistribution should be reviewed against the source licence.

Author: Anupriya Singh · MIT licence applies to project code.
