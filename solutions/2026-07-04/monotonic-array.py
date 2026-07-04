# Title: Monotonic Array
# URL: https://leetcode.com/problems/monotonic-array/
# Difficulty: Easy

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = True
        is_decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                is_increasing = False
            if nums[i] < nums[i+1]:
                is_decreasing = False
            
            # Optimization: If it's neither increasing nor decreasing, it's not monotonic.
            # We can return False immediately.
            if not is_increasing and not is_decreasing:
                return False
        
        # If we reach here, it means the array is either entirely increasing, 
        # entirely decreasing, or both (e.g., all elements are the same).
        return is_increasing or is_decreasing
