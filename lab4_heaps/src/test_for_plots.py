from heap import Heap
from generated_list import mylist
import pytest


length_list = [10000, 20000, 30000, 40000, 60000, 80000, 100000]


@pytest.mark.parametrize("length", length_list)
def test_dheap_creating(length, benchmark):
    def function():
        dheap = Heap(2, mylist[:length])
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_theap_creating(length, benchmark):
    def function():
        theap = Heap(3, mylist[:length])
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_qheap_creating(length, benchmark):
    def function():
        qheap = Heap(4, mylist[:length])
    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_dheap_pop(length, benchmark):
    def function():
        dheap = Heap(2, mylist)
        for i in range(length):
            dheap.pop()

    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_theap_pop(length, benchmark):
    def function():
        theap = Heap(3, mylist)
        for i in range(length):
            theap.pop()

    benchmark(function)


@pytest.mark.parametrize("length", length_list)
def test_qheap_pop(length, benchmark):
    def function():
        qheap = Heap(4, mylist)
        for i in range(length):
            qheap.pop()

    benchmark(function)
