class Solution:
    def minGroups(self, intervals):
        events = []
        
        # Create two events for each interval: a start and an end
        for interval in intervals:
            events.append((interval[0], 1))  # Starting event
            events.append((interval[1] + 1, -1))  # Ending event (+1 to mark the end is exclusive)
        
        # Sort the events: first by time, then by type (end event comes before start event)
        events.sort()
        
        max_groups = 0
        current_groups = 0
        
        # Traverse through the sorted events
        for event in events:
            current_groups += event[1]
            max_groups = max(max_groups, current_groups)
        
        return max_groups

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    intervals1 = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    intervals2 = [[1,3],[5,6],[8,10],[11,13]]
    
    print(solution.minGroups(intervals1))  # Output: 3
    print(solution.minGroups(intervals2))  # Output: 1
