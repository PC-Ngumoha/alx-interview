#!/usr/bin/python3
"""
0-validate_utf8.py

Contains the definition of the validUTF8() function which takes
data set containing multiple characters and determines whether the
data set represents a valid UTF8 encoding.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    validUTF8(data)

    Args:
      - data (list[int]) -> data set to validate.

    Returns:
      - A bool representing whether it's valid or not.
    """
    if data is None:
        return False

    for elem in data:
        if elem < 0 or elem > 255:
            return False
        elem_bin = bin(elem)[2:].zfill(8)
        # print(elem_bin, end=' ')
        if elem_bin[0] != '0':
            return False
        if len(elem_bin) != 8:
            return False
        elem_dec = int(elem_bin, 2)
        # print(elem_dec, end=', ')
        if elem_dec > 127:
            return False
    return True
