# Data and model notes

The repository's train.csv contains 2,000 synthetic customer records (confirmed by the author). Identified source: [SaaS Customer Churn Prediction Dataset — Suhani Gupta (Kaggle)](https://www.kaggle.com/datasets/suhanigupta04/saas-customer-churn-prediction-dataset). The supplied Kaggle data card specifies CC0: Public Domain, a fictional company called TechFlow and 2,500 records split across train.csv and test.csv. The repository's 2,000-record sample matches the training dataset's reported structure and aggregate statistics. A byte-for-byte comparison with the upstream download has not been performed. Dataset licensing is separate from project code licensing. The application reads only tenure, login frequency, daily usage and churn labels; it does not return names, emails, IDs or support text.

| Field | Definition |
| --- | --- |
| Account_Age_Days | Recorded account age in days |
| Login_Frequency | Daily, Weekly or Rarely |
| Daily_Usage_Mins | Recorded daily usage in minutes |
| Churn | Binary label (1 = churned) |

Churn proportion is the fraction of records labelled churned, not a time-period churn rate. Segments use fixed illustrative bands. No dates or event histories are available.

The offline model is logistic regression with a stratified 80/20 split, standardised numeric variables and one-hot login frequency. Preprocessing is fitted only on training data. It reports ROC-AUC, average precision, precision, recall, accuracy, confusion matrix and majority baseline.

This is classification of synthetic cross-sectional labels, not validated prediction of future churn. Observation timing is unknown, so leakage is possible. No live risk scoring, causal claims, or intervention outcomes are presented. Run the evaluation script to obtain results.
