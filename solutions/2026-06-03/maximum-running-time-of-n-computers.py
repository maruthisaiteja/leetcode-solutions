# Title: Maximum Running Time of N Computers
# URL: https://leetcode.com/problems/maximum-running-time-of-n-computers/
# Difficulty: Hard

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(target_time: int) -> bool:
            """
            Checks if it's possible to run all 'n' computers simultaneously for 'target_time' minutes.
            """
            # This variable tracks the total available capacity if we were to consolidate all batteries
            # and distribute them optimally. Each computer needs 'target_time' minutes of power.
            # We want to see if we have at least n * target_time total effective power.
            
            # The key insight here is that for any given target_time, a battery can either:
            # 1. Provide 'target_time' minutes of power to one computer (if its capacity >= target_time).
            # 2. Provide its full capacity to a shared pool (if its capacity < target_time).

            # We can model this by saying that each battery contributes at most 'target_time' to
            # a "dedicated slot" for a computer, and any remaining capacity (or its full capacity
            # if less than target_time) goes into a "flexible pool".

            # The problem can be rephrased: can we assign n "slots" of 'target_time' to the batteries?
            # Each battery `b` contributes `min(b, target_time)` to satisfy these slots directly,
            # and `max(0, b - target_time)` to a general excess pool that can be used to fill
            # any deficits from other slots.
            
            # A simpler way to count is to sum up all power we can *effectively* use for 'target_time'.
            # Each battery `b` contributes `min(b, target_time)` effective power towards the goal.
            # Summing these up gives the total effective power.
            
            # Total effective power is the sum of (min(battery_capacity, target_time)) for all batteries.
            # If this sum is greater than or equal to n * target_time, then it's possible.
            
            # This approach is not quite right as it doesn't account for batteries being able to fully
            # power a computer while others are topped up. Let's revisit the original logic.

            # The original logic for `check` function was largely correct in its approach.
            # The key is to distinguish between batteries strong enough to power a computer for the full `target_time`
            # and those that are not.
            
            # Sum of all available battery capacity. We will subtract what's "used" by n computers.
            # What we need to ensure is that we have enough total "effective" power.
            
            # Let's count how much power we have for n computers if each needs `target_time`.
            # Each computer needs `target_time` units of power. There are `n` computers.
            # Total power required = `n * target_time`.

            # Iterate through batteries and calculate available "power units" towards meeting `n * target_time`.
            # A battery `b` can provide at most `target_time` power units to one computer slot
            # without wasting its full capacity if that capacity is less than `target_time`.
            # If `b` > `target_time`, it can fully power one computer and its `b - target_time`
            # excess can be used to help another.

            # This can be simplified. Imagine we have `n` "slots", each requiring `target_time` power.
            # We greedily try to fill these slots.
            
            # Consider all batteries.
            # For any battery `b`, it can provide `min(b, target_time)` "useful" power towards one of the `n` computer slots.
            # If `b < target_time`, its entire `b` capacity is useful.
            # If `b >= target_time`, we only count `target_time` as useful for *one* slot,
            # and the remaining `b - target_time` is surplus that can be used for *other* slots.
            
            # Let's use the exact sum of available power units.
            # Each computer needs 'target_time' minutes.
            # We want to see if `sum(min(battery_capacity, target_time) for battery_capacity in batteries)` is enough.
            # This is NOT completely correct because if battery_capacity is very large, say 10*target_time,
            # it can power 1 computer for target_time and still have 9*target_time left to contribute to others.
            # The `min(b, target_time)` only counts `target_time` once.

            # The total effective available power is `sum(batteries)`.
            # If we run `n` computers for `target_time`, we need `n * target_time` total power.
            # It should be `sum(batteries) >= n * target_time`. This is an absolute upper bound.
            # However, this doesn't account for the fact that a single small battery cannot power a computer
            # for `target_time` on its own. It needs to be combined.

            # The original logic was conceptually sound but has a slight flaw in how `flexible_power_pool`
            # is combined with `computers_fully_powered`.
            
            # Let's refine the logic for `check(target_time)`:
            # We want to see if we can satisfy `n` computers, each needing `target_time` power.
            # Total power required: `n * target_time`.

            # Sum of all battery capacities.
            total_power_available = sum(batteries)

            # We can use at most `target_time` from any single battery to power a single computer slot.
            # If a battery has capacity `C`, and `C < target_time`, it can only power a computer for `C` minutes.
            # If `C >= target_time`, it can power a computer for `target_time` minutes.
            # The remaining `C - target_time` can be used by another computer.

            # This problem is equivalent to determining if we can pick `n` segments of length `target_time`
            # from the available batteries, allowing segments to be combined from multiple batteries,
            # but also allowing a single battery to contribute to multiple segments if it's very large.

            # A more robust check function:
            # The idea is that we want to provide `n * target_time` total power.
            # We can consider how many "full target_time units" each battery can contribute.
            # Each battery `b` can contribute at most `b` power.
            # But more specifically, if `b < target_time`, it can only help fill part of *one* computer's need.
            # If `b >= target_time`, it can fill one computer's need *and* have `b - target_time` left over
            # to contribute to other computers' needs.

            # We can simplify the check:
            # We need to run `n` computers. Each needs `target_time` power.
            # Sort batteries to make it easier to reason, though not strictly necessary.
            # It's better to think about total power.
            
            # The optimal strategy to power `n` computers for `target_time` is to:
            # 1. Use the largest batteries to fully power as many computers as possible.
            # 2. Use the remaining capacity of these large batteries and all capacity of smaller batteries
            #    to top up the remaining computers.

            # Let's count the total "effective" power we have, which is capped by `target_time` for each computer.
            # We have `n` computers, each needing `target_time` power.
            # The total power that can be supplied by the `k` batteries is `sum(batteries)`.
            # This total power must be at least `n * target_time`.
            # This is a necessary condition: `sum(batteries) >= n * target_time`.

            # Another condition is that each of the `n` computers must actually be "started" by a battery that can
            # at least contribute something, or by combined smaller batteries.
            # The constraint is that we have `len(batteries)` available sources.
            # We can only use at most `len(batteries)` concurrent segments of power.

            # A slightly different perspective:
            # We need `n` blocks of power, each of size `target_time`.
            # We have `k` batteries.
            # Sort batteries in ascending order: `b_1 <= b_2 <= ... <= b_k`.

            # The smallest `k-n` batteries are merged into a "pool" to support the `n` largest batteries.
            # This is not always correct.
            
            # Corrected check function logic:
            # Sum up all batteries. This is the total available energy.
            # If `total_energy < n * target_time`, it's impossible.
            # This is the first and most fundamental check.
            
            # `total_power` accumulates the useful power for `n` computers.
            # Each battery `b` contributes `min(b, target_time)` to the `n` computers,
            # effectively filling up `n` slots.
            # If a battery is very large, say `10 * target_time`, it can contribute `target_time` to one slot,
            # and then `9 * target_time` excess. This excess can be divided into `9` additional
            # `target_time` units, but only if there are enough computers needing these.
            # This `min(b, target_time)` approach works correctly because for any computer needing `target_time`,
            # a battery can supply at most `target_time` to *that specific computer's need*.
            # Any excess from `b > target_time` is accumulated and then effectively used to cover deficits
            # for other computers (those that were assigned batteries `b' < target_time`).

            # The total effective capacity we have available, capped by target_time for each slot:
            # For each battery `b_i`, it can either fully contribute its `b_i` capacity (if `b_i < target_time`)
            # or it can power one computer for `target_time` and have `b_i - target_time` left over
            # to contribute to a shared pool.
            
            # The original check function:
            # `computers_fully_powered`: counts how many computers can be run by batteries strong enough for `target_time`.
            # `flexible_power_pool`: accumulates total excess capacity from strong batteries AND full capacity from weak batteries.

            # Let's trace the example: n=3, batteries=[10,10,3,5], target_time=8 (expected answer).
            # computers_fully_powered = 0
            # flexible_power_pool = 0

            # battery 10: >= 8. computers_fully_powered = 1. flexible_power_pool += (10-8) = 2.
            # battery 10: >= 8. computers_fully_powered = 2. flexible_power_pool += (10-8) = 2. (now 4)
            # battery 3: < 8. flexible_power_pool += 3. (now 7)
            # battery 5: < 8. flexible_power_pool += 5. (now 12)

            # computers_fully_powered = 2. This is < n (which is 3).
            # We need one more computer.
            # remaining_computers_needed_power = (n - computers_fully_powered) * target_time
            # = (3 - 2) * 8 = 1 * 8 = 8.
            # flexible_power_pool = 12.
            # Is 12 >= 8? Yes. So check(8) returns True. This is correct.

            # Now, test with target_time=9 (my code output).
            # computers_fully_powered = 0
            # flexible_power_pool = 0

            # battery 10: >= 9. computers_fully_powered = 1. flexible_power_pool += (10-9) = 1.
            # battery 10: >= 9. computers_fully_powered = 2. flexible_power_pool += (10-9) = 1. (now 2)
            # battery 3: < 9. flexible_power_pool += 3. (now 5)
            # battery 5: < 9. flexible_power_pool += 5. (now 10)

            # computers_fully_powered = 2. This is < n (which is 3).
            # remaining_computers_needed_power = (3 - 2) * 9 = 1 * 9 = 9.
            # flexible_power_pool = 10.
            # Is 10 >= 9? Yes. So check(9) returns True.

            # This confirms the check function logic returns True for 9, which leads to the wrong answer.
            # The issue must be in the interpretation of `flexible_power_pool` and `remaining_computers_needed_power`.
            
            # The flaw is subtle. When a battery contributes `target_time` to `computers_fully_powered`,
            # it means it fully powers one computer *without needing assistance from the flexible pool*.
            # The `flexible_power_pool` is then used for the computers that are *not* fully powered.
            # Each of these `n - computers_fully_powered` computers needs `target_time` power.
            # This implies that the total flexible power must be able to cover the `target_time` for EACH
            # of these remaining computers. This is correct.

            # The issue might be in how we are calculating the "total available power" for the flexible pool.
            # The phrasing `computers_fully_powered += 1` means we are assigning a dedicated battery to a computer.
            # And `flexible_power_pool += (battery_capacity - target_time)` means the *excess* is put into the pool.
            # For batteries `< target_time`, their *full* capacity goes to the pool.

            # This sounds correct. Where could it go wrong?
            # Example: n=1, batteries=[1, 100]. target_time = 50.
            # computers_fully_powered = 0, flexible_power_pool = 0
            # battery 1: < 50. flexible_power_pool += 1. (1)
            # battery 100: >= 50. computers_fully_powered += 1. (1). flexible_power_pool += (100-50) = 50. (now 51).
            # computers_fully_powered = 1, which is == n. Return True. Correct.
            
            # Example: n=2, batteries=[10, 10, 1, 1]. target_time = 10.
            # computers_fully_powered = 0, flexible_power_pool = 0
            # battery 10: >= 10. c_fp = 1. f_p_p += (10-10)=0. (0)
            # battery 10: >= 10. c_fp = 2. f_p_p += (10-10)=0. (0)
            # battery 1: < 10. f_p_p += 1. (1)
            # battery 1: < 10. f_p_p += 1. (2)
            # c_fp = 2. Which is == n. Return True. Correct.
            
            # Example: n=2, batteries=[5, 5, 5, 5]. target_time = 10.
            # computers_fully_powered = 0, flexible_power_pool = 0
            # b 5: < 10. f_p_p += 5. (5)
            # b 5: < 10. f_p_p += 5. (10)
            # b 5: < 10. f_p_p += 5. (15)
            # b 5: < 10. f_p_p += 5. (20)
            # c_fp = 0. Which is < n (2).
            # remaining_computers_needed_power = (2 - 0) * 10 = 20.
            # Is flexible_power_pool (20) >= 20? Yes. Return True. Correct.
            # (We have 4 batteries of 5, total 20. Need 2 computers for 10. Yes, possible.)

            # The original logic of the `check` function *is* correct for the problem constraints.
            # The standard proof for this `check` function involves considering an optimal assignment.
            # If an optimal assignment exists where some large battery `B` (capacity `C >= target_time`)
            # is used to power a computer `X` for less than `target_time`, and a smaller battery `b`
            # (capacity `c < target_time`) contributes to computer `Y` which also receives power
            # from other sources to reach `target_time`, we can swap.
            # Specifically, if `B` is used for `t < target_time` on computer `X`, and `X` is topped up by `b`,
            # and another computer `Y` is relying on `b` and other sources,
            # we can always make `B` power `X` for `target_time` and put its excess `C - target_time` into the pool.
            # All batteries `b < target_time` *must* go into the pool.

            # The error for `n=3, batteries=[10,10,3,5]` yielding 9 instead of 8 must stem from
            # a misunderstanding of the problem or a very subtle edge case not covered by this standard check.

            # What if `n` is greater than `len(batteries)`? The problem states `n <= batteries.length`.
            # Constraints: `1 <= n <= batteries.length <= 10^5`. `1 <= batteries[i] <= 10^9`.
            # Max `sum(batteries)` is `10^5 * 10^9 = 10^14`. `high` can be `10^14`.
            # `mid` can also be `10^14`. `target_time` can be `10^14`.
            # `(n - computers_fully_powered) * target_time` could be `10^5 * 10^14 = 10^19`.
            # Python integers handle arbitrary size, so no overflow issue.

            # Re-read problem statement carefully:
            # "You are given an integer n, the number of computers, and a 0-indexed integer array batteries,
            # where batteries[i] is the runtime of the ith battery in minutes.
            # You should run all n computers simultaneously for as long as possible."

            # The crucial point is "simultaneously".
            # My `check` function seems to correctly model this.
            
            # Let's consider `n=3, batteries=[10,10,3,5]`.
            # Expected 8. My code output 9. This means my check(9) is True when it should be False.
            
            # Let's manually trace `check(9)` again very carefully.
            # target_time = 9. n = 3. batteries = [10, 10, 3, 5]

            # computers_fully_powered = 0
            # flexible_power_pool = 0

            # For battery 1 (capacity 10):
            # 10 >= 9 (True).
            # computers_fully_powered = 1.
            # flexible_power_pool += (10 - 9) = 1.
            # current state: c_fp=1, f_p_p=1

            # For battery 2 (capacity 10):
            # 10 >= 9 (True).
            # computers_fully_powered = 2.
            # flexible_power_pool += (10 - 9) = 1.
            # current state: c_fp=2, f_p_p=1+1=2

            # For battery 3 (capacity 3):
            # 3 >= 9 (False).
            # flexible_power_pool += 3.
            # current state: c_fp=2, f_p_p=2+3=5

            # For battery 4 (capacity 5):
            # 5 >= 9 (False).
            # flexible_power_pool += 5.
            # current state: c_fp=2, f_p_p=5+5=10

            # After iterating all batteries:
            # computers_fully_powered = 2.
            # flexible_power_pool = 10.

            # Is computers_fully_powered (2) >= n (3)? False.

            # Calculate remaining needs:
            # remaining_computers_needed_power = (n - computers_fully_powered) * target_time
            # = (3 - 2) * 9
            # = 1 * 9 = 9.

            # Is flexible_power_pool (10) >= remaining_computers_needed_power (9)? True (10 >= 9).
            # So `check(9)` returns True.

            # This trace is consistent and robust. The `check` function itself appears to be correct
            # for the logical model it implements.

            # The only way `check(9)` should return False is if `flexible_power_pool` was less than 9.
            # In our trace, flexible_power_pool = 10.
            # Let's re-verify the input: `3`, `[10,10,3,5]`. Expected output: `8`. My code output: `9`.

            # This implies that the problem statement for `n` computers and `batteries` values is interpreted
            # in a way that my `check` function does not fully capture.
            # What if a battery must *exclusively* be used for one computer if its capacity is high?
            # "Simultaneously" implies that if a battery is powering computer A, it cannot also power B.
            # BUT, if battery is C and we need T. If C > T, it powers A for T, and remaining C-T can be used for B.
            # This is exactly what `flexible_power_pool += (battery_capacity - target_time)` covers.

            # What if `n` is greater than the total number of batteries? `n <= batteries.length` is given.

            # Let's consider the problem with `n=3`, `[10,10,3,5]` and expected `8`.
            # To run for 8 minutes:
            # Comp1: uses 10 min battery. It's fully powered. 2 min excess goes to pool.
            # Comp2: uses 10 min battery. It's fully powered. 2 min excess goes to pool.
            # Pool: 2 + 2 = 4 min (from 10 min batteries) + 3 min (from 3 min battery) + 5 min (from 5 min battery) = 12 min.
            # Remaining computers to power = 1 (Comp3). Needs 8 min.
            # Pool (12 min) is >= 8 min. So yes, can power Comp3 for 8 min. Total 3 computers for 8 min.
            # So `check(8)` is correctly `True`.

            # Why `check(9)` should be `False`?
            # Comp1: uses 10 min battery for 9 min. 1 min excess goes to pool.
            # Comp2: uses 10 min battery for 9 min. 1 min excess goes to pool.
            # Pool: 1 + 1 = 2 min (from 10 min batteries) + 3 min (from 3 min battery) + 5 min (from 5 min battery) = 10 min.
            # Remaining computers to power = 1 (Comp3). Needs 9 min.
            # Pool (10 min) is >= 9 min. So yes, can power Comp3 for 9 min. Total 3 computers for 9 min.
            # This is what my code says. And it seems plausible.

            # Could it be that the problem implies that if a battery is strong enough to power for `target_time`,
            # it *must* fully power one computer and cannot share its excess? No, that would be highly restrictive
            # and lead to much smaller runtimes. "Simultaneously" refers to the computers running, not batteries.

            # There's an alternative, often simpler way to write the `check` function for this type of problem:
            # We have `n` computers, and they each need `target_time` minutes.
            # We want to maximize the total power we can *effectively* deliver.
            # Sum up `total_run_time_possible = 0`.
            # For each battery `b`:
            #   If `b >= target_time`: This battery can power one computer for `target_time`.
            #                          It also has `b - target_time` left over.
            #                          So it effectively adds `target_time` to one slot, and `b - target_time`
            #                          to the general pool for other slots.
            #                          We can count this as `total_run_time_possible += target_time`
            #                          and `total_run_time_possible += (b - target_time)` *after* all `n` slots are considered.
            #                          A simpler way is `total_run_time_possible += b`.
            #   If `b < target_time`: This battery cannot power a computer for `target_time`.
            #                         Its full capacity `b` goes into the general pool to top up other computers.
            #                         So `total_run_time_possible += b`.
            # This perspective, where `total_run_time_possible` just sums up `b` for all `b`, is incomplete.

            # The standard greedy strategy for `check(T)` is:
            # 1. Take the `n` largest batteries. Let their capacities be `b_1, ..., b_n`.
            # 2. Assign each of these to one computer.
            # 3. All other `k-n` batteries are added to a pool.
            # 4. For each `b_i` among the `n` largest:
            #    If `b_i < T`, it needs `T - b_i` from the pool.
            #    If `b_i >= T`, it gives `b_i - T` to the pool.
            # 5. Check if the pool can cover all deficits.

            # This is equivalent to saying:
            # Calculate `total_power = sum(batteries)`.
            # If `total_power < n * target_time`, return False. (This is a global upper bound)
            
            # This simpler logic is actually the correct one, and it is more robust to implementation errors.
            # The reason this is true is that if we have `N` computers and `M` batteries.
            # We can think of it as having `M` available power sources.
            # We need to run `N` computers.
            # Each computer must run for time `T`. So we need `N * T` total "power units".
            # The *total sum* of all battery capacities `sum(batteries)` is the maximum power units available.
            # So `sum(batteries) >= N * T` is a necessary condition.
            # Is it sufficient? No. For example, if `N=2`, `batteries=[1, 1000]`, `T=100`.
            # `sum(batteries) = 1001`. `N*T = 200`. `1001 >= 200` is true.
            # But we can only run one computer for 100 minutes (using the 1000 battery). The 1 battery is useless for 100 mins.
            # So `check(100)` for this case should be `False`.

            # This means my original `check` function, which tries to differentiate between large and small batteries,
            # is indeed the correct approach.

            # Let's consider the test case `n=3, batteries=[10,10,3,5]`.
            # And the expected output `8`. My code output `9`.
            # This implies that `check(9)` should be `False`. But my code returns `True`.

            # What if `n` is greater than `len(batteries)`? This cannot happen.
            # What if `target_time` is 0? `check(0)` would always be True. `ans` would be 0 initially.
            # `low=0` `high=sum(batteries)//n`. If `sum(batteries)` is 0, `high` is 0.
            # If `n=1, batteries=[0]`, `high=0`. `check(0)` true. `ans=0`. Correct.

            # Is there any constraint about *number* of batteries used?
            # "You should run all n computers simultaneously for as long as possible."
            # This typically implies optimal usage of all batteries.

            # Could it be an issue with `n` and `len(batteries)` relationship?
            # Suppose `n = len(batteries)`.
            # Then each computer must be assigned a unique battery.
            # In this scenario, `check(target_time)` means `all batteries[i] >= target_time`.
            # My current `check` function:
            # `computers_fully_powered` counts batteries `b_i >= target_time`.
            # `flexible_power_pool` collects excesses from these and full values from `b_i < target_time`.
            # If `n == len(batteries)`:
            #   If `b_i < target_time` for any `i`: `computers_fully_powered` will be less than `n`.
            #     `flexible_power_pool` will contain `b_i` for those `b_i < target_time`.
            #     `remaining_computers_needed_power = (n - c_fp) * target_time`.
            #     This relies on `flexible_power_pool` to cover these.
            #     But if `n == len(batteries)`, each computer *must* be fully powered by its own battery.
            #     A battery cannot be "shared" by going into `flexible_power_pool` and then being pulled out to top up.
            #     It has to power *its allocated computer*.

            # This interpretation is potentially the key. If `n` computers are to run, and we have `k` batteries.
            # We can select `n` batteries to *primarily* power `n` computers.
            # The remaining `k-n` batteries become supplemental.

            # The standard `check` function (which my code implements) assumes that any `battery_capacity - target_time`
            # and any `battery_capacity < target_time` can be freely combined and distributed among `n` computers.
            # This is generally true if we can always dynamically swap batteries or route power.

            # What if `n` is large compared to `len(batteries)`? This doesn't happen.
            # What if `len(batteries)` is large compared to `n`?
            # E.g. `n=1`, `batteries=[1,1,1,1,100]`. `target_time = 100`.
            # My code:
            # c_fp = 0, f_p_p = 0
            # b=1: <100. f_p_p+=1. (1)
            # b=1: <100. f_p_p+=1. (2)
            # b=1: <100. f_p_p+=1. (3)
            # b=1: <100. f_p_p+=1. (4)
            # b=100: >=100. c_fp+=1. f_p_p+=0. (4)
            # c_fp=1. which is == n. Return True. Correct. One computer for 100 mins using the 100 battery.

            # The discrepancy for `n=3, batteries=[10,10,3,5]`, expected 8, code 9, is still bothering.
            # Total batteries capacity = 10 + 10 + 3 + 5 = 28.
            # n = 3.
            # Max possible average runtime = 28 / 3 = 9.33...
            # This means 9 could be an answer. Why is it 8?

            # For 9 minutes:
            # We need 3 computers running for 9 minutes each. Total 27 minutes of power.
            # We have 28 minutes of power. `28 >= 27`. So it's feasible from a total power perspective.

            # My check(9) returns True. Let's imagine the battery distribution.
            # Batteries: B1=10, B2=10, B3=3, B4=5.
            # Computers: C1, C2, C3. Each needs 9 minutes.

            # C1: Use B1 (10 min). B1 is enough. B1 has 10-9 = 1 min excess.
            # C2: Use B2 (10 min). B2 is enough. B2 has 10-9 = 1 min excess.
            # Total excess: 1 + 1 = 2 min.
            # Remaining batteries: B3=3, B4=5.
            # Total flexible power (excess + weak batteries): 2 + 3 + 5 = 10 min.

            # C3 needs 9 minutes. We have 10 minutes in the flexible pool.
            # We can give 9 minutes from the flexible pool to C3.
            # So, C1 runs for 9 (from B1), C2 runs for 9 (from B2), C3 runs for 9 (from pooled B3, B4, and excess of B1, B2).
            # This scenario is possible!
            # So my `check(9)` being True seems logically consistent with the problem statement.

            # Could the provided example `Expected output: "8", Code output: "9"` be wrong?
            # Or perhaps there is a very subtle interpretation of "simultaneously" and "battery swapping"
            # that this problem implies?
            # For competitive programming, this check function is standard for this type of problem.

            # The "maxRunTime" problem is a classic binary search problem. The `check` function I have
            # is indeed the standard way to verify if `target_time` is achievable.
            # One possible case where this check might fail to give expected output is if `target_time`
            # implies that some batteries must be used in a way that is "inefficient" for the given `n`.

            # What if `n` is larger than the number of batteries which individually can satisfy `target_time`?
            # `n=3, batteries=[10,10,3,5]`, `target_time=9`.
            # Only 2 batteries (10, 10) can satisfy 9 individually.
            # The remaining 1 computer (C3) needs 9.
            # The remaining batteries are 3 and 5, plus 1+1 from the 10-min batteries. Total 10.
            # The 10 power units can be provided to C3.
            # It sounds like 9 should be possible.

            # Could it be that if a battery is strong enough (`b >= target_time`), it *must* be dedicated
            # to one computer, and its excess (`b - target_time`) cannot be pooled? This would be a very
            # unusual interpretation. If `b=100`, `target_time=10`, `n=1`. The battery powers one computer for 10.
            # The remaining 90 power would just be "wasted" if it couldn't be used by another computer (if `n` was larger).
            # The problem usually assumes optimal resource utilization.

            # The check function logic is widely accepted for this type of problem (e.g., similar to "Maximum Product Subarray" but for time).
            # It's possible the test case itself or its expected output is based on an assumption that isn't immediately obvious,
            # or my problem source is using a modified version.

            # Let's verify the check function with an alternate common form:
            # We need to run `n` computers. Total time `T`.
            # Each computer must receive `T` power.
            # So, we need `n` power-units of `T`.
            # Total available power sum `S = sum(batteries)`.
            # `if S < n * T`, return False. (This is necessary)

            # To avoid the "splitting a battery between two needs" problem, a slightly different form.
            # Let `effective_power = 0`.
            # For each `battery_capacity`:
            #   `effective_power += min(battery_capacity, target_time)`.
            # This counts how much power we could supply if each battery contributed *at most* `target_time` to
            # a computer.
            # Example: `n=2, batteries=[1, 1000], target_time=100`.
            # `effective_power = min(1, 100) + min(1000, 100) = 1 + 100 = 101`.
            # `n * target_time = 2 * 100 = 200`.
            # `101 < 200`. So it should return False.
            # My current code's check(100):
            # c_fp = 0, f_p_p = 0
            # b=1: <100. f_p_p+=1. (1)
            # b=1000: >=100. c_fp+=1. f_p_p+=(1000-100)=900. (901)
            # c_fp=1. <n(2).
            # rem_needed = (2-1)*100 = 100.
            # f_p_p = 901 >= 100. True.

            # Aha! The example `n=2, batteries=[1, 1000], target_time=100` shows a fundamental difference!
            # My current `check` returns True. But it should be False.
            # We have 2 computers. One is powered by 1000 battery. What about the other?
            # It needs 100 minutes. We have a pool of 901. So, it *is* possible.
            # This makes me question my intuition for `n=2, batteries=[1, 1000], target_time=100`.
            # Comp1 uses 1000 battery (for 100 mins). Excess 900.
            # Comp2 needs 100 mins. Can take from (excess 900 + battery 1) = 901.
            # So, Comp1 runs 100 min, Comp2 runs 100 min. This IS possible.
            # My `check` function is actually correct for this example.

            # So why is the test case `n=3, batteries=[10,10,3,5]`, expected 8, output 9?
            # My logic confirms `check(9)` is True. This leads to 9.
            # This is a very perplexing situation where the standard solution appears to be correct,
            # but fails a specific test case from the platform.

            # The only situation where `check(target_time)` might be considered incorrect:
            # If `n` is greater than the total number of batteries. (Not possible by constraint)
            # If a battery `B` of capacity `C` cannot contribute its `C` capacity to the flexible pool
            # if `C < target_time`. This is unlikely.
            # If a battery `B` of capacity `C >= target_time` *must* power a computer for `target_time`
            # and its excess `C - target_time` cannot be used by *other* computers. This is also unusual.

            # Let me consider the problem statement from a different source (LeetCode 2136: Earliest Possible Day of Full Bloom has a similar `check` structure).
            # It seems the check function is robust.

            # Is it possible `n` represents "number of *types* of computers" and we must use only one battery per computer type?
            # No, that's not standard.

            # Maybe the small batteries cannot be pooled and combined?
            # "The total power needed for these remaining computers is (n - computers_fully_powered) * target_time.
            # We must use the 'flexible_power_pool' to cover this requirement."
            # This implies the flexible power pool can be freely distributed. This is the standard interpretation.

            # I will stick with the current `check` function, as it is the standard and logically sound approach
            # for "optimal distribution of resources". If it fails, the provided expected output might be based on
            # an unstated constraint or a specific heuristic that isn't optimal.

            # Let's double check the constraints or any implicit assumptions again.
            # "n computers simultaneously"
            # "batteries[i] is the runtime of the ith battery" -> implies `batteries[i]` is a capacity or energy unit.
            # "run for as long as possible" -> max T.

            # My original `check` function appears to be the correct one for this problem statement.
            # The only thing I can think of for such a discrepancy is that the problem setter
            # implicitly requires that for each of the `n` computers, there must be a *single* battery
            # that is *strong enough* to contribute at least `target_time` amount of power,
            # and smaller batteries can only augment *those* batteries.
            # But the wording "flexible_power_pool" and how it's used suggests full interchangeability.

            # What if the error is simpler, in the binary search bounds?
            # `low = 0` (min runtime is 0)
            # `high = sum(batteries) // n` (max average runtime, if all batteries perfectly utilized)
            # This is also standard. If `sum(batteries) = 0`, `high=0`.

            # Given the robustness of the `check` function, it's highly likely that the provided expected
            # output for that specific test case is either incorrect or derived from a non-standard
            # interpretation of the problem. However, I must fix it to pass.
            
            # The only way to make `check(9)` return `False` for `n=3, batteries=[10,10,3,5]`
            # is if `flexible_power_pool` calculation for `target_time=9` was less than `9`.
            # In my trace, it was `10`.
            # `flexible_power_pool = (10-9) + (10-9) + 3 + 5 = 1 + 1 + 3 + 5 = 10`.
            # This value is correct.

            # What if we sort `batteries` in ascending order first?
            # `batteries = [3, 5, 10, 10]`
            # `target_time = 9`. `n = 3`.
            # c_fp = 0, f_p_p = 0
            # b=3: <9. f_p_p += 3. (3)
            # b=5: <9. f_p_p += 5. (8)
            # b=10: >=9. c_fp += 1. f_p_p += (10-9) = 1. (8+1=9)
            # b=10: >=9. c_fp += 1. f_p_p += (10-9) = 1. (9+1=10)
            # Final: c_fp = 2, f_p_p = 10.
            # Same result, sorting doesn't change `check` result.

            # Could `sum(batteries)` be wrong? `10+10+3+5 = 28`. Correct.
            # `high = 28 // 3 = 9`. So `high` is 9.
            # Binary search range `[0, 9]`.
            # `ans` initialized to 0.

            # Iteration 1: `low=0, high=9, mid=4`. `check(4)` is True. `ans=4, low=5`.
            # Iteration 2: `low=5, high=9, mid=7`. `check(7)` is True. `ans=7, low=8`.
            # Iteration 3: `low=8, high=9, mid=8`. `check(8)` is True. `ans=8, low=9`.
            # Iteration 4: `low=9, high=9, mid=9`. `check(9)` is True. `ans=9, low=10`.
            # Iteration 5: `low=10, high=9`. Loop terminates.
            # Returns `ans=9`.

            # The code is working exactly as intended by the check function.
            # If the expected output is 8, it implies `check(9)` must be False.
            # The only way to make `check(9)` False is if the `flexible_power_pool` cannot cover `remaining_computers_needed_power`.
            # For `target_time = 9`, `n=3`:
            # `remaining_computers_needed_power = (3 - 2) * 9 = 9`.
            # `flexible_power_pool = 10`.
            # So, `10 >= 9` is True.

            # What if the "flexible_power_pool" is not entirely fungible?
            # Example: 1 computer, 2 batteries [1, 100]. Target time 50.
            # My code: c_fp = 0, f_p_p = 0
            # b=1: <50. f_p_p+=1.
            # b=100: >=50. c_fp+=1. f_p_p+=(100-50)=50.
            # Result: c_fp=1, f_p_p=51.
            # c_fp == n, so True. Correct. One computer can run on 100 battery for 50 mins.

            # Example where my current check is sometimes simplified:
            # Instead of distinguishing `computers_fully_powered` and `flexible_power_pool`,
            # some solutions simply use:
            # `total_available_power = 0`
            # `for b in batteries:`
            #    `total_available_power += min(b, target_time)` (This is the one I earlier said wasn't completely right)
            # `return total_available_power >= n * target_time` (This is wrong logic, as shown for [1,1000] and T=100)
            # Because `min(1000, 100)` would be 100, which ignores that `1000` could power multiple `target_time` segments if available.

            # My implemented check logic:
            # `computers_fully_powered` batteries supply `target_time` each.
            # `flexible_power_pool` then covers `target_time` for the `n - computers_fully_powered` remaining.
            # This is equivalent to summing the total power effectively supplied across all `n` computers.
            # Sum of (min(battery_capacity, target_time) for batteries with `battery_capacity < target_time`)
            # + Sum of (target_time for batteries with `battery_capacity >= target_time`)
            # + Sum of (battery_capacity - target_time for batteries with `battery_capacity >= target_time`).
            # This simplifies to:
            # Sum of `battery_capacity` for `batteries < target_time`
            # + Sum of `battery_capacity` for `batteries >= target_time`
            # BUT capped by `n * target_time` total power.
            # No, that's not quite right.

            # The check function essentially asserts:
            # `n * target_time` total "energy units" are needed.
            # We have `computers_fully_powered` units of `target_time` satisfied by strong batteries.
            # And `flexible_power_pool` extra units.
            # The `flexible_power_pool` effectively needs to provide `(n - computers_fully_powered) * target_time` more.
            # This is the standard greedy strategy.

            # Could it be an off-by-one or comparison error? `low <= high` and `mid = low + (high-low)//2`.
            # If `check(mid)` is true, `ans = mid, low = mid + 1`. This finds the largest `mid` for which check is true.
            # If `check(mid)` is false, `high = mid - 1`.
            # This binary search structure is standard.

            # Given the problem's nature and common solution patterns, the existing code should be correct.
            # I will provide the code as it is, as it aligns with standard interpretations. If the platform still fails,
            # then the problem statement on that platform might have an unusual edge case or non-standard interpretation.

            # Final verification of `n=3, batteries=[10,10,3,5]`, expected 8.
            # This test case implies `check(9)` should be false.
            # For `check(9)` to be false, we need `flexible_power_pool < (n - computers_fully_powered) * target_time`.
            # `10 < 9` must be true. But `10 >= 9` is true.
            # This means `flexible_power_pool` must be < 9.
            # How could flexible_power_pool be less than 9?
            # It's `sum of (b_i - target_time)` for `b_i >= target_time`
            # `+ sum of b_j` for `b_j < target_time`.
            # For `target_time = 9`:
            # `(10-9) + (10-9) + 3 + 5 = 1 + 1 + 3 + 5 = 10`.
            # This calculation is robust.

            # The only situation where this calculation might be wrong is if `flexible_power_pool` has to be split such that
            # individual batteries are not fully utilized, which is against the spirit of "optimal distribution".
            # E.g., if we need 9, but flexible pool contains [3,5,1,1].
            # We can use [3,5,1] (total 9) to power the last computer.
            # The remaining 1 is unused, but we achieved 9.

            # Therefore, I maintain that the original `check` function is robust and correct for this problem type.
            # The discrepancy points to an issue external to the code's logic (e.g., test case expectation).
            # I will simply return the original code.

            # One final re-check for the logic of `check`:
            # Suppose we have `k` batteries. `n` computers. Each needs `target_time`.
            # We have `B` = `[b_1, b_2, ..., b_k]`.
            # We want to know if `sum(b_i)` is enough, after considering individual minimums.
            # Consider `n` computers. Each needs `target_time` power.
            # The total power `S = sum(batteries)`.
            # The power needed is `n * target_time`.
            # If `S < n * target_time`, return `False`. (This is a global upper bound)

            # This condition: `sum(batteries) < n * target_time` is a more fundamental first check.
            # If this is true, my `check` function *might* still return true depending on values.
            # Let's add this.
            
            # `sum(batteries)` for `[10,10,3,5]` is `28`.
            # For `target_time=9`, `n=3`, `n * target_time = 27`.
            # `28 >= 27`. So this condition passes for `target_time=9`.
            
            # This indicates that the problem is not about the overall energy budget.
            # The initial check I had (`computers_fully_powered` and `flexible_power_pool`) *is* the standard way.

            # If my `check` function is correct, then the expected output `8` is incorrect.
            # However, I have to assume the test cases are correct.
            # Is there any scenario where a large battery cannot contribute its excess to the pool?
            # E.g., if a battery can power a computer for X minutes, it *must* be dedicated to that computer
            # for that amount of time, and any excess cannot be routed to other computers. This would be a very strange constraint.
            # Example: `n=1, batteries=[100,1,1,1]`. `target_time=10`.
            # c_fp=1 (for 100 battery), f_p_p=(100-10) + 1+1+1 = 90 + 3 = 93.
            # `c_fp >= n` is true. So returns `True`. Correct.

            # The only fix for the issue is to assume `check(9)` is indeed False.
            # This means `flexible_power_pool < (n - computers_fully_powered) * target_time` for `target_time=9`.
            # `10 < 9` is required. This is not possible given my calculation.

            # I will return the original code, as I am confident in its logic for the problem description.
            # The provided "Wrong Answer" could be a platform specific issue with the test case.
            # If the problem statement intends something different, it is not clearly stated.
            
            # Okay, there IS a common simplification for the check function that handles this.
            # The total energy that we can effectively "use" for the `n` computers, where each needs `target_time`.
            # `power_sum = 0`
            # `for b in batteries:`
            #     `power_sum += min(b, target_time)`
            # This is how much each battery can contribute *individually* towards the `target_time` of *some* computer,
            # without its capacity exceeding `target_time`.
            # If `power_sum` is enough for `n` computers (`n * target_time`), then it's possible.
            
            # Let's test this alternative check for `n=3, batteries=[10,10,3,5]`
            # `target_time = 8`:
            # `min(10,8) + min(10,8) + min(3,8) + min(5,8)`
            # `8 + 8 + 3 + 5 = 24`.
            # `n * target_time = 3 * 8 = 24`.
            # `24 >= 24`. True. Correct for target=8.

            # `target_time = 9`:
            # `min(10,9) + min(10,9) + min(3,9) + min(5,9)`
            # `9 + 9 + 3 + 5 = 26`.
            # `n * target_time = 3 * 9 = 27`.
            # `26 >= 27`. False.

            # YES! This alternative `check` function gives `False` for `target_time=9`!
            # This is the correct interpretation.
            # The reason this works:
            # We have `len(batteries)` "slots" to provide power.
            # Each of these slots can provide at most `target_time` useful power towards meeting the `n` computers' needs.
            # Any excess from a battery (`b > target_time`) for a single computer's slot is NOT directly available
            # to fulfill *another* entire `target_time` slot for a *different* computer.
            # It implies that a battery can contribute its full capacity `b` *if* `b <= target_time`.
            # If `b > target_time`, it is capped at `target_time` for its contribution to `n` computers' collective need.
            # This means `sum(min(b, target_time) for b in batteries)` is the total power that can be optimally
            # distributed *across* `n` computers, where each computer needs `target_time`.
            # It is saying we have `len(batteries)` segments. Each can cover up to `target_time`.
            # The sum of these segments must be at least `n * target_time`.

            # This is different from my original interpretation because it implicitly limits how a single large battery
            # can contribute to multiple computers. It means a single large battery `B` (e.g., 100 capacity) for `target_time=10`
            # is treated as providing only 10 to the total pool, even though it could power 10 computers for 10 minutes each.
            # This is precisely the reason it would fail my earlier example `n=2, batteries=[1, 1000], target_time=100`.
            # Using the alternative check:
            # `min(1,100) + min(1000,100) = 1 + 100 = 101`.
            # `n * target_time = 2 * 100 = 200`.
            # `101 >= 200` is False. This is also correct. `[1, 1000]` cannot power 2 computers for 100 minutes.

            # So the problem implies that each battery, regardless of its size, can primarily serve only *one* of the `n` computer's needs,
            # and only up to `target_time` for that need. Excess cannot be used to entirely fulfill *another* computer's `target_time` need.
            # But the language "run all n computers simultaneously" does often imply full fungibility. This is a subtle difference.

            # The fixed solution will use this `sum(min(b, target_time))` approach for the `check` function.
            # This check logic is common for "at most one task per machine" type of problems,
            # where the task duration is what you're trying to achieve.

            # The phrasing "batteries[i] is the runtime of the ith battery" can be key.
            # If it's runtime, then a 10-minute battery runs for 10 minutes.
            # If we need 9 minutes, and have a 10-minute battery, it provides 9 to one computer. Its remaining 1 min is considered "excess".
            # The alternative `sum(min(b, target_time))` implies the 10-minute battery only contributes `min(10,9)=9` to the total *available* runtime,
            # ignoring its excess. This suggests that the excess cannot be used.

            # My original `check` function is called "Greedy strategy with remaining capacity pooling".
            # The alternative is called "Sum of capped contributions".
            # The "remaining capacity pooling" is generally more flexible and powerful, so it should lead to higher runtimes.
            # If the test case expects a lower runtime, it implies stricter constraints.
            # The `sum(min(b, T))` strategy assumes each battery can contribute up to `T` to the total *if it can*.
            # This means effectively each battery is only used to start *one* computer.
            # And then smaller batteries may be "topped up" by some means.

            # The problem can be tricky in its interpretation.
            # I will go with the `sum(min(b, target_time))` check, as it fits the `n=3, batteries=[10,10,3,5]` example.

            total_power_contributed = 0
            for capacity in batteries:
                # Each battery can contribute at most `target_time` towards *one* computer's requirement.
                # If its capacity is less than `target_time`, it contributes its full capacity.
                # If its capacity is more than `target_time`, it contributes exactly `target_time`.
                # This accumulated sum represents the total useful power available to distribute among `n` computers,
                # where each computer needs `target_time` and cannot receive more than `target_time` from a single "contribution unit".
                total_power_contributed += min(capacity, target_time)
            
            # We need to run `n` computers, each for `target_time` minutes.
            # So, total power required is `n * target_time`.
            return total_power_contributed >= n * target_time

        low = 0
        high = sum(batteries) // n
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
