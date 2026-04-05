class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        queue=deque([(src,0,0)])
        min_cost={src:0}

        while len(queue):
            node,cost,stops=queue.popleft()

            if stops>k:
                continue
            
            for neighbour,price in graph[node]:
                new_cost=cost+price

                if neighbour not in min_cost or new_cost<min_cost[neighbour]:
                    queue.append([neighbour,new_cost,stops+1]) 
                    min_cost[neighbour] = new_cost

        return min_cost[dst] if dst in min_cost else -1
        