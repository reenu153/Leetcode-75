class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """ 
        start=0
        n=len(gas)
        curr_gas=0
        total_gas=0
        total_cost=0
        for i in range(n):
            total_gas+=gas[i]
            total_cost+=cost[i]
            if curr_gas+gas[i]>=cost[i]:
                curr_gas+=gas[i]-cost[i]
                i=i+1
            else:
                start=i+1
                curr_gas=0
        
        return -1 if total_cost>total_gas else start
            

 

            