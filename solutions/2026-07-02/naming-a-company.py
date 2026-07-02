# Title: Naming a Company
# URL: https://leetcode.com/problems/naming-a-company/
# Difficulty: Hard

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Step 1: Group ideas by their first letter.
        # The values for each key will be a set of suffixes.
        # Using a defaultdict simplifies handling characters that might not have any ideas.
        groups = collections.defaultdict(set)
        for idea in ideas:
            # idea[0] is the first character, idea[1:] is the suffix
            groups[idea[0]].add(idea[1:])

        # Step 2: Initialize the total count of distinct valid company names.
        total_distinct_names = 0

        # Step 3: Iterate through all unique pairs of distinct first characters.
        # There are 26 possible lowercase English letters ('a' through 'z').
        # We use nested loops to select two distinct characters, char1 and char2.
        # The outer loop goes from 'a' to 'z' (represented by char_code1 from 0 to 25).
        # The inner loop goes from the next character after char1 to 'z'
        # (represented by char_code2 from char_code1 + 1 to 25).
        # This ensures that each pair (char1, char2) is considered exactly once,
        # and char1 is always different from char2.
        for char_code1 in range(26):
            for char_code2 in range(char_code1 + 1, 26):
                char1 = chr(ord('a') + char_code1)
                char2 = chr(ord('a') + char_code2)

                # Get the sets of suffixes for ideas starting with char1 and char2.
                # If no idea starts with a particular character, its set will be empty
                # due to using defaultdict(set).
                suffixes1 = groups[char1]
                suffixes2 = groups[char2]

                # Step 4: Calculate the number of suffixes unique to each group (suffixes1 or suffixes2).
                # A suffix 's_A' (from idea_A = char1 + s_A) can be part of a valid new name
                # (char2 + s_A) if 'char2 + s_A' is NOT in the original 'ideas' list.
                # In terms of our groups, this means 's_A' must NOT be in groups[char2].
                # Similarly for s_B (from idea_B = char2 + s_B) and groups[char1].

                # Find suffixes that exist in both sets. These suffixes, when swapped,
                # would form a name that already exists in 'ideas', thus making the pair invalid.
                common_suffixes = suffixes1.intersection(suffixes2)
                
                # Count suffixes that are in suffixes1 but NOT in suffixes2.
                # These are the 's_A's for which 'char2 + s_A' would be a new unique name.
                distinct_in_suffixes1 = len(suffixes1) - len(common_suffixes)
                
                # Count suffixes that are in suffixes2 but NOT in suffixes1.
                # These are the 's_B's for which 'char1 + s_B' would be a new unique name.
                distinct_in_suffixes2 = len(suffixes2) - len(common_suffixes)

                # Step 5: Add the contribution of this pair of first characters to the total.
                # If we have 'k1' distinct suffixes for char1 (i.e., 'distinct_in_suffixes1')
                # and 'k2' distinct suffixes for char2 (i.e., 'distinct_in_suffixes2'),
                # then there are k1 * k2 ways to pick (idea_A, idea_B) where
                # idea_A starts with char1 and idea_B starts with char2,
                # such that both swapped names are new.
                #
                # For each such valid selection (idea_A, idea_B):
                # - It forms a company name: (char2 + s_A) + " " + (char1 + s_B).
                # - The reversed selection (idea_B, idea_A) is also valid and distinct:
                #   (char1 + s_B) + " " + (char2 + s_A).
                # Therefore, each combination of (distinct_in_suffixes1, distinct_in_suffixes2)
                # contributes 2 distinct valid company names.
                total_distinct_names += 2 * distinct_in_suffixes1 * distinct_in_suffixes2

        return total_distinct_names
