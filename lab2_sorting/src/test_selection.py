from selection import min, selection_sort
from random import randint

def test_min_1(benchmark):
    result = benchmark(min, [9, 2, 7, 3, 0])
    assert result == 0


def test_min_2(benchmark):
    result = benchmark(min, [-10, 35, 9, -4, 17])
    assert result == -10


def test_min_3(benchmark):
    result = benchmark(min, [17])
    assert result == 17

def test_selection_sorting_1(benchmark):
    result = benchmark(selection_sort, [5, 3, 8, 4, 8, 4, 90, 3, 0, 1, 5])
    assert result == [0, 1, 3, 3, 4, 4, 5, 5, 8, 8, 90]


def test_selection_sorting_2(benchmark):
    result = benchmark(selection_sort, [1, 6, 3, 8, 4, 0, 1, 5, 764, 64, 96, 36])
    assert result == [0, 1, 1, 3, 4, 5, 6, 8, 36, 64, 96, 764]


def test_selection_sorting_3(benchmark):
    result = benchmark(selection_sort, [445, 5, 576, 100, 633, 93, 9, 559, 341, 409, 626, 621, 543, 202, 8, 215, 487, 589, 25, 392, 256, 554, 186, 184, 476, 122, 3, 636, 125, 144, 407, 525, 594, 404, 229, 585, 176, 188, 387, 52, 599, 492, 509, 159, 634, 616, 617, 169, 643, 154, 590, 640, 533, 442, 516, 513, 278, 281, 244, 92, 132, 474, 487, 454, 590, 477, 197, 423, 316, 45, 200, 92, 462, 66, 309, 518, 328, 196, 88, 517, 375, 485, 93, 334, 465, 149, 16, 327, 229, 202, 612, 263, 71, 43, 427, 615, 32, 273, 332, 576])
    assert result == [3, 5, 8, 9, 16, 25, 32, 43, 45, 52, 66, 71, 88, 92, 92, 93, 93, 100, 122, 125, 132, 144, 149, 154, 159, 169, 176, 184, 186, 188, 196, 197, 200, 202, 202, 215, 229, 229, 244, 256, 263, 273, 278, 281, 309, 316, 327, 328, 332, 334, 341, 375, 387, 392, 404, 407, 409, 423, 427, 442, 445, 454, 462, 465, 474, 476, 477, 485, 487, 487, 492, 509, 513, 516, 517, 518, 525, 533, 543, 554, 559, 576, 576, 585, 589, 590, 590, 594, 599, 612, 615, 616, 617, 621, 626, 633, 634, 636, 640, 643]


def test_selection_sorting_4(benchmark):
    result = benchmark(selection_sort, [319, 617, 357, 189, 608, 409, 400, 47, 88, 78, 509, 645, 156, 139, 304, 40, 562, 645, 502, 433, 412, 446, 266, 33, 644, 440, 409, 542, 360, 542, 470, 36, 440, 119, 497, 110, 183, 513, 553, 352, 134, 122, 610, 535, 13, 414, 527, 244, 399, 226, 638, 538, 136, 107, 382, 286, 343, 408, 395, 232, 118, 297, 40, 627, 54, 86, 542, 505, 308, 105, 62, 344, 12, 552, 34, 655, 633, 159, 538, 421, 475, 651, 380, 306, 491, 615, 613, 215, 422, 177, 19, 106, 41, 145, 216, 474, 217, 488, 267, 115])
    assert result == [12, 13, 19, 33, 34, 36, 40, 40, 41, 47, 54, 62, 78, 86, 88, 105, 106, 107, 110, 115, 118, 119, 122, 134, 136, 139, 145, 156, 159, 177, 183, 189, 215, 216, 217, 226, 232, 244, 266, 267, 286, 297, 304, 306, 308, 319, 343, 344, 352, 357, 360, 380, 382, 395, 399, 400, 408, 409, 409, 412, 414, 421, 422, 433, 440, 440, 446, 470, 474, 475, 488, 491, 497, 502, 505, 509, 513, 527, 535, 538, 538, 542, 542, 542, 552, 553, 562, 608, 610, 613, 615, 617, 627, 633, 638, 644, 645, 645, 651, 655]


def test_selection_sorting_5(benchmark):
    new_list = []
    for i in range(100):
        new_list.append(randint(0, 5363))
    result = benchmark(selection_sort, new_list)
    assert result == sorted(new_list)


def test_selection_sorting_6(benchmark):
    result = benchmark(selection_sort, [])
    assert result == []


def test_selection_sorting_7(benchmark):
    result = benchmark(selection_sort, [4, 4, 4, 4, 4])
    assert result == [4, 4, 4, 4, 4]
