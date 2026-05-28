# Title: Minimum String Length After Balanced Removals
# URL: https://leetcode.com/problems/minimum-string-length-after-balanced-removals/
# Difficulty: Medium

class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        unpaired_a = 0
        unpaired_b = 0

        for char in s:
            if char == 'a':
                # If there are any unpaired 'b's, this 'a' can cancel one of them out.
                # This effectively removes a balanced 'ab' or 'ba' substring.
                if unpaired_b > 0:
                    unpaired_b -= 1
                else:
                    # Otherwise, this 'a' becomes a new unpaired 'a'.
                    unpaired_a += 1
            else:  # char == 'b'
                # If there are any unpaired 'a's, this 'b' can cancel one of them out.
                if unpaired_a > 0:
                    unpaired_a -= 1
                else:
                    # Otherwise, this 'b' becomes a new unpaired 'b'.
                    unpaired_b += 1
        
        # The minimum length of the string after all possible removals
        # is the total number of characters that could not be paired up.
        return unpaired_a + unpaired_b
