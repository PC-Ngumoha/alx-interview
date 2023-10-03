#!/usr/bin/python3
"""
lockboxes (Mock Interview)

My attempt at writing a function which takes a row of
boxes with boxes which may or may not contain keys to
open subsequent boxes and then determine if all the boxes
can be unlocked/opened
"""


def canUnlockAll(boxes):
    """
    canUnlockAll()

    Args:
      - boxes -> list of boxes

    Return:
      - True -> All boxes can be unlocked.
      - False -> Not all boxes can be unlocked.

    Observation:
      - I ended up making use of a Depth First Search Algorithm which
        keeps track of boxes visited and uses that to determine if all boxes
        can be unlocked or not.

    TODO: I'm going to need to learn more about different algorithm formation
    techniques.
    """
    n_boxes = len(boxes)
    visited = set()  # Keeps track of boxes we've visited
    key_stack = [0]

    while key_stack:
        current_box = key_stack.pop()

        if current_box not in visited:
            visited.add(current_box)
            keys = boxes[current_box]

        for key in keys:
            if key >= 0 and key < n_boxes:
                key_stack.append(key)

    return n_boxes == len(visited)
