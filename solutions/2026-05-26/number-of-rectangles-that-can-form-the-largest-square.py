# Title: Number Of Rectangles That Can Form The Largest Square
# URL: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# Difficulty: Easy

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        count = 0

        for l, w in rectangles:
            current_k = min(l, w)
            
            if current_k > maxLen:
                maxLen = current_k
                count = 1
            elif current_k == maxLen:
                count += 1

        return count
