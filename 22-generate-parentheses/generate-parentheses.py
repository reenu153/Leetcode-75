class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(ans,open,close):
            if len(ans)==2*n:
                res.append(ans)
            
            if open<n:
                backtrack(ans+"(",open+1,close)
            
            if close<open:
                backtrack(ans+")",open,close+1)
        
        backtrack("",0,0)
        return res