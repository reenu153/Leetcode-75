class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        # tasks= sorted(tasks, reverse=True)
        # workers= sorted(workers, reverse=True)
        # max_count=0
        # tasks_copy=tasks[:]
        # offset=0
        # while(len(tasks_copy)):
        #     pills_local=pills
        #     workers_copy=workers[:]
        #     count=0
        #     for i in tasks_copy:
        #         if len(workers_copy) and workers_copy[0]>=i:
        #             count+=1
        #             workers_copy.pop(0)
        #         else:
        #             for w in workers_copy[::-1]:
        #                 if pills_local and w+strength>=i:
        #                     pills_local-=1
        #                     workers_copy.remove(w)
        #                     count+=1
        #                     break
        #     if count>max_count:
        #         max_count=count
        #     offset+=1
        #     tasks_copy=tasks_copy[offset:]
        # return max_count

        def canAssign(tasks, workers, pills):
            workers = deque(workers)
            for i in tasks:
                if len(workers) and workers[0]>=i:
                    workers.popleft()
                else:
                    used=False
                    if pills and workers and workers[-1]+strength>=i:
                        pills-=1
                        workers.pop()
                        used=True
                    else: 
                        for w in reversed(workers):
                            if pills and w+strength>=i:
                                pills-=1
                                workers.remove(w)
                                used=True
                                break
                    
                    if not used:
                            return False
            return True

        tasks.sort()
        workers= sorted(workers, reverse=True)
        left=0
        right=min(len(tasks),len(workers))      
        
        while(left<right):
            mid=(left+right+1)//2
            tasks_copy=tasks[:mid][::-1]
            if(canAssign(tasks_copy,workers[:],pills)):
                left=mid
            else:
                right=mid-1
            
        return left


        