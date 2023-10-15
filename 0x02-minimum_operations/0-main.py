#!/usr/bin/python3
"""
Main file for testing
"""
import time
minOperations = __import__('0-minoperations').minOperations

start = time.perf_counter()
n = 1000
print("Min # of operations to reach {} char: {} time: {} seconds".format(
  n, minOperations(n), time.perf_counter() - start))