# Title: Find Subarrays With Equal Sum
# URL: https://leetcode.com/problems/find-subarrays-with-equal-sum/
# Difficulty: Easy

class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen_sums = set()
        n = len(nums)
        for i in range(n - 1):
            current_sum = nums[i] + nums[i+1]
            if current_sum in seen_sums:
                return True
            seen_sums.add(current_sum)
        return False
