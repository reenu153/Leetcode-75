class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0
        flag=True
        strlen= len(t)
        strlen2= len(s)
        if strlen2==0:
            return True
        if strlen==0:
            return False
        for i in range(0,strlen2):
                print(j)
                while(t[j]!=s[i] and j<strlen-1):
                    j+=1
                if(t[j]==s[i]):
                    print(t[j])
                    j+=1
                else:
                    flag=False
                    break
                if j>strlen-1:
                    break

        if i==strlen2-1 and flag==True:
            return True
        else:
            return False
                


        