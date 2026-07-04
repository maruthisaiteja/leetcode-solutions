# Title: Range Sum of BST
# URL: https://leetcode.com/problems/range-sum-of-bst/
# Difficulty: Easy

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0
        stack = []

        if root:
            stack.append(root)

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                range_sum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            elif node.val < low:
                # Node value is too small. All values in the left subtree
                # would also be smaller than 'low'. So, only explore the
                # right subtree, which might contain values within the range.
                if node.right:
                    stack.append(node.right)
            else: # node.val > high
                # Node value is too large. All values in the right subtree
                # would also be larger than 'high'. So, only explore the
                # left subtree, which might contain values within the range.
                if node.left:
                    stack.append(node.left)
        
        return range_sum
