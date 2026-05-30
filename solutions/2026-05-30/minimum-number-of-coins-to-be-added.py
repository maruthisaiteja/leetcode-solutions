# Title: Minimum Number of Coins to be Added
# URL: https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
# Difficulty: Medium

from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()  # Sort the coins to process them in ascending order

        added_coins_count = 0
        # 'reachable' represents the maximum sum 'S' such that all integers in [1, S]
        # are currently obtainable using the coins processed so far (both original and added).
        reachable = 0  
        coin_idx = 0   # Pointer for the sorted coins array

        # We continue adding coins or using existing ones until 'reachable' covers 'target'.
        while reachable < target:
            # Case 1: If we have an available coin in 'coins' that is small enough
            # to extend our 'reachable' range (i.e., coins[coin_idx] <= reachable + 1),
            # we use it. This extends our range by the value of the coin.
            if coin_idx < len(coins) and coins[coin_idx] <= reachable + 1:
                reachable += coins[coin_idx]
                coin_idx += 1
            # Case 2: We have a gap. 'reachable + 1' is the smallest number we cannot currently form.
            # This happens if either:
            #   a) We've exhausted all given coins (coin_idx >= len(coins)).
            #   b) The next available coin (coins[coin_idx]) is too large
            #      (coins[coin_idx] > reachable + 1).
            # In this case, we must add a new coin. The most efficient coin to add is
            # 'reachable + 1' itself. By adding 'reachable + 1', we make all sums
            # from 1 to 'reachable' (which we already could form) plus 'reachable + 1'
            # formable. This means we can now form sums up to 'reachable + (reachable + 1)',
            # effectively doubling our 'reachable' range (plus one).
            else:
                reachable += (reachable + 1)  # Extends range from [1, reachable] to [1, 2 * reachable + 1]
                added_coins_count += 1
        
        return added_coins_count
