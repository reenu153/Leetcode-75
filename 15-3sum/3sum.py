class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums=sorted(nums)
        n=len(nums)
        pairs=[]

        for i in range(n-2):

            if nums[i]>0:
                break

            if i>0 and nums[i]==nums[i-1]:
                continue

            left=i+1
            right=n-1

            while(left<right):
            
                curr_sum=nums[i]+nums[left]+nums[right]
                if curr_sum>0:
                    right-=1
                elif curr_sum<0:
                    left+=1
                else:
                    pairs.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while  nums[left]==nums[left-1] and left<right:
                        left+=1               

        return pairs
        
        
