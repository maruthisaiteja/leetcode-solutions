# Title: Minimum Increase to Maximize Special Indices
# URL: https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/
# Difficulty: Medium

from typing import List

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)

        # Handle edge cases where no special indices are possible.
        # A special index i requires nums[i-1], nums[i], nums[i+1] to exist.
        # This means 1 <= i <= n-2.
        # If n < 3, no such i exists. In this scenario, no operations are needed, so the cost is 0.
        if n < 3:
            return 0

        # Helper function to compare two states (count_of_special_indices, total_cost).
        # It returns the state that is considered 'better' based on the problem's criteria:
        # 1. Prioritize a higher count of special indices.
        # 2. If counts are equal, prioritize a lower total cost.
        def better(s1, s2):
            count1, cost1 = s1
            count2, cost2 = s2
            if count1 > count2:
                return s1
            if count2 > count1:
                return s2
            # If counts are equal, choose the one with the minimum cost.
            if cost1 < cost2:
                return s1
            else:  # If cost2 is less than or equal to cost1, s2 is better or equally good.
                return s2

        # Initialize DP states for the first possible special index (index 1).
        # `cost_1` is the minimum number of operations required to make nums[1] special.
        # For nums[1] to be special, nums[1] must be greater than nums[0] and nums[2].
        # The minimum value nums[1] must take is max(nums[0], nums[2]) + 1.
        cost_1 = max(0, max(nums[0], nums[2]) + 1 - nums[1])

        # `prev_not_special`: Represents the best state (max_special_indices, min_cost)
        #                     if the *previous* index (conceptually index 1 in this initialization context)
        #                     was NOT made special.
        # `prev_special`:     Represents the best state (max_special_indices, min_cost)
        #                     if the *previous* index (index 1) WAS made special.

        # Initial state considering index 1:
        # If index 1 is NOT special: We have 0 special indices so far, and 0 cost for this choice.
        prev_not_special = (0, 0)
        # If index 1 IS special: We have 1 special index (index 1), and `cost_1` operations incurred.
        prev_special = (1, cost_1)

        # Iterate from index 2 up to n-2. These are all the remaining possible special indices.
        # 'i' represents the current index being considered.
        for i in range(2, n - 1):
            # Calculate the cost to make the current index 'i' special.
            # This cost is based on the original values of nums[i-1], nums[i], nums[i+1].
            current_cost_i = max(0, max(nums[i-1], nums[i+1]) + 1 - nums[i])

            # Determine the state if current index 'i' is NOT special.
            # If 'i' is not special, we can take the best outcome from the previous index (i-1),
            # regardless of whether (i-1) was special or not.
            curr_not_special = better(prev_not_special, prev_special)

            # Determine the state if current index 'i' IS special.
            # If 'i' is special, then the immediately preceding index 'i-1' CANNOT be special
            # due to the adjacency rule (no two adjacent special indices).
            # Therefore, we must have come from the state where 'i-1' was NOT special (`prev_not_special`).
            # We increment the special index count by 1 and add `current_cost_i` to the total cost.
            curr_special = (prev_not_special[0] + 1, prev_not_special[1] + current_cost_i)

            # Update the 'prev' states for the next iteration.
            prev_not_special = curr_not_special
            prev_special = curr_special
        
        # After iterating through all possible special indices (from 1 to n-2),
        # the final answer is the better of the two states for the last considered index (n-2):
        # - The state where the last index (n-2) was not special.
        # - The state where the last index (n-2) was special.
        final_result = better(prev_not_special, prev_special)
        
        # The problem asks for the minimum total operations (cost).
        # This is the second element of our `(count, cost)` tuple.
        return final_result[1]
