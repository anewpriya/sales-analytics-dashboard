# Data and model notes

The repository's train.csv contains 2,000 synthetic customer records (confirmed by the author). The exact original Kaggle URL and redistribution terms have not been verified. The application reads only tenure, login frequency, daily usage and churn labels; it does not return names, emails, IDs or support text.

| Field | Definition |
| --- | --- |
| Account_Age_Days | Recorded account age in days |
| Login_Frequency | Daily, Weekly or Rarely |
| Daily_Usage_Mins | Recorded daily usage in minutes |
| Churn | Binary label (1 = churned) |

Churn proportion is the fraction of records labelled churned, not a time-period churn rate. Segments use fixed illustrative bands. No dates or event histories are available.

The offline model is logistic regression with a stratified 80/20 split, standardised numeric variables and one-hot login frequency. Preprocessing is fitted only on training data. It reports ROC-AUC, average precision, precision, recall, accuracy, confusion matrix and majority baseline.

This is classification of synthetic cross-sectional labels, not validated prediction of future churn. Observation timing is unknown, so leakage is possible. No live risk scoring, causal claims, or intervention outcomes are presented. Run the evaluation script to obtain results.
