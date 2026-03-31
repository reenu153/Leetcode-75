class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map=defaultdict(int)
        for i in nums:
            map[i]+=1
        return heapq.nlargest(k,map.keys(),key=lambda x:map[x])
        