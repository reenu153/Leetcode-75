class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # coins=sorted(coins,reverse=True)
        # tot=0
        # count=0
        # for coin in coins:
        #     num=floor((amount-tot)/coin)
        #     tot+=(coin*num)
        #     count+=num

        # return count if tot==amount else -1

        dp=[float('inf')]*(amount+1)
        dp[0]=0

        for x in range(1,amount+1):
            for coin in coins:
                if coin<=x:
                    dp[x]=min(dp[x],dp[x-coin]+1) 
        
        return dp[amount] if dp[amount]!=float('inf') else -1
            
             
