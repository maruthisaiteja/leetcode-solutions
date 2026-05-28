# Title: Earliest Finish Time for Land and Water Rides II
# URL: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
# Difficulty: Medium

class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        import bisect

        def calculate_min_finish_for_order(rides1: list[tuple[int, int]], rides2: list[tuple[int, int]]) -> int:
            n1 = len(rides1)
            n2 = len(rides2)

            # Sort rides2 by start_time for efficient querying using binary search.
            # This modification is in-place. For the second call to this function,
            # `rides_water` (or `rides_land`) might already be sorted if it was `rides2` in the previous call.
            # This is fine as sorting an already sorted list has no ill effect.
            rides2.sort(key=lambda x: x[0])

            # Precompute prefix minimums of duration for rides2.
            # min_dur_prefix[k] stores min(duration) for rides2[0...k-1].
            # min_dur_prefix[0] is float('inf') as there are no rides before index 0.
            min_dur_prefix = [float('inf')] * (n2 + 1)
            for k in range(n2):
                min_dur_prefix[k+1] = min(min_dur_prefix[k], rides2[k][1])

            # Precompute suffix minimums of (start_time + duration) for rides2.
            # min_start_plus_dur_suffix[k] stores min(start_time + duration) for rides2[k...n2-1].
            # min_start_plus_dur_suffix[n2] is float('inf') as there are no rides after index n2-1.
            min_start_plus_dur_suffix = [float('inf')] * (n2 + 1)
            for k in range(n2 - 1, -1, -1):
                min_start_plus_dur_suffix[k] = min(min_start_plus_dur_suffix[k+1], rides2[k][0] + rides2[k][1])

            # Extract start times for efficient binary search.
            rides2_start_times = [r[0] for r in rides2]

            min_overall_finish = float('inf')

            # Iterate through each ride from the first category (rides1)
            for s1, d1 in rides1:
                first_ride_finish_time = s1 + d1

                # Find the index 'k' in rides2_start_times such that
                # rides2_start_times[k] is the first start_time >= first_ride_finish_time.
                k = bisect.bisect_left(rides2_start_times, first_ride_finish_time)

                # Case 1: The second ride (from rides2) can be started immediately after the first ride finishes.
                # This happens if its start_time is less than `first_ride_finish_time`.
                # We consider rides2[0...k-1]. For these, the actual start time will be `first_ride_finish_time`.
                # To minimize the overall finish time, we pick the one with the minimum duration among these.
                if k > 0:
                    min_dur_val = min_dur_prefix[k]
                    candidate_finish = first_ride_finish_time + min_dur_val
                    min_overall_finish = min(min_overall_finish, candidate_finish)

                # Case 2: The second ride (from rides2) opens at or after first_ride_finish_time.
                # For these rides, we must wait until they open. The start time for the second ride
                # will be its own `start_time`.
                # We consider rides2[k...n2-1]. For these, the finish time is `start_time + duration`.
                # To minimize overall finish time, we pick the one with the minimum `(start_time + duration)`.
                if k < n2:
                    min_start_plus_dur_val = min_start_plus_dur_suffix[k]
                    candidate_finish = min_start_plus_dur_val
                    min_overall_finish = min(min_overall_finish, candidate_finish)
            
            return min_overall_finish

        rides_land = []
        for i in range(len(landStartTime)):
            rides_land.append((landStartTime[i], landDuration[i]))

        rides_water = []
        for i in range(len(waterStartTime)):
            rides_water.append((waterStartTime[i], waterDuration[i]))
        
        # Calculate minimum finish time if a land ride is taken first, then a water ride.
        min_lw = calculate_min_finish_for_order(rides_land, rides_water)
        
        # Calculate minimum finish time if a water ride is taken first, then a land ride.
        min_wl = calculate_min_finish_for_order(rides_water, rides_land)
        
        return min(min_lw, min_wl)
