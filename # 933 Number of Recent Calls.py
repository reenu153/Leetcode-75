# 933. Number of Recent Calls

class RecentCounter(object):

    def __init__(self):
        self.counter=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        print(t)
        while len(self.counter) and self.counter[0]<(t-3000):
            del self.counter[0]
        self.counter.append(t)

        return len(self.counter)


        