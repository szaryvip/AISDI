from generated_list import mylist
from bst import BSTTree
from avl import AVLTree
import pytest

length_list = [100, 1000, 2000, 4000, 6000, 8000, 10000]
full_bst_tree = BSTTree(mylist)
full_avl_tree = AVLTree(mylist)


@pytest.mark.parametrize("length", length_list)
def test_bst_tree_inserting(length, benchmark):
    def function():
        tree = BSTTree(mylist[:length])
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_avl_tree_inserting(length, benchmark):
    def function():
        tree = AVLTree(mylist[:length])
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_bst_tree_finding(length, benchmark):
    def function():
        for element in mylist[:length]:
            full_bst_tree.find(element)
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_avl_tree_finding(length, benchmark):
    def function():
        for element in mylist[:length]:
            full_avl_tree.find(element)
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_bst_tree_deleting(length, benchmark):
    def function():
        for element in mylist[:length]:
            full_bst_tree.delete(element)
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_avl_tree_deleting(length, benchmark):
    def function():
        for element in mylist[:length]:
            full_avl_tree.delete(element)
    benchmark(function)
