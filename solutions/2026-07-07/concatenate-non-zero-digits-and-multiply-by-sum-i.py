# Title: Concatenate Non-Zero Digits and Multiply by Sum I
# URL: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Difficulty: Easy

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s_n = str(n)
        
        non_zero_digits_list = []
        for digit_char in s_n:
            if digit_char != '0':
                non_zero_digits_list.append(digit_char)
        
        x = 0
        if non_zero_digits_list:
            x_str = "".join(non_zero_digits_list)
            x = int(x_str)
            
        sum_of_digits_in_x = 0
        s_x = str(x)
        for digit_char_x in s_x:
            sum_of_digits_in_x += int(digit_char_x)
            
        return x * sum_of_digits_in_x
