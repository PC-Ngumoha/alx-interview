#!/usr/bin/python3
"""
File: 0-rotate_2d_matrix.py

Purpose: Contains the function 'rotate_2d_matrix' which implements an
algorithm to rotate a 2D matrix by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """
    rotate_2d_matrix(matrix)

    Parameters:
      - matrix: The matrix we want to rotate by 90 degrees

    Returns:
      - Nothing. Rotates the matrix in place
    """
    matrix_size = len(matrix)
    last_row_index = matrix_size - 1
    temp_matrix = []
    for j in range(0, matrix_size):
        rotated_row = []
        for i in range(last_row_index, -1, -1):
            rotated_row.append(matrix[i][j])
        temp_matrix.append(rotated_row)
    matrix[:] = temp_matrix
