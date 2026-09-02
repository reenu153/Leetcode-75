class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for n in nums:
            sublen=1
            if n-1 in nums:
                continue
            while n+1 in nums:
                sublen+=1
                n=n+1
            if sublen>longest:
                longest=sublen
        
        return longest
                