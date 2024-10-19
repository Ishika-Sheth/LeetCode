class Solution:
    def findKthBit(self, n, k):
        # Recursive function to find the k-th bit in Sn
        if n == 1:
            return "0"
        
        length = (1 << n) - 1  # Length of Sn, which is 2^n - 1
        
        mid = length // 2 + 1  # The middle element in the current Sn
        
        if k == mid:
            return "1"  # The middle element is always 1
        elif k < mid:
            return self.findKthBit(n - 1, k)  # If k is in the first half, it corresponds to Sn-1
        else:
            # If k is in the second half, it corresponds to the reversed and inverted Sn-1
            return '1' if self.findKthBit(n - 1, length - k + 1) == '0' else '0'

# Example usage:
solution = Solution()
print(solution.findKthBit(3, 1))  # Output: "0"
print(solution.findKthBit(4, 11))  # Output: "1"
