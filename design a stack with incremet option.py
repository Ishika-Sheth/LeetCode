class CustomStack:

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k, val):
        # Increment bottom k elements by val
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val

# Example usage:
stk = CustomStack(3)
stk.push(1)                    # stack becomes [1]
stk.push(2)                    # stack becomes [1, 2]
print(stk.pop())               # return 2, stack becomes [1]
stk.push(2)                    # stack becomes [1, 2]
stk.push(3)                    # stack becomes [1, 2, 3]
stk.push(4)                    # stack remains [1, 2, 3] because maxSize is 3
stk.increment(5, 100)          # stack becomes [101, 102, 103]
stk.increment(2, 100)          # stack becomes [201, 202, 103]
print(stk.pop())               # return 103, stack becomes [201, 202]
print(stk.pop())               # return 202, stack becomes [201]
print(stk.pop())               # return 201, stack becomes []
print(stk.pop())               # return -1, stack is empty
