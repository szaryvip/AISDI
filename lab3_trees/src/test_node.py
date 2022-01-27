from node import Node

def test_create_node_without_sons():
    mynode = Node(None, 5)
    assert mynode.value() == 5
    assert mynode.parent() == None
    assert mynode.left_son() == None
    assert mynode.right_son() == None


def test_create_node_with_family():
    parent = Node(None, 6)
    left = Node(None, 3)
    right = Node(None, 5)
    actual = Node(parent, 4, left, right)
    parent.set_left_son(actual)
    assert actual.parent() == parent
    assert actual.left_son() == left
    assert actual.right_son() == right
    assert left.parent() == actual
    assert right.parent() == actual


def test_node_one_son():
    parent = Node(None, 6)
    left = Node(None, 3)
    right = Node(None, 5)
    actual = Node(parent, 4, left, right)
    parent.set_left_son(actual)
    assert parent.one_son() == True
    assert actual.one_son() == False


def test_node_heights():
    parent = Node(None, 6)
    left = Node(None, 3)
    right = Node(None, 5)
    actual = Node(parent, 4, left, right)
    parent.set_left_son(actual)
    assert actual.left_height() == 1
    assert actual.right_height() == 1
    assert left.left_height() == 0


def test_node_deep():
    parent = Node(None, 6)
    left = Node(None, 3)
    right = Node(None, 5)
    actual = Node(parent, 4, left, right)
    parent.set_left_son(actual)
    assert parent.deep() == 0
    assert actual.deep() == 1
    assert left.deep() == 2
    assert right.deep() == 2


def test_node_balance():
    parent = Node(None, 6)
    left = Node(None, 3)
    right = Node(None, 5)
    actual = Node(parent, 4, left, right)
    parent.set_left_son(actual)
    assert actual.balance() == 0


def test_node_is_leaf():
    parent = Node(None, 6)
    left = Node(None, 3)
    right = Node(None, 5)
    actual = Node(parent, 4, left, right)
    parent.set_left_son(actual)
    assert left.is_leaf() == True
    assert right.is_leaf() == True
    assert actual.is_leaf() == False


def test_reset_node():
    parent = Node(None, 3)
    node = Node(parent, 2)
    left = Node(node, 1)
    assert node.parent() == parent
    assert node.left_son() == None
    node.reset(None, 5, left)
    assert node.parent() == None
    assert node.value() == 5
    assert node.left_son() == left


def test_node_x_y():
    node = Node(None, 2)
    assert node.x() == 0
    assert node.y() == 0
    node.set_x(2)
    node.set_y(4)
    assert node.x() == 2
    assert node.y() == 4



