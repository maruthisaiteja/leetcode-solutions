# Title: Crawler Log Folder
# URL: https://leetcode.com/problems/crawler-log-folder/
# Difficulty: Easy

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log == "./":
                continue
            else:  # log is "x/"
                depth += 1
        return depth
