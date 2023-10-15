# Minimum Operations (Mock Interview Question)

#### Minimum Operations (Thought process)

**Overview:** In this problem, we are given a character `H` in a file and a number `n` and we are asked to create function that calculates the minimum number of operations `num_ops` required to get `n` number of `H` characters in the file. NOTE: We can only perform these two operations in the file: `Copy All` and `Paste`

**Assumptions:** 
For the number of operations to be considered minimum;
- `num_ops` <= `n`
- There must be exactly `n` values of `H` in the file i.e len(`H`) == n

Just going over some of the walkthroughs:

Given: n = 9, the algorithm should give us `6` as the output:

```
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
``` 
Counting only the occurrences of `Copy All` and `Paste`, we can see that we have `6` operations which is less than `9` (value of n)


As another example, let's say we're given n = 4, the algorithm spits back `4`:

```
H => Copy All => Paste => HH => Copy All => Paste => HHHH
```


Final example, let's say we were given n = 12, the algorithm spits back `7`:

```
H => Copy All => Paste => HH => Copy All => Paste => HHHH => Copy All => Paste => HHHHHHHH => Paste => HHHHHHHHHHHH
```



After thinking about this for a while and how it works, I came with this algorithm which I hope can solve all cases of this problem:

**Pseudocode**

```
function minOps(n) -> {
	let numOps = 0;
	let copyBuffer = '';
	let textBuffer = 'H';


	LOOP FOREVER {
		
		if length(textBuffer) == n {
			RETURN numOps;
		}

		if length(textBuffer) > n OR numOps > n {
			RETURN 0;
		}

		// Copy All Operation
		if MODULUS(n, length(textBuffer)) == 0 {
			copyBuffer = textBuffer;
			numOps += 1;
		}

		// Paste Operation
		CONCATENATE(textBuffer, copyBuffer);
		numOps += 1;
		
	}

}
```

