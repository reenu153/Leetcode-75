class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """       
        maxvol=0
        x1=0
        x2=len(height)-1
        
        while(x1<x2):
            vol = min(height[x1], height[x2]) * (x2 - x1)
            maxvol = max(maxvol, vol)
            if(height[x1]>height[x2]):
                x2=x2-1
            else:
                x1=x1+1
        return maxvol




        
        