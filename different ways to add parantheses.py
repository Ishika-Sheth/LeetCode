class Solution:
    def diffWaysToCompute(self, expression):
        # Memoization dictionary to store results of sub-expressions
        memo = {}

        # Helper function that recursively computes all the possible values
        def compute(expr):
            if expr in memo:
                return memo[expr]

            res = []
            for i, c in enumerate(expr):
                if c in "+-*":
                    # Recursively solve left and right sub-expressions
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])

                    # Combine results of left and right based on the operator
                    for l in left:
                        for r in right:
                            if c == '+':
                                res.append(l + r)
                            elif c == '-':
                                res.append(l - r)
                            elif c == '*':
                                res.append(l * r)

            # If no operator was found, this is a single number, so return it
            if not res:
                res.append(int(expr))

            memo[expr] = res
            return res

        return compute(expression)


# Example usage:
solution = Solution()

# Test case 1
expression1 = "2-1-1"
print(solution.diffWaysToCompute(expression1))  # Output: [0, 2]

# Test case 2
expression2 = "2*3-4*5"
print(solution.diffWaysToCompute(expression2))  # Output: [-34, -14, -10, -10, 10]
