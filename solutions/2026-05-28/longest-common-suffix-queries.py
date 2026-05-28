# Title: Longest Common Suffix Queries
# URL: https://leetcode.com/problems/longest-common-suffix-queries/
# Difficulty: Hard

class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores (min_length_word, min_index_word) among words
        # that have the suffix represented by the path to this node.
        # Initialized with 'infinity' to ensure any actual word is better.
        self.best_candidate = (float('inf'), float('inf'))

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        # Step 1: Find the overall shortest word and its index for the default case (LCS = 0).
        # This will be the answer if no common suffix is found or if the longest
        # common suffix is the empty string, requiring selection by length then index.
        min_len_overall = float('inf')
        min_idx_overall = -1

        for i, word in enumerate(wordsContainer):
            if len(word) < min_len_overall:
                min_len_overall = len(word)
                min_idx_overall = i
            elif len(word) == min_len_overall and i < min_idx_overall:
                min_idx_overall = i
        
        default_best_match_info = (min_len_overall, min_idx_overall)

        # Step 2: Build the Suffix Trie (Trie on reversed words).
        # Each node stores the best candidate (smallest length, then smallest index)
        # among all words in wordsContainer that pass through that node (i.e., share that suffix).
        root = TrieNode()
        # The root node itself represents the empty suffix, so its best_candidate
        # should reflect the overall best word in wordsContainer.
        root.best_candidate = default_best_match_info

        for i, word in enumerate(wordsContainer):
            curr = root
            len_word = len(word)
            reversed_word = word[::-1]
            
            for char in reversed_word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # Update best_candidate for the current node.
                # Python's tuple comparison handles (length, index) lexicographically,
                # which is exactly the desired secondary and tertiary criteria.
                curr.best_candidate = min(curr.best_candidate, (len_word, i))

        # Step 3: Process queries.
        ans = []
        for query_word in wordsQuery:
            curr = root
            # Initialize with the global best (shortest length, then smallest index).
            # This handles cases where no common suffix is found (LCS length 0).
            best_match_for_query = default_best_match_info 
            current_lcs_length = 0 # Length of the longest common suffix found so far for this query.

            reversed_query = query_word[::-1]

            for i, char in enumerate(reversed_query):
                if char in curr.children:
                    curr = curr.children[char]
                    potential_lcs_length = i + 1 # The depth in the Trie is the length of the suffix.
                    potential_best_candidate = curr.best_candidate

                    # Prioritize finding a *longer* common suffix.
                    if potential_lcs_length > current_lcs_length:
                        current_lcs_length = potential_lcs_length
                        best_match_for_query = potential_best_candidate
                    # If LCS length is the same, apply secondary criteria
                    # (shortest word length, then smallest index).
                    # `min()` on tuples ensures this.
                    elif potential_lcs_length == current_lcs_length:
                        best_match_for_query = min(best_match_for_query, potential_best_candidate)
                else:
                    # No more common suffix characters found, stop traversing.
                    break
            
            ans.append(best_match_for_query[1]) # Append the index (second element of the tuple)
        
        return ans
