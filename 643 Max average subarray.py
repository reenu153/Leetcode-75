class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        j=0
        sum=0

        for i in range(0,k):
            sum+=nums[i]
        max_sum=sum
        i=k
        while(i<length):

            sum=sum+nums[i]-nums[j]
            if sum>max_sum:
                max_sum=sum
            j+=1
            i+=1

        return float(max_sum)/k
        


        