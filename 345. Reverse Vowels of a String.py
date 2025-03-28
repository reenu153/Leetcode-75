class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        indices=[]
        initial={}
        reverse={}
        vowels= {'a','e','i','o','u','A','E','I','O','U'}
        length= len(s)

        if length<=1:
            return s

        for i in range(0, length):
            if s[i] in vowels:
                initial[i]=s[i]
                indices.append(i)
        
        vow_len=len(initial)
        i=0
        j=vow_len-1
        
        if vow_len<=1:
            return s
            

        print(initial)

        while(i<=vow_len/2):            
            key1= indices[i]
            key2= indices[j]
            reverse[key2]=initial[key1]
            reverse[key1]=initial[key2]
            j-=1
            i+=1

            
        
        final=""
        for i in range(0, length):
            if i in initial:
                final+=reverse[i]
            else:
                final+=s[i]

        return final   

