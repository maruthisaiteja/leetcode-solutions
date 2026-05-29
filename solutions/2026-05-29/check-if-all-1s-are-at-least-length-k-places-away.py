# Title: Check If All 1's Are at Least Length K Places Away
# URL: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Difficulty: Easy

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one_idx = -1 # Initialize to -1, indicating no '1' has been seen yet.
                          # This value ensures that the first '1' encountered
                          # will not trigger the distance check.

        for i in range(len(nums)):
            if nums[i] == 1:
                # If a '1' is found and it's not the very first '1' in the array
                # (i.e., last_one_idx has been updated from its initial -1)
                if last_one_idx != -1:
                    # Calculate the number of elements (zeros) between the current '1'
                    # at index 'i' and the last '1' found at 'last_one_idx'.
                    # The number of zeros is (i - last_one_idx - 1).
                    if (i - last_one_idx - 1) < k:
                        # If the count of zeros is less than k, the condition is violated.
                        return False
                
                # Update last_one_idx to the current index of the '1'
                # for subsequent distance calculations.
                last_one_idx = i
        
        # If the loop completes, it means all '1's satisfied the condition.
        # This also covers cases with 0 or 1 '1's, as no 'False' was returned.
        return True
