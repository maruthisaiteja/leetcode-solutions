# Title: Find the Median of the Uniqueness Array
# URL: https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/
# Difficulty: Hard

import collections
from typing import List

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        total_subarrays = n * (n + 1) // 2
        
        target_k = (total_subarrays - 1) // 2 + 1
        
        def count_subarrays_le_distinct(max_distinct: int) -> int:
            count = 0
            left = 0
            
            freq = collections.defaultdict(int)
            current_distinct = 0
            
            for right in range(n):
                if freq[nums[right]] == 0:
                    current_distinct += 1
                freq[nums[right]] += 1
                
                while current_distinct > max_distinct:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        current_distinct -= 1
                    left += 1
                
                count += (right - left + 1)
            
            return count

        low = 1
        high = n
        ans = n
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if count_subarrays_le_distinct(mid) >= target_k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
