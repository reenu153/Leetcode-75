class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length=len(flowerbed)
        count=0
        flag= False
        impossible_indices=set()

        for i in range(0,length):
            if i==0:
                if length>1:
                    if( flowerbed[0]==0 and flowerbed[1]==0):
                        count+=1
                        i+=1
                        impossible_indices.add(1)
                else:
                    if flowerbed[0]==0:
                        return True
            elif i==length-1:
                    if(flowerbed[i]==0 and flowerbed[i-1]==0 and i not in impossible_indices):
                        count+=1
                   
            elif flowerbed[i]==0:
                    if flowerbed[i+1]==0 and flowerbed[i-1]==0 and i not in impossible_indices:
                        count+=1
                        impossible_indices.update([i-1,i+1])
                        i+=1
                    else:
                        continue
            if count>=n:
                flag=True
                break 
        print(count)
        return flag       


            