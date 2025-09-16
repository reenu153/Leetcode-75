class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map={'(':')','{':'}','[':']'}
        top=0
        stack=[s[0]]
      
        for i in s[1:]:
            if i not in map.keys():
                if top>-1 and stack[top] in map.keys() and i==map[stack[top]]:
                    stack.pop()
                    top-=1   
                else:
                    return False 
            else:
                stack.append(i)
                top+=1

        return not len(stack)
            
        


            
        