# Title: Find the Lexicographically Smallest Valid Sequence
# URL: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
# Difficulty: Medium

import bisect

class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # Precompute positions of each character in word1
        # pos[char_code] stores a sorted list of indices where 'char' appears in word1
        pos = [[] for _ in range(26)]
        for i, char_code in enumerate(word1):
            pos[ord(char_code) - ord('a')].append(i)

        # max_first_idx_for_suffix[k][d] stores the maximum index 'j' in word1
        # such that word1[j] can be chosen for word2[k], AND the remaining suffix
        # word2[k+1:] can be completed using 'd' mismatches, with indices strictly
        # greater than 'j'.
        # If no such 'j' exists, it's -1 (or a sentinel indicating impossibility).
        # k goes from 0 to m (length of word2), d goes from 0 to 1.
        
        # Initialize with -1 (sentinel for impossible)
        max_first_idx_for_suffix = [[-1] * 2 for _ in range(m + 1)]

        # Base case: For an empty suffix word2[m:], no character needs to be picked.
        # So, the "maximum first index" is conceptual, meaning any index 'j' < n is valid
        # if the subsequent (empty) suffix can be matched.
        # We use 'n' as a sentinel to mean "any index less than n is potentially valid for the current position".
        max_first_idx_for_suffix[m][0] = n 
        max_first_idx_for_suffix[m][1] = n

        # Fill DP table from m-1 down to 0
        for k in range(m - 1, -1, -1):
            for d in range(2): # d = 0 (0 mismatches), d = 1 (1 mismatch)
                current_max_j = -1 # Initialize with impossible for word2[k]

                # Option 1: Match word2[k] perfectly
                # If word2[k] is matched perfectly, the remaining suffix word2[k+1:]
                # must be completed using 'd' mismatches.
                max_idx_for_next_char = max_first_idx_for_suffix[k + 1][d]

                if max_idx_for_next_char != -1: # If suffix completion is possible
                    target_char_code = ord(word2[k]) - ord('a')
                    idx_list = pos[target_char_code]
                    
                    # We need to find the largest index `j` in `idx_list` such that `j < max_idx_for_next_char`.
                    # bisect_left(list, x) returns an insertion point. If x is present, it's before (to the left of)
                    # any existing entries of x. If x is not present, it's where x would be inserted to maintain order.
                    # So, idx_list[search_idx - 1] would be the largest element < max_idx_for_next_char.
                    search_idx = bisect.bisect_left(idx_list, max_idx_for_next_char)
                    
                    if search_idx > 0: # If there's at least one such index
                        j_perfect = idx_list[search_idx - 1]
                        current_max_j = max(current_max_j, j_perfect)


                # Option 2: Match word2[k] with a mismatch (if diff budget allows)
                if d > 0: # Only if we have budget for a mismatch
                    # If word2[k] is matched with a mismatch, the remaining suffix word2[k+1:]
                    # must be completed using 'd - 1' mismatches.
                    max_idx_for_next_char = max_first_idx_for_suffix[k + 1][d - 1]
                    
                    if max_idx_for_next_char != -1: # If suffix completion is possible
                        j_mismatch_max_val = -1 # Max index in word1 that causes mismatch and allows suffix completion

                        target_char_code = ord(word2[k]) - ord('a')
                        for c_code in range(26):
                            if c_code == target_char_code: # Skip matching char
                                continue
                            
                            idx_list_other_char = pos[c_code]
                            # Find largest index `j` in `idx_list_other_char` such that `j < max_idx_for_next_char`
                            search_idx_other = bisect.bisect_left(idx_list_other_char, max_idx_for_next_char)
                            
                            if search_idx_other > 0:
                                j_mismatch_max_val = max(j_mismatch_max_val, idx_list_other_char[search_idx_other - 1])
                        
                        if j_mismatch_max_val != -1:
                            current_max_j = max(current_max_j, j_mismatch_max_val)
                
                max_first_idx_for_suffix[k][d] = current_max_j
        
        # Greedy construction of the lexicographically smallest sequence
        ans = []
        current_w1_idx_prev = -1 # Previous index chosen in word1. Initialized to -1.
        diff_budget = 1 # We can afford at most one mismatch

        for k in range(m): # Iterate for each character in word2
            j_chosen = n # Sentinel for no valid index found for current word2[k]
            diff_used_for_j = 0 # Mismatch count if j_chosen is picked

            # Strategy: Prioritize perfect match if it yields a smaller or equal 'j',
            # otherwise consider mismatch.

            # Try to find the smallest 'j' for word2[k] that allows a perfect match
            target_char_code = ord(word2[k]) - ord('a')
            idx_list_perfect = pos[target_char_code]
            
            # Find smallest `j` in `idx_list_perfect` such that `j > current_w1_idx_prev`
            search_idx = bisect.bisect_right(idx_list_perfect, current_w1_idx_prev)
            
            if search_idx < len(idx_list_perfect):
                j_potential_perfect = idx_list_perfect[search_idx]
                # Check if this j_potential_perfect allows completing the suffix word2[k+1:]
                # with `diff_budget` mismatches.
                # This means j_potential_perfect must be strictly less than the maximum allowed
                # first index for word2[k+1] (given diff_budget).
                if j_potential_perfect < max_first_idx_for_suffix[k + 1][diff_budget]:
                    j_chosen = j_potential_perfect
                    diff_used_for_j = 0 # This choice results in 0 mismatch

            # Try to find the smallest 'j' for word2[k] that requires a mismatch (if budget allows)
            if diff_budget > 0:
                j_potential_mismatch = n # Initialize with impossible
                
                for c_code in range(26):
                    if c_code == target_char_code:
                        continue
                    
                    idx_list_other_char = pos[c_code]
                    # Find smallest `j` in `idx_list_other_char` such that `j > current_w1_idx_prev`
                    search_idx_other = bisect.bisect_right(idx_list_other_char, current_w1_idx_prev)
                    
                    if search_idx_other < len(idx_list_other_char):
                        candidate_j = idx_list_other_char[search_idx_other]
                        # Check if candidate_j allows completing suffix word2[k+1:] with (diff_budget - 1) mismatches
                        if candidate_j < max_first_idx_for_suffix[k + 1][diff_budget - 1]:
                            j_potential_mismatch = min(j_potential_mismatch, candidate_j)
                
                # If a valid mismatch option was found and it's lexicographically smaller
                # than the current j_chosen, or j_chosen is still 'n' (impossible), update j_chosen.
                if j_potential_mismatch < j_chosen:
                    j_chosen = j_potential_mismatch
                    diff_used_for_j = 1 # This choice results in 1 mismatch
                
            # If no valid index 'j' was found for word2[k] (j_chosen is still 'n')
            if j_chosen == n:
                return [] # No valid sequence exists

            ans.append(j_chosen)
            current_w1_idx_prev = j_chosen
            diff_budget -= diff_used_for_j
        
        return ans
