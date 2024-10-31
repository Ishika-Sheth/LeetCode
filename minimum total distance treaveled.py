class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][0] = float('inf')  
        for j in range(1, m + 1):  
            for i in range(1, n + 1):
                dp[i][j] = dp[i][j - 1] 
                total_distance = 0

                for k in range(1, min(i, factory[j - 1][1]) + 1):
                    total_distance += abs(robot[i - k] - factory[j - 1][0])
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)

        return dp[n][m]