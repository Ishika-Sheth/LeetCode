import heapq

class Solution:
    def smallestRange(self, nums):
        # Min-heap to store (value, row, index) where 'value' is the current value from the list,
        # 'row' is the index of the list, and 'index' is the index of the element in the list.
        min_heap = []
        
        # We also keep track of the maximum element in the current window.
        max_value = float('-inf')
        
        # Initialize the heap with the first element of each list.
        for row in range(len(nums)):
            heapq.heappush(min_heap, (nums[row][0], row, 0))
            max_value = max(max_value, nums[row][0])
        
        # Initial range
        result_range = [float('-inf'), float('inf')]
        
        # Process the heap
        while True:
            min_value, row, index = heapq.heappop(min_heap)
            
            # Update the range if the current range is smaller than the previous one.
            if max_value - min_value < result_range[1] - result_range[0]:
                result_range = [min_value, max_value]
            
            # If we reached the end of one of the lists, stop (as we cannot cover all lists anymore).
            if index + 1 == len(nums[row]):
                break
            
            # Move to the next element in the same list.
            next_value = nums[row][index + 1]
            heapq.heappush(min_heap, (next_value, row, index + 1))
            
            # Update the max_value since we're adding a new element.
            max_value = max(max_value, next_value)
        
        return result_range

# Example usage
nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
solution = Solution()
print(solution.smallestRange(nums))  # Output: [20, 24]
