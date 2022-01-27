from merge import merge_sort
from bubble import bubble_sort
from quick import quick_sort
from selection import selection_sort
from create_list import create_list_from_text_file, pan_tadeusz
import sys
sys.setrecursionlimit(5000)

def test_bubble_sort_8(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:8])
	assert True


def test_bubble_sort_16(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:16])
	assert True


def test_bubble_sort_32(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:32])
	assert True


def test_bubble_sort_64(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:64])
	assert True


def test_bubble_sort_128(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:128])
	assert True


def test_bubble_sort_256(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:256])
	assert True


def test_bubble_sort_512(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:512])
	assert True


def test_bubble_sort_1024(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:1024])
	assert True


def test_bubble_sort_2048(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:2048])
	assert True


def test_bubble_sort_4096(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:4096])
	assert True


def test_bubble_sort_8192(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:8192])
	assert True


def test_bubble_sort_16384(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:16384])
	assert True


def test_bubble_sort_32768(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:32768])
	assert True


def test_bubble_sort_65536(benchmark):
	benchmark(bubble_sort, pan_tadeusz[:65536])
	assert True


def test_selection_sort_8(benchmark):
	benchmark(selection_sort, pan_tadeusz[:8])
	assert True


def test_selection_sort_16(benchmark):
	benchmark(selection_sort, pan_tadeusz[:16])
	assert True


def test_selection_sort_32(benchmark):
	benchmark(selection_sort, pan_tadeusz[:32])
	assert True


def test_selection_sort_64(benchmark):
	benchmark(selection_sort, pan_tadeusz[:64])
	assert True


def test_selection_sort_128(benchmark):
	benchmark(selection_sort, pan_tadeusz[:128])
	assert True


def test_selection_sort_256(benchmark):
	benchmark(selection_sort, pan_tadeusz[:256])
	assert True


def test_selection_sort_512(benchmark):
	benchmark(selection_sort, pan_tadeusz[:512])
	assert True


def test_selection_sort_1024(benchmark):
	benchmark(selection_sort, pan_tadeusz[:1024])
	assert True


def test_selection_sort_2048(benchmark):
	benchmark(selection_sort, pan_tadeusz[:2048])
	assert True


def test_selection_sort_4096(benchmark):
	benchmark(selection_sort, pan_tadeusz[:4096])
	assert True


def test_selection_sort_8192(benchmark):
	benchmark(selection_sort, pan_tadeusz[:8192])
	assert True


def test_selection_sort_16384(benchmark):
	benchmark(selection_sort, pan_tadeusz[:16384])
	assert True


def test_selection_sort_32768(benchmark):
	benchmark(selection_sort, pan_tadeusz[:32768])
	assert True


def test_selection_sort_65536(benchmark):
	benchmark(selection_sort, pan_tadeusz[:65536])
	assert True


def test_merge_sort_8(benchmark):
	benchmark(merge_sort, pan_tadeusz[:8])
	assert True


def test_merge_sort_16(benchmark):
	benchmark(merge_sort, pan_tadeusz[:16])
	assert True


def test_merge_sort_32(benchmark):
	benchmark(merge_sort, pan_tadeusz[:32])
	assert True


def test_merge_sort_64(benchmark):
	benchmark(merge_sort, pan_tadeusz[:64])
	assert True


def test_merge_sort_128(benchmark):
	benchmark(merge_sort, pan_tadeusz[:128])
	assert True


def test_merge_sort_256(benchmark):
	benchmark(merge_sort, pan_tadeusz[:256])
	assert True


def test_merge_sort_512(benchmark):
	benchmark(merge_sort, pan_tadeusz[:512])
	assert True


def test_merge_sort_1024(benchmark):
	benchmark(merge_sort, pan_tadeusz[:1024])
	assert True


def test_merge_sort_2048(benchmark):
	benchmark(merge_sort, pan_tadeusz[:2048])
	assert True


def test_merge_sort_4096(benchmark):
	benchmark(merge_sort, pan_tadeusz[:4096])
	assert True


def test_merge_sort_8192(benchmark):
	benchmark(merge_sort, pan_tadeusz[:8192])
	assert True


def test_merge_sort_16384(benchmark):
	benchmark(merge_sort, pan_tadeusz[:16384])
	assert True


def test_merge_sort_32768(benchmark):
	benchmark(merge_sort, pan_tadeusz[:32768])
	assert True


def test_merge_sort_65536(benchmark):
	benchmark(merge_sort, pan_tadeusz[:65536])
	assert True


def test_quick_sort_8(benchmark):
	benchmark(quick_sort, pan_tadeusz[:8])
	assert True


def test_quick_sort_16(benchmark):
	benchmark(quick_sort, pan_tadeusz[:16])
	assert True


def test_quick_sort_32(benchmark):
	benchmark(quick_sort, pan_tadeusz[:32])
	assert True


def test_quick_sort_64(benchmark):
	benchmark(quick_sort, pan_tadeusz[:64])
	assert True


def test_quick_sort_128(benchmark):
	benchmark(quick_sort, pan_tadeusz[:128])
	assert True


def test_quick_sort_256(benchmark):
	benchmark(quick_sort, pan_tadeusz[:256])
	assert True


def test_quick_sort_512(benchmark):
	benchmark(quick_sort, pan_tadeusz[:512])
	assert True


def test_quick_sort_1024(benchmark):
	benchmark(quick_sort, pan_tadeusz[:1024])
	assert True


def test_quick_sort_2048(benchmark):
	benchmark(quick_sort, pan_tadeusz[:2048])
	assert True


def test_quick_sort_4096(benchmark):
	benchmark(quick_sort, pan_tadeusz[:4096])
	assert True


def test_quick_sort_8192(benchmark):
	benchmark(quick_sort, pan_tadeusz[:8192])
	assert True


def test_quick_sort_16384(benchmark):
	benchmark(quick_sort, pan_tadeusz[:16384])
	assert True


def test_quick_sort_32768(benchmark):
	benchmark(quick_sort, pan_tadeusz[:32768])
	assert True


def test_quick_sort_65536(benchmark):
	benchmark(quick_sort, pan_tadeusz[:65536])
	assert True


