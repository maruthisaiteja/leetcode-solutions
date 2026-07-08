# Title: Find Words That Can Be Formed by Characters
# URL: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
# Difficulty: Easy

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Step 1: Count the frequency of characters in the available 'chars' string.
        # collections.Counter is an efficient way to store character frequencies.
        chars_count = collections.Counter(chars)
        
        total_length = 0
        
        # Step 2: Iterate through each word in the given list of words.
        for word in words:
            # Step 3: Count the frequency of characters for the current word.
            word_count = collections.Counter(word)
            
            # Step 4: Check if the current word can be formed using the characters
            # available in 'chars'. This means that for every character in 'word',
            # its frequency in 'word_count' must be less than or equal to its
            # frequency in 'chars_count'.
            # The Counter object supports comparison operations like '<=' which
            # conveniently checks this condition (i.e., if 'word_count' is a sub-multiset
            # of 'chars_count').
            if word_count <= chars_count:
                # If the word can be formed, add its length to the total_length.
                total_length += len(word)
                
        # Step 5: Return the sum of lengths of all good strings.
        return total_length
