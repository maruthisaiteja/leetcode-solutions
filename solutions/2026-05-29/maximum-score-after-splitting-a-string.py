# Title: Maximum Score After Splitting a String
# URL: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# Difficulty: Easy

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        # Initialize counts for the first possible split (after s[0]):
        # left = s[0]
        # right = s[1:]
        
        # current_zeros_left will store the count of zeros in the left substring.
        # Start by assuming the first character s[0] is in the left substring.
        current_zeros_left = 1 if s[0] == '0' else 0
        
        # current_ones_right will store the count of ones in the right substring.
        # Initially, it contains all ones from s[1:]
        current_ones_right = 0
        for i in range(1, n):
            if s[i] == '1':
                current_ones_right += 1
                
        # Initialize max_score with the score of the first split.
        max_score = current_zeros_left + current_ones_right
        
        # Iterate through the remaining possible split points.
        # The split point moves from after s[0] to after s[n-2].
        # In each iteration, s[i] moves from the right substring to the left substring.
        for i in range(1, n - 1):
            # Update counts based on s[i] moving to the left substring
            if s[i] == '0':
                current_zeros_left += 1
            else: # s[i] == '1'
                current_ones_right -= 1
            
            # Calculate the score for the current split
            current_score = current_zeros_left + current_ones_right
            
            # Update max_score if the current score is higher
            max_score = max(max_score, current_score)
            
        return max_score
