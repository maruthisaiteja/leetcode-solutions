# Title: Monotone Increasing Digits
# URL: https://leetcode.com/problems/monotone-increasing-digits/
# Difficulty: Medium

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n)) 
        
        i_to_nine = len(s) 
        
        for i in range(len(s) - 2, -1, -1):
            if s[i] > s[i+1]:
                s[i] = str(int(s[i]) - 1)
                i_to_nine = i + 1
                
        for i in range(i_to_nine, len(s)):
            s[i] = '9'
            
        return int("".join(s))
