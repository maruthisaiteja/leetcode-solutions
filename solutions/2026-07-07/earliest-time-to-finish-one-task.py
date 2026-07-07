# Title: Earliest Time to Finish One Task
# URL: https://leetcode.com/problems/earliest-time-to-finish-one-task/
# Difficulty: Easy

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(s + t for s, t in tasks)
