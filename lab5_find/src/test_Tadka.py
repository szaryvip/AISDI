from find_kmp import find_kmp
from find_kr import find_kr
from find_n import find_n
from pan_Tadek import tekst, slowa
import pytest


n_list = list(range(100, 1100, 100))


@pytest.mark.parametrize("n", n_list)
def test_find_kmp_n_words(n, benchmark):
    def function():
        for slowo in slowa[:n]:
            find_kmp(slowo, tekst)
    benchmark(function)


@pytest.mark.parametrize("n", n_list)
def test_find_kr_n_words(n, benchmark):
    def function():
        for slowo in slowa[:n]:
            find_kr(slowo, tekst)
    benchmark(function)


@pytest.mark.parametrize("n", n_list)
def test_find_n_n_words(n, benchmark):
    def function():
        for slowo in slowa[:n]:
            find_n(slowo, tekst)
    benchmark(function)
