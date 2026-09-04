class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        maxAmt=0
        x1=0
        x2=len(height)-1

        while(x1<x2):
            h=height[x1] if height[x1]<height[x2] else height[x2]
            if (h*(x2-x1))>maxAmt:
                maxAmt=h*(x2-x1)
            if height[x1]>height[x2]:
                x2=x2-1
            else:
                x1=x1+1

        return maxAmt