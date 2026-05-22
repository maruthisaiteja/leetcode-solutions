# Title: Find Missing and Repeated Values
# URL: https://leetcode.com/problems/find-missing-and-repeated-values/
# Difficulty: Easy

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        
        total_elements = m * n
        
        # Create a frequency array/hash map for numbers from 1 to total_elements
        # Index 0 is often unused, so size is total_elements + 1
        counts = [0] * (total_elements + 1)
        
        # Populate frequency counts by iterating through the grid
        for r in range(m):
            for c in range(n):
                num = grid[r][c]
                counts[num] += 1
        
        repeated = -1
        missing = -1
        
        # Iterate from 1 to total_elements to find the repeated and missing numbers
        for i in range(1, total_elements + 1):
            if counts[i] == 2:
                repeated = i
            elif counts[i] == 0:
                missing = i
                
        return [repeated, missing]
