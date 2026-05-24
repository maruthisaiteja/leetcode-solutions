# Title: Swim in Rising Water
# URL: https://leetcode.com/problems/swim-in-rising-water/
# Difficulty: Hard

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # dist[r][c] will store the minimum time 't' (maximum elevation encountered) 
        # required to reach cell (r, c) from the starting cell (0, 0).
        # Initialize all distances to infinity.
        dist = [[float('inf')] * n for _ in range(n)]
        
        # The priority queue stores tuples of (current_max_elevation, row, col).
        # It acts as a min-heap, ensuring that we always process the path
        # with the smallest maximum elevation encountered so far.
        pq = []
        
        # Start at cell (0, 0). The elevation at this cell is grid[0][0].
        # So, the initial maximum elevation for the path to (0, 0) is grid[0][0].
        dist[0][0] = grid[0][0]
        heapq.heappush(pq, (grid[0][0], 0, 0))
        
        # Directions for 4-directional movement: up, down, left, right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        while pq:
            # Pop the cell with the smallest current maximum elevation from the priority queue.
            current_max_elevation, r, c = heapq.heappop(pq)
            
            # If the current_max_elevation is greater than the best known maximum elevation
            # to reach (r, c), it means we have already found a better path, so skip.
            if current_max_elevation > dist[r][c]:
                continue
            
            # If we have reached the bottom-right cell (n-1, n-1),
            # this `current_max_elevation` is the minimum time needed.
            # Dijkstra's guarantees that the first time we extract the target node,
            # it's with its shortest path value (in this case, minimum maximum elevation).
            if r == n - 1 and c == n - 1:
                return current_max_elevation
            
            # Explore all 4-directionally adjacent neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                # Check if the neighbor is within the grid boundaries
                if 0 <= nr < n and 0 <= nc < n:
                    # Calculate the new maximum elevation for the path to (nr, nc)
                    # through (r, c). This is the maximum of the current path's
                    # maximum elevation (to reach r, c) and the elevation of the
                    # neighbor cell (nr, nc) itself.
                    new_max_elevation = max(current_max_elevation, grid[nr][nc])
                    
                    # If this new path offers a smaller maximum elevation to reach (nr, nc)
                    # than previously recorded, update its distance and add it to the priority queue.
                    if new_max_elevation < dist[nr][nc]:
                        dist[nr][nc] = new_max_elevation
                        heapq.heappush(pq, (new_max_elevation, nr, nc))
                        
        # This part should theoretically not be reached because the problem constraints
        # imply that a path always exists (as water level can rise indefinitely).
        return -1
