# Title: Count Partitions With Max-Min Difference at Most K
# URL: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/
# Difficulty: Medium

import collections

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # dp[i] will store the number of ways to partition nums[0...i-1]
        # dp[0] = 1 represents one way to partition an empty prefix (by doing nothing)
        dp = [0] * (n + 1)
        dp[0] = 1

        # S_dp[x] stores the sum of dp[0] + ... + dp[x]
        # S_dp[0] = dp[0] = 1
        S_dp = [0] * (n + 1)
        S_dp[0] = 1

        left = 0  # Left pointer for the sliding window [left, i] (inclusive)
        min_dq = collections.deque()  # Stores indices, values are non-decreasing
        max_dq = collections.deque()  # Stores indices, values are non-increasing

        for i in range(n):
            # 1. Add current element nums[i] (index i) to deques
            # Maintain monotonicity: remove elements from the back that are "worse" than nums[i]
            while min_dq and nums[min_dq[-1]] >= nums[i]:
                min_dq.pop()
            min_dq.append(i)

            while max_dq and nums[max_dq[-1]] <= nums[i]:
                max_dq.pop()
            max_dq.append(i)

            # 2. Shrink window from the left if max-min difference exceeds k
            # 'left' is the earliest possible start index for the last segment ending at 'i'.
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                # The element at 'left' is causing the condition violation.
                # Remove it from the front of the deques if it's the current min/max.
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1  # Move the left pointer to shrink the window

            # At this point, the window nums[left...i] is the largest valid segment ending at i.
            # Any segment nums[j...i] where j >= left will also be valid.
            # dp[i+1] is the number of ways to partition nums[0...i].
            # This is the sum of dp[j] for all valid j in [left, i].
            # Using the prefix sum array S_dp:
            # sum(dp[x] for x in range(left, i+1)) = S_dp[i] - S_dp[left-1] (if left > 0)
            # If left == 0, it's just S_dp[i].
            
            dp[i+1] = (S_dp[i] - (S_dp[left - 1] if left > 0 else 0) + MOD) % MOD
            
            # Update the prefix sum array for dp values
            S_dp[i+1] = (S_dp[i] + dp[i+1]) % MOD

        return dp[n]
