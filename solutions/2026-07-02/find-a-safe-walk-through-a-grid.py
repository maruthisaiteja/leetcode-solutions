# Title: Find a Safe Walk Through a Grid
# URL: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
# Difficulty: Medium

import collections
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        # visited[r][c][h] stores whether cell (r,c) has been visited with 'h' health
        # The health value 'h' represents the health *after* any reduction for being on cell (r,c).
        # 'h' can range from 1 up to the initial 'health'.
        # The third dimension size is `health + 1` to allow indexing up to `health` (0 to health).
        visited = [[[False] * (health + 1) for _ in range(n)] for _ in range(m)]

        q = collections.deque()

        # Calculate initial health upon arrival at (0,0) and after potential reduction.
        current_health_at_00 = health
        if grid[0][0] == 1:
            current_health_at_00 -= 1
        
        # If health drops to 0 or less at the starting cell itself, it's impossible to start.
        if current_health_at_00 < 1:
            return False

        # Add starting state to queue: (row, col, current_health)
        # current_health is the health *after* the cell's effect.
        q.append((0, 0, current_health_at_00))
        visited[0][0][current_health_at_00] = True

        # Directions for movement: up, down, left, right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c, h = q.popleft()

            # If we reached the target cell (m-1, n-1) with health >= 1, we found a safe path.
            # The 'h' value in the state (r, c, h) is always guaranteed to be >= 1.
            if r == m - 1 and c == n - 1:
                return True

            # Explore neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check if neighbor is within grid bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # 'h' is the health at cell (r,c) *after* its reduction.
                    # This 'h' is the health upon arrival at (nr,nc) *before* any reduction from (nr,nc).
                    next_h_after_reduction = h
                    if grid[nr][nc] == 1:
                        next_h_after_reduction -= 1
                    
                    # If health remains positive (>= 1) after potential reduction at (nr,nc)
                    # and this specific (nr, nc, next_h_after_reduction) state hasn't been visited yet,
                    # add it to the queue.
                    if next_h_after_reduction >= 1 and not visited[nr][nc][next_h_after_reduction]:
                        visited[nr][nc][next_h_after_reduction] = True
                        q.append((nr, nc, next_h_after_reduction))

        # If the queue becomes empty and the destination was never reached, no safe path exists.
        return False
