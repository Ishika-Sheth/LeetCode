class Solution:
    def arrayRankTransform(self, arr):
        # Create a sorted version of the array without duplicates
        sorted_arr = sorted(set(arr))
        
        # Create a dictionary that maps each element to its rank
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_arr)}
        
        # Replace each element in the array with its rank
        return [rank_map[val] for val in arr]

# Example usage
solution = Solution()
print(solution.arrayRankTransform([40, 10, 20, 30]))  # Output: [4, 1, 2, 3]
print(solution.arrayRankTransform([100, 100, 100]))   # Output: [1, 1, 1]
print(solution.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))  # Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]
