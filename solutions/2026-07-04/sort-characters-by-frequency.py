# Title: Sort Characters By Frequency
# URL: https://leetcode.com/problems/sort-characters-by-frequency/
# Difficulty: Medium

class Solution:
    def frequencySort(self, s: str) -> str:
        import collections

        # 1. Count character frequencies
        # collections.Counter is a dictionary subclass for counting hashable objects.
        char_counts = collections.Counter(s)

        # 2. Sort characters by frequency in descending order
        # char_counts.items() returns a list of (character, frequency) pairs.
        # The key for sorting is the frequency (item[1]), and we sort in reverse order
        # to get decreasing frequency.
        sorted_chars_by_frequency = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

        # 3. Construct the result string
        # We'll build a list of strings and then join them for efficiency.
        result_parts = []
        for char, count in sorted_chars_by_frequency:
            # Append the character repeated 'count' times to the list.
            result_parts.append(char * count)

        # Join all parts to form the final sorted string.
        return "".join(result_parts)
