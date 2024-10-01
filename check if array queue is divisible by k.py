from collections import defaultdict

class Solution:
    def canArrange(self, arr, k):
        remainder_count = defaultdict(int)
        
        # Count occurrences of each remainder when divided by k
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        # Check for valid pairings
        for num in arr:
            remainder = num % k
            
            # If the remainder is 0, we need an even number of such elements
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            
            # If remainder is not 0, we need the complementary remainder
            elif remainder_count[remainder] != remainder_count[k - remainder]:
                return False
        
        return True

# Example usage in the form expected by the problem:
solution = Solution()
arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k1 = 5
print(solution.canArrange(arr1, k1))  # Output: True

arr2 = [1, 2, 3, 4, 5, 6]
k2 = 7
print(solution.canArrange(arr2, k2))  # Output: True

arr3 = [1, 2, 3, 4, 5, 6]
k3 = 10
print(solution.canArrange(arr3, k3))  # Output: False
