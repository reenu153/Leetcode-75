class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #backtracking - binary decision tree with path including and excluding elements to avoid duplicates

        track=[]
        res=[]

        def backtrack(i, track):
            #base case
            # if candidates list is exhausted return

            if i>=len(candidates) or sum(track)>target:
                return 

            if sum(track)==target:
                res.append(track.copy())
                return 

            track.append(candidates[i])
            backtrack(i, track)
            track.pop()
            backtrack(i+1,track)

        backtrack(0,track)  
        return res
                





