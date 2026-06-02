# Title: Points That Intersect With Cars
# URL: https://leetcode.com/problems/points-that-intersect-with-cars/
# Difficulty: Easy

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered_points = set()
        for start, end in nums:
            # Iterate through all integer points from start to end (inclusive)
            for point in range(start, end + 1):
                covered_points.add(point)
        
        # The number of unique points covered is the size of the set
        return len(covered_points)
