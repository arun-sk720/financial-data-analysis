import os
import matplotlib.pyplot as plt

def plot_status(status_counts):
    os.makedirs('reports', exist_ok=True)

    status_counts.plot(kind='bar')
    plt.title('Loan Status Distribution')
    plt.xlabel('Status')
    plt.ylabel('Count')

    plt.savefig('reports/output_report.png')
    plt.close()
