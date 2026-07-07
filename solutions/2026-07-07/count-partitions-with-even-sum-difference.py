# Title: Count Partitions with Even Sum Difference
# URL: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
# Difficulty: Easy

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 == 0:
            return n - 1
        else:
            return 0
