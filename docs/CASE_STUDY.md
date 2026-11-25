# From churn analysis to product decisions

## Question
Which observed behaviours distinguish active and churned accounts, and what should a product team investigate next?

## Evidence
The synthetic sample contains 2,000 accounts: 1,263 active and 737 churned (36.85%). Active accounts average 47.7 minutes of daily use compared with 16.4 for churned accounts, a difference of approximately 31.3 minutes.

## Decisions
Prioritise investigation of activation and low engagement. Use tenure, usage and login segments to identify candidate audiences. Translate findings into proposed onboarding and re-engagement experiments rather than treating usage as a proven cause.

## Implementation
Flask serves aggregate analytics from pandas; React and Chart.js present comparisons and filters. The offline logistic regression baseline tests classification methodology separately from the dashboard.

## Next validation
Confirm original dataset provenance; collect timestamped pre-churn events; evaluate prospective risk models and run controlled experiments. No production deployment or live customer outcome is claimed.
