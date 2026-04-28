def analyze_data(df):
    total_loans = df['loan_amount'].sum()
    avg_interest = df['interest_rate'].mean()
    status_counts = df['status'].value_counts()
    return {"total_loans": total_loans, "avg_interest": avg_interest, "status_counts": status_counts}
