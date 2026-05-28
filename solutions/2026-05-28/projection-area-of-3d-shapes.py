# Title: Projection Area of 3D Shapes
# URL: https://leetcode.com/problems/projection-area-of-3d-shapes/
# Difficulty: Easy

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total_area = 0

        # Calculate XY-plane projection area (top view)
        # Each cell (i, j) with at least one cube (grid[i][j] > 0) contributes 1 to the area.
        for r in range(n):
            for c in range(n):
                if grid[r][c] > 0:
                    total_area += 1
        
        # Calculate ZX-plane projection area (side view from positive Y-axis, looking at rows)
        # For each row, the projection height is the maximum height in that row.
        for r in range(n):
            total_area += max(grid[r])
            
        # Calculate YZ-plane projection area (front view from positive X-axis, looking at columns)
        # For each column, the projection height is the maximum height in that column.
        for c in range(n):
            max_height_in_column = 0
            for r in range(n):
                max_height_in_column = max(max_height_in_column, grid[r][c])
            total_area += max_height_in_column
            
        return total_area
