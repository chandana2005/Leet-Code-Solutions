class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0]*(n+1) 
        dp[1]=1
        shares = 0
        for day in range(2, n+1): 
            if day - delay >= 1: 
                shares += dp[day-delay]
            if day - forget >=1:
                shares -= dp[day-forget]
            shares %=MOD
            dp[day] = shares
        result =0
        for day in range(n - forget + 1, n + 1):
            result = (result + dp[day]) % MOD

        return result
