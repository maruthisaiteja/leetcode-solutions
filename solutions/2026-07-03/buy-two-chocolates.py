# Title: Buy Two Chocolates
# URL: https://leetcode.com/problems/buy-two-chocolates/
# Difficulty: Easy

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        # The two cheapest chocolates will be at the beginning of the sorted array
        cost_of_two_cheapest = prices[0] + prices[1]
        
        if money >= cost_of_two_cheapest:
            return money - cost_of_two_cheapest
        else:
            # If we cannot afford even the two cheapest chocolates,
            # we return the original amount of money.
            return money
