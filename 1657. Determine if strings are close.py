from collections import Counter, defaultdict

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        len1=len(word1)
        len2=len(word2)
        if len1!=len2:
            return False
        
        d1=defaultdict(int)
        d2=defaultdict(int)

        for i in range(0,len1):
            d1[word1[i]]+=1
            d2[word2[i]]+=1

        keys1=Counter(d1.keys())
        keys2=Counter(d2.keys())
        val1=Counter(d1.values())
        val2=Counter(d2.values())

        print(d1,d2)

        return keys1==keys2 and val1==val2