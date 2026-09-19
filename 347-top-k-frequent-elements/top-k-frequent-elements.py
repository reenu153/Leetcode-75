class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        counter={}
        for num in nums:
            if num in counter.keys():
                counter[num]+=1
            else:
                counter[num]=1

        sorted_count=sorted(counter, key=counter.get,reverse=True)

        return sorted_count[:k]

           
        
        

