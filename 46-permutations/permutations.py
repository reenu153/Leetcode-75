class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:  
        res=[]
        def backtrack(i,nums):
           
            if i==len(nums)-1:
                res.append(nums[:])
                return

            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                backtrack(i+1,nums)
                nums[i],nums[j]=nums[j],nums[i]

 

        backtrack(0,nums)

        return res