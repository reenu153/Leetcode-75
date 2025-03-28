
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = 0 
        n = len(candies)
        result=[]
        for i in range(0,n):
            if candies[i]>greatest:
                greatest=candies[i]
            
        for i in range(0,n):
            if candies[i]+ extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result

        