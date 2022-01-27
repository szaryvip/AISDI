import json
import sys
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

path = '.benchmarks/Linux-CPython-3.8-64bit'
files = [f for f in listdir(path) if isfile(join(path, f))]
files.sort()
our_file = files[-1]
our_path = path + '/' + our_file

with open(our_path, 'r') as file:
    values = {'bst_insert': [], 'avl_insert': [], 'bst_find': [], 'avl_find': [], 'bst_delete': [], 'avl_delete': []}
    data = json.load(file)
    data = data['benchmarks']
    for item in data:
        if 'bst_tree_inserting' in item['name']:
            values['bst_insert'].append(item['stats']['min'])
        if 'avl_tree_inserting' in item['name']:
            values['avl_insert'].append(item['stats']['min'])
        if 'bst_tree_finding' in item['name']:
            values['bst_find'].append(item['stats']['min'])
        if 'avl_tree_finding' in item['name']:
            values['avl_find'].append(item['stats']['min'])
        if 'bst_tree_deleting' in item['name']:
            values['bst_delete'].append(item['stats']['min'])
        if 'avl_tree_deleting' in item['name']:
            values['avl_delete'].append(item['stats']['min'])

def draw_plot(y_lines = False, save = True, mode = 'insert', file_name = "Trees_plot.png"):
    x_ticks = [100, 1000, 2000, 4000, 6000, 8000, 10000]
    if mode == 'find' or mode == 'delete':
        y_ticks = [1e-4, 1e-2, 2e-2, 4e-2, 8e-2, 1e-1]
    elif mode == 'insert':
        y_ticks = [1, 10, 20, 40, 80, 140]
    plt.xticks(x_ticks)
    plt.yticks(y_ticks)
    plt.xlabel("Items")
    plt.ylabel("Seconds")
    title = f'{mode}'
    plt.title(title)
    if y_lines:
        for y in y_ticks:
            plt.hlines(y, x_ticks[0], x_ticks[-1], linestyles="dashed", color="gray")
    if mode == 'insert':
        plt.plot(x_ticks, values["bst_insert"], ".-", label = "BST")
        plt.plot(x_ticks, values["avl_insert"], ".-", label = "AVL")
    elif mode == 'find':
        plt.plot(x_ticks, values["bst_find"], ".-", label = "BST")
        plt.plot(x_ticks, values["avl_find"], ".-", label = "AVL")
    elif mode == 'delete':
        plt.plot(x_ticks, values["bst_delete"], ".-", label = "BST")
        plt.plot(x_ticks, values["avl_delete"], ".-", label = "AVL")

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

draw_plot(False, True, 'insert',  "Inserting.png")
