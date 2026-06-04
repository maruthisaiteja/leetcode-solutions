# Title: Cheapest Flights Within K Stops
# URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Difficulty: Medium

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize an array to store the minimum cost to reach each city.
        # All cities start with an infinite cost, except the source city which has a cost of 0.
        prices = [float('inf')] * n
        prices[src] = 0

        # We need to find paths with at most 'k' stops, which means at most 'k+1' flights.
        # The Bellman-Ford-like approach iterates 'k+1' times.
        # Each iteration considers paths that are one flight longer than the previous iteration.
        for _ in range(k + 1):
            # Create a temporary array to store prices calculated in the current iteration.
            # This is crucial: we must use prices from the *previous* iteration (stored in 'prices')
            # to calculate the 'new_prices' for the *current* iteration.
            # This ensures that we are correctly finding paths with an increasing number of flights.
            new_prices = list(prices)

            # Iterate through all available flights.
            for fro, to, price in flights:
                # If the source city 'fro' was not reachable in the previous iteration
                # (its cost is still infinity), we cannot extend a path from it.
                if prices[fro] == float('inf'):
                    continue
                
                # Calculate the cost of reaching 'to' by taking a flight from 'fro'.
                # Update 'new_prices[to]' if this path offers a cheaper cost.
                new_prices[to] = min(new_prices[to], prices[fro] + price)
            
            # After processing all flights for the current iteration,
            # update the main 'prices' array with the new minimum costs found.
            # These 'prices' will then be used for the next iteration.
            prices = new_prices
        
        # After 'k+1' iterations, 'prices[dst]' will contain the cheapest price
        # to reach the destination 'dst' using at most 'k' stops (i.e., 'k+1' flights).
        # If 'prices[dst]' is still 'float('inf')', it means 'dst' is unreachable
        # within the given constraints, so we return -1. Otherwise, return the cost.
        return prices[dst] if prices[dst] != float('inf') else -1
