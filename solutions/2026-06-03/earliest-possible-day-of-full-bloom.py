# Title: Earliest Possible Day of Full Bloom
# URL: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
# Difficulty: Hard

import collections
from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # 1. Combine plantTime and growTime for each seed.
        # We store them as (growTime, plantTime) pairs.
        # This allows us to sort primarily by growTime, which is the key insight for this problem.
        seeds = []
        for i in range(len(plantTime)):
            seeds.append((growTime[i], plantTime[i]))
        
        # 2. Sort the seeds in descending order of their growTime.
        # The greedy strategy is to plant seeds with longer grow times earlier.
        # This minimizes the overall latest bloom day.
        seeds.sort(key=lambda x: x[0], reverse=True)
        
        # 3. Initialize variables.
        # 'current_planting_time' tracks the cumulative time spent planting all seeds up to the current one.
        # This variable effectively represents the timestamp when the current seed finishes planting,
        # and its growth period can officially begin.
        current_planting_time = 0
        
        # 'max_bloom_day' will store the latest bloom day among all seeds processed so far.
        # This is our target value to minimize.
        max_bloom_day = 0
        
        # 4. Iterate through the sorted seeds and calculate bloom days.
        for g_time, p_time in seeds:
            # Add the current seed's planting time to the cumulative planting time.
            # After this operation, 'current_planting_time' is the moment this seed is fully planted.
            current_planting_time += p_time
            
            # The bloom day for the current seed is its planting completion time
            # plus its total growth duration.
            # We update 'max_bloom_day' if this seed blooms later than any previous seed.
            max_bloom_day = max(max_bloom_day, current_planting_time + g_time)
            
        # 5. Return the calculated earliest day when all seeds are blooming.
        return max_bloom_day
