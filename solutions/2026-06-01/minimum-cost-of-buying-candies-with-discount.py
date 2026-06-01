# Title: Minimum Cost of Buying Candies With Discount
# URL: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Difficulty: Easy

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Step 1: Sort the candies in descending order of their cost.
        # This greedy approach ensures that for every group of three candies,
        # we buy the two most expensive ones and get the third most expensive one for free.
        # This maximizes the value of the candy obtained for free, thus minimizing total cost.
        cost.sort(reverse=True)

        total_cost = 0
        n = len(cost)

        # Step 2: Iterate through the sorted candies, processing them in groups of three.
        # 'i' will be the index of the first candy in each group.
        for i in range(0, n, 3):
            # We always pay for the most expensive candy in the current group of three.
            total_cost += cost[i]
            
            # We also pay for the second most expensive candy in the current group,
            # if it exists (i.e., if there are at least two candies left in the group).
            if i + 1 < n:
                total_cost += cost[i + 1]
            
            # The third candy in this group (at index i + 2) is taken for free.
            # We explicitly skip paying for it by incrementing 'i' by 3 in the loop header.
            # If i + 2 is out of bounds, it means there isn't a third candy to take for free,
            # or only one or two candies remained at the very end, which are correctly handled
            # by the above additions to total_cost.

        return total_cost
