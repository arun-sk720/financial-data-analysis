import matplotlib.pyplot as plt

def plot_status(status_counts):
    status_counts.plot(kind='bar')
    plt.savefig('reports/output_report.png')
    plt.close()
