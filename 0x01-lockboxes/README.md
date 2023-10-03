# Lockboxes (Mock Interview)

Our objective is to create an algorithm that can determine if all boxes in a row of boxes can be unlocked based on the keys found in each box.

**Rough Reasoning:**

Let us  consider the first sample:


Sample 1:

  0    1    2    3    4
[[1], [2], [3], [4], []]

Return: True (All boxes can be unlocked)

Reason/Steps: From observation, I observed that the reason this evaluates to true is because of the fact that each box contains one key which unlocks a box in front of it. Below is my mental breakdown of the flow of this process:

- At box 0, we have key 1. Since there is a box 1, we unlock it using key 1

- At box 1, we have key 2. Since there is a box 2, we unlock it using key 2

- At box 2, we have key 3. Since there is a box 3, we unlock it using key 3

- At box 3, we have a 4. We then unlock box 4

- At box 4, there are no keys to be found. But we are already at the end of our journey since all boxes have been visited. So, we go ahead and return TRUE. All boxes in this sample can indeed be opened/unlocked.


Alright, now let's consider the second sample:


Sample 2:
     0       1       2          3       4      5     6
[[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

Return: True (All boxes can also be unlocked)

Reason / Steps: I think that the reason why this is possible is because each box in the row of boxes contains a key that can open a box in front of it. Another thing I noticed in this sample is that there is a potential for the algorithm to visit a particular box more than once and when it does so, we want it to keep track of where it stopped the last time it was there. My mental breakdown of the steps necessary to do this is as given below:


- At box 0, we get the keys 1, 4, 6. we go to box 1

- At box 1, we get the key 2. we go to box 2

- At box 2, we get the keys 0, 4, 1. we go back to box 0

- At box 0, we have already explored key 1, so we have the keys 4, 6. we go to box 4

- At box 4, we have key 3, we go to box 3

- At box 3, we have keys 5, 6, 2. we go to box 5

- At box 5, we have keys 4, 1. We go back to box 4.

- At box 4, we have no other keys except 3, so we go back to box 3

- At box 3, we have explored key 5, so we go to box 6.

- At box 6, we have key 6. So, we stop there. And because we have explored all boxes 0 - 6, we return TRUE


Now let's consider the third

Sample 3:

   0      1       2       3    4     5      6
[[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

Return: False (Not all boxes can be unlocked)

Reason:

- At box 0, we have keys 1, 4. we go to box 1.
- At box 1, we have key 2. we go to box 2.
- At box 2, we have key 0, 4, 1, we go back to box 0.
- At box 0, we go to box 4.
- At box 4, we have no other keys to more boxes to explore, so we return FALSE.





Here's an idea, 


     0       1       2          3       4      5     6
[[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

Step 1,
visited = {}, stack = [0]

is box 0 in visited? NO
	visited.add(0) -> {0}
	keys = boxes[box 0]

	for key in keys:
		if key is valid box number:
			stack.add(key) -> [1, 4, 6]
Step 2:

visited = {0}, stack = [1, 4, 6]

while stack:

	box = stack.pop() #1

	is box in visited? NO
		visited.add(1) -> {0, 1}
		keys = boxes[box]

		for key in keys:
			if key is valid box number:
				stack.add(key) -> [4, 6, 2]
Step 3:

visited = {0, 1}, stack = [4, 6, 2]

while stack:

	box = stack.pop() #4

	is box in visited? NO
		visited.add(4) -> {0, 1, 4}
		keys = boxes[box]

		for key in keys:
			if key is valid box number:
				stack.add(key) -> [6, 2, 3]

Step 4:
visited = {0, 1, 4}, stack = [6, 2, 3]

while stack:

	box = stack.pop() #6

	is box in visited? NO
		visited.add(6) -> {0, 1, 4, 6}
		keys = boxes[box]

		for key in keys:
			if key is valid box number:
				stack.add(key) -> [2, 3, 6]

Step 5:
visited = {0, 1, 4, 6}, stack = [2, 3, 6]

while stack:

	box = stack.pop() #2

	is box in visited? NO
		visited.add(2) -> {0, 1, 4, 6, 2}
		keys = boxes[box] -> [0, 4, 1]

		for key in keys:
			if key is valid box number:
				stack.add(key) -> [3, 6, 0, 4, 1]


Step 6:
visited = {0, 1, 4, 6, 2}, stack = [3, 6, 0, 4, 1]

while stack:

	box = stack.pop() #3

	is box in visited? NO
		visited.add(3) -> {0, 1, 4, 6, 2, 3}
		keys = boxes[box] -> [5, 6, 2]

		for key in keys:
			if key is valid box number:
				stack.add(key) -> [6, 0, 4, 1, 5, 6, 2]

Step 7:
visited = {0, 1, 4, 6, 2, 3}, stack = [6, 0, 4, 1, 5, 6, 2]

while stack:

	box = stack.pop() #6

	is box in visited? YES
	

Step 8:

visited = {0, 1, 4, 6, 2, 3}, stack = [0, 4, 1, 5, 6, 2]

while stack:

	box = stack.pop() #0

	is box in visited? YES

Step 9:
visited = {0, 1, 4, 6, 2, 3}, stack = [4, 1, 5, 6, 2]

while stack:

	box = stack.pop() #4

	is box in visited? YES

Step 10:

visited = {0, 1, 4, 6, 2, 3}, stack = [1, 5, 6, 2]

while stack:

	box = stack.pop() #1

	is box in visited? YES

Step 11:

visited = {0, 1, 4, 6, 2, 3}, stack = [5, 6, 2]

while stack:

	box = stack.pop() #5

	is box in visited? NO
		visited.add(5) -> {0, 1, 4, 6, 2, 3, 5}
		keys = boxes[box] -> [4, 1]

		for key in keys:
			if key is valid box number:
				stack.add(key) -> [6, 2, 4, 1]

Step 12:
visited = {0, 1, 4, 6, 2, 3, 5}, stack = [2, 4, 1]

while stack:

	box = stack.pop() #6 2 4 1

	is box in visited? YES

if len(visited) == len(boxes), RETURN TRUE ELSE RETURN FALSE
IT RETURNS TRUE

Considering sample 3:

   0      1       2       3    4     5      6
[[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

ROUGH WALKTHROUGH: I tried to write this in a concise manner due to space and time constraints. I hope you can still follow along.

visited = {0, 1, 4, 2} stack = []

while stack:

	box = stack.pop() #0, #1, #4, #2, #0, #4, #1 

	is box in visited?
		NO:
		visited.add(box: 2) -> {0, 1, 4, 2}
		keys = boxes[box] -> [0, 4, 1]

		for key in keys:
			if key >= 0 and key < len(boxes):
				stack.add(key) -> [4, 1]

		YES:
			DO NOTHING
		

if len(visited) === len(boxes) RETURN TRUE ELSE RETURN FALSE
IT RETURNS FALSE.

Considering the above, I got some insight into the way to solve this problem.

**Final Algorithm:**
```
function canUnlockAll(boxes):
	let n_boxes = boxes.length;
	let visited = SET {}
	let stack = [0]; // first box is already unlocked

	while stack:
		let current_box = stack.pop()

		if current_box not in visited:
			visited.add(current_box)
			let keys = boxes[current_box]

			for key	in keys:
				if key >= 0 && key < n_boxes:
					stack.add(key)
	COMPARE visited.length === n_boxes:
		IF EQUAL:
			RETURN True
		ELSE:
			RETURN False
```


**Plain Explanation:**

- After hours of research and some ChatGPT 😏, I discovered that this problem is most efficiently solved through the use of a Depth First Search or DFS Algorithm which is what the above is.

- The way it works is that, the algorithm keeps track of two things :
	- A set of boxes which we have visited
	- A stack of keys which we have obtained from all boxes visited up to this point.
- Initially the only key we have in the stack in the key to the zeroth box which is already unlocked. So, with that, we check if the zeroth box has been visited before. Since we're just starting out, the zeroth box has not yet been visited, so we take not of that by adding the box's index to the set of visited boxes and then we proceed to fetch all the valid keys in that box adding them to the stack.

- We repeat this process on other boxes whose keys we've been able to add to the stack, appending their contained keys as well to the stack the first time we unlock them and continue going through the stack until it runs out of stored keys either because we've visited all boxes and obtained all their constituent keys or because we were unable to visit all boxes but have exhausted the keys in the stack (Mainly because of a discontinuity in the keys we could access).

- Then we compare the number of boxes we were able to visit to the number of boxes we have in total. If they are equal in number, it means we successfully unlocked and visited all the available, so our algorithm returns **True** to indicate that this is the case. Otherwise, if they are not equal in number meaning we couldn't unlock and visit all, our algorithm indicates by returning **False**.

- And then, the program comes to an end.
