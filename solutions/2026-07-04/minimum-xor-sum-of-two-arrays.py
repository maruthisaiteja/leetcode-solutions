# Title: Minimum XOR Sum of Two Arrays
# URL: https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
# Difficulty: Hard

class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)

        # dp[mask] stores the minimum XOR sum when:
        # 1. The elements nums1[0], nums1[1], ..., nums1[k-1] have been paired,
        #    where k is the number of set bits in 'mask'.
        # 2. The elements of nums2 used for these pairings are those indicated by 'mask'.
        # Initialize dp with infinity. dp[0] = 0 because no elements paired yields an XOR sum of 0.
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        # Iterate through all possible masks from 0 to 2^n - 1.
        # Processing masks in increasing numerical order implicitly ensures that
        # when we calculate dp[new_mask], the prerequisite dp[mask] (which has fewer set bits)
        # has already been computed.
        for mask in range(1 << n):
            # If this state is unreachable (e.g., no path leads to this mask), skip it.
            if dp[mask] == float('inf'):
                continue

            # 'k' represents the number of elements from nums1 that have already been paired.
            # This is equivalent to the number of set bits in the current 'mask'.
            # We use `bin(mask).count('1')` to count set bits in Python 3.9.
            k = bin(mask).count('1')

            # If 'k' equals 'n', it means all 'n' elements from nums1 have been paired.
            # In this case, there are no more elements of nums1 to pair, so we continue to the next mask.
            if k == n:
                continue
            
            # We are trying to pair nums1[k] with an unused element from nums2.
            # Iterate through all possible indices 'j' for nums2.
            for j in range(n):
                # Check if the j-th element of nums2 (nums2[j]) is not yet used in the current 'mask'.
                # The expression `(mask & (1 << j))` checks if the j-th bit is set in 'mask'.
                # If it's not set (i.e., `nums2[j]` is unused), we can form a new pair.
                if not (mask & (1 << j)):
                    # Create a new mask by setting the j-th bit, indicating that nums2[j] is now used.
                    new_mask = mask | (1 << j)
                    
                    # Calculate the XOR sum for this new state.
                    # It's the sum from the previous state (dp[mask]) plus the XOR value of the new pair (nums1[k] ^ nums2[j]).
                    current_xor_sum = dp[mask] + (nums1[k] ^ nums2[j])
                    
                    # Update dp[new_mask] if this path yields a smaller XOR sum.
                    dp[new_mask] = min(dp[new_mask], current_xor_sum)

        # The final answer is dp[(1 << n) - 1].
        # This state represents the minimum XOR sum when all 'n' elements of nums1 are paired
        # with all 'n' elements of nums2 (i.e., the mask has all bits set, indicating all nums2 elements are used).
        return dp[(1 << n) - 1]
