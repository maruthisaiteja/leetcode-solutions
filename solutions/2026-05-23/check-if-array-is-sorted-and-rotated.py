# Title: Check if Array Is Sorted and Rotated
# URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# Difficulty: Easy

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        descent_count = 0

        # Count the number of "descents" (where nums[i] > nums[i+1])
        # A descent indicates a break in the non-decreasing order.
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                descent_count += 1
        
        # If descent_count is 0, the array is already sorted in non-decreasing order
        # (equivalent to being rotated 0 positions).
        if descent_count == 0:
            return True
        
        # If descent_count is 1, there is exactly one rotation point.
        # For the array to be sorted and rotated, the elements before the rotation point
        # must be non-decreasing, and elements after must be non-decreasing.
        # Additionally, the last element must be less than or equal to the first element
        # to maintain the non-decreasing order across the rotation boundary.
        # Example: [3,4,5,1,2] -> descent at (5,1). nums[-1]=2 <= nums[0]=3. True.
        # Example: [2,1,3,4] -> descent at (2,1). nums[-1]=4 <= nums[0]=2. False.
        elif descent_count == 1:
            return nums[n-1] <= nums[0]
        
        # If descent_count is greater than 1, there are multiple breaks in the non-decreasing order.
        # This implies the array cannot be formed by a single rotation of a sorted array.
        else:
            return False
