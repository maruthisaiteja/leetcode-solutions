# Title: Count Tested Devices After Test Operations
# URL: https://leetcode.com/problems/count-tested-devices-after-test-operations/
# Difficulty: Easy

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices_count = 0
        # reduction_count keeps track of how many devices before the current one
        # have been tested. Each tested device reduces the battery percentage
        # of all subsequent devices by 1.
        reduction_count = 0

        for original_battery_percentage in batteryPercentages:
            # Calculate the effective battery percentage for the current device.
            # This accounts for the cumulative reduction from previously tested devices.
            current_effective_battery = original_battery_percentage - reduction_count

            # If the effective battery percentage is greater than 0, the device is tested.
            # The problem states battery percentage never goes below 0, so if
            # current_effective_battery becomes 0 or less due to reductions,
            # it effectively means its battery is 0 and it won't be tested.
            if current_effective_battery > 0:
                tested_devices_count += 1
                # Since this device was tested, it will contribute to reducing
                # the battery percentages of all subsequent devices.
                reduction_count += 1
            # If current_effective_battery <= 0, the device is not tested,
            # and it does not affect the battery percentages of subsequent devices.

        return tested_devices_count
