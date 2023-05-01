import matplotlib.pyplot as plt

def plot(title, xlabel, ylabel, results, filename, base=2):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xscale("log", base=base)
    
    for (label, size, time) in results:
        plt.plot(size, time, label=label, marker='o', markersize=4)

    plt.legend(loc="upper left")

    plt.savefig(filename)
    plt.clf()