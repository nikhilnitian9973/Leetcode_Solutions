class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <=2:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # dp = [-1]*(n+1)
        # def fn(n):
        #     if n<=2:
        #         return n
        #     if dp[n] !=-1:
        #         return dp[n]
        #     dp[n] = fn(n-1)+fn(n-2)
        #     return dp[n]
        # return fn(n)
        if n == 1:
            return 1
        dp = [-1]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]