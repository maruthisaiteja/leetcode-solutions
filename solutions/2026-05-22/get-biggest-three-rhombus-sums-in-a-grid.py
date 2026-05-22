# Title: Get Biggest Three Rhombus Sums in a Grid
# URL: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
# Difficulty: Medium

from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # dp1[r][c] stores prefix sums along top-left to bottom-right diagonals (r-c = const)
        # Sums from (r', c') to (r, c) where r'<=r, c'<=c, r'-c'=r-c
        dp1 = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                dp1[r][c] = grid[r][c]
                if r > 0 and c > 0:
                    dp1[r][c] += dp1[r-1][c-1]
        
        # dp2[r][c] stores prefix sums along top-right to bottom-left diagonals (r+c = const)
        # Sums from (r', c') to (r, c) where r'<=r, c'>=c, r'+c'=r+c
        dp2 = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n - 1, -1, -1):
                dp2[r][c] = grid[r][c]
                if r > 0 and c < n - 1:
                    dp2[r][c] += dp2[r-1][c+1]
        
        # Helper function to get sum along r-c = const diagonal segment
        def get_diag1_sum(r1, c1, r2, c2):
            # Sum from (r1, c1) to (r2, c2) where r1 <= r2, c1 <= c2, and r-c is constant
            res = dp1[r2][c2]
            if r1 > 0 and c1 > 0:
                res -= dp1[r1-1][c1-1]
            return res

        # Helper function to get sum along r+c = const diagonal segment
        def get_diag2_sum(r1, c1, r2, c2):
            # Sum from (r1, c1) to (r2, c2) where r1 <= r2, c1 >= c2, and r+c is constant
            res = dp2[r2][c2]
            if r1 > 0 and c1 < n - 1:
                res -= dp2[r1-1][c1+1]
            return res

        rhombus_sums = set()

        # Iterate over all possible top corners (r, c)
        for r in range(m):
            for c in range(n):
                # k=0 case: area 0 rhombus, just a single cell
                rhombus_sums.add(grid[r][c])

                # Iterate over possible side lengths k (radius of the rhombus)
                # A rhombus is defined by its top corner (r,c) and radius k.
                # The four corners are:
                # Top: (r, c)
                # Left: (r + k, c - k)
                # Right: (r + k, c + k)
                # Bottom: (r + 2 * k, c)
                
                # Check boundary conditions for the corners:
                # 1. Bottom corner must be within rows: r + 2*k < m  =>  k <= (m - 1 - r) // 2
                # 2. Left corner must be within columns: c - k >= 0   =>  k <= c
                # 3. Right corner must be within columns: c + k < n  =>  k <= n - 1 - c
                
                max_k_possible = min((m - 1 - r) // 2, c, n - 1 - c)

                for k in range(1, max_k_possible + 1):
                    # Coordinates of the four corners
                    r_top, c_top = r, c
                    r_left, c_left = r + k, c - k
                    r_right, c_right = r + k, c + k
                    r_bottom, c_bottom = r + 2 * k, c

                    # Calculate sums of the four segments of the rhombus border
                    # Path A-B (top to left): (r_top, c_top) to (r_left, c_left) along r+c=const diagonal
                    sum_AB = get_diag2_sum(r_top, c_top, r_left, c_left)
                    
                    # Path A-C (top to right): (r_top, c_top) to (r_right, c_right) along r-c=const diagonal
                    sum_AC = get_diag1_sum(r_top, c_top, r_right, c_right)
                    
                    # Path B-D (left to bottom): (r_left, c_left) to (r_bottom, c_bottom) along r-c=const diagonal
                    sum_BD = get_diag1_sum(r_left, c_left, r_bottom, c_bottom)
                    
                    # Path C-D (right to bottom): (r_right, c_right) to (r_bottom, c_bottom) along r+c=const diagonal
                    sum_CD = get_diag2_sum(r_right, c_right, r_bottom, c_bottom)
                    
                    current_rhombus_sum = sum_AB + sum_AC + sum_BD + sum_CD
                    
                    # Each corner cell is included in two segment sums, so subtract them once
                    current_rhombus_sum -= (grid[r_top][c_top] + grid[r_left][c_left] + 
                                            grid[r_right][c_right] + grid[r_bottom][c_bottom])
                    
                    rhombus_sums.add(current_rhombus_sum)
        
        # Convert the set of sums to a list, sort in descending order, and take the top 3
        result = sorted(list(rhombus_sums), reverse=True)
        return result[:3]
