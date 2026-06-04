# Title: Self Crossing
# URL: https://leetcode.com/problems/self-crossing/
# Difficulty: Hard

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)

        # A path needs at least 4 segments (d0, d1, d2, d3) to potentially cross.
        # If n < 4, the loop range(3, n) will be empty, so it will correctly return False.
        # No explicit check `if n < 4: return False` is strictly necessary, but included for clarity.
        if n < 4:
            return False

        # Iterate from the 4th segment (index 3) up to the last segment
        # distance[i] refers to the current segment length
        # distance[i-1], distance[i-2], etc., refer to previous segment lengths
        for i in range(3, n):
            # Case 1: The current path segment crosses the segment 3 steps prior.
            # This happens when the path spirals inward too quickly.
            # E.g., d[i] (East) crosses d[i-3] (North).
            # Condition: current segment (d[i]) is long enough to cross d[i-2],
            # AND the segment before current (d[i-1]) is short enough to allow this crossing.
            if distance[i] >= distance[i-2] and \
               distance[i-1] <= distance[i-3]:
                return True

            # Case 2: The current path segment "touches" or crosses the segment 4 steps prior.
            # This requires at least 5 segments (i >= 4) to have distance[i-4] exist.
            # E.g., d[i] (North) touches/crosses d[i-4] (North).
            # This occurs when the 'width' of the inner spiral (d[i-1]) equals the 'width' of the outer spiral (d[i-3]),
            # AND the current segment (d[i]) combined with segment 4 steps prior (d[i-4])
            # is long enough to meet or extend past segment 2 steps prior (d[i-2]).
            if i >= 4:
                if distance[i-1] == distance[i-3] and \
                   distance[i] + distance[i-4] >= distance[i-2]:
                    return True
            
            # Case 3: The current path segment crosses the segment 5 steps prior.
            # This requires at least 6 segments (i >= 5) to have distance[i-5] exist.
            # This is a more complex crossing, where the spiral has contracted, then potentially expanded,
            # and the current segment cuts across a much earlier segment (e.g., d[i] crosses d[i-5]).
            # The conditions ensure a specific geometric configuration leading to a crossing:
            # - distance[i-2] >= distance[i-4]: The segment 2 steps back is at least as long as the segment 4 steps back,
            #                                    ensuring overlap in one dimension.
            # - distance[i-1] + distance[i-5] >= distance[i-3]: The sum of segment 1 step back and segment 5 steps back
            #                                                  is sufficient to cover segment 3 steps back, ensuring overlap in the perpendicular dimension.
            # - distance[i] + distance[i-4] >= distance[i-2]: The sum of the current segment and segment 4 steps back
            #                                               is sufficient to cover segment 2 steps back, ensuring overlap in the first dimension.
            # - distance[i-1] <= distance[i-3]: This additional condition ensures that the path does not expand too much
            #                                   outwards in the perpendicular direction such that the current segment (d[i])
            #                                   flies over the segment 5 steps prior (d[i-5]) without crossing it.
            #                                   This was the missing condition causing the "Wrong Answer" on the given test case.
            if i >= 5:
                if distance[i-2] >= distance[i-4] and \
                   distance[i-1] + distance[i-5] >= distance[i-3] and \
                   distance[i] + distance[i-4] >= distance[i-2] and \
                   distance[i-1] <= distance[i-3]: # Added this crucial check
                    return True
        
        return False
