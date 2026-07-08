# Title: Smallest Value After Replacing With Sum of Prime Factors
# URL: https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/
# Difficulty: Medium

class Solution:
    def _sum_prime_factors(self, k: int) -> int:
        """
        Calculates the sum of prime factors of k, including multiplicity.
        For example:
        _sum_prime_factors(15) = 3 + 5 = 8
        _sum_prime_factors(8) = 2 + 2 + 2 = 6
        _sum_prime_factors(5) = 5 (since 5 is prime)
        """
        sum_factors = 0
        d = 2
        temp_k = k
        
        # Iterate from d=2 up to sqrt(temp_k)
        # We use d * d <= temp_k instead of d <= math.sqrt(temp_k) for integer arithmetic performance.
        while d * d <= temp_k:
            while temp_k % d == 0:
                sum_factors += d
                temp_k //= d
            d += 1
            
        # If temp_k is still greater than 1 after the loop, it means the remaining temp_k
        # is a prime factor itself (the largest one).
        if temp_k > 1:
            sum_factors += temp_k
            
        return sum_factors

    def smallestValue(self, n: int) -> int:
        smallest_val = n  # Initialize smallest_val with the initial n
        visited = set()   # To detect cycles and fixed points
        
        current_val = n
        
        while True:
            # Always update smallest_val with the current value in the sequence
            smallest_val = min(smallest_val, current_val)

            # If current_val has been visited before, it means we've entered a cycle
            # or reached a fixed point that was already part of the sequence.
            # In either case, further iterations will only repeat values already seen,
            # so we can break.
            if current_val in visited:
                break
            
            # Mark current_val as visited
            visited.add(current_val)
            
            # Compute the next value in the sequence
            next_val = self._sum_prime_factors(current_val)
            
            # Move to the next value
            current_val = next_val
            
        return smallest_val
