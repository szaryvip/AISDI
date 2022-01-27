
lengths = [2**x for x in range(3, 17)]
names = ['bubble_sort', 'selection_sort', 'merge_sort', 'quick_sort']


with open('test_pan_tadeusz.py', 'w', encoding='utf8') as file_handle:
    print('''from merge import merge_sort
from bubble import bubble_sort
from quick import quick_sort
from selection import selection_sort
from create_list import create_list_from_text_file, pan_tadeusz
import sys
sys.setrecursionlimit(5000)\n''', file=file_handle)
    for name in names:
        for length in lengths:
            print(f'def test_{name}_{length}(benchmark):', file=file_handle)
            print(f'\tbenchmark({name}, pan_tadeusz[:{length}])\n\tassert True', file=file_handle)
            print('', file=file_handle)
            print('', file=file_handle)
