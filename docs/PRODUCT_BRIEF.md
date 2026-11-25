# Product brief

## Problem
Product and lifecycle teams need to identify behavioural segments associated with churn and decide which interventions to test.

## Users
Product managers, growth marketers and customer success leads.

## MVP
- Aggregate churn metrics, engagement comparisons and segment-level churn proportions.
- Login-frequency filter; tenure and usage segmentation.
- Action recommendations with hypotheses and measurement plans.
- Offline interpretable classification baseline for analytical learning.

## Acceptance criteria
Metrics reconcile to the source CSV; segment totals reconcile to the selected population; invalid filters return a clear error; names, emails and ticket text are not exposed by the API; empty groups display unavailable values.

## Decisions
Keep the Flask/React stack. Use account-tenure bands, not time-based retention cohorts, because the dataset has no event history. Do not deploy a customer-level risk score without pre-outcome features and prospective validation.

## Success measures
Proposed usability test: users can identify a segment and articulate a testable intervention without assistance. Measure task completion and time to insight. No user testing has been conducted.
