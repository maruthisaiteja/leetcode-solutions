# Title: Sliding Puzzle
# URL: https://leetcode.com/problems/sliding-puzzle/
# Difficulty: Hard

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Convert the 2x3 board into a 1D string for easier manipulation and hashing
        # Example: [[1,2,3],[4,5,0]] -> "123450"
        initial_state = "".join(str(x) for row in board for x in row)
        target_state = "123450"

        # Define neighbors for each position on the 2x3 board
        # Positions are indexed 0 to 5 in the flattened string:
        # 0 1 2
        # 3 4 5
        # For a given position of '0', these are the indices of tiles it can swap with.
        pos_to_neighbors = {
            0: (1, 3),    # '0' at index 0 can swap with tile at 1 (right) or 3 (down)
            1: (0, 2, 4), # '0' at index 1 can swap with tile at 0 (left), 2 (right), or 4 (down)
            2: (1, 5),    # '0' at index 2 can swap with tile at 1 (left) or 5 (down)
            3: (0, 4),    # '0' at index 3 can swap with tile at 0 (up) or 4 (right)
            4: (1, 3, 5), # '0' at index 4 can swap with tile at 1 (up), 3 (left), or 5 (right)
            5: (2, 4)     # '0' at index 5 can swap with tile at 2 (up) or 4 (left)
        }

        # BFS initialization
        # The queue stores tuples of (current_state_string, moves_count)
        queue = collections.deque([(initial_state, 0)])
        
        # The visited set stores strings of states to prevent cycles and redundant processing
        visited = {initial_state}

        while queue:
            current_state, moves = queue.popleft()

            # If the current state is the target, we found the shortest path
            if current_state == target_state:
                return moves

            # Find the position (index) of '0' in the current state string
            zero_idx = current_state.find('0')

            # Generate next possible states by swapping '0' with its adjacent tiles
            for neighbor_idx in pos_to_neighbors[zero_idx]:
                # Convert the current_state string to a list of characters to perform the swap
                state_list = list(current_state)
                
                # Perform the swap: '0' moves to neighbor_idx, and the neighbor tile moves to zero_idx
                state_list[zero_idx], state_list[neighbor_idx] = state_list[neighbor_idx], state_list[zero_idx]
                
                # Convert the list of characters back to a string for the new state
                new_state = "".join(state_list)

                # If this new state has not been visited, add it to the queue and visited set
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))

        # If the queue becomes empty and the target state was never reached, it's impossible
        return -1
