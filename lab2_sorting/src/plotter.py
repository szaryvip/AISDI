import json
import sys
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from generator_test import lengths


path = '.benchmarks/Linux-CPython-3.8-64bit'
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort()
our_file = files[-1]
our_path = path + '/' + our_file

with open(our_path, 'r') as file:
    values = {'bubble': [], 'selection': [], 'merge': [], 'quick': []}
    data = json.load(file)
    data = data['benchmarks']
    for item in data:
        if 'bubble' in item['name']:
            values['bubble'].append(item['stats']['min'])
        if 'selection' in item['name']:
            values['selection'].append(item['stats']['min'])
        if 'merge' in item['name']:
            values['merge'].append(item['stats']['min'])
        if 'quick' in item['name']:
            values['quick'].append(item['stats']['min'])


def draw_plot(y_lines = False, time = "s", save = True, file_name = "Pan_Tadeusz_plot.png"):
    x_ticks = [8, 4096, 8192, 16384, 32768, 65536]
    if time == "s":
        y_ticks = [15, 30, 60, 90, 120, 150, 180, 210, 270, 330]
    elif time == "m":
        y_ticks = [60, 120, 180, 210, 270, 330]
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlabel("Words")
    plt.ylabel("Seconds")
    plt.title('"Pan Tadeusz" sorting by various functions')
    if y_lines:
        for y in y_ticks:
            plt.hlines(y, x_ticks[0], x_ticks[-1], linestyles="dashed", color="gray")

    plt.plot(lengths, values["bubble"], ".-", label = "Bubble")
    plt.plot(lengths, values["selection"], ".-", label = "Selection")
    plt.plot(lengths, values["merge"], ".-", label = "Merge")
    plt.plot(lengths, values["quick"], ".-", label = "Quick")

    plt.legend()

    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    if save:
        fig = plt.gcf()
        fig.set_size_inches((12, 6), forward=False)
        fig.savefig(file_name, dpi=500)

    plt.show()

draw_plot(False, "s", True, "Sorting_clear.png")
