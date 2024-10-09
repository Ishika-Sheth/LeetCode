class Solution:
    def minAddToMakeValid(self, s):
        # Initialize counters for unbalanced open and close parentheses
        open_needed = 0
        close_needed = 0

        # Iterate through the string
        for char in s:
            if char == '(':
                # We need a matching closing parenthesis for each open parenthesis
                open_needed += 1
            elif char == ')':
                if open_needed > 0:
                    # A matching opening parenthesis is available, so we can balance one
                    open_needed -= 1
                else:
                    # No matching opening parenthesis, we need an extra one
                    close_needed += 1

        # Total moves needed is the sum of unbalanced open and close parentheses
        return open_needed + close_needed

# Example usage:
s = Solution()
print(s.minAddToMakeValid("())"))  # Output: 1
print(s.minAddToMakeValid("((("))  # Output: 3
