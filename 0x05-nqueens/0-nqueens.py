#!/usr/bin/python3
"""
0-nqueens.py

My attempt at implementing an algorithm to solve the N-Queens
mock interview question from ALX SE.
"""


def place_n_queens(n: int) -> None:
    """Wraps the main logic for the nqueens problem

    Parameters:
        - n: limit of the board's dimensions

    Returns:
        - None
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    solution = []

    def backtrack_queens(r: int) -> None:
        """ Implements the main logic

        Parameters:
            - r: current row in consideration

        Returns:
            - None

        Also Note:
            - c: current column in consideration
        """
        if r == n:
            print(solution)
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            else:
                solution.append([r, c])
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                backtrack_queens(r + 1)

                solution.remove([r, c])
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

    backtrack_queens(0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    N = sys.argv[1]

    if not N.isnumeric():
        print('N must be a number')
        sys.exit(1)

    if int(N) < 4:
        print('N must be at least 4')
        sys.exit(1)

    place_n_queens(int(N))
