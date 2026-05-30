# Title: Vertical Order Traversal of a Binary Tree
# URL: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Difficulty: Hard

import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Store nodes grouped by column. Each entry will be a list of (row, value) tuples.
        # Example: { col_idx: [(row1, val1), (row2, val2), ...], ... }
        columns = collections.defaultdict(list)

        # Queue for BFS: stores (node, row, col)
        # Start with the root at (0, 0)
        queue = collections.deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            # Append the (row, value) for the current node to its corresponding column list
            columns[col].append((row, node.val))

            # Enqueue left child with updated coordinates
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            # Enqueue right child with updated coordinates
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        # Prepare the final result
        result = []
        
        # Get all unique column indices and sort them to process columns from left to right
        sorted_column_keys = sorted(columns.keys())

        for col_key in sorted_column_keys:
            # Get all (row, value) pairs for the current column
            nodes_in_col = columns[col_key]
            
            # Sort these nodes based on the problem's criteria:
            # 1. By row (top-to-bottom)
            # 2. If rows are the same, by value (ascending)
            # Python's default tuple sort handles this automatically:
            # (row1, val1) < (row2, val2) if row1 < row2 or (row1 == row2 and val1 < val2)
            nodes_in_col.sort()
            
            # Extract just the values from the sorted list for the current column
            current_column_values = [val for row, val in nodes_in_col]
            result.append(current_column_values)

        return result
