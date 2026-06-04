# Title: Total Waviness of Numbers in Range I
# URL: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# Difficulty: Medium

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness_sum = 0

        for num in range(num1, num2 + 1):
            s_num = str(num)
            n = len(s_num)

            # Numbers with fewer than 3 digits have a waviness of 0.
            if n < 3:
                continue

            current_num_waviness = 0
            # Iterate through digits that can be peaks or valleys.
            # These are digits from index 1 to n-2 (inclusive),
            # as the first and last digits cannot be peaks or valleys.
            for i in range(1, n - 1):
                d_left = int(s_num[i - 1])
                d_current = int(s_num[i])
                d_right = int(s_num[i + 1])

                # Check for peak: strictly greater than both neighbors
                if d_current > d_left and d_current > d_right:
                    current_num_waviness += 1
                # Check for valley: strictly less than both neighbors
                elif d_current < d_left and d_current < d_right:
                    current_num_waviness += 1
            
            total_waviness_sum += current_num_waviness
            
        return total_waviness_sum
