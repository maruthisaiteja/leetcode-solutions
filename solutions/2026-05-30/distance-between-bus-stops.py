# Title: Distance Between Bus Stops
# URL: https://leetcode.com/problems/distance-between-bus-stops/
# Difficulty: Easy

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)

        # Calculate the total distance of the circular route
        total_distance = sum(distance)

        # Calculate the distance in one direction (e.g., clockwise from start to destination)
        distance_path1 = 0
        current_stop = start
        
        # Iterate until we reach the destination.
        # distance[i] represents the distance from stop i to stop (i+1)%n.
        # We sum these distances along the path from 'start' up to the stop *before* 'destination'.
        while current_stop != destination:
            distance_path1 += distance[current_stop]
            current_stop = (current_stop + 1) % n
        
        # The distance in the other direction is the total_distance minus distance_path1
        distance_path2 = total_distance - distance_path1
        
        # Return the minimum of the two path distances
        return min(distance_path1, distance_path2)
