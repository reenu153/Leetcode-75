from collections import defaultdict

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        d=defaultdict(int)

        for num in nums:
            if d[k-num]>0:
                count+=1
                d[k-num]-=1
            else:
                d[num]+=1

        return count


