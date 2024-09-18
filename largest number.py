from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Custom comparator to decide the order of numbers
        def compare(x, y):
            # Compare concatenated results: xy and yx
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert all numbers to strings for easy concatenation comparison
        nums = list(map(str, nums))
        
        # Sort the array using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted array into a single string
        result = ''.join(nums)
        
        # Edge case: If the result is all zeros (e.g., [0, 0]), return "0"
        if result[0] == '0':
            return '0'
        
        return result

# Example usage:
# Create an instance of the Solution class
solution = Solution()

# Example test cases
nums1 = [10, 2]
nums2 = [3, 30, 34, 5, 9]

print(solution.largestNumber(nums1))  # Output: "210"
print(solution.largestNumber(nums2))  # Output: "9534330"
