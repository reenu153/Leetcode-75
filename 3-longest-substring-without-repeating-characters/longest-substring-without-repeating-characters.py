class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        i=0
        sub=s[0]
        longest=1
        subind={s[0]:0}
        for j in range(1,len(s)):
            if s[j] in sub:
                i=subind[s[j]]+1
                subind[s[j]]=j
                sub=s[i:j+1]
            else:
                sub=sub+s[j]
                subind[s[j]]=j
            if len(sub)>longest:
                    longest=len(sub)
        
        return longest

