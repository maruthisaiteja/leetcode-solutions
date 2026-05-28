# Title: DI String Match
# URL: https://leetcode.com/problems/di-string-match/
# Difficulty: Easy

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        
        low = 0
        high = n
        
        perm_result = []
        
        for char_instruction in s:
            if char_instruction == 'I':
                perm_result.append(low)
                low += 1
            else: # char_instruction == 'D'
                perm_result.append(high)
                high -= 1
        
        # After the loop, one number from the range [0, n] remains unused.
        # This remaining number will be equal to 'low' (and also 'high').
        # Append this last number to complete the permutation.
        perm_result.append(low) 
        
        return perm_result
