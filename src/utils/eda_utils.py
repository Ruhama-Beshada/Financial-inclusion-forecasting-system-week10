import matplotlib.pyplot as plt

def plot_trend(series, title):
    plt.figure(figsize=(10, 5))
    plt.plot(series.index, series.values, marker='o')
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Average Value")
    plt.grid(True)
    plt.show()
