from matplotlib import pyplot as plt

class PlotStats:
    def __init__(self, data):
        self.data = data

    def plot_hbar(self):
        tags = list(self.data.keys())
        counts = list(self.data.values())
        plt.barh(tags, counts)
        plt.xlabel("Count")
        plt.title("Count of Tags")
        plt.xticks(range(0, max(counts) + 1))
        plt.show()