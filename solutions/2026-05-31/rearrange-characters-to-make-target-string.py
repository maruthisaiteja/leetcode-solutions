# Title: Rearrange Characters to Make Target String
# URL: https://leetcode.com/problems/rearrange-characters-to-make-target-string/
# Difficulty: Easy

from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_counts = Counter(s)
        target_counts = Counter(target)

        max_copies = float('inf')

        for char, required_count in target_counts.items():
            available_count = s_counts.get(char, 0)
            
            # If a character required by target is not available in s at all,
            # then we cannot make any copies requiring that character.
            # The integer division naturally handles this:
            # if available_count is 0 and required_count > 0, result is 0.
            possible_copies_for_this_char = available_count // required_count
            max_copies = min(max_copies, possible_copies_for_this_char)
        
        return max_copies
