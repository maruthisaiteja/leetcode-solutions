# Title: Maximum XOR for Each Query
# URL: https://leetcode.com/problems/maximum-xor-for-each-query/
# Difficulty: Medium

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        result = []
        
        # Calculate the maximum possible value (mask) for k.
        # This value has 'maximumBit' ones (e.g., if maximumBit=3, mask is 111_2 = 7).
        # Any k must be less than 2^maximumBit, so the maximum value k can take is (2^maximumBit - 1).
        target_max_xor_val = (1 << maximumBit) - 1
        
        # Calculate the initial XOR sum of all elements in the original nums array.
        current_xor_sum = 0
        for num in nums:
            current_xor_sum ^= num
            
        # Perform n queries. Each query involves finding k for the current array
        # and then removing the last element.
        # We iterate from the end of the original nums array backwards.
        # In each iteration 'i', nums[i] is considered the last element of the
        # current array that will be "removed" for the next query.
        for i in range(n - 1, -1, -1):
            # For the current array (whose XOR sum is current_xor_sum),
            # we want to find k such that (current_xor_sum XOR k) is maximized.
            # To maximize this XOR result, each bit of k should be the opposite
            # of the corresponding bit in current_xor_sum, up to maximumBit-1.
            # This is achieved by XORing current_xor_sum with target_max_xor_val.
            k = current_xor_sum ^ target_max_xor_val
            result.append(k)
            
            # After the k for the current query is determined and stored,
            # simulate the removal of the last element from the array.
            # The last element to be removed (in the context of processing queries
            # from full array to single-element array) is nums[i] from the original array.
            # To remove nums[i]'s effect from current_xor_sum, we XOR it again:
            # (A ^ B) ^ B = A
            current_xor_sum ^= nums[i]
            
        return result
