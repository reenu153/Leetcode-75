class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g,reverse=True)
        s=sorted(s,reverse=True)
        count=0
        j=0
        if not len(s) or not len(g):
            return 0
        for i in range(len(g)):
            if s[j]>=g[i]:
                count+=1
                j+=1
                if (j>=len(s)):
                    break
            
        return count