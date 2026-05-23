# Title: Number of Ways to Stay in the Same Place After Some Steps
# URL: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
# Difficulty: Hard

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        # The maximum position we need to consider is bounded by arrLen and steps.
        # If we are at index `j` after `k` steps, we need at least `j` steps
        # to return to index 0. So, `k + j` must be less than or equal to `steps`.
        # This implies `j <= steps - k`.
        # Also, the maximum index we can reach in `k` steps is `k`.
        # So, at any step `k`, the position `j` is bounded by `min(k, steps - k)`.
        # The maximum value of `min(k, steps - k)` across all `k` (from 0 to steps)
        # occurs when `k` is approximately `steps / 2`. This maximum value is `steps // 2`.
        # Therefore, we only need to track positions from `0` up to `steps // 2`.
        # We also cannot exceed `arrLen - 1`.
        # So, the maximum relevant index is `min(arrLen - 1, steps // 2)`.
        
        max_pos = min(arrLen - 1, steps // 2)

        # The size of our DP array will be `max_pos + 1` (to include index 0).
        dp_size = max_pos + 1 
        
        # dp[j] will store the number of ways to be at index j after the current step.
        # Initialize dp array for the start state (0 steps): 1 way to be at index 0.
        dp = [0] * dp_size
        dp[0] = 1

        # Iterate for each step from 1 to `steps`
        for _ in range(steps):
            new_dp = [0] * dp_size
            # Calculate ways for each position j in the current step
            for j in range(dp_size):
                # Number of ways to reach `j` in the current step
                # is the sum of ways to reach `j`, `j-1`, or `j+1` in the previous step.
                
                # Option 1: Stay at current position j (from dp[j] in previous step)
                val = dp[j]

                # Option 2: Move right to j from j-1 (from dp[j-1] in previous step)
                # This is only possible if j > 0 (i.e., we can come from a left position)
                if j > 0:
                    val = (val + dp[j-1]) % MOD
                
                # Option 3: Move left to j from j+1 (from dp[j+1] in previous step)
                # This is only possible if j+1 is within our tracked `dp_size` range.
                if j < dp_size - 1:
                    val = (val + dp[j+1]) % MOD
                
                new_dp[j] = val
            dp = new_dp
        
        # After `steps` iterations, dp[0] will contain the number of ways
        # to be at index 0.
        return dp[0]
