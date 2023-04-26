import matplotlib.pyplot as plt

def plot(title, xlabel, ylabel, results, filename, base=2):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    for (label, size, time) in results:
        plt.plot(size, time, label=label)

    plt.legend(loc="upper left")
    plt.xscale("log", base=base)

    plt.savefig(filename)
    plt.clf()