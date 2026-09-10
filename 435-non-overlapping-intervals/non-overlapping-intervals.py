class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals, key=lambda x:x[1])
        last=intervals[0]
        removed=[]
        for a,b in intervals[1:]:
            if a<last[1]:
                removed.append([a,b])
            else:
                last=[a,b]
        return len(removed)

