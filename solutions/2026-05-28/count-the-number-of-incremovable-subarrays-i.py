# Title: Count the Number of Incremovable Subarrays I
# URL: https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/
# Difficulty: Easy

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def is_strictly_increasing(arr: List[int]) -> bool:
            """
            Checks if a given array is strictly increasing.
            An empty array or a single-element array is considered strictly increasing.
            """
            if len(arr) <= 1:
                return True
            for k in range(len(arr) - 1):
                if arr[k] >= arr[k+1]:
                    return False
            return True

        n = len(nums)
        count = 0

        # Iterate over all possible start indices 'i' for the subarray to remove
        for i in range(n):
            # Iterate over all possible end indices 'j' for the subarray to remove
            # 'j' must be greater than or equal to 'i' to form a valid non-empty subarray
            for j in range(i, n):
                # The subarray to remove is nums[i...j] (inclusive)
                
                # Construct the array that remains after removing nums[i...j]
                # nums[:i] gets elements from index 0 up to i-1
                # nums[j+1:] gets elements from index j+1 to the end
                remaining_elements = nums[:i] + nums[j+1:]
                
                # Check if the constructed remaining_elements array is strictly increasing
                if is_strictly_increasing(remaining_elements):
                    count += 1
        
        return count
