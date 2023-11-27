# Island Perimeter (Mock Interview)

## My Thought Process

### Overview
Let's say that we're given an grid like this:

```
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
```

By representing this as a graph, we can see that the grid looks like this:

```
     _
  0 |1| 0 0
   _   _
  |1 1 1| 0
  0 |1| 0 0
   _
  |1 1| 0 0
   _ _
```
From the diagram above (Or at least my attempt at drawing a diagram 😊), we can see that the parameter of the given island is denoted by the use of the **|** and **_** symbols. So from the above diagram, we can denote that the perimeter of the island denoted by the given formation of **1**s is **16**. But, now the question on your mind and on the mind of anyone who ever worked on this project is going to be **HOW**? So, let's talk about that.

### Constraints
An important point to make is the fact that islands within the grid can come in any form possible but for this problem, we're only considering those which meet and comply with the following contraints:
- They are completely surrounded by water. Essentially we're expecting to have a structure of **1**s surrounded by a pool of **0**s.
- There is only one island in each grid.
- Islands can not have lakes within them. Essentially there shouldn't be a situation where we have a **0** in the midst of **1**s.

### Observations
Now, with these constraints in mind and observing the figure above, we can notice a few things about where we marked out the perimeter for the given island. some of these are:
- The edge of the island that borders the end of the grid on either the horizontal (row of the grid) or the vertical (column of the grid) is counted as part of the perimeter of the island within said grid. And as such should contribute a **1** to the overall count for the perimeter.

- The edge of a cell of land on the island which borders a cell of water (_i.e_ any cell with the value of **0** ) on either the horizontal or the vertical is also counted as part of the parameter of the island within said grid. And as such should contribute a **1** to the overall count for the perimeter.

- The search for the perimeter is also to be conducted in all four directions of the current cell.

- To eliminate the possibility of counting the perimeter of a cell of land on the island more than once, we need to have a way of keeping track of which cells of land we have already visited. And then we are able to avoid revisiting them. Thus, they contribute a **0** to the overall count for the perimeter.

- Also, to eliminate the rate of occurrence of false starts, we'll to iterate through as many rows and columns of the grid containing **0**s until we get to one containing a **1** and then from that point we can start the search.

### Pseudocode
So, with all these observations in mind, we can create the following pseudocode:

```

func island_perimeter(Grid) -> {
  FOR row in Grid:
    FOR column in Grid[row]:
      if Grid[row][column].EQUALS(1):
        RETURN get_perimeter(row, column)
}

func get_perimeter(row, column) -> {
  // OUT OF GRID BOUNDARIES
  IF row < Grid.left or row > Grid.right or column < Grid[row].left or column > Grid[row].right:
    RETURN 1
  // CURRENTLY ON WATER
  IF Grid[row][column].EQUALS(0):
    RETURN 1
  // ARE WE REVISITING THIS CELL?
  IF Grid[row][column].EQUALS('v'):
    RETURN 0
  // CHECK TO THE left, top, right and bottom
  RETURN get_perimeter(row, column - 1) + get_perimeter(row - 1, column)
    + get_perimeter(row, column + 1) + get_perimeter(row + 1, column)
}
```
