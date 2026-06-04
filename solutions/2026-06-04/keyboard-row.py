# Title: Keyboard Row
# URL: https://leetcode.com/problems/keyboard-row/
# Difficulty: Easy

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            # Constraints state 1 <= words[i].length, so 'word' will not be empty.
            # Determine which row the first character belongs to.
            # This row will be the target for all subsequent characters in the word.
            first_char_lower = word[0].lower()
            
            target_row_set = None
            if first_char_lower in row1:
                target_row_set = row1
            elif first_char_lower in row2:
                target_row_set = row2
            elif first_char_lower in row3:
                target_row_set = row3
            
            # According to constraints, words[i] consists of English letters,
            # so first_char_lower will always be in one of the sets,
            # and target_row_set will never be None.

            is_one_row = True
            for char in word:
                if char.lower() not in target_row_set:
                    is_one_row = False
                    break # Character found in a different row, so this word fails.
            
            if is_one_row:
                result.append(word)
        
        return result
