from termcolor import colored as c


def draw_colour_map(map_: dict, way: dict,
                way_colour: str = "yellow",
                zero_colour: str = "blue",
                emptiness_colour: str = "grey"):
    """
    Printing the map with colour
    In:
    - map_: dict -> dict where key is (x,y), value is the distance
    - way: dict -> dict with (x, y) as keys and distance as values
    Optional In:
    - way_colour: str -> colour of the way
    - zero_colour: str -> colour of the zeros
    - emptiness_colour: str -> colour of the rest of the map
    """
    width = max(key[0] for key in map_.keys())+1
    height = max(key[1] for key in map_.keys())+1
    for y in range(height):
        for x in range(width):
            if (x, y) in way:
                if way[(x, y)] == 0:
                    print(c(str(map_[(x, y)]), zero_colour), end=" ")
                else:
                    print(c(str(map_[(x, y)]), way_colour), end=" ")
            else:
                print(c(str(map_[(x, y)]), emptiness_colour), end=" ")
        print()
