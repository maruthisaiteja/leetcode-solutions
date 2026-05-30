# Title: Maximum Good Subarray Sum
# URL: https://leetcode.com/problems/maximum-good-subarray-sum/
# Difficulty: Medium

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_subarray_sum = -float('inf')  # Initialize with negative infinity to handle potentially negative sums
        
        # P_j represents prefix_sums[j] (sum of nums[0]...nums[j-1])
        # P_j starts at 0, representing prefix_sums[0] (empty sum)
        P_j = 0 
        
        # min_prefix_sum_for_val stores a mapping:
        # value -> minimum prefix_sums[idx] such that nums[idx] == value
        # This helps find the smallest P[i] for a given nums[i] = target
        min_prefix_sum_for_val = {}
        
        for j in range(len(nums)):
            current_val = nums[j]
            
            # P_j_plus_1 is prefix_sums[j+1] (sum of nums[0]...nums[j])
            # This is the prefix sum *including* the current element nums[j]
            P_j_plus_1 = P_j + current_val
            
            # Check for two conditions for nums[i] to satisfy |nums[i] - nums[j]| == k
            # Condition 1: nums[i] == nums[j] + k
            target1 = current_val + k
            if target1 in min_prefix_sum_for_val:
                # We found a potential start element nums[i] (where i < j)
                # with nums[i] == target1.
                # To maximize sum(nums[i...j]) = P[j+1] - P[i], we need to minimize P[i].
                min_P_i = min_prefix_sum_for_val[target1]
                current_good_subarray_sum = P_j_plus_1 - min_P_i
                max_subarray_sum = max(max_subarray_sum, current_good_subarray_sum)
            
            # Condition 2: nums[i] == nums[j] - k
            target2 = current_val - k
            if target2 in min_prefix_sum_for_val:
                # Similar logic for target2
                min_P_i = min_prefix_sum_for_val[target2]
                current_good_subarray_sum = P_j_plus_1 - min_P_i
                max_subarray_sum = max(max_subarray_sum, current_good_subarray_sum)
            
            # Update min_prefix_sum_for_val for the current element nums[j]
            # P_j (which is prefix_sums[j]) is the prefix sum up to nums[j-1].
            # This P_j acts as prefix_sums[i] if current_val (nums[j]) were to be nums[i]
            # in a future subarray (where k is the end index).
            if current_val not in min_prefix_sum_for_val or P_j < min_prefix_sum_for_val[current_val]:
                min_prefix_sum_for_val[current_val] = P_j
            
            # Move P_j to the next prefix sum for the next iteration
            # P_j now holds prefix_sums[j+1]
            P_j = P_j_plus_1
            
        # If max_subarray_sum is still negative infinity, it means no good subarrays were found.
        # In that case, return 0 as per problem statement.
        if max_subarray_sum == -float('inf'):
            return 0
        else:
            return int(max_subarray_sum) # Cast to int as sums will be integer values
