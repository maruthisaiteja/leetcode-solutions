# Title: Defanging an IP Address
# URL: https://leetcode.com/problems/defanging-an-ip-address/
# Difficulty: Easy

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
