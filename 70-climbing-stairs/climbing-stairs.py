class Solution:
    memo={}
    def climbStairs(self, n: int) -> int:
            if n<=0:
                return 0
            if n==1 or n==2:
                return n
            if n in self.memo.keys():
                return self.memo[n]
            self.memo[n]= self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.memo[n]
        