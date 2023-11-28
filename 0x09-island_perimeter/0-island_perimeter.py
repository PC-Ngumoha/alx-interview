#!/usr/bin/python3
"""
0-island_perimeter: Implements my solution to the algo problem from ALX.
"""


def island_perimeter(grid):
    """ island_perimeter()

    Parameters:
      - grid: Grid representing the island for which we want the perimeter.

    Returns:
      - perimeter of the island.
    """
    def get_perimeter(i, j):
        """ get_perimeter()

        Parameters:
          - i: current row being evaluated
          - j: current column being evaluated

        Returns:
          - 1, 0 or sum of perimeter of the current cell under consideration.
        """
        if (i < 0 or i > len(grid) - 1) or (j < 0 or j > len(grid[i]) - 1):
            return 1
        if grid[i][j] == 0:
            return 1
        if grid[i][j] == 'v':
            return 0
        grid[i][j] = 'v'
        return (get_perimeter(i, j-1) + get_perimeter(i-1, j)
                + get_perimeter(i, j+1) + get_perimeter(i+1, j))

    result = 0
    if type(grid) != list:
        return 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                result = get_perimeter(row, col)
    return result

# NOTE: This is not my code
# def island_perimeter(grid):
#     """Computes the perimeter of an island with no lakes.
#     """
#     perimeter = 0
#     if type(grid) != list:
#         return 0
#     n = len(grid)
#     for i, row in enumerate(grid):
#         m = len(row)
#         for j, cell in enumerate(row):
#             if cell == 0:
#                 continue
#             edges = (
#                 i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
#                 j == m - 1 or (m > j + 1 and row[j + 1] == 0),
#                 i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
#                 j == 0 or row[j - 1] == 0,
#             )
#             perimeter += sum(edges)
#     return perimeter
