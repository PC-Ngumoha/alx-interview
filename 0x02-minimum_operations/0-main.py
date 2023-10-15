#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 20
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 27
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 31
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 101
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
