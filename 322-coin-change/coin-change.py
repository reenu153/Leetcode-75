class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[inf]*(amount+1)
        dp[0]=0

        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=inf:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        
        return dp[amount] if dp[amount]!=inf else -1