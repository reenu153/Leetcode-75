class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        leng=len(s)
        stripped=""

        for i in range(0,leng):
            if s[i]!='*':
                stripped=stripped+s[i]
            else:
                stripped=stripped[:-1]
        
        return stripped
            