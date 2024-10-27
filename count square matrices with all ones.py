class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # For the first row or first column, we can only have squares of size 1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # Take the minimum of the three neighboring squares + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Add the size of the square to the count
                    count += dp[i][j]
        
        return count

# Example usage:
matrix1 = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
print(Solution().countSquares(matrix1))  # Output: 15

matrix2 = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]
print(Solution().countSquares(matrix2))  # Output: 7
