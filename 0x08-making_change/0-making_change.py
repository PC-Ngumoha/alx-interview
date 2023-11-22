#!/usr/bin/python3
"""
0-making_change.py

Contains the definition of the makeChange function which determines
the minimum number of coins in your wallet are required to meet a
a given amount
"""
from typing import List


def makeChange(coins, total):
    """Determines minimum number of coins to use as change for total.

    Parameter:
      - coins: The denominations of coins you have to make change.
      - total: The amount/denomination your coin combination has to meet.

    Returns:
      - change: The count of coins needed to meet total or -1 if not possible.
    """
    count = 0
    denominations = sorted(coins, reverse=True)

    if total <= 0:
        return count

    while len(denominations) > 0:
        current = denominations[0]
        if total >= current:
            count += int(total / current)
            total %= current
        if total == 0:
            break
        denominations.pop(0)
    if len(denominations) == 0:
        count = -1
    return count
