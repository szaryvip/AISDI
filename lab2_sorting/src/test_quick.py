from quick import quick_sort, partition


def test_quick_sorting_1(benchmark):
    result = benchmark(quick_sort, [4, 3, 2, 5, 1])
    assert result == [1, 2, 3, 4, 5]


def test_quick_sorting_2(benchmark):
    result = benchmark(quick_sort, [-10, -50, 0, 220, 120])
    assert result == [-50, -10, 0, 120, 220]


def test_quick_sorting_empty(benchmark):
    result = benchmark(quick_sort, [])
    assert result == []


def test_quick_sorting_equal(benchmark):
    result = benchmark(quick_sort, [7, 7, 7, 7])
    assert result == [7, 7, 7, 7]


def test_quick_sorting_3(benchmark):
    result = benchmark(quick_sort, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1])
    assert result == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_quick_sorting_4(benchmark):
    result = benchmark(quick_sort, [445, 5, 576, 100, 633, 93, 9, 559, 341, 409, 626, 621, 543, 202, 8, 215, 487, 589, 25, 392, 256, 554, 186, 184, 476, 122, 3, 636, 125, 144, 407, 525, 594, 404, 229, 585, 176, 188, 387, 52, 599, 492, 509, 159, 634, 616, 617, 169, 643, 154, 590, 640, 533, 442, 516, 513, 278, 281, 244, 92, 132, 474, 487, 454, 590, 477, 197, 423, 316, 45, 200, 92, 462, 66, 309, 518, 328, 196, 88, 517, 375, 485, 93, 334, 465, 149, 16, 327, 229, 202, 612, 263, 71, 43, 427, 615, 32, 273, 332, 576])
    assert result == [3, 5, 8, 9, 16, 25, 32, 43, 45, 52, 66, 71, 88, 92, 92, 93, 93, 100, 122, 125, 132, 144, 149, 154, 159, 169, 176, 184, 186, 188, 196, 197, 200, 202, 202, 215, 229, 229, 244, 256, 263, 273, 278, 281, 309, 316, 327, 328, 332, 334, 341, 375, 387, 392, 404, 407, 409, 423, 427, 442, 445, 454, 462, 465, 474, 476, 477, 485, 487, 487, 492, 509, 513, 516, 517, 518, 525, 533, 543, 554, 559, 576, 576, 585, 589, 590, 590, 594, 599, 612, 615, 616, 617, 621, 626, 633, 634, 636, 640, 643]
