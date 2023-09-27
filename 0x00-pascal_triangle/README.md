# Pascal's Triangle (Mock Interview)

_A different way to describe the triangle is to view the first line is an infinite sequence of zeros except for a single 1_


**Typical structure**:

							1
						1		1
					1		2		1
				1		3		3		1

...


**Sample Case**: Let's we are told to find the pascal's triangle of the number 5, It will be good to picture this as a matrix as shown below with the matrix being synonymous with an array of arrays, each row of the matrix will represent the element/constituent arrays and each column representing an index in the constituent array.

  	**0	1	2	3	4	5**

**0**	1

**1**	1	1

**2**	1	2	1	

**3**	1	3	3	1

**4**	1	4	6	4	1

**5**	1	5	10	10	5	1


So, I'm noticing a trend, A few points to note:

- The size of each array within the overall is one greater than the current value of 'i' as we iteratively create the sequence 'n' times.

- In other to get the current value at the current index 'i' in the current array in formation, We need to get the sum of the elements at indexes 'i - 1' and 'i + 1' in the previous sequence/array. Where any of these do not exist, we simply add the one which does to zero (0).

- As a special case, when we are generating the zeroth array (array at index 0), we simply return an array containing a single element with the number one (1) as it's value.

From this idea, I ended up crafting the following pseudocode for an algorithm that does this.

Pseudocode:
```
function pascal_triangle(n):

	let triangle = [];
	let prev = [];

	if n <= 0:
		return triangle;

	for i in range(0, n):
		let curr = [];

		if i === 0:
			curr = [1];
		else:
			for j in range(0, i + 1):
				if j === 0 or j === 1:
					curr.add(1);
					continue;
				curr.add( prev[j - 1] + prev[j] );				
		triangle.add(curr);
		prev = curr;
	return triangle;
```


So, let's walk through the algorithm mentally. Suppose n = 5, according to our algorithm:

At i = 0;
```
prev = [], curr = [1], triangle = [[1]]
```

At i = 1; 
```
prev = [1], curr = [1, 1], triangle = [[1], [1, 1]] 
```

At i = 2; 
```
prev = [1, 1], curr = [1, 2, 1], triangle = [[1], [1, 1], [1, 2, 1]]
```

At i = 3;
```
prev = [1, 2, 1], curr = [1, 3, 3, 1], triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
```

At i = 4;

```
prev = [1, 3, 3, 1], curr = [1, 4, 6, 4, 1], triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

So, final output should look like this:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```
