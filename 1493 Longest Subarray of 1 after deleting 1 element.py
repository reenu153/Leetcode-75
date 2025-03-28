class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len=0
        zero_index=[]
        length= len(nums)
        curr_len=0
        for i in range(0, length):
            print(curr_len)
            if nums[i]==1:
                curr_len+=1
            else:
                zero_index.append(i)
                zero_count=len(zero_index)
                if curr_len>max_len:
                        max_len=curr_len
                if zero_count==1:
                    continue
                elif zero_count==2:
                     curr_len=i-zero_index[0]-1
                else:
                    curr_len=i-zero_index[zero_count-2]-1

        if nums[length-1]==1 and curr_len>max_len:
            max_len=curr_len   
        if len(zero_index)==0:
            max_len=max_len-1

        return max_len
        

                

