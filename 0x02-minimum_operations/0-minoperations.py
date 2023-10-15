#!/usr/bin/python3
"""
In this problem, we are given a character `H` in a file and a number `n` and
we are asked to create a function that calculates the minimum number of
operations `num_ops` required to get `n` number of `H` characters in the
file. A point to note is that we can only perform these two operations in the
file: `Copy All` and `Paste`
"""


def minOperations(n: int) -> int:
    """
    minOperations(n)

    Args:
        - n (int) -> number of H characters to create

    Returns:
        - num_ops (int) -> number of operations required to create n H
        characters
    """
    num_ops: int = 0
    copy_buffer: str = ''
    text_buffer: str = 'H'

    while True:
        if len(text_buffer) == n:
            return num_ops
        if len(text_buffer) > n or num_ops > n:
            return 0
        if n % len(text_buffer) == 0:
            copy_buffer = text_buffer
            num_ops += 1
        text_buffer += copy_buffer
        num_ops += 1
