# Title: Longest Strictly Increasing or Strictly Decreasing Subarray
# URL: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Difficulty: Easy

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        max_len = 1
        current_inc_len = 1
        current_dec_len = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                current_inc_len += 1
                current_dec_len = 1  # Strictly decreasing sequence is broken
            elif nums[i] < nums[i-1]:
                current_dec_len += 1
                current_inc_len = 1  # Strictly increasing sequence is broken
            else:  # nums[i] == nums[i-1]
                # Both strictly increasing and strictly decreasing sequences are broken
                current_inc_len = 1
                current_dec_len = 1

            # Update the overall maximum length
            max_len = max(max_len, current_inc_len, current_dec_len)
            
        return max_len
