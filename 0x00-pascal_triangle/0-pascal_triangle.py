"""
0-pascal_triangle.py

Contains the code for the implementation of an algorithm that displays
the pascal's triangle of the number one less than the given positive number
"""


def pascal_triangle(rows):
    """
    pascal_triangle(n) function

    Args:
      - n -> Number of rows of pascal's triangle to generate.

    Returns:
      - output -> A list of lists of integers representing the
                  pascal's triangle of 'n'.
    """
    triangle = []
    prev_row = []

    if rows <= 0:
        return triangle

    for i in range(0, rows):
        curr_row = []

        if i == 0:
            curr_row = [1]
        else:
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    curr_row.append(1)
                    continue
                curr_row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(curr_row)
        prev_row = curr_row
    return triangle
