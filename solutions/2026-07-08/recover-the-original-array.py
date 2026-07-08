# Title: Recover the Original Array
# URL: https://leetcode.com/problems/recover-the-original-array/
# Difficulty: Hard

import collections
from typing import List

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        nums.sort()

        # Helper function to check if a given k_val is valid
        # and construct the original array arr
        def check_k(k_val: int) -> List[int] | None:
            # k must be a positive integer as per problem description
            if k_val <= 0:
                return None
            
            # Use a frequency counter to track available numbers in nums
            # This allows efficient lookups and updates for duplicate numbers
            temp_counts = collections.Counter(nums)
            
            current_arr = []
            
            # Iterate through the sorted nums array.
            # The smallest available number must always be a 'lower' value.
            for num_val in nums:
                if temp_counts[num_val] == 0:
                    # This number has already been paired as either a lower or higher value
                    continue
                
                # Assume num_val is a 'lower' value (arr_i - k_val)
                # The corresponding 'higher' value would be (arr_i + k_val)
                # which can also be expressed as (num_val + k_val + k_val) = num_val + 2 * k_val
                corresponding_higher_val = num_val + 2 * k_val
                
                # Check if the corresponding 'higher' value exists and is available in temp_counts
                if temp_counts[corresponding_higher_val] > 0:
                    # If found, this is a valid pair for the current k_val.
                    # Calculate arr_i = lower_val + k_val
                    current_arr.append(num_val + k_val)
                    
                    # Decrement counts for both the lower and higher values used
                    temp_counts[num_val] -= 1
                    temp_counts[corresponding_higher_val] -= 1
                else:
                    # If a corresponding higher_val is not found or not available,
                    # this k_val is not valid for forming all pairs.
                    return None
            
            # If we successfully iterated through all numbers in nums and formed 'n' pairs,
            # current_arr should contain exactly 'n' elements.
            if len(current_arr) == n:
                return current_arr
            else:
                # This case implies an internal logic error if previous checks were strict,
                # but serves as a safeguard.
                return None
        
        # The smallest element in the sorted combined array, nums[0],
        # must correspond to some arr_x - k.
        # Its partner, arr_x + k, must also be present in `nums`.
        # This means arr_x + k = (arr_x - k) + 2k = nums[0] + 2k.
        # We iterate through all other elements nums[i] in the sorted array
        # to find a potential candidate for `nums[0] + 2k`.
        for i in range(1, len(nums)):
            # The difference (nums[i] - nums[0]) would be equal to 2k.
            # Therefore, `diff` must be positive and even.
            diff = nums[i] - nums[0]
            if diff > 0 and diff % 2 == 0:
                k_candidate = diff // 2
                result = check_k(k_candidate)
                if result is not None:
                    # We found a valid k and the corresponding original array `arr`.
                    # Since any valid `arr` is acceptable, we can return it immediately.
                    return result

        # The problem statement guarantees that at least one valid array arr exists.
        # Thus, the code should always find and return a result before reaching this line.
        return []
