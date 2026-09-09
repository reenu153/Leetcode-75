class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows,cols=len(heights),len(heights[0])
        pac,atl=[],[]

        def dfs(r,c,visit,prevHeight):
            if (r,c)in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c]<prevHeight:
                return
            visit.append((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for c in range(cols): #only border rows
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        for r in range(rows): #only border rows
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        atl=set(atl)
        res=[]
        for el in pac:
            if el in atl:
                res.append(el)
        
        return res
