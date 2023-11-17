# N-Queens (Mock Interview)

## My Thoughts

For anyone who is conversant with the game of chess, it's clear that the piece we know as the queen can move any number of squares along the _columns_, _rows_ and _diagonals_ of the chess board. So for a queen to not be under attack from another queen, it has to not be in the same _row_, _column_ or _diagonal_ as that queen.

So, in order to create an algorithm which is able to check this, we are going to have to keep track of the following information:

- column number of the already positioned queen in the directly preceding row on the chess board
- positive diagonal of said queen
- negative diagonal of said queen


So, with that in mind, I came up with the following pseudocode which I hope could solve this problem in the most efficient way using the problem solving technique known as _Backtracking_:

**Pseudocode:**

```
N = INPUT()

cols = SET()
pos_diag = SET()
neg_diag = SET()
res = []

func place_queens(row: int, limit: int):
	if row == limit, then:
		PRINT res
		RETURN

	col = 0
	while col < limit:
		if cols.contain(col) or pos_diag.contain(row + col) or neg_diag.contain(row - col):
			col += 1
			SKIP
		else:
			res.ADD([row, col])
			cols.ADD(col)
			pos_diag.ADD(row + col)
			neg_diag.ADD(row - col)
			CALL place_queens(row + 1, limit)
			res.REMOVE([row, col])
			cols.REMOVE(col)
			pos_diag.REMOVE(row + col)
			neg_diag.REMOVE(row - col)

CALL place_queens(0, N)
```


## Useful Links:

- [Backtracking - Wikipedia Article](https://en.wikipedia.org/wiki/Backtracking)
- [Abdul Bari - Youtube Channel playlist on algorithms](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
- [N-Queens detailed explanation - Youtube Video](https://www.youtube.com/watch?v=Ph95IHmRp5M&t=10s)