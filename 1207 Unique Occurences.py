#1207 Unique Number of Occurences 
from collections import defaultdict

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d= defaultdict(int)
        for num in arr:
            d[num]+=1
        
        occurences=d.values()
        occ_count=defaultdict(int)
        for count in occurences:
            occ_count[count]+=1
            if occ_count[count]>1:
                return False
        
        return True