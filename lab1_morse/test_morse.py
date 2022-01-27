from morse import morse, translate
from io import StringIO
import argparse
import sys
import os


def test_txt_file(benchmark):
    result = benchmark(translate, "test.txt")
    assert result == '.- .-..'


def test_morse_01(benchmark):
    result = benchmark(morse, ["tekst do tlumaczenia"])
    assert result == '- . -.- ... - / -.. --- / - .-.. ..- -- .- -.-. --.. . -. .. .-'

def test_morse_02(benchmark):
    data = list(StringIO("tekst do tlumaczenia"))
    result = benchmark(morse, data)
    assert result == '- . -.- ... - / -.. --- / - .-.. ..- -- .- -.-. --.. . -. .. .-'


def test_not_existed_file(benchmark):
    result = benchmark(translate, "notexisted.file")
    assert result == "[-] File not found!"
