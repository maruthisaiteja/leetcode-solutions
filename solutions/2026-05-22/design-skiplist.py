# Title: Design Skiplist
# URL: https://leetcode.com/problems/design-skiplist/
# Difficulty: Hard

import random

class SkiplistNode:
    """
    Represents a node in the Skiplist.
    Each node has a value and a list of 'next' pointers, one for each level
    it participates in. The size of `next` array is `level + 1`.
    """
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * (level + 1)

class Skiplist:
    """
    Implements a Skiplist data structure.
    Operations: search, add, erase, all with O(log n) average time complexity.
    """
    
    # Maximum number of levels for a node.
    # log2(2*10^4) approx 14.28. 16 is a common choice for such constraints.
    MAX_LEVEL = 16 
    
    # Probability of a node being promoted to the next level. Standard is 0.5.
    PROBABILITY = 0.5

    def __init__(self):
        """
        Initializes the Skiplist object.
        A sentinel 'head' node is created with a value of -1 (conceptual -infinity)
        and it participates in all possible MAX_LEVELs.
        'level' tracks the current highest active level in the skiplist.
        """
        self.level = 0
        # The head node's next array is sized to MAX_LEVEL + 1 to accommodate all potential levels.
        self.head = SkiplistNode(-1, self.MAX_LEVEL) 

    def _random_level(self) -> int:
        """
        Generates a random level for a new node.
        The level starts at 0 and increments with PROBABILITY until MAX_LEVEL is reached
        or the probability check fails.
        """
        lvl = 0
        while random.random() < self.PROBABILITY and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def _find_predecessors(self, target: int) -> list[SkiplistNode]:
        """
        Finds the predecessors for a given target value at each relevant level.
        A predecessor 'p' at level 'i' is the node such that p.val < target
        and p.next[i] is None or p.next[i].val >= target.
        The result 'update' array stores these predecessor nodes.
        """
        # 'update' stores the last node less than 'target' encountered at each level.
        # It needs to be MAX_LEVEL + 1 in size to potentially store predecessors
        # up to MAX_LEVEL, even if self.level is currently lower.
        update = [None] * (self.MAX_LEVEL + 1) 
        curr = self.head

        # Start from the highest active level (self.level) and move downwards to level 0.
        for i in range(self.level, -1, -1):
            # Traverse forward in the current level as long as the next node exists
            # and its value is less than the target.
            while curr.next[i] is not None and curr.next[i].val < target:
                curr = curr.next[i]
            # Store the current node as the predecessor for level i.
            # At this point, curr.next[i] is either None or has a value >= target.
            update[i] = curr 
        return update

    def search(self, target: int) -> bool:
        """
        Searches for the target integer in the Skiplist.
        Returns True if found, False otherwise.
        """
        # Find the predecessors using the helper method.
        # The node immediately after update[0] should be the target
        # if it exists at level 0.
        update = self._find_predecessors(target)
        node = update[0].next[0] # Get the node at level 0 right after its predecessor
        return node is not None and node.val == target

    def add(self, num: int) -> None:
        """
        Inserts the given integer 'num' into the Skiplist.
        """
        # Find predecessors for 'num' at all levels currently active in the skiplist.
        update = self._find_predecessors(num)

        # Determine a random level for the new node.
        new_level = self._random_level()

        # If the new node's level is higher than the current highest active level
        # of the skiplist, update the skiplist's level. For the newly activated
        # levels, the 'head' node becomes the predecessor.
        if new_level > self.level:
            # For levels from (current self.level + 1) up to new_level,
            # the head node is the predecessor because these levels are currently empty.
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head 
            self.level = new_level # Update the skiplist's highest active level

        # Create the new node with the determined value and level.
        new_node = SkiplistNode(num, new_level)

        # Link the new node into the skiplist at all levels it participates in (from 0 up to new_level).
        for i in range(new_level + 1):
            new_node.next[i] = update[i].next[i] # New node points to the node that was after its predecessor
            update[i].next[i] = new_node         # Predecessor now points to the new node

    def erase(self, num: int) -> bool:
        """
        Removes one occurrence of the given integer 'num' from the Skiplist.
        Returns True if 'num' was found and removed, False otherwise.
        If multiple 'num' values exist, any one of them is removed (specifically, the first one found).
        """
        # Find predecessors for 'num' at all levels.
        update = self._find_predecessors(num)

        # Check if the node to be deleted actually exists at level 0.
        # 'node_to_delete' will be the first occurrence of 'num' if duplicates exist.
        node_to_delete = update[0].next[0]
        if node_to_delete is None or node_to_delete.val != num:
            return False # Num not found in the skiplist

        # Unlink the 'node_to_delete' from all levels it participates in.
        for i in range(self.level + 1):
            # If update[i].next[i] points to the specific node_to_delete object,
            # it means node_to_delete was promoted to level 'i' and should be unlinked.
            if update[i].next[i] is node_to_delete:
                update[i].next[i] = node_to_delete.next[i] # Bypass the node_to_delete

        # After deletion, check if the highest levels of the skiplist have become empty.
        # If so, decrement self.level until an occupied level is found or level 0 is reached.
        while self.level > 0 and self.head.next[self.level] is None:
            self.level -= 1

        return True
