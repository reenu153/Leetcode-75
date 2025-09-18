class Solution(object):
    def dp(self,n,memo):
        if n in memo.keys():
            return memo[n]
        memo[n] = self.dp(n-1,memo) + self.dp(n-2,memo)
        return memo[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={1:1,2:2}
        return self.dp(n,memo)



    

        
        