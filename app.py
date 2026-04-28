```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Financial Data Dashboard")

df = pd.read_csv("data/sample_data.csv")

st.subheader("📊 Raw Data")
st.dataframe(df)

total_loans = df['loan_amount'].sum()
avg_interest = df['interest_rate'].mean()

st.subheader("📈 Key Metrics")
st.write(f"Total Loan Amount: ₹{total_loans}")
st.write(f"Average Interest Rate: {avg_interest:.2f}%")

st.subheader("📉 Loan Status Distribution")
status_counts = df['status'].value_counts()

fig, ax = plt.subplots()
status_counts.plot(kind='bar', ax=ax)
st.pyplot(fig)
