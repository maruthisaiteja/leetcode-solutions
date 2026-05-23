# Title: Water Bottles
# URL: https://leetcode.com/problems/water-bottles/
# Difficulty: Easy

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk_bottles = 0
        empty_bottles = 0

        # Initially, drink all available numBottles
        total_drunk_bottles += numBottles
        empty_bottles += numBottles

        # Continue as long as we have enough empty bottles to make an exchange
        while empty_bottles >= numExchange:
            # Calculate how many new full bottles can be obtained from exchanges
            new_full_bottles = empty_bottles // numExchange

            # Drink these new full bottles
            total_drunk_bottles += new_full_bottles

            # Update the count of empty bottles:
            # 1. Add the empty bottles from the newly drunk bottles.
            # 2. Add the leftover empty bottles that were not used for exchange.
            empty_bottles = (empty_bottles % numExchange) + new_full_bottles
        
        return total_drunk_bottles
