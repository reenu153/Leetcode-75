#394. Decode String

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def decode(st, count):
            decoded=""
            for i in range(0,int(count)):
                decoded=decoded+st
            return decoded

        digits={'1','2','3','4','5','6','7','8','9','0'}
        count=""
        stack=[]
        top=-1
        for i in s:
            if i == ']':
                sub=""
                while stack[top]!='[':
                    sub=stack.pop()+sub
                    top-=1
                stack.pop()
                top-=1
                while top!=-1 and stack[top] in digits:
                    count=stack.pop()+count
                    top-=1
                print(count, int(count))
                decoded=decode(sub,int(count))
                stack.append(decoded)
                top+=1
                count=""
            else:
                stack.append(i)
                top+=1

        output=""
        for i in stack:
            output+=i

        return output
                
        