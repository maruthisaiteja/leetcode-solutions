# Title: Earliest Finish Time for Land and Water Rides I
# URL: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
# Difficulty: Easy

class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        
        min_overall_finish_time = float('inf')
        
        for i in range(n):
            for j in range(m):
                # Plan 1: Land ride i first, then Water ride j
                # Finish time for land ride i (started at its earliest possible time)
                finish_land_i = landStartTime[i] + landDuration[i]
                
                # Start time for water ride j
                # It must start after land ride i finishes AND after water ride j opens
                start_water_j = max(finish_land_i, waterStartTime[j])
                
                # Total finish time for this sequence (Land i -> Water j)
                current_finish_time_LW = start_water_j + waterDuration[j]
                min_overall_finish_time = min(min_overall_finish_time, current_finish_time_LW)
                
                # Plan 2: Water ride j first, then Land ride i
                # Finish time for water ride j (started at its earliest possible time)
                finish_water_j = waterStartTime[j] + waterDuration[j]
                
                # Start time for land ride i
                # It must start after water ride j finishes AND after land ride i opens
                start_land_i = max(finish_water_j, landStartTime[i])
                
                # Total finish time for this sequence (Water j -> Land i)
                current_finish_time_WL = start_land_i + landDuration[i]
                min_overall_finish_time = min(min_overall_finish_time, current_finish_time_WL)
                
        return int(min_overall_finish_time)
