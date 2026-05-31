# Title: Destroying Asteroids
# URL: https://leetcode.com/problems/destroying-asteroids/
# Difficulty: Medium

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # To destroy all asteroids, we want to maximize our planet's mass
        # at each step to be able to overcome larger asteroids.
        # The most effective strategy is to destroy the smallest asteroids first.
        # This allows us to accumulate mass as quickly as possible from
        # easily defeatable targets, strengthening the planet for subsequent,
        # potentially larger asteroids.

        # 1. Sort the asteroids by their mass in non-decreasing order.
        # This ensures we always try to collide with the smallest available asteroid first.
        asteroids.sort()

        # 2. Initialize the planet's current mass with the given starting mass.
        current_mass = mass

        # 3. Iterate through each asteroid in the sorted list.
        for asteroid_mass in asteroids:
            # 4. Check if the planet's current mass is greater than or equal to the
            # mass of the current asteroid.
            if current_mass >= asteroid_mass:
                # If yes, the asteroid is destroyed, and its mass is added to the planet.
                current_mass += asteroid_mass
            else:
                # If no, the planet cannot destroy this asteroid.
                # Since we are processing asteroids in ascending order of mass,
                # if we cannot destroy the current asteroid, we certainly cannot
                # destroy any subsequent (larger or equal mass) asteroids either.
                # Thus, it's impossible to destroy all asteroids.
                return False
        
        # 5. If the loop completes, it means the planet successfully destroyed
        # all asteroids.
        return True
