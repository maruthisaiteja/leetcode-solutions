# Title: Minimum Score of a Path Between Two Cities
# URL: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Difficulty: Medium

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        min_score = float('inf')
        
        q = collections.deque([1])
        visited = {1} 

        while q:
            curr_city = q.popleft()

            for neighbor, dist in adj[curr_city]:
                min_score = min(min_score, dist)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return min_score
