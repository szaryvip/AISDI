# nolo
from typing import List


def find_kmp(substring: str, text: str) -> List[int]:
    """Parameters:
        substring: substring to be found
        text: text to be searched
    Returns:
        List of positions in ascending order of the beginnings of
        `substring` in `text`.
    """
    text_len = len(text)
    subs_len = len(substring)
    if subs_len == 0:
        raise ValueError("substring cant be empty!")
    text_index = 0
    subs_index = 0
    back_index = 0
    back = False
    indexes = []
    while text_index != text_len:
        letter = text[text_index]
        if back:
            back_index += 1
        if letter == substring[subs_index]:
            if letter == substring[0] and not back:
                back = not back
            if subs_index == subs_len-1:
                indexes.append(text_index-subs_len+1)
                text_index -= back_index
                back = False
                back_index = 0
                subs_index = 0
            else:
                subs_index += 1
        else:
            text_index -= back_index
            back = False
            back_index = 0
            subs_index = 0
        text_index += 1
    return indexes
