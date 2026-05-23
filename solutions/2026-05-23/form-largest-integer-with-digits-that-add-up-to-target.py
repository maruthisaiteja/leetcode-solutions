# Title: Form Largest Integer With Digits That Add up to Target
# URL: https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
# Difficulty: Hard

from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [(-1, ()) for _ in range(target + 1)]
        dp[0] = (0, ())

        for t in range(1, target + 1):
            current_best_len = -1
            current_best_digits = ()

            for j in range(9, 0, -1):
                digit_cost = cost[j - 1]

                if t >= digit_cost:
                    prev_len, prev_digits = dp[t - digit_cost]

                    if prev_len != -1:
                        new_len = prev_len + 1
                        new_digits = prev_digits + (j,) 

                        if new_len > current_best_len:
                            current_best_len = new_len
                            current_best_digits = new_digits
                        elif new_len == current_best_len:
                            if new_digits > current_best_digits:
                                current_best_digits = new_digits
            
            dp[t] = (current_best_len, current_best_digits)

        final_len, final_digits = dp[target]

        if final_len == -1:
            return "0"
        else:
            return "".join(map(str, final_digits))
