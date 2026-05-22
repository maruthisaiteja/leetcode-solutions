# Title: Triples with Bitwise AND Equal To Zero
# URL: https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/
# Difficulty: Hard

class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        MAX_VAL = 1 << 16  # Represents 2^16, the upper bound for numbers in nums.

        # Step 1: Compute frequencies of AND results for pairs (nums[i], nums[j])
        # counts[val] will store the number of pairs (i, j) such that nums[i] & nums[j] == val.
        # The maximum possible value for nums[i] & nums[j] is less than 2^16,
        # so an array of size MAX_VAL is sufficient.
        counts = [0] * MAX_VAL
        n = len(nums)

        for i in range(n):
            for j in range(n):
                and_result = nums[i] & nums[j]
                counts[and_result] += 1
        
        # Step 2: Iterate through each nums[k] and find compatible pairs (i, j)
        # We need (nums[i] & nums[j]) & nums[k] == 0.
        # Let x = nums[i] & nums[j]. We need x & nums[k] == 0.
        total_triples = 0
        for k in range(n):
            target_val_k = nums[k]
            
            # Iterate through all possible values 'x' that could be an AND result of two numbers.
            # Only consider 'x' values that actually appeared (i.e., counts[x] > 0).
            for x in range(MAX_VAL):
                if counts[x] > 0:
                    if (x & target_val_k) == 0:
                        # If (x & target_val_k) == 0, then any pair (i, j) that produced 'x'
                        # can form a valid triple with the current nums[k].
                        # Add the number of such pairs (counts[x]) to the total.
                        total_triples += counts[x]
                        
        return total_triples
