from dijkstra import split_text, get_neighbours, Node
from dijkstra import dijkstra, do_you_know_the_way, find_zeros
from pytest import raises


def test_split_text_1():
    mapa = "10\n12"
    map_ = split_text(mapa)
    assert map_ == {(0, 0): 1, (1, 0): 0, (0, 1): 1, (1, 1): 2}


def test_split_text_2():
    mapa = "394\n423"
    map_ = split_text(mapa)
    assert map_ == {(0, 0): 3, (1, 0): 9, (2, 0): 4,
                    (1, 0): 4, (1, 1): 2, (1, 2): 3}


def test_split_text_3():
    mapa = "024\n932\n422"
    map_ = split_text(mapa)
    assert map_ == {(0, 0): 0, (1, 0): 2, (2, 0): 4,
                    (1, 0): 9, (1, 1): 3, (1, 2): 2,
                    (2, 0): 4, (2, 1): 2, (2, 2): 2}


def test_split_text_empty():
    mapa = ""
    assert split_text(mapa) == {}


def test_get_neighbours_1():
    our_map = split_text("10\n12")
    the_table = dict((key, Node()) for key in our_map.keys())
    neighbours = get_neighbours((0, 0), the_table)
    assert neighbours == [(1, 0, (0, 0)), (0, 1, (0, 0))]


def test_get_neighbours_2():
    our_map = split_text("759\n276\n304")
    the_table = dict((key, Node()) for key in our_map.keys())
    neighbours = get_neighbours((1, 1), the_table)
    assert neighbours == [(1, 0, (0, 0)), (0, 1, (0, 0)),
                          (1, 2, (0, 0)), (2, 1, (0, 0))]


def test_find_zeros_1():
    map_ = split_text("10\n10")
    assert find_zeros(map_) == [(1, 0), (1, 1)]


def test_find_zeros_2():
    map_ = split_text("9044\n7476\n9460\n7434")
    assert find_zeros(map_) == [(0, 1), (2, 3)]


def test_find_zeros_no_zero():
    map_ = split_text("15\n12")
    with raises(BufferError):
        find_zeros(map_)


def test_find_zeros_only_one():
    map_ = split_text("10\n12")
    with raises(BufferError):
        find_zeros(map_)


def test_find_zeros_too_many_zeros():
    map_ = split_text("00\n02")
    with raises(BufferError):
        find_zeros(map_)


def test_dijkstra():
    our_map = split_text("10\n01")
    the_table = dict((key, Node()) for key in our_map.keys())
    for key in the_table.keys():
        the_table[key].neighbours = get_neighbours(key, the_table)
    zeros = find_zeros(our_map)
    the_table[zeros[0]].distance = 0
    the_table = dijkstra((1, 0), the_table, our_map)
    exp_node_1 = Node(1, (0, 1))
    exp_node_2 = Node(1, (1, 1))
    assert the_table[(0, 0)].distance == exp_node_1.distance
    assert the_table[(1, 1)].distance == exp_node_2.distance


def test_do_you_know_the_way():
    our_map = split_text("20\n01")
    the_table = dict((key, Node()) for key in our_map.keys())
    for key in the_table.keys():
        the_table[key].neighbours = get_neighbours(key, the_table)
    zeros = find_zeros(our_map)
    the_table[zeros[0]].distance = 0
    the_table = dijkstra((1, 0), the_table, our_map)
    the_way = do_you_know_the_way(zeros, the_table, our_map)
    assert the_way == {(0, 1): 0, (1, 1): 1, (1, 0): 0}
