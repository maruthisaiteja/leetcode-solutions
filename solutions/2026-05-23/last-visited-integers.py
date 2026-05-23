# Title: Last Visited Integers
# URL: https://leetcode.com/problems/last-visited-integers/
# Difficulty: Easy

class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k_consecutive_neg_ones = 0

        for num in nums:
            if num != -1:
                # If a positive integer is encountered, prepend it to the front of seen.
                # Using insert(0, num) for prepending.
                seen.insert(0, num)
                # Reset the consecutive -1 counter
                k_consecutive_neg_ones = 0
            else:
                # If -1 is encountered, increment k_consecutive_neg_ones
                k_consecutive_neg_ones += 1
                
                # Let k be the number of consecutive -1s seen so far
                k = k_consecutive_neg_ones

                # If k is less than or equal to the length of seen
                if k <= len(seen):
                    # Append the k-th element of seen to ans.
                    # Since seen is prepended, the k-th element (1-indexed)
                    # corresponds to index k-1 (0-indexed).
                    ans.append(seen[k-1])
                else:
                    # If k is strictly greater than the length of seen, append -1 to ans.
                    ans.append(-1)
        
        return ans
