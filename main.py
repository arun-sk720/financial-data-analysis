from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_status

def main():
    df = clean_data('data/sample_data.csv')
    results = analyze_data(df)

    print("Total Loans:", results['total_loans'])
    print("Average Interest:", results['avg_interest'])

    print("\nStatus Counts:\n", results['status_counts'])
    print("\nAvg Interest by Status:\n", results['avg_interest_by_status'])

    print("\nHigh Risk Loans:\n", results['high_risk_loans'])

    plot_status(results['status_counts'])

if __name__ == "__main__":
    main()
