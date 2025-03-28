#735. Astroid Collision

#Todo: cleanup 

class Solution(object):

    def isSignSame(self,a,b):
        sign1pos=a>0
        sign2pos=b>0
        return (sign1pos and sign2pos) or (not sign1pos and not sign2pos)

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack=[asteroids[0]]
        count=1
        leng=len(asteroids)

        for i in range(1,leng):
            check=True
            if not count or self.isSignSame(asteroids[i],stack[count-1]):
                stack.append(asteroids[i])
                count+=1
            else:
                first=stack[count-1]
                second=asteroids[i]
                stackOnly=False
                while(check):  
                        #  check if first number is going to left and second to right
                        sign1pos=first>0
                        if not sign1pos:
                            if not stackOnly:
                                stack.append(second)
                                count+=1
                            break
                        if abs(second)==abs(first):
                            stack.pop()
                            if stackOnly:
                                stack.pop()
                                count-=1
                            count-=1      
                        elif abs(second)>abs(first):
                            stack.pop()
                            if stackOnly:
                                stack.pop()
                                count-=1
                            stack.append(second)
                        elif stackOnly:
                            stack.pop()
                            count-=1
                            
                        if count>1:
                            first=stack[count-2]
                            second=stack[count-1]
                            check = not (self.isSignSame(second,first))
                            stackOnly=True
                        else:
                            check=False
                            break

        return stack
                    


