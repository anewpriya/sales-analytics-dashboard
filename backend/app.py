from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load data once when the app starts
df = pd.read_csv('data/train.csv')

# Route 1: Get overall metrics
@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """
    Returns overall churn metrics
    GET /api/metrics
    """
    total_customers = len(df)
    churned_customers = df['Churn'].sum()
    active_customers = total_customers - churned_customers
    churn_rate = (churned_customers / total_customers) * 100
    
    return jsonify({
        'total_customers': int(total_customers),
        'churned_customers': int(churned_customers),
        'active_customers': int(active_customers),
        'churn_rate': round(churn_rate, 2)
    })

# Route 2: Get detailed comparison
@app.route('/api/comparison', methods=['GET'])
def get_comparison():
    """
    Returns detailed metrics comparing churned vs active customers
    GET /api/comparison
    """
    churned = df[df['Churn'] == 1]
    active = df[df['Churn'] == 0]
    
    return jsonify({
        'churned': {
            'count': int(len(churned)),
            'avg_account_age_days': round(churned['Account_Age_Days'].mean(), 1),
            'avg_daily_usage_mins': round(churned['Daily_Usage_Mins'].mean(), 1),
            'login_frequency': churned['Login_Frequency'].value_counts().to_dict()
        },
        'active': {
            'count': int(len(active)),
            'avg_account_age_days': round(active['Account_Age_Days'].mean(), 1),
            'avg_daily_usage_mins': round(active['Daily_Usage_Mins'].mean(), 1),
            'login_frequency': active['Login_Frequency'].value_counts().to_dict()
        }
    })

# Route 3: Get insights
@app.route('/api/insights', methods=['GET'])
def get_insights():
    """
    Returns business insights derived from the data
    GET /api/insights
    """
    churned = df[df['Churn'] == 1]
    active = df[df['Churn'] == 0]
    
    usage_diff = active['Daily_Usage_Mins'].mean() - churned['Daily_Usage_Mins'].mean()
    age_diff = active['Account_Age_Days'].mean() - churned['Account_Age_Days'].mean()
    churn_rate = (df['Churn'].sum() / len(df)) * 100
    
    return jsonify({
        'insights': [
            f"Active customers use the platform {usage_diff:.1f} more minutes/day than churned customers",
            f"Churned customers are {age_diff:.1f} days younger on average (newer accounts)",
            f"Overall churn rate is {churn_rate:.1f}%",
            "Low daily usage is the strongest indicator of churn risk"
        ]
    })

# Route 4: Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    GET /api/health
    """
    return jsonify({
        'status': 'API is running',
        'data_loaded': True,
        'total_records': len(df)
    })

if __name__ == '__main__':
    print("🚀 Starting SaaS Analytics API...")
    print("📊 Loaded", len(df), "customer records")
    print("Visit http://localhost:5000/api/health to test")
    app.run(debug=True, host='localhost', port=5000)