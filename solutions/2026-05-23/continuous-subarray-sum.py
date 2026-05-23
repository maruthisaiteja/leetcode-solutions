# Title: Continuous Subarray Sum
# URL: https://leetcode.com/problems/continuous-subarray-sum/
# Difficulty: Medium

import collections

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first seen index for each remainder
        # { remainder: index }
        # Initialize with {0: -1} to handle cases where the subarray
        # starts from index 0 and its sum is a multiple of k.
        # A prefix sum of 0 at index -1 means the sum up to any index i
        # being a multiple of k implies the subarray from index 0 to i
        # has a sum which is a multiple of k.
        remainder_map = {0: -1}
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k

            if remainder in remainder_map:
                # If this remainder has been seen before, it means there's a subarray
                # between the previous occurrence's index and the current index
                # whose sum is a multiple of k.
                prev_index = remainder_map[remainder]
                
                # Check if the length of this subarray is at least two.
                # The subarray is from nums[prev_index + 1] to nums[i].
                # Its length is i - (prev_index + 1) + 1 = i - prev_index.
                if i - prev_index >= 2:
                    return True
            else:
                # If this remainder is seen for the first time, store its index.
                # We only store the *first* occurrence of a remainder to ensure
                # we maximize the distance `i - prev_index`.
                remainder_map[remainder] = i
        
        return False
