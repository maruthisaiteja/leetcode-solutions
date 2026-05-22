# Title: Search in Rotated Sorted Array
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            # Case 1: Left half is sorted (from low to mid)
            if nums[low] <= nums[mid]:
                # Check if target is within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    # Target is in the unsorted right half
                    low = mid + 1
            # Case 2: Right half is sorted (from mid to high)
            else:
                # Check if target is within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    # Target is in the unsorted left half
                    high = mid - 1
        
        return -1
