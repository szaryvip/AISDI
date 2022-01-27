from find_n import find_n


def test_find_1(function=find_n):
    results = function("ACACAGT", "ACAT ACGACACAGT")
    assert results == [8]


def test_find_2(function=find_n):
    results = function("ABCDABD", "ABC ABCDAB ABCDABCDABDE")
    assert results == [15]


def test_find_3(function=find_n):
    results = function("PATI", "MANAMANAPATIPITIPI")
    assert results == [8]


def test_find_4(function=find_n):
    results = function("AABA", "AABAACAADAABAABA")
    assert results == [0, 9, 12]


def test_find_5(function=find_n):
    results = function("AAAAA", "AAAAAAAAAAAAAAAAAA")
    assert results == list(range(14))


def test_find_6(function=find_n):
    results = function("CAT", "CATCATCATDOCGY")
    assert results == [0, 3, 6]


def test_find_7(function=find_n):
    results = function("DOG", "CATCATCATDOCGY")
    assert results == []


def test_find_8(function=find_n):
    results = function("", "AAAABLAHBLAHAAAA")
    assert results == []


def test_find_9(function=find_n):
    results = function("CATONAG", "CATONAG")
    assert results == [0]


def test_find_10(function=find_n):
    results = function("DOGSGBDR", "DOGS")
    assert results == []


def test_find_11(function=find_n):
    results = function("", "")
    assert results == []


def test_multiple_matches_2():
    assert find_n('a', 'aaaaa') == [0, 1, 2, 3, 4]
