#!/usr/bin/python3
"""
In this problem, we are given a character `H` in a file and a number `n` and
we are asked to create a function that calculates the minimum number of
operations `num_ops` required to get `n` number of `H` characters in the
file. A point to note is that we can only perform these two operations in the
file: `Copy All` and `Paste`
"""


# ITERATIVE APPROACH

# def minOperations(n: int) -> int:
#     """
#     minOperations(n)

#     Args:
#         - n (int) -> number of H characters to create

#     Returns:
#         - num_ops (int) -> number of operations required to create n H
#         characters
#     """
#     if n <= 1:
#         return 0
#     all_ops = [0] * (n + 1)

#     for i in range(2, n + 1):
#         all_ops[i] = i

#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 all_ops[i] = min(all_ops[i], all_ops[j] + i // j)
#     return all_ops[n]


# RECURSIVE APPROACH

def minOperations(n: int, memo: dict = {}) -> int:
    """
    minOperations(n)

    Args:
        - n (int) -> number of H characters to create
        - memo (dict) -> a cache to store the values from previous recursions

    Returns:
        - num_ops (int) -> number of operations required to create n H
        characters
    """
    if n in memo:
        return memo[n]

    if n <= 1:
        return 0

    min_ops = n 

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            min_ops = min(min_ops, minOperations(i, memo) + n // i)

    memo[n] = min_ops
    return min_ops
