import pandas as pd
import numpy as np

# Load the training data
df = pd.read_csv('data/train.csv')

print("=" * 60)
print("SAAS CUSTOMER CHURN ANALYSIS - DATA OVERVIEW")
print("=" * 60)

# 1. Basic statistics
print(f"\nTotal customers: {len(df)}")
print(f"Churned customers: {df['Churn'].sum()}")
print(f"Active customers: {len(df) - df['Churn'].sum()}")

# 2. Churn rate
churn_rate = (df['Churn'].sum() / len(df)) * 100
print(f"\nChurn Rate: {churn_rate:.2f}%")

# 3. Average metrics by churn status
print("\n" + "=" * 60)
print("CHURNED vs ACTIVE CUSTOMERS")
print("=" * 60)

churned = df[df['Churn'] == 1]
active = df[df['Churn'] == 0]

print(f"\nCHURNED CUSTOMERS (n={len(churned)}):")
print(f"  - Average Account Age: {churned['Account_Age_Days'].mean():.1f} days")
print(f"  - Average Daily Usage: {churned['Daily_Usage_Mins'].mean():.1f} minutes")
print(f"  - Login Frequency breakdown:")
print(churned['Login_Frequency'].value_counts())

print(f"\nACTIVE CUSTOMERS (n={len(active)}):")
print(f"  - Average Account Age: {active['Account_Age_Days'].mean():.1f} days")
print(f"  - Average Daily Usage: {active['Daily_Usage_Mins'].mean():.1f} minutes")
print(f"  - Login Frequency breakdown:")
print(active['Login_Frequency'].value_counts())

# 4. Insights
print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

usage_diff = active['Daily_Usage_Mins'].mean() - churned['Daily_Usage_Mins'].mean()
age_diff = active['Account_Age_Days'].mean() - churned['Account_Age_Days'].mean()

print(f"\n✓ Active customers use the platform {usage_diff:.1f} more minutes/day")
print(f"✓ Churned customers are {age_diff:.1f} days younger (newer accounts)")
print(f"✓ {churn_rate:.1f}% of customers churned")

print("\n" + "=" * 60)