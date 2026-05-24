# Title: The Employee That Worked on the Longest Task
# URL: https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
# Difficulty: Easy

from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        current_start_time = 0
        max_duration = 0
        hardest_worker_id = -1 

        for employee_id, leave_time in logs:
            duration = leave_time - current_start_time

            if duration > max_duration:
                max_duration = duration
                hardest_worker_id = employee_id
            elif duration == max_duration:
                # If durations are tied, return the smallest ID
                hardest_worker_id = min(hardest_worker_id, employee_id)
            
            current_start_time = leave_time
        
        return hardest_worker_id
