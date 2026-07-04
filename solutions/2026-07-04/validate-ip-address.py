# Title: Validate IP Address
# URL: https://leetcode.com/problems/validate-ip-address/
# Difficulty: Medium

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def is_ipv4(ip_str: str) -> bool:
            parts = ip_str.split('.')
            if len(parts) != 4:
                return False
            
            for part in parts:
                # 1. Check for empty parts (e.g., "1.1..1", ".1.1.1", "1.1.1.")
                if not part:
                    return False
                
                # 2. Check for non-digit characters
                if not part.isdigit():
                    return False
                
                # 3. Check for leading zeros (e.g., "01" is invalid, "0" is valid)
                # A part is invalid if its length is greater than 1 AND it starts with '0'.
                if len(part) > 1 and part[0] == '0':
                    return False
                
                # 4. Check range 0-255
                num = int(part)
                if not (0 <= num <= 255):
                    return False
            
            return True

        def is_ipv6(ip_str: str) -> bool:
            parts = ip_str.split(':')
            if len(parts) != 8:
                return False
            
            # Valid hexadecimal characters
            hex_digits = "0123456789abcdefABCDEF"
            
            for part in parts:
                # 1. Check length of each part (1 to 4 characters)
                # This also implicitly handles empty parts like "" resulting from "::" or leading/trailing colons
                if not (1 <= len(part) <= 4):
                    return False
                
                # 2. Check if all characters are valid hexadecimal digits
                for char in part:
                    if char not in hex_digits:
                        return False
            
            return True

        # Main logic to determine IP type
        if '.' in queryIP and ':' not in queryIP:
            # If it contains '.' but not ':', it might be IPv4
            if is_ipv4(queryIP):
                return "IPv4"
        elif ':' in queryIP and '.' not in queryIP:
            # If it contains ':' but not '.', it might be IPv6
            if is_ipv6(queryIP):
                return "IPv6"
        
        # If it contains both, neither, or neither valid separator structure, it's "Neither"
        return "Neither"
