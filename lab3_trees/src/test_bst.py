from bst import BSTTree
from generated_list import mylist


def test_create_empty_list():
    tree = BSTTree([])
    assert tree.top() == None


def test_create_with_None():
    tree = BSTTree(None)
    assert tree.top() == None


def test_tree_one_item():
    tree = BSTTree([1])
    assert tree.top().value() == 1


def test_tree_top_2_sons():
    tree = BSTTree([2,1,3])
    assert tree.top().value() == 2
    assert tree.top().left_son().value() == 1
    assert tree.top().right_son().value() == 3


def test_tree_3_elements():
    tree = BSTTree([1,2,3])
    assert tree.top().value() == 1
    assert tree.top().left_son() == None
    assert tree.top().right_son().value() == 2
    assert tree.top().right_son().right_son().value() == 3


def test_tree_hights():
    tree = BSTTree([2,1,3,4])
    assert tree.top().left_height() == 1
    assert tree.top().right_height() == 2
    assert tree.height() == 2


def test_tree_deleting_leaf():
    tree = BSTTree([2,1,3,4])
    assert tree.top().left_son().value() == 1
    tree.delete(1)
    assert tree.top().left_son() == None


def test_tree_deleting_node_with_one_son():
    tree = BSTTree([2,1,3,4])
    assert tree.top().right_son().value() == 3
    tree.delete(3)
    assert tree.top().right_son().value() == 4


def test_tree_deleting_node_with_2_sons():
    tree = BSTTree([2,1,4,3,5])
    assert tree.top().right_son().value() == 4
    tree.delete(4)
    assert tree.top().right_son().value() == 5
    assert tree.top().right_son().left_son().value() == 3
    assert tree.top().right_son().right_son() == None
