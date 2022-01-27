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
        "find_kmp": [],
        "find_kr": [],
        "find_n": []
    }
    data = json.load(file)
    data = data["benchmarks"]
    for item in data:
        if "test_find_kmp_n_words" in item["name"]:
            values["find_kmp"].append(item["stats"]["min"])
        elif "test_find_kr_n_words" in item["name"]:
            values["find_kr"].append(item["stats"]["min"])
        elif "test_find_n_n_words" in item["name"]:
            values["find_n"].append(item["stats"]["min"])


def draw_plot(y_lines=False, save=True,
              file_name="find_algorithms.png"):
    x_ticks = list(range(100, 1100, 100))
    y_ticks = [0, 40, 80, 120]
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlabel("Words")
    plt.ylabel("Seconds")
    plt.title("Find algorithms for 100-1000 words")
    if y_lines:
        for y in y_ticks:
            plt.hlines(y, x_ticks[0], x_ticks[-1],
                       linestyles="dashed", color="gray")
    plt.plot(x_ticks, values["find_kmp"], ".-", label="Knutha-Morrisa-Pratta")
    plt.plot(x_ticks, values["find_kr"], ".-", label="Karpa-Rabina")
    plt.plot(x_ticks, values["find_n"], ".-", label="Naiwny")

    plt.legend()

    manager = plt.get_current_fig_manager()
    try:                    # version <  Qt4Agg backend
        manager.resize(*manager.window.maxsize())
    except AttributeError:  # version >= Qt4Agg backend
        manager.window.showMaximized()

    if save:
        fig = plt.gcf()
        fig.set_size_inches((12, 6), forward=False)
        fig.savefig(file_name, dpi=500)
    plt.show()


# draw_plot(True, True, "find_algorithms.png")
# draw_plot(False, True, "find_algorithms_clear.png")
