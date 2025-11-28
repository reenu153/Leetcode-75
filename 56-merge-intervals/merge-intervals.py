class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x:(x[0],x[1]))
        merged=[intervals[0]]
        for interval in intervals[1:]:
            last=merged[-1]
            # if last[1]==interval[1]:
            #     merged.pop()
            #     first = interval[0] if interval[0]<last[0] else last[0]
            #     merged.append([first,last[1]])
            # elif last[0]==interval[0]:
            #     merged.pop()
            #     second=interval[1] if interval[1]>last[1] else last[1]
            #     merged.append([last[0],second])
            if last[1]==interval[0]:
                merged.pop()
                merged.append([last[0],interval[1]])
            elif last[1]>interval[0]:
                if last[1]>interval[1]:
                    continue 
                merged.pop()
                merged.append([last[0],interval[1]])             
            else:
                merged.append(interval)

        return merged
        