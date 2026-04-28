from src.data_cleaning import clean_data
from src.analysis import analyze_data
from src.visualization import plot_status

def main():
    df = clean_data('data/sample_data.csv')
    results = analyze_data(df)
    print(results)
    plot_status(results['status_counts'])

if __name__ == '__main__':
    main()
