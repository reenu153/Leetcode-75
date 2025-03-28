class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=b=999999999999

        for num in nums:
            if num>b:
                return True
            if num<a:
                a=num
            elif num>a and num<b:
                b=num        

        return False

        # for i in range(0,len1-2):
        #     triple.append(nums[i])
        #     count=1
        #     for j in range(i+1, len1):
        #         if nums[j]>triple[count-1]:
        #             triple.append(nums[j])
        #             count+=1
        #         elif count==2 and nums[j]>triple[0]:
        #             del triple[1]
        #             triple.append(nums[j])

        #     if count>=3:
        #         return True
        #     triple=[]
            
        # return False