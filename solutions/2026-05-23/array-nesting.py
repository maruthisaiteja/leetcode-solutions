# Title: Array Nesting
# URL: https://leetcode.com/problems/array-nesting/
# Difficulty: Medium

class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_len = 0

        for i in range(n):
            if not visited[i]:
                current_len = 0
                current_index = i

                while not visited[current_index]:
                    visited[current_index] = True
                    current_len += 1
                    current_index = nums[current_index]
                
                max_len = max(max_len, current_len)
        
        return max_len
