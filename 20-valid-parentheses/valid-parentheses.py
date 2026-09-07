class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map={'(':')','{':'}','[':']'}

        stack=[]
        for let in s:
            if let in map.keys():
                stack.append(let)
            else:
                if len(stack):
                    last=stack.pop()
                    if let!=map[last]:
                        return False
                else:
                    return False

        return not len(stack)


            
        


            
        