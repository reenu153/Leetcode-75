class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen=maxFreq=0
        left=right=0
        n=len(s)
        freq=[0]*26

        while right<n:
            ch=s[right]
            freq[ord(ch)-ord('A')]+=1
            if freq[ord(ch)-ord('A')]>maxFreq:
                maxFreq=freq[ord(ch)-ord('A')]
            if ((right-left+1)-maxFreq) <=k:         
                if(right-left+1)>=maxLen:
                    maxLen=right-left+1
            else:
                freq[ord(s[left])-ord('A')]-=1
                left+=1
            right+=1
        

        return maxLen
        
                
