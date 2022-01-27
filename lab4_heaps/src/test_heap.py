from heap import Heap
from pytest import raises


def test_create_dheap_empty():
    heap = Heap(2)
    assert heap.get_raw_data() == []


def test_dheap_peek_empty():
    heap = Heap(2)
    with raises(IndexError):
        heap.peek()


def test_dheap_pop_empty():
    heap = Heap(2)
    with raises(IndexError):
        heap.pop()


def test_create_dheap_and_peek():
    heap = Heap(2, ['a'])
    assert heap.peek() == 'a'


def test_dheap_get_raw_data():
    heap = Heap(2, [4, 3, 2, 1])
    expected_list = [4, 3, 2, 1]
    assert heap.get_raw_data() == expected_list


def test_dheap_push():
    heap = Heap(2, [4, 3, 2])
    heap.push(1)
    expected_list = [4, 3, 2, 1]
    assert heap.get_raw_data() == expected_list


def test_dheap_pop():
    heap = Heap(2, [4, 3, 2, 1])
    expected_list = [3, 1, 2]
    poped = heap.pop()
    assert poped == 4
    assert heap.get_raw_data() == expected_list


def test_create_theap_empty():
    heap = Heap(3)
    assert heap.get_raw_data() == []


def test_theap_peek_empty():
    heap = Heap(3)
    with raises(IndexError):
        heap.peek()


def test_theap_pop_empty():
    heap = Heap(3)
    with raises(IndexError):
        heap.pop()


def test_create_theap_and_peek():
    heap = Heap(3, ['a'])
    assert heap.peek() == 'a'


def test_theap_get_raw_data():
    heap = Heap(3, [4, 3, 2, 1])
    expected_list = [4, 3, 2, 1]
    assert heap.get_raw_data() == expected_list


def test_theap_push():
    heap = Heap(3, [4, 3, 2])
    heap.push(1)
    expected_list = [4, 3, 2, 1]
    assert heap.get_raw_data() == expected_list


def test_theap_pop():
    heap = Heap(3, [4, 3, 2, 1])
    expected_list = [3, 1, 2]
    poped = heap.pop()
    assert poped == 4
    assert heap.get_raw_data() == expected_list


def test_create_qheap_empty():
    heap = Heap(4)
    assert heap.get_raw_data() == []


def test_qheap_peek_empty():
    heap = Heap(4)
    with raises(IndexError):
        heap.peek()


def test_qheap_pop_empty():
    heap = Heap(4)
    with raises(IndexError):
        heap.pop()


def test_create_qheap_and_peek():
    heap = Heap(4, ['a'])
    assert heap.peek() == 'a'


def test_qheap_get_raw_data():
    heap = Heap(4, [4, 3, 2, 1])
    expected_list = [4, 3, 2, 1]
    assert heap.get_raw_data() == expected_list


def test_qheap_push():
    heap = Heap(4, [4, 3, 2])
    heap.push(1)
    expected_list = [4, 3, 2, 1]
    assert heap.get_raw_data() == expected_list


def test_qheap_pop():
    heap = Heap(4, [4, 3, 2, 1])
    expected_list = [3, 1, 2]
    poped = heap.pop()
    assert poped == 4
    assert heap.get_raw_data() == expected_list
