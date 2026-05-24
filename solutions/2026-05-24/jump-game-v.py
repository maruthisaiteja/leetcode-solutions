# Title: Jump Game V
# URL: https://leetcode.com/problems/jump-game-v/
# Difficulty: Hard

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        
        dp = [1] * n
        
        indexed_arr = []
        for i in range(n):
            indexed_arr.append((arr[i], i))
        
        indexed_arr.sort() 
        
        for _, i in indexed_arr:
            # Check jumps to the right (i + x)
            for x in range(1, d + 1):
                j = i + x
                if j >= n: 
                    break
                
                if arr[i] <= arr[j]:
                    break
                
                dp[i] = max(dp[i], 1 + dp[j])
            
            # Check jumps to the left (i - x)
            for x in range(1, d + 1):
                j = i - x
                if j < 0: 
                    break
                
                if arr[i] <= arr[j]:
                    break
                
                dp[i] = max(dp[i], 1 + dp[j])
                
        return max(dp)
