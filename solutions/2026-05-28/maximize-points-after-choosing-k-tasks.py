# Title: Maximize Points After Choosing K Tasks
# URL: https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/
# Difficulty: Medium

class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        
        total_points = 0
        tech1_chosen_count = 0
        
        # This list will store the "penalty" for tasks where technique 2 is better
        # if we are later forced to choose technique 1 for them.
        # The penalty for task i is (technique2[i] - technique1[i]).
        # We initially choose technique2[i] for these tasks, so if we switch to technique1[i],
        # we subtract this penalty from the total points.
        penalties_if_forced_tech1 = [] 

        # First pass: Greedily choose the better technique for each task.
        # Also, count how many tasks naturally preferred technique 1.
        for i in range(n):
            if technique1[i] >= technique2[i]:
                # If technique 1 gives more or equal points, choose it.
                total_points += technique1[i]
                tech1_chosen_count += 1
            else:
                # If technique 2 gives more points, choose it for now.
                # Store the penalty if we later must switch this task to technique 1.
                total_points += technique2[i]
                penalties_if_forced_tech1.append(technique2[i] - technique1[i])
        
        # Now, check if the minimum 'k' tasks using technique 1 requirement is met.
        if tech1_chosen_count >= k:
            # The 'k' requirement is already satisfied or exceeded by greedy choices.
            # The current 'total_points' is the maximum possible.
            return total_points
        else:
            # We need to force (k - tech1_chosen_count) more tasks to use technique 1.
            # These tasks must come from those where we initially chose technique 2
            # (because technique 1 was worse).
            
            # To minimize the reduction in total points, we should force technique 1
            # on tasks with the smallest penalties (i.e., technique1[i] is closest to technique2[i]).
            
            # Sort the penalties in ascending order to easily pick the smallest ones.
            penalties_if_forced_tech1.sort()
            
            num_to_force = k - tech1_chosen_count
            
            # Apply the smallest penalties by subtracting them from total_points.
            # This effectively switches these 'num_to_force' tasks from technique 2 to technique 1.
            for i in range(num_to_force):
                total_points -= penalties_if_forced_tech1[i]
            
            return total_points
