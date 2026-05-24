# Title: Maximum Total Damage With Spell Casting
# URL: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
# Difficulty: Medium

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        import collections
        import bisect

        # Step 1: Aggregate damage for each distinct spell power.
        # Use collections.Counter to count occurrences of each power value.
        counts = collections.Counter(power)
        
        # Create a dictionary to store the total damage if all spells of a certain power are cast.
        # For example, if power = [1,1,3,4], counts = {1:2, 3:1, 4:1}.
        # total_damages = {1: 1*2, 3: 3*1, 4: 4*1} => {1:2, 3:3, 4:4}.
        total_damages = {p: p * count for p, count in counts.items()}

        # Step 2: Get a sorted list of unique spell powers.
        # This allows us to process spells in increasing order of damage.
        unique_powers = sorted(total_damages.keys())
        n = len(unique_powers)

        # Handle edge cases for small number of unique spell powers.
        if n == 0:
            return 0
        if n == 1:
            return total_damages[unique_powers[0]]

        # Step 3: Initialize DP array.
        # dp[i] will store the maximum total damage considering spells
        # from unique_powers[0] up to unique_powers[i].
        dp = [0] * n

        # Base case: For the first unique spell power, we can only take it.
        dp[0] = total_damages[unique_powers[0]]

        # Iterate through the unique spell powers to fill the DP array.
        for i in range(1, n):
            current_p = unique_powers[i]
            
            # Option 1: Do not cast spells with damage 'current_p'.
            # The maximum damage in this case is simply the maximum damage
            # obtained from considering spells up to unique_powers[i-1].
            damage_if_not_taken = dp[i-1]

            # Option 2: Cast spells with damage 'current_p'.
            # If we cast 'current_p', we gain total_damages[current_p].
            # However, we cannot cast spells with damage current_p-2 or current_p-1.
            # So, we need to find the maximum damage that can be obtained from
            # spells with values strictly less than (current_p - 2).
            
            # The value we are searching for is current_p - 2. We want elements strictly less than it.
            # bisect_left finds the insertion point for 'search_value_for_prev'.
            # All elements before this index are strictly less than 'search_value_for_prev'.
            search_value_for_prev = current_p - 2
            
            # 'idx' is the index where 'search_value_for_prev' could be inserted
            # to maintain sorted order. Effectively, unique_powers[idx] is the first
            # element >= search_value_for_prev.
            idx = bisect.bisect_left(unique_powers, search_value_for_prev)
            
            damage_from_prev_non_forbidden = 0
            if idx > 0:
                # If idx > 0, it means unique_powers[idx-1] is the largest element
                # in unique_powers that is strictly less than search_value_for_prev.
                # So, dp[idx-1] gives the maximum damage accumulated considering
                # all spells up to unique_powers[idx-1].
                damage_from_prev_non_forbidden = dp[idx - 1]
            
            # Total damage if we cast 'current_p' and the allowed previous spells.
            damage_if_taken = total_damages[current_p] + damage_from_prev_non_forbidden

            # The maximum damage at this step is the greater of the two options.
            dp[i] = max(damage_if_not_taken, damage_if_taken)

        # The final answer is the maximum damage considering all unique spell powers.
        return dp[n-1]
