# Title: Concatenate Non-Zero Digits and Multiply by Sum II
# URL: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# Difficulty: Medium

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Segment tree nodes store [x_val, sum_digits, count_non_zero_digits]
        # x_val: The integer formed by concatenating non-zero digits.
        # sum_digits: The sum of digits of x_val.
        # count_non_zero_digits: The number of non-zero digits in the segment.
        # This count is crucial for determining the power of 10 to shift x_L.
        
        # Initialize segment tree with default values [0, 0, 0]
        # A node represents a range. If it contains no non-zero digits, then x_val=0, sum_digits=0, count=0.
        tree = [[0, 0, 0] for _ in range(4 * n)]

        # Helper function to merge results from two child nodes
        def merge(left_res, right_res):
            x_L, sum_L, count_L = left_res
            x_R, sum_R, count_R = right_res
            
            # Merged x_val: left_x * (10 ^ count_R) + right_x
            # This correctly handles cases where count_R is 0 (10^0 = 1),
            # and cases where x_R is 0 if count_R is 0.
            merged_x = (x_L * pow(10, count_R, MOD) + x_R) % MOD
            
            # Merged sum_digits: sum_L + sum_R
            merged_sum = (sum_L + sum_R) % MOD
            
            # Merged count_non_zero_digits: count_L + count_R
            merged_count = count_L + count_R
            
            return [merged_x, merged_sum, merged_count]

        # Function to build the segment tree
        def build(node_idx, tree_L, tree_R):
            # Base case: leaf node
            if tree_L == tree_R:
                digit = int(s[tree_L])
                if digit != 0:
                    tree[node_idx] = [digit, digit, 1]
                else:
                    tree[node_idx] = [0, 0, 0] # For '0' digit, x=0, sum=0, count=0
                return

            # Recursive step: build left and right children, then merge
            mid = (tree_L + tree_R) // 2
            build(2 * node_idx + 1, tree_L, mid)
            build(2 * node_idx + 2, mid + 1, tree_R)
            
            tree[node_idx] = merge(tree[2 * node_idx + 1], tree[2 * node_idx + 2])

        # Function to query the segment tree for a given range [query_L, query_R]
        def query(node_idx, tree_L, tree_R, query_L, query_R):
            # Case 1: Current segment is completely outside the query range
            if tree_R < query_L or tree_L > query_R:
                return [0, 0, 0] # Identity element for merge operation (no contribution)

            # Case 2: Current segment is completely inside the query range
            if query_L <= tree_L and tree_R <= query_R:
                return tree[node_idx]

            # Case 3: Partial overlap, recurse on children and merge results
            mid = (tree_L + tree_R) // 2
            left_res = query(2 * node_idx + 1, tree_L, mid, query_L, query_R)
            right_res = query(2 * node_idx + 2, mid + 1, tree_R, query_L, query_R)
            
            return merge(left_res, right_res)

        # Build the segment tree for the entire string s
        build(0, 0, n - 1)

        results = []
        for l, r in queries:
            # Query the segment tree for the range [l, r]
            x_val, sum_val, _ = query(0, 0, n - 1, l, r)
            
            # Calculate the final answer for the query: x * sum (modulo MOD)
            ans = (x_val * sum_val) % MOD
            results.append(ans)
        
        return results
