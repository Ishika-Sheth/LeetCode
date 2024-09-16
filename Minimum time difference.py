class Solution:
    def findMinDifference(self, timePoints):
        # Convert time "HH:MM" to minutes from 00:00
        def time_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        # Convert all timePoints to minutes
        minutes = sorted([time_to_minutes(time) for time in timePoints])
        
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        
        # Compare consecutive times
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Also, compare the last and first time across the midnight boundary
        min_diff = min(min_diff, (1440 + minutes[0] - minutes[-1]) % 1440)
        
        return min_diff

# Example usage:
sol = Solution()
timePoints1 = ["23:59","00:00"]
timePoints2 = ["00:00","23:59","00:00"]

print(sol.findMinDifference(timePoints1))  # Output: 1
print(sol.findMinDifference(timePoints2))  # Output: 0
