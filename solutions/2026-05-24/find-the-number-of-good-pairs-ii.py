# Title: Find the Number of Good Pairs II
# URL: https://leetcode.com/problems/find-the-number-of-good-pairs-ii/
# Difficulty: Medium

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Define the maximum possible value for elements in nums1 and nums2, and for x // k.
        # Max nums1[i], nums2[j] is 10^6. Max x // k is 10^6 // 1 = 10^6.
        # We need frequency arrays large enough to cover this global maximum.
        GLOBAL_MAX_VAL = 10**6

        # Step 1: Pre-process nums1 to count frequencies of (nums1[i] // k)
        # for elements nums1[i] that are divisible by k.
        # We use a list for frequency counting for O(1) access time.
        # The size is GLOBAL_MAX_VAL + 1 to accommodate indices from 0 to GLOBAL_MAX_VAL.
        freq1_div_k = [0] * (GLOBAL_MAX_VAL + 1)
        max_val_in_freq1 = 0 # Track the maximum (nums1[i] // k) value actually observed
        for x in nums1:
            if x % k == 0:
                val = x // k
                freq1_div_k[val] += 1
                if val > max_val_in_freq1:
                    max_val_in_freq1 = val

        # Step 2: Pre-process nums2 to count frequencies of its elements.
        freq2_arr = [0] * (GLOBAL_MAX_VAL + 1)
        max_val_in_freq2 = 0 # Track the maximum nums2[j] value actually observed
        for y in nums2:
            # According to constraints, 1 <= nums2[j] <= 10^6, so y is always within bounds.
            freq2_arr[y] += 1
            if y > max_val_in_freq2:
                max_val_in_freq2 = y

        total_good_pairs = 0

        # Step 3: Iterate through all possible values 'd' that nums2[j] can take.
        # To optimize, we iterate 'd' only up to the maximum value observed in nums2 (max_val_in_freq2),
        # instead of the global maximum (GLOBAL_MAX_VAL).
        for d in range(1, max_val_in_freq2 + 1):
            # Only proceed if 'd' is a value present in nums2.
            if freq2_arr[d] > 0:
                # Iterate through multiples of 'd'.
                # 'multiple' will take values d, 2*d, 3*d, ...
                # To optimize, we iterate 'multiple' only up to the maximum (x // k) value observed
                # in nums1 (max_val_in_freq1), instead of the global maximum.
                for multiple in range(d, max_val_in_freq1 + 1, d):
                    # If 'multiple' (which is x // k) is present in freq1_div_k,
                    # then we have potential good pairs.
                    if freq1_div_k[multiple] > 0:
                        # The number of good pairs formed by this (d, multiple) combination
                        # is the product of their frequencies.
                        total_good_pairs += freq2_arr[d] * freq1_div_k[multiple]
        
        return total_good_pairs
