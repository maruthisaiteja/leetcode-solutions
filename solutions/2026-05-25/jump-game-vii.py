# Title: Jump Game VII
# URL: https://leetcode.com/problems/jump-game-vii/
# Difficulty: Medium

import collections
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        
        # dp[i] will be true if index i is reachable, false otherwise.
        # We start at index 0, so dp[0] is true.
        dp = [False] * n
        dp[0] = True
        
        # A deque to store indices k such that dp[k] is true.
        # This deque helps maintain the sliding window of reachable indices.
        # It stores the reachable indices in increasing order.
        q = collections.deque([0])
        
        # `j` iterates through all possible target indices from 1 to n-1.
        for j in range(1, n):
            # 1. Maintain the sliding window: Remove indices from the left of the deque
            # that are too far to the left to be a valid source for a jump to `j`.
            # An index `k` is too far if `k < j - maxJump`.
            # This means `k + maxJump < j`.
            while q and q[0] < j - maxJump:
                q.popleft()
            
            # 2. Check if the current index `j` can be reached.
            # Conditions for `j` to be reachable:
            #   a. `s[j]` must be '0'.
            #   b. There must be at least one reachable index `k` in the deque (`q` is not empty).
            #   c. The leftmost reachable index `q[0]` (which is the smallest `k` in the current valid window)
            #      must be within `minJump` distance, i.e., `q[0] <= j - minJump`.
            #      This ensures `j >= q[0] + minJump`.
            if q and q[0] <= j - minJump and s[j] == '0':
                dp[j] = True
                q.append(j) # Add the newly reachable index `j` to the deque
            
            # Optimization: If the target index `n-1` is reached, we can return early.
            # This check is valid as `dp[n-1]` can only become True when `j` is `n-1`.
            if dp[n - 1]:
                return True
                
        # After checking all indices up to `n-1`, return whether `n-1` was reachable.
        return dp[n - 1]
