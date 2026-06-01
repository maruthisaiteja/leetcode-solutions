# Title: Pascal's Triangle II
# URL: https://leetcode.com/problems/pascals-triangle-ii/
# Difficulty: Easy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            # Extend the row by appending a '1' at the end.
            # The length of row 'i' is i + 1.
            row.append(1)
            
            # Update elements from right to left (excluding the first and last '1's).
            # This order of iteration ensures that when row[j] is updated,
            # row[j-1] and the original row[j] (which corresponds to the element
            # directly above and to its left) still hold values from the
            # previous row's calculation.
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
        
        return row
