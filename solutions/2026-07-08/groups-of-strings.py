# Title: Groups of Strings
# URL: https://leetcode.com/problems/groups-of-strings/
# Difficulty: Hard

class DSU:
    def __init__(self, n: int, initial_sizes: List[int]):
        self.parent = list(range(n))
        self.size = initial_sizes[:]  # Stores the total count of original words in the component if it's a root
        self.num_components = n       # Counts the number of disjoint sets
        self.max_group_size = 0       # Stores the size of the largest group found so far

        if n > 0:
            self.max_group_size = max(initial_sizes)

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i

            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            self.num_components -= 1
            self.max_group_size = max(self.max_group_size, self.size[root_i])
            return True
        return False


class Solution:
    def word_to_mask(self, word: str) -> int:
        mask = 0
        for char_code in map(ord, word):
            mask |= (1 << (char_code - ord('a')))
        return mask

    def groupStrings(self, words: List[str]) -> List[int]:
        mask_counts = collections.defaultdict(int)
        for word in words:
            mask_counts[self.word_to_mask(word)] += 1

        unique_masks = list(mask_counts.keys())
        mask_to_id = {mask: i for i, mask in enumerate(unique_masks)}
        num_unique = len(unique_masks)

        initial_dsu_sizes = [mask_counts[unique_masks[i]] for i in range(num_unique)]
        
        dsu = DSU(num_unique, initial_dsu_sizes)

        for current_mask in unique_masks:
            current_id = mask_to_id[current_mask]

            # Operation 1: Deletion (and implicitly Addition)
            for i in range(26):
                if (current_mask >> i) & 1:  # If the i-th bit is set (character is present)
                    deleted_mask = current_mask ^ (1 << i) # Form mask by deleting i-th char
                    if deleted_mask in mask_to_id:
                        deleted_id = mask_to_id[deleted_mask]
                        dsu.union(current_id, deleted_id)
            
            # Operation 2: Replacement
            for i in range(26): # Iterate through bits to potentially remove (chars present)
                if (current_mask >> i) & 1:
                    mask_after_delete = current_mask ^ (1 << i)
                    
                    for j in range(26): # Iterate through bits to potentially add (any char)
                        replaced_mask = mask_after_delete | (1 << j)
                        
                        if replaced_mask in mask_to_id:
                            replaced_id = mask_to_id[replaced_mask]
                            dsu.union(current_id, replaced_id)

        return [dsu.num_components, dsu.max_group_size]

import collections
from typing import List
