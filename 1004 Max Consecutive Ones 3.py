class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
                
        j=0
        zero_count=0
        max_count=0
        length=len(nums)
        zero_index=[]
        
        for i in range(0,length):
            if nums[i]==1:
                continue
            elif zero_count<k:
                zero_index.append(i)
                zero_count+=1
            else:
                zero_index.append(i)
                consecs= i-j
                if consecs>max_count:
                    print(consecs)
                    max_count=consecs
                j=zero_index[0]+1
                del zero_index[0]

        consecs= i-j+1
        if consecs>max_count:
             max_count=consecs
        
        return max_count
                
                

            