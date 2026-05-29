# Title: Minimum Element After Replacement With Digit Sum
# URL: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Difficulty: Easy

class Solution:
    def _sum_digits(self, n: int) -> int:
        """Helper function to calculate the sum of digits for a given integer."""
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def minElement(self, nums: list[int]) -> int:
        """
        Replaces each element in nums with the sum of its digits and returns
        the minimum element after all replacements.
        """
        min_digit_sum = float('inf')  # Initialize with a very large value

        for num in nums:
            current_sum = self._sum_digits(num)
            if current_sum < min_digit_sum:
                min_digit_sum = current_sum

        return min_digit_sum
