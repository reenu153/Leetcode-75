class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals=sorted(intervals)
        res,i=[],0

        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1

        #merge
        if i<len(intervals):
            if intervals[i][0]<=newInterval[1]:
                new=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
                res.append(new)
            else:
                res.append(newInterval)
                res.append(intervals[i])
            i+=1
        else:
            res.append(newInterval)
            return res

        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            last=res.pop()
            res.append([min(last[0],intervals[i][0]),max(last[1],intervals[i][1])])
            i+=1
            

        while i<len(intervals):
            res.append(intervals[i])
            i+=1
             
        return res
       