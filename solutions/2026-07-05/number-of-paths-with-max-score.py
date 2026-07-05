# Title: Number of Paths with Max Score
# URL: https://leetcode.com/problems/number-of-paths-with-max-score/
# Difficulty: Hard

from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        N = len(board)
        MOD = 10**9 + 7

        dp = [[[-1, 0] for _ in range(N)] for _ in range(N)]

        dp[N-1][N-1] = [0, 1]

        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if board[r][c] == 'X' or (r == N - 1 and c == N - 1):
                    continue
                
                candidates = []

                if r + 1 < N:
                    prev_score, prev_count = dp[r+1][c]
                    if prev_score != -1:
                        candidates.append((prev_score, prev_count))
                
                if c + 1 < N:
                    prev_score, prev_count = dp[r][c+1]
                    if prev_score != -1:
                        candidates.append((prev_score, prev_count))

                if r + 1 < N and c + 1 < N:
                    prev_score, prev_count = dp[r+1][c+1]
                    if prev_score != -1:
                        candidates.append((prev_score, prev_count))
                
                if not candidates:
                    continue
                
                max_prev_score = -1
                for score, _ in candidates:
                    max_prev_score = max(max_prev_score, score)
                
                current_paths_count = 0
                for score, count in candidates:
                    if score == max_prev_score:
                        current_paths_count = (current_paths_count + count) % MOD
                
                cell_value = 0
                if board[r][c].isdigit():
                    cell_value = int(board[r][c])
                
                dp[r][c] = [max_prev_score + cell_value, current_paths_count]
        
        final_score, final_paths = dp[0][0]

        if final_score == -1:
            return [0, 0]
        else:
            return [final_score, final_paths]
