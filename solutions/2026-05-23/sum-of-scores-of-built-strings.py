# Title: Sum of Scores of Built Strings
# URL: https://leetcode.com/problems/sum-of-scores-of-built-strings/
# Difficulty: Hard

class Solution:
    def sumScores(self, s):
        n = len(s)
        if n == 0:
            return 0

        # Z-array stores Z[i] = length of the longest common prefix between s and s[i:]
        # Z[0] is typically defined as n, as s[0:] (the whole string) has an LCP of n with s.
        Z = [0] * n
        Z[0] = n  

        l, r = 0, 0  # [l, r] is the current Z-box, meaning s[l...r] is a prefix of s.
                     # l is the starting index of the Z-box, r is its ending index.

        total_score = n  # Initialize total_score with Z[0] (score for s_n)

        # Iterate from k=1 to n-1 to compute Z[k]
        for k in range(1, n):
            if k <= r:
                # If k is within an existing Z-box [l, r], we can use information from Z[k-l]
                # Z[k-l] tells us the LCP of s[k-l:] with s.
                # The length of the overlap with the current Z-box is r - k + 1.
                # Z[k] cannot be greater than this overlap, nor greater than Z[k-l].
                Z[k] = min(r - k + 1, Z[k - l])
            
            # Extend Z[k] by brute-force character comparison
            # This loop tries to match characters as long as they are equal and within bounds.
            while k + Z[k] < n and s[Z[k]] == s[k + Z[k]]:
                Z[k] += 1
            
            # If the current Z-box extends further to the right than the previous one,
            # update l and r to this new Z-box.
            if k + Z[k] - 1 > r:
                l = k
                r = k + Z[k] - 1
            
            # Add the current Z-value (score for s_{n-k}) to the total sum.
            total_score += Z[k]
        
        return total_score
