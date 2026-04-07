class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        self.map={}

        def solve(i,sum,nums,target):
            if (i,sum) in self.map:
                return self.map[(i,sum)]

            if i>len(nums)-1:
                if sum==target:
                    return 1
                return 0
            add=solve(i+1,sum+nums[i],nums,target)
            diff=solve(i+1,sum-nums[i],nums,target)
            self.map[(i,sum)]=add+diff
            return add+diff
        
        return solve(0,0,nums,target)

        