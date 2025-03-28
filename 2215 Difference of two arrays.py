from collections import defaultdict

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
        d=defaultdict(int)
        len1=len(nums1)
        len2=len(nums2)
        for i in range(0,len1):
            if d[nums1[i]]==0:
                d[nums1[i]]=1

        for i in range(0,len2):
            if d[nums2[i]]==0:
                d[nums2[i]]=2
            elif d[nums2[i]]==1:
                d[nums2[i]]=-1
        list1=[]
        list2=[]
        keys=d.keys()
        for i in keys:
            if d[i]==1:
                list1.append(i)
            elif d[i]==2:
                list2.append(i)
        
        return [list1, list2]