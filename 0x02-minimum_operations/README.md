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



After thinking about this for a while and how it works and trial and error, I came up with this algorithm which utilizes the concept of dynamic programming to solve all cases of this problem.
I hope can solve all cases of this problem:

**Pseudocode**
```
function minOperations(n) -> {

  min_ops = [0] * (n + 1) // Creating n + 1 slots

  FOR i in RANGE(2, n + 1) {
    // set this stage to the worst case scenario number of operations possible
    min_ops[i] = i;

    // Check to see if there can be a better case scenario
    FOR j in RANGE(2, i // 2 + 1) {
      if i % j == 0 {
        min_ops[i] = MINIMUM(min_ops[i], min_ops[j] + i // j)
      }
    }
  }
  return min_ops[n];
}
```
