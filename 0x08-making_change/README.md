# Making Change (Mock Interview)

## My Thought Process
So, let's say we're given a total amount of _37 kobo_ and we're asked to make change with an infinite number of coins of the _1 kobo_, _2 kobo_ and _25 kobo_ denominations respectively. In order to get the minimum number of coins required to make change that is equal to the specified total amount, the following algorithm step can be used:

**Algorithm:**

1. Get the largest denomination among the denomination of coins available
2. Can we take the selected denomination out of the total? Take it out of total. Else? Skip to step 5 below.
3. Increment count of coins
4. Has total been reduced to zero? Skip to step 6 below. Else? proceed to next step.
5. Do we have more coin denominations? Get the next largest coin denomination and repeat step 2 above. Else? Return -1 to indicate that we cannot make change
6. Return count of coins needed to match total amount.

So, with this algorithm in mind, let's create a pseudocode that'll give an idea of how to go about creating the code that will actually do this:

**Pseudocode:**

```
func makeChange(coins, total):
  count = 0
  denominations = SORT_REVERSE(coins)

  WHILE denominations is not [], do:
    current_denomination = denominations[0]
    if total is greater than or equal to current_denomination, then:
      count += WHOLE_NUMBER_DIVIDE(total, current_denomination)
      total = MODULUS(total, current_denomination)
    if total is equal to 0, then:
      Break out of loop at this point
    POP_FIRST_ELEMENT(denominations)

  if denominations is [], then:
    count = -1
  Return count
```

[2, 10, 20] -> 1
[]
-1