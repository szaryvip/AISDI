import json
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

path = ".benchmarks/Linux-CPython-3.8-64bit"
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort()
our_file = files[-1]
our_path = path + "/" + our_file

with open(our_path, "r") as file:
    values = {
        "dheap_create": [],
        "theap_create": [],
        "qheap_create": [],
        "dheap_pop": [],
        "theap_pop": [],
        "qheap_pop": [],
    }
    data = json.load(file)
    data = data["benchmarks"]
    for item in data:
        if "dheap_creating" in item["name"]:
            values["dheap_create"].append(item["stats"]["min"])
        if "theap_creating" in item["name"]:
            values["theap_create"].append(item["stats"]["min"])
        if "qheap_creating" in item["name"]:
            values["qheap_create"].append(item["stats"]["min"])
        if "dheap_pop" in item["name"]:
            values["dheap_pop"].append(item["stats"]["min"])
        if "theap_pop" in item["name"]:
            values["theap_pop"].append(item["stats"]["min"])
        if "qheap_pop" in item["name"]:
            values["qheap_pop"].append(item["stats"]["min"])


def draw_plot(y_lines=False, save=True, mode="create", file_name="Heaps_plot.png"):
    x_ticks = [10000, 20000, 30000, 40000, 60000, 80000, 100000]
    if mode == "create":
        y_ticks = [4e-3, 6e-3, 1e-2, 2e-2, 4e-2, 6e-2, 8e-2]
    elif mode == "pop":
        y_ticks = [0.15, 0.2, 0.4, 0.8, 1.2, 1.6, 2.0]
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlabel("Items")
    plt.ylabel("Seconds")
    title = f"{mode}"
    plt.title(title)
    if y_lines:
        for y in y_ticks:
            plt.hlines(y, x_ticks[0], x_ticks[-1], linestyles="dashed", color="gray")
    if mode == "create":
        plt.plot(x_ticks, values["dheap_create"], ".-", label="DoubleHeap")
        plt.plot(x_ticks, values["theap_create"], ".-", label="TripleHeap")
        plt.plot(x_ticks, values["qheap_create"], ".-", label="QuadraHeap")
    elif mode == "pop":
        plt.plot(x_ticks, values["dheap_pop"], ".-", label="DoubleHeap")
        plt.plot(x_ticks, values["theap_pop"], ".-", label="TripleHeap")
        plt.plot(x_ticks, values["qheap_pop"], ".-", label="QuadraHeap")

    plt.legend()

    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    if save:
        fig = plt.gcf()
        fig.set_size_inches((12, 6), forward=False)
        fig.savefig(file_name, dpi=500)
    plt.show()


draw_plot(True, True, "pop", "HeapPopingLines.png")
