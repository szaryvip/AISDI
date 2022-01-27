# Szary
from typing import List


def hash_func(substring: str) -> int:
    """
    Calculates hash for substring
    Returns integer
    Parameters:
    substring: substring to be found
    """
    new_hash = 0
    for letter in substring:
        new_hash += ord(letter)
    return new_hash


def next_hash(old_hash: int, first_letter: str, next_letter: str) -> int:
    """
    Calculates next hash in text
    Returns integer
    Parameters:
    old_hash: previous hash of piece of text
    first_letter: first letter of previously hashed text
    next_letter: next letter in text
    """
    new_hash = old_hash - ord(first_letter)
    new_hash += ord(next_letter)
    return new_hash


def find_kr(substring: str, text: str) -> List[int]:
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
    value_sub = hash_func(substring)
    value_text = hash_func(text[:pattern_len])
    for i in range(len(text)-pattern_len+1):
        if value_sub == value_text:
            if substring == text[i:i+pattern_len]:
                pattern_list.append(i)
        if i < (len(text)-pattern_len):
            value_text = next_hash(value_text, text[i], text[i+pattern_len])
    return pattern_list
