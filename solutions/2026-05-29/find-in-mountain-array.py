# Title: Find in Mountain Array
# URL: https://leetcode.com/problems/find-in-mountain-array/
# Difficulty: Hard

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # Step 1: Find the peak index of the mountain array
        # The peak is the largest element, where the array transitions from increasing to decreasing.
        # It's guaranteed that 0 < peak_idx < n - 1.
        low, high = 0, n - 1
        while low < high:
            mid = low + (high - low) // 2
            # If arr[mid] < arr[mid+1], we are on the ascending slope, so the peak is to the right.
            # We set low = mid + 1 to continue search in the right half.
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            # If arr[mid] > arr[mid+1], we are on the descending slope, so the peak is at or to the left of mid.
            # We set high = mid to continue search in the left half (including mid).
            else:
                high = mid
        peak_idx = low # When the loop terminates, low == high, which is the peak index.

        # Step 2: Binary search on the increasing part (from index 0 to peak_idx)
        # This is a standard binary search for an increasing array.
        def binary_search_increasing(start, end, target_val):
            l, r = start, end
            while l <= r:
                mid = l + (r - l) // 2
                mid_val = mountainArr.get(mid)
                if mid_val == target_val:
                    return mid
                elif mid_val < target_val:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        result_inc = binary_search_increasing(0, peak_idx, target)
        if result_inc != -1:
            return result_inc

        # Step 3: Binary search on the decreasing part (from peak_idx + 1 to n - 1)
        # This is a modified binary search for a decreasing array.
        def binary_search_decreasing(start, end, target_val):
            l, r = start, end
            while l <= r:
                mid = l + (r - l) // 2
                mid_val = mountainArr.get(mid)
                if mid_val == target_val:
                    return mid
                # If mid_val < target_val in a decreasing array, it means target_val
                # must be to the left (where values are larger).
                elif mid_val < target_val:
                    r = mid - 1
                # If mid_val > target_val in a decreasing array, it means target_val
                # must be to the right (where values are smaller).
                else:
                    l = mid + 1
            return -1
        
        result_dec = binary_search_decreasing(peak_idx + 1, n - 1, target)
        return result_dec
