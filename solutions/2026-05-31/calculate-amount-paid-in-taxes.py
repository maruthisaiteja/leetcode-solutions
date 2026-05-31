# Title: Calculate Amount Paid in Taxes
# URL: https://leetcode.com/problems/calculate-amount-paid-in-taxes/
# Difficulty: Easy

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total_tax = 0.0
        prev_upper = 0 # Represents the lower bound of the current tax bracket segment

        for upper, percent in brackets:
            # If there's no income left to tax, we can stop
            if income <= 0:
                break

            # Calculate the capacity of the current tax bracket segment.
            # This segment covers income from `prev_upper` up to `upper`.
            taxable_segment_capacity = upper - prev_upper

            # Determine the actual amount of income that falls into and is taxed
            # within this specific bracket segment. It's limited by either the
            # remaining income or the capacity of the current segment.
            amount_to_tax_in_this_segment = min(income, taxable_segment_capacity)

            # Calculate the tax for this amount and add it to the total
            total_tax += amount_to_tax_in_this_segment * (percent / 100.0)

            # Reduce the remaining income by the amount just taxed
            income -= amount_to_tax_in_this_segment

            # Update `prev_upper` to the current bracket's `upper` for the next iteration.
            # This makes `upper` the new lower bound for the subsequent bracket's segment.
            prev_upper = upper
        
        return total_tax
