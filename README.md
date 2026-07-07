# SaaS Analytics Dashboard

A full-stack web application for analyzing customer churn metrics and business performance. Built with Python Flask backend, React frontend, and interactive data visualization.

## 🎯 Project Overview

This project demonstrates a complete data analytics pipeline:
- **Data Analysis**: Real SaaS customer data (2,000+ records) analyzed with pandas
- **Backend API**: Flask REST API with 4 endpoints serving JSON metrics
- **Frontend Dashboard**: React interactive dashboard with Chart.js visualizations

## 📊 Key Metrics & Insights

- **Churn Rate**: 36.85% (737 out of 2,000 customers)
- **Active Customers**: 1,263
- **Critical Finding**: Active customers use the platform **31.3 more minutes/day** than churned customers
- **Business Implication**: Low daily usage is the strongest predictor of churn risk

## 🏗️ Project Structure

sales-analytics-dashboard/
├── backend/
│   ├── analyze_data.py
│   └── app.py
├── frontend/
│   └── index.html
├── data/
│   ├── train.csv
│   └── test_.csv
└── README.md

## 🚀 Tech Stack

**Backend:**
- Python 3.12
- Flask (REST API framework)
- pandas (data analysis)
- Flask-CORS (cross-origin requests)

**Frontend:**
- React 18 (via CDN)
- Chart.js (interactive charts)
- Vanilla HTML/CSS

**Data:**
- Kaggle SaaS Customer Churn Dataset
- 2,000 customer records with behavior metrics

## 📈 API Endpoints

### 1. GET `/api/health`
Health check endpoint

### 2. GET `/api/metrics`
Overall churn metrics

### 3. GET `/api/comparison`
Detailed comparison of churned vs active customers

### 4. GET `/api/insights`
Business insights derived from analysis

## 🎨 Dashboard Features

- **Metric Cards**: Total customers, churned, active, churn rate
- **Doughnut Chart**: Active vs churned customer split
- **Bar Charts**: Usage comparison and login frequency distribution
- **Key Insights**: 4 business insights auto-calculated from data
- **Responsive Design**: Works on desktop and mobile

## 🔧 Setup & Installation

### Prerequisites
- Python 3.12+
- Git

### Backend Setup

1. Clone the repository
```bash
   git clone https://github.com/anewpriya/sales-analytics-dashboard.git
   cd sales-analytics-dashboard
```

2. Install Python dependencies
```bash
   py -3.12 -m pip install flask flask-cors pandas
```

3. Run the Flask API
```bash
   py -3.12 backend/app.py
```
   API runs on `http://localhost:5000`

### Frontend Setup

1. Open the dashboard
   - Open `frontend/index.html` in your browser
   - Dashboard runs on `http://localhost:5500` (or file://)

2. Ensure Flask API is running before opening the dashboard

## 💡 Learning Outcomes

This project demonstrates:
- ✅ **Data Analysis**: Pandas for exploring customer behavior patterns
- ✅ **Backend Engineering**: REST API design and CORS implementation
- ✅ **Frontend Development**: React with external library integration
- ✅ **Data Visualization**: Interactive charts with Chart.js
- ✅ **Full-Stack Integration**: Seamless frontend-backend communication
- ✅ **Business Analytics**: Deriving actionable insights from data

## 📊 Data Source

Dataset: SaaS Customer Churn Prediction Dataset from Kaggle

**Features:**
- Customer ID, Name, Email
- Account age (days)
- Login frequency (Daily/Weekly/Rarely)
- Daily usage (minutes)
- Support ticket text
- Churn label (0=active, 1=churned)

## 🎓 Key Insights & Recommendations

### Finding 1: Usage Drives Retention
Active customers average **47.7 minutes/day** vs churned at **16.4 minutes/day**

**Recommendation**: Implement onboarding features to increase daily active usage.

### Finding 2: Newer Accounts at Risk
Churned customers are **20.4 days younger** on average

**Recommendation**: Strengthen onboarding process and early-stage customer support.

### Finding 3: Login Frequency Correlation
Active customers log in **Daily** (59.8%)
Churned customers log in **Rarely** (39.1%)

**Recommendation**: Use login frequency as an early warning signal for re-engagement campaigns.

## 🚀 Future Enhancements

- [ ] Deploy to cloud (Vercel + Heroku)
- [ ] Add database (PostgreSQL instead of CSV)
- [ ] Implement user authentication
- [ ] Add date range filtering
- [ ] Real-time data updates
- [ ] Predictive churn model (ML)

## 📝 License

MIT License - feel free to use this project for learning purposes.

## 👤 Author

**Anupriya Singh**
- GitHub: [@anewpriya](https://github.com/anewpriya)

---

**Built as a learning project to demonstrate full-stack data analytics skills.**