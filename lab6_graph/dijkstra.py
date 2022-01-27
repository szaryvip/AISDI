from __future__ import annotations
import argparse

from draw_colour_map import draw_colour_map


class Node:
    def __init__(self, distance: int = None, source: Node = None):
        self.distance = distance  # None == infinity
        self.source = source
        self.ready = False
        self.neighbours = None


def split_text(text: str) -> dict:
    """
    Change string do map (dict)
    In:
    - text: str -> map where \n is new line
    Out:
    - map: dict -> dict where key is (x,y), value is the distance
    """
    rows = text.split("\n")
    rows = [list(row) for row in [row.strip() for row in rows]]
    map_ = {}
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            map_[(x, y)] = int(cell)
    return map_


def read_file(file_name: str) -> dict:
    """
    Open and read a file with map
    In:
    - file_name: str -> path of the file
    Out:
    - map: dict -> dict where key is (x,y), value is the distance
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        map_ = "".join([line for line in file])
        return split_text(map_)


def get_neighbours(key: tuple, table: dict) -> list:
    """
    Find neighbours of the node
    In:
    - key: tuple -> tuple is (x, y) of the node in the map
    - table: dict -> table with distance between nodes
    Out:
    - list: list -> list with tuples (x, y) of the neighbours
    """
    source = key
    x, y = key
    neighbours = []
    try:
        if not table[(x+1, y)].ready:
            neighbours.append((x+1, y, source))
    except KeyError:
        pass
    try:
        if not table[(x, y+1)].ready:
            neighbours.append((x, y+1, source))
    except KeyError:
        pass
    try:
        if not table[(x-1, y)].ready:
            neighbours.append((x-1, y, source))
    except KeyError:
        pass
    try:
        if not table[(x, y-1)].ready:
            neighbours.append((x, y-1, source))
    except KeyError:
        pass
    return neighbours


def print_map(map_: dict):
    """
    Printing the map
    In:
    - map_: dict -> dict where key is (x,y), value is the distance
    """
    width = max(key[0] for key in map_.keys())+1
    height = max(key[1] for key in map_.keys())+1
    ready_map = ""
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) in map_:
                row += str(map_[(x, y)])
            else:
                row += " "
        ready_map += " ".join(list(row))
        if y != height-1:
            ready_map += "\n"
    print(ready_map)


def dijkstra(first_zero_xy: tuple, the_table: dict, map_: dict) -> dict:
    """
    Change the_table by dijkstra algorithm
    In:
    - map_: dict -> dict where key is (x,y), value is the distance
    - first_zero_xy: tuple -> coords of first zero
    - the_table: dict -> table with distance between nodes
    Out:
    - the_table: dict -> table change by dijkstra
    """
    to_check = get_neighbours(first_zero_xy, the_table)
    while to_check != []:
        to_check.sort(key=lambda x: the_table[x[2]].distance)
        x, y, source = to_check.pop(0)
        act_distance = the_table[source].distance + map_[(x, y)]
        if (the_table[(x, y)].distance is None or
                act_distance < the_table[(x, y)].distance):
            the_table[(x, y)].distance = act_distance
            the_table[(x, y)].source = source
        try:
            the_table[source].neighbours.remove((x, y, source))
        except ValueError:
            the_table[source].ready = True
        to_check += the_table[(x, y)].neighbours
    return the_table


def do_you_know_the_way(zeros: list, the_table: dict, map_: dict) -> dict:
    """
    Find the shortest way between zeros
    In:
    - map_: dict -> dict where key is (x,y), value is the distance
    - zeros: list -> list with zeros' coords
    - the_table: dict -> table with distance between nodes
    Out:
    - the_way: dict -> dict with (x, y) as keys and distance as values
    """
    the_way = {}
    act_node = zeros[1]
    while act_node != zeros[0]:
        the_way[act_node] = map_[act_node]
        act_node = the_table[act_node].source
    the_way[act_node] = map_[act_node]
    return the_way


def find_zeros(map_: dict) -> list:
    """
    Find zeros on the map
    In:
    - map_: dict -> dict where key is (x,y), value is the distance
    Out:
    - list: list -> list with zeros' coords
    """
    zeros = [key for key in map_.keys() if map_[key] == 0]
    try:
        zeros[0]
    except IndexError:
        raise BufferError("No zero in the map")
    try:
        zeros[1]
    except IndexError:
        raise BufferError("No second zero in the map")
    if len(zeros) > 2:
        raise BufferError("Too many zeros on the map")
    return zeros


def main(file_name: str, colour: bool = False,
            way_colour: str = None,
            zeros_colour: str = None,
            emptiness_colour: str = None):
    """
    Open a file with map and draw the shortest way on the screen.
    In:
    - file_name: str -> path of the file
    """
    our_map = read_file(file_name)
    the_table = dict((key, Node()) for key in our_map.keys())

    for key in the_table.keys():
        the_table[key].neighbours = get_neighbours(key, the_table)
    zeros = find_zeros(our_map)

    the_table[zeros[0]].distance = 0
    the_table = dijkstra(zeros[0], the_table, our_map)

    the_way = do_you_know_the_way(zeros, the_table, our_map)

    if colour:
        if way_colour is None:
            way_colour = "yellow"
        if zeros_colour is None:
            zeros_colour = "blue"
        if emptiness_colour is None:
            emptiness_colour = "grey"
        draw_colour_map(our_map, the_way,
                        way_colour, zeros_colour, emptiness_colour)
    else:
        print_map(the_way)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('map', help="Path to txt file with map")
    parser.add_argument('-c', '--colour', required=False, type=bool,
                        help="Print colour solution")
    parser.add_argument('-w', '--way_colour', required=False, type=str,
                        help="Colour of the way")
    parser.add_argument('-z', '--zeros_colour', required=False, type=str,
                        help="Colour of the zeros")
    parser.add_argument('-e', '--emptiness_colour', required=False, type=str,
                        help="Colour of the emptiness")
    args = parser.parse_args()
    main(args.map, args.colour,
         way_colour=args.way_colour,
         zeros_colour=args.zeros_colour,
         emptiness_colour=args.emptiness_colour)
