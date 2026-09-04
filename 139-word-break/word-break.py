class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s),-1,-1):
            for j in range(i,len(s)+1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i]=True
        
        return dp[0]