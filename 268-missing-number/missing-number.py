class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        actual=sum([i for i in range(len(nums)+1)])
        return actual-total