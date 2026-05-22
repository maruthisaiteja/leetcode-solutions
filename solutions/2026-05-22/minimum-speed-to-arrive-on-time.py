# Title: Minimum Speed to Arrive on Time
# URL: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/
# Difficulty: Medium

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        # Helper function to calculate total time for a given speed
        def calculate_total_time(speed: int) -> float:
            total_time = 0.0
            # For all trains except the last one, we must wait until the next integer hour
            for i in range(n - 1):
                # Time for current segment, rounded up to the next integer hour for departure
                total_time += math.ceil(dist[i] / speed)
            
            # Time for the last segment, no waiting after this one
            total_time += dist[n-1] / speed
            return total_time

        # Binary search for the minimum positive integer speed
        low = 1
        # The problem states the answer will not exceed 10^7.
        # So, the search space for speed is from 1 to 10^7.
        high = 10**7 
        ans = -1 # Initialize with -1 to indicate no valid speed found yet

        while low <= high:
            mid = low + (high - low) // 2
            
            time_taken = calculate_total_time(mid)
            
            if time_taken <= hour:
                # If this speed allows arrival on time, it's a potential answer.
                # We try to find an even smaller speed by searching in the lower half.
                ans = mid
                high = mid - 1
            else:
                # This speed is too slow, we need a faster speed.
                # Search in the upper half.
                low = mid + 1
                
        return ans
