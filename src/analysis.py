import pandas as pd

def analyze_data(df):
    results = {}

    # Basic stats
    results['total_loans'] = df['loan_amount'].sum()
    results['avg_interest'] = df['interest_rate'].mean()

    # Status count
    results['status_counts'] = df['status'].value_counts()

    # NEW: Avg interest per status
    results['avg_interest_by_status'] = df.groupby('status')['interest_rate'].mean()

    # NEW: High-risk loans
    avg_interest = df['interest_rate'].mean()
    results['high_risk_loans'] = df[df['interest_rate'] > avg_interest]

    # ✅ ADD THIS (correlation)
    results['correlation'] = df.corr(numeric_only=True)

    return results
