# Title: Smallest Stable Index II
# URL: https://leetcode.com/problems/smallest-stable-index-ii/
# Difficulty: Medium

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Calculate max_prefix array: max(nums[0..i]) for each i
        # max_prefix[i] stores the maximum value from nums[0] up to nums[i]
        max_prefix = [0] * n
        current_max = float('-inf')
        for i in range(n):
            current_max = max(current_max, nums[i])
            max_prefix[i] = current_max
        
        # Calculate min_suffix array: min(nums[i..n-1]) for each i
        # min_suffix[i] stores the minimum value from nums[i] up to nums[n-1]
        min_suffix = [0] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            min_suffix[i] = current_min
            
        # Iterate through each index to check for stability
        # The first index found that satisfies the condition is the smallest stable index
        for i in range(n):
            instability_score = max_prefix[i] - min_suffix[i]
            if instability_score <= k:
                return i
        
        # If no stable index is found after checking all indices, return -1
        return -1
