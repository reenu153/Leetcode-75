class MedianFinder:

    def __init__(self):

        #two heaps, large and small -> min and maxheap respectively 
        #both same size

        self.small, self.large = [],[]
        #heaps implemneted as arrays
        #elements in small <= elements in large

        #to make add and delete of data O(logn) instead O(n) like in lists
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) #to amke it max heap *-1

        #largest element in small less than smallest element in large
        if self.small and self.large and (-1 * self.small[0])>=self.large[0]: 
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        
        #uneven size
        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        
        if len(self.large)>len(self.small)+1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))


    def findMedian(self) -> float:

        if len(self.small)>len(self.large):
            return -1* self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return ((-1*self.small[0])+self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()