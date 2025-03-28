
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total=0
        for num in nums:
            total+=num
        length = len(nums)
        left=0
        right=total-nums[0]
        if left==right:
            return 0
        for i in range(1,length):
            left=left+nums[i-1]
            right=right-nums[i]
            if left==right:
                return i

        return -1
            