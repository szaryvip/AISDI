from find_kmp import find_kmp
from pytest import raises


def test_find_kmp_1():
    results = find_kmp("ACACAGT", "ACAT ACGACACAGT")
    assert results == [8]


def test_find_kmp_2():
    results = find_kmp("ABCDABD", "ABC ABCDAB ABCDABCDABDE")
    assert results == [15]


def test_find_kmp_3():
    results = find_kmp("PATI", "MANAMANAPATIPITIPI")
    assert results == [8]


def test_find_kmp_4():
    results = find_kmp("AABA", "AABAACAADAABAABA")
    assert results == [0, 9, 12]


def test_find_kmp_5():
    results = find_kmp("AAAAA", "AAAAAAAAAAAAAAAAAA")
    assert results == list(range(14))


def test_find_kmp_6():
    results = find_kmp("CAT", "CATCATCATDOCGY")
    assert results == [0, 3, 6]


def test_find_kmp_7():
    results = find_kmp("DOG", "CATCATCATDOCGY")
    assert results == []


def test_find_kmp_8():
    with raises(ValueError):
        find_kmp("", "")


def test_find_kmp_9():
    results = find_kmp("ACAB", "ACAB")
    assert results == [0]


def test_find_kmp_10():
    results = find_kmp("ACABACAD", "ACAB")
    assert results == []


def test_find_kmp_11():
    results = find_kmp("DOM", "ACACABACADAB")
    assert results == []


def test_find_kmp_12():
    with raises(ValueError):
        find_kmp("", "TCATCABACCAT")
