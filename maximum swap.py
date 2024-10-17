class Solution:
    def maximumSwap(self, num):
        # Convert the number to a list of characters (digits)
        digits = list(str(num))
        
        # Keep track of the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(digits)}
        
        # Traverse each digit and try to find a larger digit to swap
        for i, d in enumerate(digits):
            # Check for a larger digit to swap (starting from 9 to d+1)
            for larger in range(9, int(d), -1):
                if last.get(larger, -1) > i:  # if the larger digit exists after the current digit
                    # Swap the current digit with the larger digit
                    digits[i], digits[last[larger]] = digits[last[larger]], digits[i]
                    # Return the number after the swap
                    return int(''.join(digits))
        
        # If no swap can improve the number, return the original number
        return num
