class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels={'A','E','I','O','U','a','e','i','o','u'}
        count=0
        length=len(s)
        is_vowel= s[0] in vowels
        for i in range(0,k):
            if s[i] in vowels:
                count+=1
        max_count=count

        i=k
        j=1
        while(i<length):
            if is_vowel:
                count-=1
            if s[i] in vowels:
                count+=1
            is_vowel=s[j] in vowels
            if count>max_count:
                max_count=count
            i+=1
            j+=1
        
        return max_count
