# Title: Longest Common Prefix
# URL: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # According to constraints, 1 <= strs.length, so strs will not be empty.
        # Initialize prefix with the first string
        prefix = strs[0]

        # Iterate through the rest of the strings
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # While the current prefix is not a prefix of the current string
            while not current_string.startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If prefix becomes empty at any point, it means there's no common prefix at all
                # for the strings processed so far, so we can return an empty string immediately.
                if not prefix:
                    return ""
                    
        return prefix
