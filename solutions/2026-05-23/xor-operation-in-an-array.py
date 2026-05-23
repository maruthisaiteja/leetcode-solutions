# Title: XOR Operation in an Array
# URL: https://leetcode.com/problems/xor-operation-in-an-array/
# Difficulty: Easy

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            current_num = start + 2 * i
            result ^= current_num
        return result
