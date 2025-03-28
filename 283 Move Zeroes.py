class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        
        for i in range(0, l-1):
            if nums[i]==0 :
                j=i+1
                while(nums[j]==0 and j<l-1):
                    j=j+1
                if nums[j]!=0:
                    nums[i]=nums[j]
                    nums[j]=0
    
        



            
        