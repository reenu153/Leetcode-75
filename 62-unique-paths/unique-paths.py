class Solution:
    count=0
    def uniquePaths(self, m: int, n: int) -> int:
        # self.dfs(0,0,m,n)
        # return self.count

        dp=[[0]*(n)]*(m)
        for i in range(n):
            dp[0][i]=1
        for i in range(m):
            dp[i][0]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]

    # def dfs(self,i,j,m,n):
    #         if i>=m or j>=n:
    #             return 
    #         if i==m-1 and j==n-1:
    #             self.count+=1
    #             return
    #         self.dfs(i+1,j,m,n)
    #         self.dfs(i,j+1,m,n)

        