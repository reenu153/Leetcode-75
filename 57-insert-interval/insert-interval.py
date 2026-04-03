class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new=[]
        added=False

        for i in range(len(intervals)):

            if (intervals[i][1]<newInterval[0]):
                new.append(intervals[i])
            
            elif intervals[i][0]>newInterval[1] and intervals[i][1]>newInterval[1]:
                if not added:
                    new.append(newInterval)
                    added=True
                new.append(intervals[i])
            
            else:
                newInterval[0]=min(intervals[i][0],newInterval[0])
                newInterval[1]=max(intervals[i][1],newInterval[1])
   

        if not added:
            new.append(newInterval)
        return new