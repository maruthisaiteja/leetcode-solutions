# Title: Minimum Number of Operations to Satisfy Conditions
# URL: https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/
# Difficulty: Medium

import collections
import math
from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # costs[j][val] stores the minimum operations to make all cells in column j equal to 'val'.
        costs = [[0] * 10 for _ in range(n)]

        for j in range(n):
            counts = collections.Counter(grid[i][j] for i in range(m))
            for val in range(10): # Possible values are 0-9
                costs[j][val] = m - counts[val] # Operations = total rows - occurrences of 'val'

        # dp_prev[val] stores the minimum operations to satisfy conditions up to the previous column,
        # with the previous column having all elements equal to 'val'.
        dp_prev = [0] * 10

        # Base case: For the first column (j=0)
        for val in range(10):
            dp_prev[val] = costs[0][val]

        # Iterate through columns from the second column (j=1) to the last
        for j in range(1, n):
            # dp_curr[val] will store the minimum operations up to the current column j,
            # with column j having all elements equal to 'val'.
            dp_curr = [0] * 10

            # Find the two minimum values in dp_prev and their corresponding indices.
            # This is done to efficiently handle the condition where adjacent columns must have different values.
            min1_val = math.inf # Smallest total cost for previous column
            min1_idx = -1      # Value used in previous column for min1_val
            min2_val = math.inf # Second smallest total cost for previous column
            min2_idx = -1      # Value used in previous column for min2_val

            for val_prev in range(10):
                if dp_prev[val_prev] < min1_val:
                    min2_val = min1_val
                    min2_idx = min1_idx
                    min1_val = dp_prev[val_prev]
                    min1_idx = val_prev
                elif dp_prev[val_prev] < min2_val:
                    min2_val = dp_prev[val_prev]
                    min2_idx = val_prev
            
            # Calculate dp_curr for each possible value for the current column
            for val_curr in range(10):
                # If the current column's value (val_curr) is the same as the value that yielded
                # the overall minimum for the previous column (min1_idx),
                # we must use the second minimum from dp_prev (min2_val) to satisfy the condition
                # that adjacent columns must have different values.
                if val_curr == min1_idx:
                    dp_curr[val_curr] = costs[j][val_curr] + min2_val
                # Otherwise, we can use the overall minimum from dp_prev (min1_val).
                else:
                    dp_curr[val_curr] = costs[j][val_curr] + min1_val
            
            # Update dp_prev for the next iteration
            dp_prev = dp_curr

        # The minimum operations for the entire grid will be the minimum value in the final dp_prev array.
        return min(dp_prev)
