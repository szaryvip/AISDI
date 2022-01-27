from find_kr import find_kr


def test_find_1(function=find_kr):
    results = function("ACACAGT", "ACAT ACGACACAGT")
    assert results == [8]


def test_find_2(function=find_kr):
    results = function("ABCDABD", "ABC ABCDAB ABCDABCDABDE")
    assert results == [15]


def test_find_3(function=find_kr):
    results = function("PATI", "MANAMANAPATIPITIPI")
    assert results == [8]


def test_find_4(function=find_kr):
    results = function("AABA", "AABAACAADAABAABA")
    assert results == [0, 9, 12]


def test_find_5(function=find_kr):
    results = function("AAAAA", "AAAAAAAAAAAAAAAAAA")
    assert results == list(range(14))


def test_find_6(function=find_kr):
    results = function("CAT", "CATCATCATDOCGY")
    assert results == [0, 3, 6]


def test_find_7(function=find_kr):
    results = function("DOG", "CATCATCATDOCGY")
    assert results == []


def test_find_8(function=find_kr):
    results = function("", "AAAABLAHBLAHAAAA")
    assert results == []


def test_find_9(function=find_kr):
    results = function("CATONAG", "CATONAG")
    assert results == [0]


def test_find_10(function=find_kr):
    results = function("DOGSGBDR", "DOGS")
    assert results == []


def test_find_11(function=find_kr):
    results = function("", "")
    assert results == []
