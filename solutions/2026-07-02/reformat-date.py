# Title: Reformat Date
# URL: https://leetcode.com/problems/reformat-date/
# Difficulty: Easy

class Solution:
    def reformatDate(self, date: str) -> str:
        parts = date.split()
        day_str_raw = parts[0]
        month_abbr = parts[1]
        year_str = parts[2]

        # 1. Process Day component
        # Extract the numeric part of the day string (e.g., "20" from "20th")
        day_num = ""
        for char in day_str_raw:
            if char.isdigit():
                day_num += char
            else:
                # Stop when non-digit characters (like 'st', 'nd', 'rd', 'th') are encountered
                break
        
        # Format the day to be two digits (e.g., "1" -> "01", "20" -> "20")
        formatted_day = f"{int(day_num):02d}"

        # 2. Process Month component
        # Map month abbreviations to their two-digit numeric form
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        formatted_month = month_map[month_abbr]

        # 3. Process Year component
        # The year is already in the required 4-digit string format
        formatted_year = year_str

        # 4. Combine into YYYY-MM-DD format
        return f"{formatted_year}-{formatted_month}-{formatted_day}"
