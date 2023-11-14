# Rotate 2D Matrix (Mock Interview)

## My Thought Process

**INPUT:**

3X3 Matrix

```
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```


**OUTPUT:**

3X3 Matrix formed by rotating the Input matrix at 90 degrees

```
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]

```

HOW (At Input):

```
    i0  i1  i2
j0	1	  2	  3

j1	4	  5	  6

j2	7	  8	  9
```


The following pseudocode simply copies the matrix as it is:

**Pseudocode:**
```
START PROGRAM
new_matrix = []
For i = 0; i <= matrix.length - 1; i++:
  new_matrix.at(i) = []
  For j = 0; j <= matrix.at(i).length - 1; j++:
    new_matrix.at(i).ADD(matrix.at(i).at(j))
  END For
END For
matrix = new_matrix
END PROGRAM
```




HOW (At Output):

```
  j2  j1  j0
i0  7 4 1

i1  8 5 2

i2  9 6 3
```


The following pseudocode tries to create the 90 degree rotated version of the input matrix:

**Pseudocode:**
```
START PROGRAM
new_matrix = []
For j = 0; j <= matrix.length - 1; j++:
	new_matrix.at(j) = []
	For i = matrix.at(j).length - 1; i >= 0; i--:
		new_matrix.at(i).ADD(matrix.at(i).at(j))
	END For
END For
matrix = new_matrix
END PROGRAM
```


**NOTE:** In both of the codes illustrated above, _i_ indicates a row on the matrix and _j_ indicates a column on same matrix






