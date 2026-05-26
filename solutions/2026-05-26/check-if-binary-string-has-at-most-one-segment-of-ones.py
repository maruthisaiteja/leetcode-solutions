# Title: Check if Binary String Has at Most One Segment of Ones
# URL: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Difficulty: Easy

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen_zero = False
        for char in s:
            if char == '1':
                if seen_zero:
                    # Found a '1' after a '0', indicating more than one segment of ones.
                    return False
            else: # char == '0'
                # Mark that we have encountered a '0'. Any subsequent '1' will make it multiple segments.
                seen_zero = True
        
        # If the loop completes, it means no '1' was found after a '0'.
        # This implies there's at most one segment of ones (or exactly one, given s[0] is '1').
        return True
