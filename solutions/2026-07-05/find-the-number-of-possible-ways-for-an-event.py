# Title: Find the Number of Possible Ways for an Event
# URL: https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/
# Difficulty: Hard

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        # Precompute factorials and inverse factorials
        # Max value for nCr arguments is x (for C(x, k) and C(k, j))
        max_val = x
        fact = [1] * (max_val + 1)
        invFact = [1] * (max_val + 1)

        for i in range(1, max_val + 1):
            fact[i] = (fact[i - 1] * i) % MOD

        # Modular inverse using Fermat's Little Theorem: a^(MOD-2) % MOD
        invFact[max_val] = power(fact[max_val], MOD - 2) 
        for i in range(max_val - 1, -1, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD

        def nCr(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0
            num = fact[n_val]
            den = (invFact[r_val] * invFact[n_val - r_val]) % MOD
            return (num * den) % MOD

        total_ways = 0

        # Iterate over k, the number of non-empty stages
        # k can range from 0 to x.
        # If k > n (more non-empty stages than performers), the number of ways to assign performers
        # will be 0, which the formula correctly handles.
        for k in range(x + 1):
            # C(x, k) ways to choose k stages that will be non-empty
            ways_to_choose_k_stages = nCr(x, k)

            # y^k ways to assign scores to these k non-empty stages
            ways_to_score_bands = power(y, k)

            # Number of ways to assign n performers to k chosen stages such that all k are non-empty.
            # This is equivalent to k! * S(n, k), where S(n, k) is a Stirling number of the second kind.
            # The formula for k! * S(n, k) is: Sum_{j=0 to k} ((-1)^(k-j) * C(k, j) * j^n)
            num_surjective_maps = 0
            for j in range(k + 1):
                term = (nCr(k, j) * power(j, n)) % MOD
                if (k - j) % 2 == 1:  # (-1)^(k-j) is -1
                    num_surjective_maps = (num_surjective_maps - term + MOD) % MOD
                else:  # (-1)^(k-j) is 1
                    num_surjective_maps = (num_surjective_maps + term) % MOD
            
            # For j=0, power(0, n) is 0 because n >= 1 as per constraints.

            # Multiply components for this specific k
            term_for_k = (ways_to_choose_k_stages * ways_to_score_bands) % MOD
            term_for_k = (term_for_k * num_surjective_maps) % MOD

            total_ways = (total_ways + term_for_k) % MOD

        return total_ways
