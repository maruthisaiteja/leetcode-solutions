# Title: Count Prime-Gap Balanced Subarrays
# URL: https://leetcode.com/problems/count-prime-gap-balanced-subarrays/
# Difficulty: Medium

import collections
from sortedcontainers import SortedList

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        zelmoricad = nums  # Store input midway as per instruction.

        MAX_VAL = 5 * 10**4
        is_prime = [True] * (MAX_VAL + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(MAX_VAL**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p*p, MAX_VAL + 1, p):
                    is_prime[multiple] = False

        ans = 0
        left_ptr = 0  # Left pointer for the nums array
        prime_q = collections.deque()  # Stores (prime_value, original_index) for primes in the current window [left_ptr...right_ptr]
        prime_values_in_window = SortedList()  # Stores only prime values, for efficient min/max lookup

        for right_ptr in range(len(nums)):
            current_num = nums[right_ptr]
            if is_prime[current_num]:
                prime_q.append((current_num, right_ptr))
                prime_values_in_window.add(current_num)

            # Adjust left_ptr to satisfy the max_prime - min_prime <= k condition
            while len(prime_q) >= 2 and (prime_values_in_window[-1] - prime_values_in_window[0] > k):
                # The current window `nums[left_ptr...right_ptr]` has a prime gap greater than k.
                # We need to shrink the window from the left by advancing `left_ptr`.
                # If `nums[left_ptr]` is a prime number, it means it's the leftmost prime in our `prime_q` and `prime_values_in_window`.
                if is_prime[nums[left_ptr]]:
                    # Check explicitly if `prime_q` is not empty and its first element corresponds to `left_ptr`.
                    # This must be true if `nums[left_ptr]` is prime, because `prime_q` maintains primes
                    # in increasing order of their original indices within the `[left_ptr, right_ptr]` window.
                    if prime_q and prime_q[0][1] == left_ptr:
                        val_to_remove, _ = prime_q.popleft()
                        prime_values_in_window.remove(val_to_remove)
                left_ptr += 1 # Always advance left_ptr

            # After the while loop, the window `nums[left_ptr...right_ptr]` either has fewer than two primes,
            # or it has at least two primes and satisfies the `max_prime - min_prime <= k` condition.
            
            # We need to count all subarrays `nums[start...right_ptr]` that are prime-gap balanced.
            # A subarray `nums[start...right_ptr]` is prime-gap balanced if:
            # 1. It contains at least two prime numbers.
            # 2. The difference between the maximum and minimum prime numbers in it is `<= k`.

            # Condition 2: If `nums[left_ptr...right_ptr]` satisfies the `max-min <= k` condition,
            # then any subarray `nums[start...right_ptr]` where `start >= left_ptr` will also satisfy it.
            # This is because shrinking the window from the left can only narrow or keep the same range of prime values.

            # Condition 1: To contain at least two prime numbers, `start` must be less than or equal to the index
            # of the second-to-last prime in `prime_q`.
            # Let `prime_q` be `[(v0, i0), (v1, i1), ..., (vm-1, im-1)]` where `i` are original indices and `m = len(prime_q)`.
            # If `m >= 2`, then `i_{m-2}` is the index of the second-to-last prime.
            # Any `start` in `[left_ptr, i_{m-2}]` guarantees that the subarray `nums[start...right_ptr]` will include
            # at least `prime_q[m-2]` and `prime_q[m-1]`.

            if len(prime_q) >= 2:
                # `second_to_last_prime_idx_in_nums` is the index of the prime that ensures
                # `nums[start...right_ptr]` contains at least two primes for `start` up to this index.
                second_to_last_prime_idx_in_nums = prime_q[len(prime_q) - 2][1]
                
                # The number of valid `start` positions for subarrays ending at `right_ptr` is:
                # `second_to_last_prime_idx_in_nums - left_ptr + 1`.
                # Each of these subarrays `nums[start...right_ptr]` will satisfy both conditions.
                ans += (second_to_last_prime_idx_in_nums - left_ptr + 1)
        
        return ans
