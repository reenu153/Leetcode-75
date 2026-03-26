class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l= len(height)
        tot=0

        max_height=height[0]
        max_index=0
        for i in range(1,l):
            if height[i]>=max_height:
                max_height=height[i]
                max_index=i

        curr_max=0
        for i in range(0,max_index):
            if height[i]>curr_max:
                curr_max=height[i]
            else:
                tot+=curr_max-height[i]

        curr_max=0
        for i in range(l-1,max_index,-1):
            if height[i]>curr_max:
                curr_max=height[i]
            else:
                tot+=curr_max-height[i]

        return tot
                
            



        