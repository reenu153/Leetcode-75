class Solution:
    _longest=0
    _string=""
    def checkPalindrome(self,l,r,s):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1) > self._longest:
                    self._longest=r-l+1
                    self._string=s[l:r+1]
                l=l-1
                r=r+1


    def longestPalindrome(self, s: str) -> str:
        
        for i in range(len(s)):
            #odd
            l=i 
            r=i
            self.checkPalindrome(l,r,s)

            # #even
            l=i
            r=i+1
            self.checkPalindrome(l,r,s)
        
        return self._string
