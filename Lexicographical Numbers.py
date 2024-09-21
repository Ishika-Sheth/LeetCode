class Solution:
    def lexicalOrder(self, n):
        result = []

        def dfs(current):
            if current > n:
                return
            result.append(current)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        # Start DFS for each number from 1 to 9
        for i in range(1, 10):
            dfs(i)

        return result

# Example usage
solution = Solution()

# Example 1
n1 = 13
print(solution.lexicalOrder(n1))  # Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2
n2 = 2
print(solution.lexicalOrder(n2))  # Output: [1, 2]
