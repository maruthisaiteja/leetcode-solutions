# Title: Maximum Number of Jumps to Reach the Last Index
# URL: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
# Difficulty: Medium

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # dp[i] stores the maximum number of jumps to reach index i from index 0.
        # Initialize with -1 to indicate that an index is unreachable.
        dp = [-1] * n
        
        # Base case: To reach index 0, 0 jumps are needed.
        dp[0] = 0
        
        # Iterate through each index j from 1 to n-1 (the potential destination)
        for j in range(1, n):
            # Iterate through all possible previous indices i (from 0 to j-1)
            # This is the potential source index for a jump to j.
            for i in range(j):
                # Check if index i is reachable (dp[i] is not -1)
                # and if a jump from i to j is valid according to the target condition.
                # The condition is -target <= nums[j] - nums[i] <= target,
                # which is equivalent to abs(nums[j] - nums[i]) <= target.
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target:
                    # If a valid path is found, update dp[j].
                    # We want the maximum number of jumps, so we take the maximum
                    # between the current value of dp[j] and (jumps to i) + 1.
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # The result is the maximum number of jumps to reach the last index (n-1).
        return dp[n-1]
