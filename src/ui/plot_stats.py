from matplotlib import pyplot as plt

class PlotStats:
    """Luokka joka visualisoi saaamansa datan."""
    def __init__(self, data):
        """Luokan konstruktori, joka luo uuden PlotStats-olion.

        Args:
            Visualisoitava data.
        """
        self.data = data

    def plot_hbar(self):
        """Piirtää vaakapalkkikaavion sanakirjassa olevan datan perusteella."""

        tags = list(self.data.keys())
        counts = list(self.data.values())
        plt.barh(tags, counts)
        plt.xlabel("Count")
        plt.title("Count of Tags")
        plt.xticks(range(0, max(counts) + 1))
        plt.show()