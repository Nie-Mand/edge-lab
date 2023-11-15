import matplotlib.pyplot as plt


def plot(simulator, l, fpath):

    dataset = []
    for _ in range(l):
        dataset.append(simulator.next_value())

    x = range(len(dataset))
    y = dataset

    # Plot
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Collected data")
    plt.title("Collected data from sensor")
    plt.savefig(fpath + "-plot.png")

    # Histogram
    plt.clf()
    plt.hist(dataset, bins=100)
    plt.xlabel("X")
    plt.ylabel("Frequency")
    plt.savefig(fpath + "-histogram.png")
