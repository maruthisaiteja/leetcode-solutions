# Title: Split the Array to Make Coprime Products
# URL: https://leetcode.com/problems/split-the-array-to-make-coprime-products/
# Difficulty: Hard

import collections
import math

class Solution:
    # Sieve of Eratosthenes to find smallest prime factor (SPF) for numbers up to MAX_VAL
    # spf[i] stores the smallest prime factor of i
    MAX_VAL = 10**6
    spf = [0] * (MAX_VAL + 1)
    
    # Flag to ensure sieve is initialized only once across all instances/calls
    _sieve_initialized = False

    @classmethod
    def _sieve(cls):
        if cls._sieve_initialized:
            return

        for i in range(2, cls.MAX_VAL + 1):
            cls.spf[i] = i
        
        # Iterate up to sqrt(MAX_VAL) for primes
        for i in range(2, int(math.sqrt(cls.MAX_VAL)) + 1):
            if cls.spf[i] == i: # i is prime
                # Mark multiples of i, starting from i*i
                for multiple in range(i * i, cls.MAX_VAL + 1, i):
                    if cls.spf[multiple] == multiple: # only update if not already marked by a smaller prime
                        cls.spf[multiple] = i
        cls._sieve_initialized = True

    # Memoization for prime factors of a number
    # This cache is shared across all instances of Solution and test cases to avoid re-computing factors
    _prime_factors_cache = {}

    def _get_prime_factors(self, num: int) -> set[int]:
        if num == 1:
            return set()
        if num in self._prime_factors_cache:
            return self._prime_factors_cache[num]

        factors = set()
        temp_num = num
        while temp_num > 1:
            factors.add(self.spf[temp_num])
            temp_num //= self.spf[temp_num]
        
        self._prime_factors_cache[num] = factors
        return factors

    def findValidSplit(self, nums: list[int]) -> int:
        # Ensure the sieve is initialized before any factor calculations
        self._sieve()

        n = len(nums)
        # A split at index i is valid if 0 <= i <= n - 2.
        # If n=1, then n-2 = -1, so no valid i exists.
        if n == 1:
            return -1 

        # left_prime_counts[p] = number of elements in the left segment (nums[0...i])
        # that have 'p' as a prime factor.
        left_prime_counts = collections.Counter()
        
        # right_prime_counts[p] = number of elements in the right segment (nums[i+1...n-1])
        # that have 'p' as a prime factor.
        right_prime_counts = collections.Counter()
        
        # common_prime_factor_count: number of distinct prime factors that are
        # present in both the left product and the right product.
        # This count is 0 if and only if the products are coprime.
        common_prime_factor_count = 0

        # Initialize right_prime_counts by considering all numbers initially in the right segment (conceptual i = -1)
        for num in nums:
            for p in self._get_prime_factors(num):
                right_prime_counts[p] += 1
        
        # Iterate i from 0 to n-2. This is the split point.
        for i in range(n - 1): # loop up to n-2 inclusive
            num_i = nums[i] # The current number being moved from right to left
            factors_of_num_i = self._get_prime_factors(num_i)

            for p in factors_of_num_i:
                # Step 1: Process 'p' being removed from the right segment.
                # Check if 'p' was a prime factor of the product of the right segment *before* this operation.
                was_in_right_product = (right_prime_counts[p] > 0)
                right_prime_counts[p] -= 1
                # Check if 'p' is *still* a prime factor of the product of the right segment *after* this operation.
                is_in_right_product = (right_prime_counts[p] > 0)

                if was_in_right_product and not is_in_right_product:
                    # 'p' just ceased to be a prime factor of the right product.
                    # If 'p' was also a prime factor of the left product, it's no longer common.
                    if left_prime_counts[p] > 0:
                        common_prime_factor_count -= 1

                # Step 2: Process 'p' being added to the left segment.
                # Check if 'p' was a prime factor of the product of the left segment *before* this operation.
                was_in_left_product = (left_prime_counts[p] > 0)
                left_prime_counts[p] += 1
                # Check if 'p' is *still* a prime factor of the product of the left segment *after* this operation.
                is_in_left_product = (left_prime_counts[p] > 0)

                if not was_in_left_product and is_in_left_product:
                    # 'p' just became a prime factor of the left product.
                    # If 'p' is currently also a prime factor of the right product, it's now common.
                    if right_prime_counts[p] > 0:
                        common_prime_factor_count += 1
            
            # After moving nums[i], check if the products are coprime
            if common_prime_factor_count == 0:
                return i
        
        # If no valid split is found after checking all possible 'i', return -1
        return -1
