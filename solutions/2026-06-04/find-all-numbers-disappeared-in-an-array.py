# Title: Find All Numbers Disappeared in an Array
# URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Difficulty: Easy

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        disappeared_numbers = []
        for i in range(n):
            if nums[i] > 0:
                disappeared_numbers.append(i + 1)
        
        return disappeared_numbers
