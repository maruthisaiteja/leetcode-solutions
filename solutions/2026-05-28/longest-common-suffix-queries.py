# Title: Longest Common Suffix Queries
# URL: https://leetcode.com/problems/longest-common-suffix-queries/
# Difficulty: Hard

import collections
from typing import List

class TrieNode:
    def __init__(self):
        # Using collections.defaultdict to automatically create new TrieNodes
        # when a child character is accessed for the first time.
        self.children = collections.defaultdict(TrieNode)
        
        # best_word_info stores a tuple: (length_of_word_in_container, original_index_in_container)
        # It represents the best word from wordsContainer that has the suffix corresponding
        # to the path from the root to this node.
        # Initialized with float('inf') for both length and index to ensure any
        # valid word will be considered 'better' initially.
        self.best_word_info = (float('inf'), float('inf'))

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        # Helper function to update a Trie node's best_word_info based on problem rules:
        # 1. Smallest length of the word
        # 2. Earliest occurrence (smallest original index) if lengths are tied
        def update_node_best(node: TrieNode, new_word_len: int, new_word_idx: int):
            current_best_len, current_best_idx = node.best_word_info
            
            if new_word_len < current_best_len:
                # This word is strictly shorter, so it's the new best.
                node.best_word_info = (new_word_len, new_word_idx)
            elif new_word_len == current_best_len:
                # Lengths are equal, compare by original index.
                # If the new word's index is earlier, it's the new best.
                if new_word_idx < current_best_idx:
                    node.best_word_info = (new_word_len, new_word_idx)

        # 1. Build the Trie: Insert reversed words from wordsContainer
        for j, word in enumerate(wordsContainer):
            curr = root
            word_len = len(word)
            word_rev = word[::-1]

            # Update the root node's best_word_info for the "empty suffix" case.
            # This ensures the root always holds the overall shortest (then earliest)
            # word from wordsContainer, which is the default answer if no common suffix is found.
            update_node_best(curr, word_len, j)

            # Traverse the reversed word, creating nodes and updating their best_word_info
            # Each node `curr` along the path represents a suffix of the current `word`.
            for char in word_rev:
                curr = curr.children[char] # defaultdict creates node if `char` not in children
                update_node_best(curr, word_len, j) # Update the current node's info

        ans = []
        # 2. Process each query
        for query_word in wordsQuery:
            query_word_rev = query_word[::-1]
            curr = root
            
            # Initialize current best match with the root's info.
            # This represents the best choice for a 0-length common suffix.
            best_suffix_len = 0
            best_wc_len, best_wc_idx = root.best_word_info 

            # Traverse the Trie using the reversed query word
            for k, char in enumerate(query_word_rev):
                if char not in curr.children:
                    # The current character `char` does not exist as a child,
                    # meaning no words in wordsContainer share a longer suffix.
                    # We break and use the best candidate found so far.
                    break
                
                curr = curr.children[char]
                current_suffix_len = k + 1 # Length of the common suffix matched up to this node

                node_wc_len, node_wc_idx = curr.best_word_info

                # Apply the problem's comparison rules:
                # 1. Prioritize the longest common suffix.
                # 2. If suffix lengths are tied, prioritize the smallest word length from wordsContainer.
                # 3. If suffix length and word length are tied, prioritize the earliest occurrence index.
                
                if current_suffix_len > best_suffix_len:
                    # Found a strictly longer common suffix, so this is immediately the new best choice.
                    best_suffix_len = current_suffix_len
                    best_wc_len = node_wc_len
                    best_wc_idx = node_wc_idx
                elif current_suffix_len == best_suffix_len:
                    # Same common suffix length, compare based on word length.
                    if node_wc_len < best_wc_len:
                        # This node's associated word has a smaller length, making it better.
                        best_wc_len = node_wc_len
                        best_wc_idx = node_wc_idx
                    elif node_wc_len == best_wc_len:
                        # Tie in suffix length and word length, compare by original index.
                        # If this node's associated word occurred earlier, it's better.
                        if node_wc_idx < best_wc_idx:
                            best_wc_idx = node_wc_idx
                        
            ans.append(best_wc_idx)
            
        return ans
