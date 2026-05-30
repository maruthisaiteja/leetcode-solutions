# Title: Height Checker
# URL: https://leetcode.com/problems/height-checker/
# Difficulty: Easy

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
                
        return count
