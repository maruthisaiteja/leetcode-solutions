# Title: Apply Operations to Maximize Frequency Score
# URL: https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/
# Difficulty: Hard

class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        nums.sort()  # Sort the array to easily find subarrays and medians
        n = len(nums)

        # Calculate prefix sums for efficient range sum queries
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        # Helper function to get sum of elements in nums[start...end-1]
        def get_range_sum(start: int, end: int) -> int:
            return prefix_sum[end] - prefix_sum[start]

        # check(m) returns True if it's possible to achieve a frequency of 'm'
        # with at most 'k' operations, False otherwise.
        def check(m: int) -> bool:
            # Iterate through all possible windows of length 'm'
            for left in range(n - m + 1):
                right = left + m - 1
                
                # The target value for all elements in the window is the median.
                # In a sorted array, the median index for a window [left...right]
                # is left + m // 2.
                idx_median = left + m // 2
                target_value = nums[idx_median]

                # Calculate the cost for elements to the left of the median (exclusive of median itself).
                # These elements are nums[left ... idx_median-1].
                # Number of elements: (idx_median - left).
                # Total sum required if all were target_value: (idx_median - left) * target_value.
                # Current sum: get_range_sum(left, idx_median).
                # Cost: (sum_required - current_sum).
                cost_left = (idx_median - left) * target_value - get_range_sum(left, idx_median)

                # Calculate the cost for elements to the right of the median (exclusive of median itself).
                # These elements are nums[idx_median+1 ... right].
                # Number of elements: (right - idx_median).
                # Total sum required if all were target_value: (right - idx_median) * target_value.
                # Current sum: get_range_sum(idx_median + 1, right + 1).
                # Cost: (current_sum - sum_required).
                cost_right = get_range_sum(idx_median + 1, right + 1) - (right - idx_median) * target_value

                total_cost = cost_left + cost_right

                if total_cost <= k:
                    return True  # Found a window of length 'm' that satisfies the condition
            return False         # No window of length 'm' satisfies the condition

        # Binary search for the maximum possible frequency 'm'
        ans = 1  # A frequency of 1 is always possible (cost is 0 for any single element)
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid       # 'mid' is achievable, try for a larger frequency
                low = mid + 1
            else:
                high = mid - 1  # 'mid' is not achievable, try for a smaller frequency
        
        return ans
