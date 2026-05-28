# Title: Count of Integers
# URL: https://leetcode.com/problems/count-of-integers/
# Difficulty: Hard

import functools

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        # Helper function to count numbers <= S_str_local whose digit sum is within [min_sum, max_sum].
        # Includes numbers with fewer digits than S_str_local by using `is_leading_zero` logic.
        def count_valid_upto_S(S_str_local: str) -> int:
            
            # @functools.lru_cache(None) is used for memoization.
            # The cache is specific to the `solve` function instance created within `count_valid_upto_S`.
            # min_sum and max_sum are accessed from the outer scope.
            @functools.lru_cache(None)
            def solve(index, current_sum, is_tight, is_leading_zero):
                # Pruning: If the current sum of digits already exceeds max_sum,
                # no further digits can make this a valid number.
                if current_sum > max_sum:
                    return 0

                # Base case: We have processed all digit positions.
                # If current_sum is within the required range [min_sum, max_sum],
                # then this is a valid number.
                # Note: `is_leading_zero` being true when `index == len(S_str_local)`
                # implies the number formed is 0. Since `min_sum >= 1`, 0 is never counted.
                if index == len(S_str_local):
                    return 1 if current_sum >= min_sum else 0

                ans = 0
                # Determine the upper limit for the current digit.
                # If `is_tight` is true, we are restricted by the digit at `S_str_local[index]`.
                # Otherwise, we can place any digit from 0 to 9.
                upper_bound = int(S_str_local[index]) if is_tight else 9

                for digit in range(upper_bound + 1):
                    # `new_is_tight` is true if we were tight and chose the upper_bound digit.
                    new_is_tight = is_tight and (digit == upper_bound)

                    if is_leading_zero:
                        if digit == 0:
                            # If we are placing leading zeros and the current digit is 0,
                            # we remain in leading zero mode, and current_sum doesn't change.
                            ans = (ans + solve(index + 1, current_sum, new_is_tight, True)) % MOD
                        else:
                            # If we are placing leading zeros and the current digit is non-zero,
                            # we transition out of leading zero mode, and add the digit to current_sum.
                            ans = (ans + solve(index + 1, current_sum + digit, new_is_tight, False)) % MOD
                    else:
                        # If we are not in leading zero mode, we simply add the digit to current_sum.
                        ans = (ans + solve(index + 1, current_sum + digit, new_is_tight, False)) % MOD
                
                return ans

            # Initial call to the recursive solve function:
            # - `index = 0`: Start from the first digit.
            # - `current_sum = 0`: Initial sum of digits is 0.
            # - `is_tight = True`: Initially, we are restricted by the digits of S_str_local.
            # - `is_leading_zero = True`: Initially, we can place leading zeros to form shorter numbers.
            result = solve(0, 0, True, True)
            
            # Clear the cache after each call to count_valid_upto_S to ensure independence
            # between calculations for `num2` and `num1 - 1`.
            solve.cache_clear() 
            return result

        # Step 1: Count numbers <= num2 that satisfy the digit sum criteria.
        res2 = count_valid_upto_S(num2)
        
        # Step 2: Calculate num1 - 1 and count numbers <= (num1 - 1) that satisfy the criteria.
        # This is because we need to find numbers x such that num1 <= x <= num2.
        # This is equivalent to (count of x <= num2) - (count of x < num1).
        # And (count of x < num1) is (count of x <= num1 - 1).
        num1_int = int(num1)
        num1_minus_1_str = str(num1_int - 1)
        
        res1_minus_1 = count_valid_upto_S(num1_minus_1_str)
        
        # Step 3: Compute the final result.
        # Ensure the result is non-negative using (A - B + MOD) % MOD.
        return (res2 - res1_minus_1 + MOD) % MOD
