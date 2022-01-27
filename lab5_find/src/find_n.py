# Szary
from typing import List


def find_n(substring: str, text: str) -> List[int]:
    """
    Parameters:
    substring: substring to be found
    text: text to be searched
    Returns:
    List of positions in ascending order of the beginnings of
    ``substring`` in ``text``.
    """
    pattern_list = []
    pattern_len = len(substring)
    if pattern_len > len(text) or pattern_len == 0:
        return pattern_list
    for i in range(len(text[:-(pattern_len)])+1):
        j = 0
        while j < pattern_len and text[i+j] == substring[j]:
            j += 1
        if j == pattern_len:
            pattern_list.append(i)
    return pattern_list
