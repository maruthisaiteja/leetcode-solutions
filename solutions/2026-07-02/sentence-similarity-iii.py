# Title: Sentence Similarity III
# URL: https://leetcode.com/problems/sentence-similarity-iii/
# Difficulty: Medium

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(' ')
        words2 = sentence2.split(' ')

        n1 = len(words1)
        n2 = len(words2)

        # Ensure words1 refers to the longer or equal length sentence.
        # This simplifies the logic, as we only need to consider inserting words into words2
        # (or equivalently, removing words from words1).
        if n1 < n2:
            words1, words2 = words2, words1
            n1, n2 = n2, n1

        # Case 1: If sentences have equal length, they must be identical.
        # An "empty" sentence insertion means no change, so sentences must be exactly the same.
        if n1 == n2:
            return words1 == words2
        
        # Case 2: n1 > n2.
        # The shorter sentence (words2) must be formed by a prefix of words1
        # followed by a suffix of words1, effectively having a single middle section of words1 removed.

        # Find the length of the common prefix
        left = 0
        while left < n2 and words1[left] == words2[left]:
            left += 1
        
        # Find the length of the common suffix
        right = 0
        # The condition 'left + right < n2' is crucial.
        # It ensures that the elements being compared for the suffix match in words2
        # do not overlap with the elements already matched by the prefix.
        # In words2, 'left' points to the first word *not* matched by the prefix.
        # 'n2 - 1 - right' points to the word being compared for suffix match from the end.
        while left + right < n2 and words1[n1 - 1 - right] == words2[n2 - 1 - right]:
            right += 1
        
        # For the sentences to be similar, all words in the shorter sentence (words2)
        # must be covered by the combined matched prefix and suffix.
        # This means the total count of matched words (left + right) must be at least n2.
        # Due to the loop condition 'left + right < n2', the maximum value 'left + right' can reach is n2.
        # So, 'left + right >= n2' effectively becomes 'left + right == n2'.
        return left + right >= n2
