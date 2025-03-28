class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        index1=0
        index2=0
        merged=""
        len1= len(word1)
        len2= len(word2)
        length= len2 if len1>len2 else len1
        for i in range(0,length):
            merged=merged+word1[i]+word2[i]
        if(len1>len2):
            merged=merged+word1[len2:len1]
        else:
            merged=merged+word2[len1:len2]
        return merged