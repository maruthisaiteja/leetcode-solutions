# Title: Escape a Large Maze
# URL: https://leetcode.com/problems/escape-a-large-maze/
# Difficulty: Hard

import collections
from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # Convert blocked cells to a set for O(1) average time complexity lookups.
        blocked_set = set(tuple(b) for b in blocked)
        
        # The maximum number of cells that can be surrounded by `N` blocked cells
        # is roughly `N * (N-1) / 2` (for a triangular configuration).
        # Since `N = len(blocked)` is at most 200, this maximum area is about
        # 200 * 199 / 2 = 19900 cells.
        # If a BFS explores more cells than this, it means it has successfully
        # broken out of any potential enclosure formed by the `blocked` cells.
        # We use a slightly larger and simpler constant as the escape threshold.
        # 200 * 200 = 40000 is a safe upper bound for the number of cells that can be trapped.
        # If a BFS visits more than LIMIT cells, it's considered "escaped".
        LIMIT = 200 * 200 

        def bfs_can_escape(start_pos: List[int], end_pos: List[int]) -> bool:
            """
            Performs a BFS from start_pos to check if it can reach end_pos
            or escape the local blocked area.
            Returns True if end_pos is reached or if LIMIT cells are visited (escaped).
            Returns False if trapped without reaching end_pos or escaping.
            """
            q = collections.deque([(start_pos[0], start_pos[1])])
            visited = {(start_pos[0], start_pos[1])}
            
            count = 0 # Number of unique cells visited
            
            # Possible directions: North, East, South, West
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while q:
                cx, cy = q.popleft()
                
                # If target is reached, success
                if cx == end_pos[0] and cy == end_pos[1]:
                    return True
                
                count += 1
                # If we've visited more than LIMIT cells, we've escaped any enclosure
                if count > LIMIT:
                    return True
                
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    
                    # Check boundary conditions (0 to 1 million)
                    # and if the square is not blocked or already visited
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and \
                       (nx, ny) not in blocked_set and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            
            # If the queue becomes empty and we haven't reached target or exceeded LIMIT,
            # it means the start_pos is trapped.
            return False

        # Check if source can reach target or escape the blocked region
        if not bfs_can_escape(source, target):
            return False
        
        # Check if target can reach source or escape the blocked region.
        # This is a crucial second check. If source can escape, it means it can reach the "open" grid.
        # But target might be trapped in another small blocked area, preventing the overall path.
        # Conversely, if target can escape, it means it can reach the "open" grid.
        # If both can escape, they can definitely reach each other through the vast open space.
        if not bfs_can_escape(target, source):
            return False
            
        # If both checks pass, it means either source reached target directly,
        # or source escaped and target escaped (or reached source directly).
        # In all these scenarios, escape is possible.
        return True
