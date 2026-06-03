# Title: Number of Equivalent Domino Pairs
# URL: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Difficulty: Easy

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Use an array to store frequencies of encoded dominoes.
        # Since dominoes[i][j] values are between 1 and 9,
        # we can encode a normalized domino (min_val, max_val) as min_val * 10 + max_val.
        # This results in integer keys ranging from 11 (for [1,1]) to 99 (for [9,9]).
        # An array of size 100 (indices 0-99) is sufficient to store counts.
        counts = [0] * 100 
        
        for a, b in dominoes:
            # Normalize the domino: ensure the smaller number comes first.
            # This makes [1,2] and [2,1] equivalent and both map to the same internal representation.
            if a > b:
                a, b = b, a
            
            # Encode the normalized domino into a single integer.
            # For example, [1,2] becomes 1*10 + 2 = 12.
            # This integer serves as an index into our counts array.
            encoded_domino = a * 10 + b
            counts[encoded_domino] += 1
            
        total_equivalent_pairs = 0
        
        # Iterate through the frequencies stored in the counts array.
        for count in counts:
            # If there are 'count' equivalent dominoes of a certain type,
            # the number of pairs (i, j) with i < j that can be formed from them
            # is given by the combination formula "count choose 2", which is count * (count - 1) / 2.
            if count >= 2:
                total_equivalent_pairs += (count * (count - 1)) // 2
                
        return total_equivalent_pairs
