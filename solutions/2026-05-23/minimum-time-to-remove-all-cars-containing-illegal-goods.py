# Title: Minimum Time to Remove All Cars Containing Illegal Goods
# URL: https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
# Difficulty: Hard

class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)

        # left[i] stores the minimum cost to remove all '1's in s[0...i]
        # considering only operations 1 (remove from left) and 3 (remove anywhere).
        left = [0] * n
        current_left_cost = 0  # Represents the cost for an empty prefix (left_cost[-1])
        for i in range(n):
            if s[i] == '1':
                current_left_cost += 2
            # Option 1: Remove s[i] (if '1') using operation 3, adding 2 to previous optimal cost.
            # Option 2: Remove the entire prefix s[0...i] by repeatedly removing from the left end.
            # This costs i+1 units of time, regardless of content.
            current_left_cost = min(current_left_cost, i + 1)
            left[i] = current_left_cost

        # right[i] stores the minimum cost to remove all '1's in s[i...n-1]
        # considering only operations 2 (remove from right) and 3 (remove anywhere).
        right = [0] * n
        current_right_cost = 0  # Represents the cost for an empty suffix (right_cost[n])
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                current_right_cost += 2
            # Option 1: Remove s[i] (if '1') using operation 3, adding 2 to subsequent optimal cost.
            # Option 2: Remove the entire suffix s[i...n-1] by repeatedly removing from the right end.
            # This costs n-i units of time, regardless of content.
            current_right_cost = min(current_right_cost, n - i)
            right[i] = current_right_cost

        # Initialize minimum total cost.
        # Since n >= 1, right[0] is always valid.
        # This covers the case where the entire string is cleared from the right (left part is empty).
        min_total_cost = right[0]

        # Consider the case where the entire string is cleared from the left (right part is empty).
        min_total_cost = min(min_total_cost, left[n - 1])

        # Iterate through all possible split points 'i'.
        # A split point 'i' means we clear s[0...i] using left-sided logic (cost left[i])
        # and s[i+1...n-1] using right-sided logic (cost right[i+1]).
        # The loop runs for i from 0 to n-2, covering all internal splits.
        for i in range(n - 1):
            min_total_cost = min(min_total_cost, left[i] + right[i + 1])

        return min_total_cost
