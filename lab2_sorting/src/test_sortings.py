from merge import merge_sort
from bubble import bubble_sort
from quick import quick_sort
from selection import selection_sort
from create_list import create_list_from_text_file, pan_tadeusz

length = 10000

def test_quick_sort(benchmark):
    result = benchmark(quick_sort, pan_tadeusz[:length])
    assert result == sorted(pan_tadeusz[:length])


def test_merge_sort(benchmark):
    result = benchmark(merge_sort, pan_tadeusz[:length])
    assert result == sorted(pan_tadeusz[:length])


def test_selection_sort(benchmark):
    result = benchmark(selection_sort, pan_tadeusz[:length])
    assert result == sorted(pan_tadeusz[:length])


def test_bubble_sort(benchmark):
    result = benchmark(bubble_sort, pan_tadeusz[:length])
    assert result == sorted(pan_tadeusz[:length])
