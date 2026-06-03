# Title: Earliest Finish Time for Land and Water Rides II
# URL: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
# Difficulty: Medium

class Solution:
    def _solve_one_direction(self, first_starts: list[int], first_durations: list[int], second_starts: list[int], second_durations: list[int]) -> int:
        """
        Calculates the earliest finish time for the scenario where a ride from
        the 'first' category is taken, followed by a ride from the 'second' category.
        """
        N1 = len(first_starts)
        N2 = len(second_starts)

        # 1. Prepare second rides data: combine start time and duration, then sort by start time.
        #    Also precompute 'start + duration' which is needed for suffix min.
        # Each tuple stores (second_start_time, second_duration, second_start_time + second_duration)
        second_rides_info = []
        for i in range(N2):
            second_rides_info.append((second_starts[i], second_durations[i], second_starts[i] + second_durations[i]))
        
        # Sort second rides by their start times
        second_rides_info.sort()

        # Extract sorted components for easier access. These lists are derived from second_rides_info
        # after sorting by start time.
        sorted_second_start_times = [ride[0] for ride in second_rides_info]
        sorted_second_durations = [ride[1] for ride in second_rides_info]
        sorted_second_finish_times_at_open = [ride[2] for ride in second_rides_info] # This is second_starts[j] + second_durations[j]

        # 2. Precompute prefix/suffix minimums for second rides
        #    prefix_min_duration[k]: minimum duration among second_rides[0]...second_rides[k] (in sorted order)
        prefix_min_duration = [0] * N2
        # N2 is guaranteed to be at least 1 by problem constraints if this function is called.
        prefix_min_duration[0] = sorted_second_durations[0]
        for i in range(1, N2):
            prefix_min_duration[i] = min(prefix_min_duration[i-1], sorted_second_durations[i])

        #    suffix_min_sum_duration[k]: minimum (start_time + duration) among second_rides[k]...second_rides[N2-1] (in sorted order)
        suffix_min_sum_duration = [0] * N2
        # N2 is guaranteed to be at least 1 by problem constraints.
        suffix_min_sum_duration[N2-1] = sorted_second_finish_times_at_open[N2-1]
        for i in range(N2 - 2, -1, -1):
            suffix_min_sum_duration[i] = min(suffix_min_sum_duration[i+1], sorted_second_finish_times_at_open[i])
        
        # 3. Iterate through first rides and find the overall minimum finish time
        min_total_finish_time = float('inf')

        for i in range(N1):
            first_ride_finish_time = first_starts[i] + first_durations[i]

            # Find the split point `k` in sorted_second_start_times using binary search.
            # `k` is the index of the first ride in `second_rides_info`
            # whose `start_time` is strictly greater than `first_ride_finish_time`.
            k = bisect.bisect_right(sorted_second_start_times, first_ride_finish_time)

            # Case 1: The second ride `j` can start immediately after the first ride finishes.
            # This happens if `second_starts[j] <= first_ride_finish_time`.
            # These are rides with indices `0` through `k-1` in the sorted `second_rides_info`.
            # The total finish time for such a pair (first_ride[i], second_ride[j]) is
            # `first_ride_finish_time + second_durations[j]`.
            # To minimize this, we take `first_ride_finish_time + min(second_durations[j])`
            # where `j` is in `[0, k-1]`.
            if k > 0:
                candidate_finish_time_1 = first_ride_finish_time + prefix_min_duration[k-1]
                min_total_finish_time = min(min_total_finish_time, candidate_finish_time_1)

            # Case 2: The second ride `j` must wait until its opening time (because it opens after the first ride finishes).
            # This happens if `second_starts[j] > first_ride_finish_time`.
            # These are rides with indices `k` through `N2-1` in the sorted `second_rides_info`.
            # The total finish time for such a pair (first_ride[i], second_ride[j]) is
            # `second_starts[j] + second_durations[j]`.
            # To minimize this, we take `min(second_starts[j] + second_durations[j])`
            # where `j` is in `[k, N2-1]`.
            if k < N2:
                candidate_finish_time_2 = suffix_min_sum_duration[k]
                min_total_finish_time = min(min_total_finish_time, candidate_finish_time_2)
        
        return min_total_finish_time

    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        ans = float('inf')

        # Scenario 1: Land ride first, then Water ride
        ans = min(ans, self._solve_one_direction(landStartTime, landDuration, waterStartTime, waterDuration))

        # Scenario 2: Water ride first, then Land ride
        # This is symmetric, so we just swap the arguments to the helper function.
        ans = min(ans, self._solve_one_direction(waterStartTime, waterDuration, landStartTime, landDuration))

        return int(ans) # Return as int as per problem description.
