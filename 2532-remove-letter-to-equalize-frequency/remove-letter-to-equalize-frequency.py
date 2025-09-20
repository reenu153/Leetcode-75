class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        map=defaultdict(int)

        for i in word:
            map[i]+=1

        freq=sorted(map.values())

        if len(set(freq))>2:
            return False
        # if len(set(freq))<2:
        #     return freq[0]==1

        print(freq)
        pos1=sorted(map.values())
        if pos1[0]>1:
            pos1[0]-=1
        else:
            del pos1[0]
        if len(set(pos1))==1:
            return True
        print(pos1,freq)
        if freq[-1]>1:
            freq[-1]-=1
        else:
            del freq[-1]
        if len(set(freq))==1:
            return True
        return False







