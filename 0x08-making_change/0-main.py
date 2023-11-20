#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange
import time

start_time = time.perf_counter()
# print(makeChange([1, 2, 25], 37))

# print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange())

print(f'Elapsed Time: {time.perf_counter() - start_time} seconds')
