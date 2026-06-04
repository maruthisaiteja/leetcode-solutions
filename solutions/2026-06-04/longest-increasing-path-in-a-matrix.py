# Title: Longest Increasing Path in a Matrix
# URL: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Difficulty: Hard

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]  # Memoization table to store results of dfs(r, c)

        # Directions for moving up, down, left, right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c):
            # If the longest path starting from (r, c) has already been computed, return it
            if memo[r][c] != 0:
                return memo[r][c]

            # The current cell itself contributes 1 to the path length
            current_max_path = 1

            # Explore all four possible neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check if the neighbor is within bounds and has a strictly greater value
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    # Recursively find the longest path starting from the neighbor
                    # Add 1 to include the current cell in the path
                    current_max_path = max(current_max_path, 1 + dfs(nr, nc))
            
            # Store the computed result in the memoization table before returning
            memo[r][c] = current_max_path
            return current_max_path

        overall_max_path = 0
        # We need to call DFS for every cell, as the longest path could start anywhere
        for r in range(m):
            for c in range(n):
                overall_max_path = max(overall_max_path, dfs(r, c))
        
        return overall_max_path
