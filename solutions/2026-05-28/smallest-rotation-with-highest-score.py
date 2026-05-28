# Title: Smallest Rotation with Highest Score
# URL: https://leetcode.com/problems/smallest-rotation-with-highest-score/
# Difficulty: Hard

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        
        # `change[k]` will store the net change in score when transitioning
        # from rotation `k-1` to rotation `k`.
        # `score[k] = score[k-1] + change[k]`
        # For k=0, `change[0]` is conceptually the initial score, though we calculate it separately.
        change = [0] * n
        
        # Calculate the initial score for k=0
        current_score = 0
        for i in range(n):
            if nums[i] <= i:
                current_score += 1
        
        # Iterate through each original element `nums[i]` to determine its score contributions
        # across all rotations and update the `change` array.
        for i in range(n):
            val = nums[i]
            
            # 1. Point Loss:
            # An element `nums[i]` (originally at index `i`) contributes a point if its
            # current index `j` satisfies `val <= j`.
            # A point is lost when `j` drops below `val`. This happens when `j` was `val`
            # and then shifts to `val - 1`.
            # The rotation `k_at_val` where `nums[i]` is at index `val` is:
            # `(i - k_at_val + n) % n = val`  => `k_at_val = (i - val + n) % n`
            # At the next rotation, `k_next_loss = (k_at_val + 1) % n`, `nums[i]` will be at index `val - 1`.
            # So, for rotation `k_next_loss`, `nums[i]` stops contributing (if it was).
            # This causes a score decrease of 1 at `k_next_loss`.
            k_at_val = (i - val + n) % n
            k_next_loss = (k_at_val + 1) % n
            change[k_next_loss] -= 1
            
            # 2. Point Gain (due to wrap-around):
            # When an element `nums[i]` rotates from index `0` (which happens at rotation `k=i`)
            # to index `n-1` (which happens at rotation `k=i+1`), it potentially gains a point.
            # At `k=i`, `nums[i]` is at index `0`. It contributes if `val <= 0`.
            # At `k=i+1`, `nums[i]` is at index `n-1`. It contributes if `val <= n-1` (always true since `val < n`).
            # If `val > 0`, it did not contribute at `k=i` but will contribute at `k=i+1`. So it gains a point.
            # If `val == 0`, it contributed at `k=i` and also at `k=i+1`, so no net change here.
            # The `change` values added below effectively handle both cases:
            #   For `val == 0`: `k_next_loss` will be `(i - 0 + 1 + n) % n = (i + 1) % n`.
            #                   `k_for_wrap_around` will also be `(i + 1) % n`.
            #                   So `change[(i+1)%n]` gets `-1` and then `+1`, resulting in `0` net change for `nums[i] = 0`.
            #                   This correctly reflects that `nums[i]=0` always contributes a point regardless of rotation.
            # For this reason, we simply always apply the +1 at `k_for_wrap_around`.
            k_for_wrap_around = (i + 1) % n
            change[k_for_wrap_around] += 1

        # Now, `current_score` holds the score for `k=0`.
        # We find the maximum score by iterating `k` from 1 to `n-1`, updating the score using `change` array.
        max_score = current_score
        best_k = 0
        
        for k in range(1, n):
            current_score += change[k]
            if current_score > max_score:
                max_score = current_score
                best_k = k
            # If `current_score == max_score`, we keep the smallest `best_k`,
            # so no action is needed here.
        
        return best_k
