# Title: Recover a Tree From Preorder Traversal
# URL: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# Difficulty: Hard

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.traversal_str = traversal
        self.idx = 0 # Global index to keep track of the current position in the traversal string
        
        # This helper function attempts to build a node at the given depth.
        # It updates self.idx as it consumes parts of the string.
        # If a node cannot be formed at the expected_depth, it returns None
        # and resets self.idx to its state before the current call.
        def dfs(expected_depth: int) -> Optional[TreeNode]:
            original_idx = self.idx 
            
            # If we've reached or gone past the end of the string, no more nodes can be parsed.
            if self.idx >= len(self.traversal_str):
                return None
            
            # 1. Parse dashes
            current_dashes = 0
            # Count leading dashes from the current index.
            while self.idx < len(self.traversal_str) and self.traversal_str[self.idx] == '-':
                current_dashes += 1
                self.idx += 1
            
            # If the number of dashes does not match the expected depth,
            # this segment does not represent a child node at the current expected_depth.
            # We must revert self.idx and signal that no node was found here.
            # This is how the recursion "backs out" when it finds a sibling or an ancestor.
            # The root node (expected_depth=0) must have 0 dashes.
            if current_dashes != expected_depth:
                self.idx = original_idx # Revert index to before attempting to parse this segment
                return None
            
            # 2. Parse value
            val_start_idx = self.idx
            # Read digits to form the node's value.
            while self.idx < len(self.traversal_str) and self.traversal_str[self.idx].isdigit():
                self.idx += 1
            
            # If no digits were found after dashes, it means the traversal string is malformed
            # at this point (e.g., "1--" or "1-"). This segment is invalid.
            if val_start_idx == self.idx:
                self.idx = original_idx # Revert index
                return None # Signal failure to parse a valid node

            # Convert the extracted digits to an integer value.
            node_val = int(self.traversal_str[val_start_idx:self.idx])
            node = TreeNode(node_val)
            
            # 3. Recursively build left child
            # An immediate child will have a depth of expected_depth + 1.
            node.left = dfs(expected_depth + 1)
            
            # 4. Recursively build right child
            # Per problem statement: "If a node has only one child, that child is guaranteed to be the left child."
            # This implies if node.left is None, then node.right must also be None (for a valid traversal).
            # Our recursive structure naturally handles this:
            # If the call for node.left returns None, then the next call for node.right will correctly
            # determine that the subsequent segment is not at expected_depth + 1 (either it's for an ancestor,
            # or it's the end of the string), and thus return None as well.
            node.right = dfs(expected_depth + 1)
            
            return node

        # Start the recovery process from the root, which is always at depth 0.
        return dfs(0)
