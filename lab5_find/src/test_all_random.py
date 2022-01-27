from find_kmp import find_kmp
from find_kr import find_kr
from find_n import find_n
import random

randint = random.randint

alphabet = ["A", "B"]
alphabet_len = len(alphabet)


def random_data():
    random_int = randint(4, 12)
    random_word = "".join(list(alphabet[randint(0, alphabet_len-1)]
                          for i in range(randint(4, random_int))))
    random_sentence = "".join(list(alphabet[randint(0, alphabet_len-1)]
                              for i in range(randint(16, random_int*10))))
    return random_word, random_sentence


def test_1():
    random_word, random_sentence = random_data()
    print(random_word, random_sentence)
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    return result_kmp == result_kr == result_n


def test_2():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_3():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_4():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_5():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_6():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_7():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_8():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n


def test_9():
    random_word, random_sentence = random_data()
    result_kmp = find_kmp(random_word, random_sentence)
    result_kr = find_kr(random_word, random_sentence)
    result_n = find_n(random_word, random_sentence)
    assert result_kmp == result_kr == result_n
