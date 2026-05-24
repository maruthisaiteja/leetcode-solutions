# Title: Bus Routes
# URL: https://leetcode.com/problems/bus-routes/
# Difficulty: Hard

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create an adjacency list where keys are bus stops and values are lists of route indices
        # that pass through that stop.
        stop_to_routes = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        # Initialize a queue for BFS. It will store route indices.
        q = collections.deque()
        
        # Keep track of visited routes to avoid cycles and redundant processing.
        visited_routes = set()

        # Start the BFS by finding all routes that pass through the source stop.
        # If the source stop is not part of any route, stop_to_routes.get(source, []) will be empty.
        for route_idx in stop_to_routes.get(source, []):
            q.append(route_idx)
            visited_routes.add(route_idx)
        
        # If no routes start at the source, and source != target, it's impossible to travel.
        # The BFS loop won't run, and -1 will be returned, which is correct.
        
        # 'buses' counts the number of buses taken. Since we've already "taken" the initial routes,
        # we start counting from 1.
        buses = 1 

        while q:
            # Process all routes at the current level (i.e., all routes reachable with 'buses' number of transfers).
            level_size = len(q)
            for _ in range(level_size):
                current_route_idx = q.popleft()

                # Iterate through all stops on the current bus route.
                for stop in routes[current_route_idx]:
                    # If we reach the target stop, we've found the shortest path.
                    if stop == target:
                        return buses
                    
                    # From the current stop, we can transfer to any other bus route
                    # that also passes through this stop.
                    for next_route_idx in stop_to_routes.get(stop, []):
                        if next_route_idx not in visited_routes:
                            visited_routes.add(next_route_idx)
                            q.append(next_route_idx)
            
            # After processing all routes at the current level, increment the bus count
            # for the next level of transfers.
            buses += 1
        
        # If the queue becomes empty and the target stop was never reached,
        # it means there's no path from source to target.
        return -1
