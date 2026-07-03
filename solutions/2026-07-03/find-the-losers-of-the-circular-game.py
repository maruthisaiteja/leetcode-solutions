# Title: Find the Losers of the Circular Game
# URL: https://leetcode.com/problems/find-the-losers-of-the-circular-game/
# Difficulty: Easy

from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        received_ball = set()
        
        current_friend = 1  # 1-indexed friend who currently holds the ball
        turn_multiplier = 1 # This multiplies with 'k' to determine the pass distance
        
        # The 1st friend receives the ball initially (this is the first 'receipt')
        received_ball.add(current_friend)
        
        # Simulate the game turns
        while True:
            # Calculate the distance for the current turn
            # On the i-th turn, the friend passes it i*k steps away.
            # Here, turn_multiplier acts as 'i'.
            distance_to_pass = turn_multiplier * k
            
            # Determine the next friend to receive the ball
            # Friends are 1-indexed. To use modulo arithmetic (0 to n-1), convert current_friend.
            # (current_friend - 1) makes it 0-indexed.
            # Add the distance.
            # Apply modulo n to handle wrapping around the circle.
            # Add 1 back to convert it to 1-indexed.
            next_friend_0_indexed = (current_friend - 1 + distance_to_pass) % n
            next_friend = next_friend_0_indexed + 1
            
            # Check if this next_friend has already received the ball
            if next_friend in received_ball:
                # If they have, the game ends according to the rules.
                break
            else:
                # If not, add them to the set of friends who received the ball.
                received_ball.add(next_friend)
                # This friend now holds the ball.
                current_friend = next_friend
                # Increment the turn multiplier for the next round.
                turn_multiplier += 1
        
        # After the game ends, identify the losers.
        # Losers are friends who are from 1 to n but are NOT in the received_ball set.
        losers = []
        for i in range(1, n + 1): # Iterate through all possible friend numbers
            if i not in received_ball:
                losers.append(i)
                
        # The problem asks for the losers in ascending order.
        # Our loop builds the 'losers' list in ascending order, so no explicit sort is needed.
        return losers
