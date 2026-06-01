# Title: Power Grid Maintenance
# URL: https://leetcode.com/problems/power-grid-maintenance/
# Difficulty: Medium

import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        # DSU structure
        # parent[i] stores the parent of station i.
        # Initially, each station is its own parent.
        parent = list(range(c + 1)) 
        
        # Find operation with path compression.
        # Returns the representative (root) of the set containing i.
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]
        
        # Union operation. Merges the sets containing i and j.
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_j] = root_i # Attach root_j's tree to root_i
                return True
            return False

        # is_online[i] is True if station i is operational, False otherwise.
        # Stations are 1-indexed, so the array is of size c+1.
        is_online = [True] * (c + 1)

        # Build initial connected components using DSU based on given connections.
        for u, v in connections:
            union(u, v)
        
        # After all initial unions, flatten the DSU trees to ensure all nodes point directly to their root.
        # This makes subsequent find operations for query processing faster.
        # Also, collect all members for each component.
        component_members = {}
        for i in range(1, c + 1):
            root = find(i) # This call also applies path compression for i
            if root not in component_members:
                component_members[root] = []
            component_members[root].append(i)
        
        # Initialize min-heaps for each component.
        # online_min_heaps[root] will store a min-heap of station IDs
        # that are currently online within the component rooted at 'root'.
        online_min_heaps = {}
        for root, members in component_members.items():
            # Initially, all members are online, so heapify the list of members.
            heapq.heapify(members) # In-place heapify
            online_min_heaps[root] = members

        results = []
        for query_type, x in queries:
            if query_type == 1: # Maintenance check for station x
                if is_online[x]:
                    # If x is online, it resolves the check itself.
                    results.append(x)
                else:
                    # If x is offline, find the root of its component.
                    root = find(x)
                    heap = online_min_heaps[root]
                    
                    # Lazily remove offline stations from the top of the heap.
                    # We only pop if the station at the top is marked as offline.
                    while heap and not is_online[heap[0]]:
                        heapq.heappop(heap)
                    
                    # After cleaning, if the heap is not empty, the smallest online station is at the top.
                    if heap:
                        results.append(heap[0])
                    else:
                        # No operational station exists in this grid.
                        results.append(-1)
            else: # query_type == 2, station x goes offline
                # Simply mark station x as offline. 
                # It will be removed from its component's heap lazily during future type 1 queries.
                is_online[x] = False
        
        return results
