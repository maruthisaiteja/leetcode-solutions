# Title: Minimum Fuel Cost to Report to the Capital
# URL: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
# Difficulty: Medium

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # n is the number of cities. For a tree with n nodes, there are n-1 roads.
        # So, n = len(roads) + 1.
        n = len(roads) + 1
        
        # If there's only one city (the capital), no travel is needed.
        if n == 1:
            return 0

        # Build adjacency list for the tree.
        # Using defaultdict for convenience, but list of lists is also fine.
        adj = collections.defaultdict(list)
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        
        # This will store the total fuel consumed.
        self.total_fuel = 0
        
        # DFS function to traverse the tree and calculate fuel cost.
        # It returns the count of people in the subtree rooted at 'u'
        # who are currently at 'u' and need to travel further up to 'parent'.
        def dfs(u, parent):
            # Each city initially has one representative.
            people_at_u = 1 
            
            # Traverse all neighbors of 'u'.
            for v in adj[u]:
                # Avoid going back to the parent to prevent infinite loops in DFS
                # and to ensure processing moves down the tree branches first.
                if v == parent:
                    continue
                
                # Recursively call DFS for child 'v'.
                # people_from_v_subtree is the count of people from the subtree
                # rooted at 'v' who have gathered at 'v'.
                people_from_v_subtree = dfs(v, u)
                
                # These people_from_v_subtree need to travel from 'v' to 'u'.
                # Calculate the number of cars needed.
                # ceil(a / b) can be implemented as (a + b - 1) // b for positive integers.
                cars_needed = (people_from_v_subtree + seats - 1) // seats
                
                # Add the fuel consumed for this segment (v to u) to the total.
                # Each car moving along one edge costs 1 liter.
                self.total_fuel += cars_needed
                
                # Add the people from 'v's subtree to the count of people at 'u'.
                people_at_u += people_from_v_subtree
                
            # Return the total count of people from 'u's subtree who are now at 'u'.
            # This count will be used by 'u's parent to calculate its own car needs.
            return people_at_u
        
        # Start the DFS from the capital city (city 0).
        # The parent of the capital is considered -1 (or None) as it's the root.
        # The return value of dfs(0, -1) (which would be 'n') is not needed for fuel calculation,
        # as fuel is accumulated in self.total_fuel.
        dfs(0, -1)
        
        # Return the accumulated total fuel cost.
        return self.total_fuel
