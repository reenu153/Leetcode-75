class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words=[]
        stringlen=len(s)
        sub=""
        for i in range(0,stringlen):
            if i==stringlen-1 and s[i]!=" ":
                sub+=s[i]
                words.append(sub)
            if s[i]==" ":
                if sub!="":
                    words.append(sub)
                    sub=""
            else:
                sub+=s[i]
                continue
        print(words)

        length= len(words)
        i=length-1
        reverse=""
        while(i>=0):
            reverse+=words[i]
            if i!=0:
                reverse+=" "
            i-=1
        return reverse.strip()
