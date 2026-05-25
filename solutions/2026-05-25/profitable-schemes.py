# Title: Profitable Schemes
# URL: https://leetcode.com/problems/profitable-schemes/
# Difficulty: Hard

from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[j][k] stores the number of ways to achieve a profit of 'k' using 'j' people.
        # The profit 'k' is capped at minProfit, meaning dp[j][minProfit] stores
        # the number of ways to achieve a profit of at least minProfit using 'j' people.
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        
        # Base case: 1 way to achieve 0 profit with 0 people (by picking no schemes).
        dp[0][0] = 1
        
        # Iterate through each scheme (crime in the original problem context)
        # g: number of people required for the current scheme
        # p: profit gained from the current scheme
        for g, p in zip(group, profit):
            # Iterate people count from max (n) down to current scheme's group size (g)
            # This backward iteration is crucial for 0/1 knapsack type problems
            # to ensure that each scheme is considered only once per path.
            for i in range(n, g - 1, -1): # i represents current total people
                # Iterate profit from max (minProfit) down to 0
                # j represents current total profit before considering the current scheme
                for j in range(minProfit, -1, -1):
                    # Calculate new profit by adding the current scheme's profit 'p'
                    # and cap it at minProfit. If j + p > minProfit, it means
                    # we have achieved at least minProfit, so we store it in the minProfit column.
                    new_profit = min(minProfit, j + p)
                    
                    # Add the number of ways to achieve profit 'j' with 'i - g' people
                    # to the ways of achieving 'new_profit' with 'i' people.
                    # This represents adding the current scheme (g people, p profit)
                    # to previous valid combinations.
                    dp[i][new_profit] = (dp[i][new_profit] + dp[i - g][j]) % MOD
        
        # The total number of profitable schemes is the sum of all ways
        # where the profit is at least minProfit. This corresponds to summing
        # all values in the `dp[i][minProfit]` column for all possible people counts `i`.
        total_ways = 0
        for i in range(n + 1):
            total_ways = (total_ways + dp[i][minProfit]) % MOD
            
        return total_ways
