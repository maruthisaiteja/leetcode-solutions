# Title: Maximum Median Sum of Subsequences of Size 3
# URL: https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/
# Difficulty: Medium

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        # k is the number of triplets, which is n // 3
        k = n // 3
        
        total_median_sum = 0
        
        # The strategy is to select the medians from specific indices
        # after sorting the array.
        # Let the sorted array be a_0, a_1, ..., a_{n-1}.
        # We need to choose k medians.
        #
        # For each triplet (x, m, y) where x <= m <= y, m is the median.
        # To maximize the sum of medians, we want to choose the largest possible elements
        # as medians, while still satisfying the median property.
        #
        # If we have 3k elements, a_0, ..., a_{3k-1}.
        # We need to form k triplets.
        # Consider the elements from the end of the array.
        # The largest k elements are a_{2k}, a_{2k+1}, ..., a_{3k-1}.
        # If we try to use these as medians, it might not be possible to form valid triplets.
        #
        # A common observation for maximizing medians is to pick from specific positions.
        # If we pick a median M, we need two elements X and Y such that X <= M <= Y.
        # To maximize M, we should pick the smallest possible X.
        #
        # Consider the elements from the largest possible indices for the medians.
        #
        # A well-known greedy strategy for this problem type is to select medians
        # from elements that are "in the middle" after some initial elements are used.
        #
        # Let's consider the elements from the end of the array, moving backwards.
        # We need to pick k elements that will serve as medians.
        # To maximize their sum, we should pick the largest k elements possible that can be medians.
        #
        # The elements nums[0], ..., nums[k-1] must serve as the smallest elements (x_j)
        # in some triplets.
        # The elements nums[k], ..., nums[n-1] are available for medians (m_j) and largest elements (y_j).
        #
        # For each triplet (x_j, m_j, y_j), we need x_j <= m_j <= y_j.
        #
        # The optimal strategy is to pick the medians as:
        # nums[k], nums[k+2], nums[k+4], ..., nums[n-2] (if n is 3k)
        # Or more generally, the elements at indices where the smallest k elements
        # have already been "skipped" and we are picking from the "middle" and later elements.
        #
        # For each triplet, we select the median from an element such that there are at least
        # 'j' smaller elements to its left (which will be x_j's) and 'j' larger elements to its right
        # (which will be y_j's).
        #
        # A simpler way to think about this:
        # We need to pick k medians. For each median, we need a smaller element and a larger element.
        # To maximize the medians, we want to choose elements that are as large as possible.
        #
        # Consider the sorted array `nums`.
        # The indices of elements that can be medians are `k` and greater.
        # The indices of elements that must be the smallest in a triplet are `0` to `k-1`.
        #
        # The elements `nums[k]`, `nums[k+1]`, `nums[k+2]`, ..., `nums[n-1]`
        # are candidates for medians and largest elements.
        #
        # The specific pattern of picking medians from `nums[k]`, `nums[k+2]`, ..., `nums[n-2]`
        # is often seen in problems where you pick k items in groups of 3.
        #
        # Let's trace it for n = 6, k = 2.
        # nums = [a0, a1, a2, a3, a4, a5]
        # k = 2.
        # We pick medians at indices k, k+2, ..., n-2
        # indices: 2, 2+2=4.
        # Medians are a2, a4. Total sum = a2 + a4.
        # Triplets: (a0, a2, a3), (a1, a4, a5).
        # This is valid: a0 <= a2 <= a3, a1 <= a4 <= a5.
        # All elements used.
        #
        # Let's trace it for n = 9, k = 3.
        # nums = [a0, a1, a2, a3, a4, a5, a6, a7, a8]
        # k = 3.
        # We pick medians at indices k, k+2, k+4, ..., n-2
        # indices: 3, 3+2=5, 3+4=7.
        # Medians are a3, a5, a7. Total sum = a3 + a5 + a7.
        # Triplets: (a0, a3, a4), (a1, a5, a6), (a2, a7, a8).
        # This is valid: a0<=a3<=a4, a1<=a5<=a6, a2<=a7<=a8. All elements used.
        #
        # So the loop should iterate k times.
        # In each iteration `j` from `0` to `k-1`, the median is at index `k + 2*j`.
        
        for j in range(k):
            # The current median candidate is at index (n // 3) + 2 * j
            # which is k + 2 * j
            total_median_sum += nums[k + 2 * j]
            
        return total_median_sum
