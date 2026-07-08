# Title: Occurrences After Bigram
# URL: https://leetcode.com/problems/occurrences-after-bigram/
# Difficulty: Easy

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        result = []
        
        # We need to access words[i], words[i+1], and words[i+2].
        # The loop must ensure that i+2 is a valid index.
        # If words has N elements (indices 0 to N-1),
        # the maximum value for i+2 is N-1.
        # This means the maximum value for i is N-1-2 = N-3.
        # Python's range(X) goes from 0 to X-1.
        # So, range(len(words) - 2) will generate i from 0 up to (len(words) - 2) - 1, which is len(words) - 3.
        # This correctly covers all possible starting positions for "first".
        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        
        return result
