# Title: Relocate Marbles
# URL: https://leetcode.com/problems/relocate-marbles/
# Difficulty: Medium

from typing import List

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        occupied_positions = set(nums)

        for i in range(len(moveFrom)):
            source_pos = moveFrom[i]
            target_pos = moveTo[i]

            # As per the problem description, it's guaranteed that moveFrom[i] is occupied.
            # All marbles at source_pos move, so source_pos becomes empty.
            occupied_positions.remove(source_pos)
            
            # The target_pos now has marbles. If it was already occupied,
            # adding it again to a set has no effect.
            occupied_positions.add(target_pos)
        
        # Convert the set of final occupied positions to a list and sort it.
        result = list(occupied_positions)
        result.sort()
        
        return result
