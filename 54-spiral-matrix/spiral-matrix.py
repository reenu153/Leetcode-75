class Solution:


    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    

        r,c,n,m=0,0,len(matrix)-1,len(matrix[0])-1
        res=[]
        while(r<=n and c<=m):
            for i in range(c,m+1):
                res.append(matrix[r][i])
            r+=1
            for i in range(r,n+1):
                res.append(matrix[i][m])
            m-=1
            for i in range(m,c-1,-1):
                res.append(matrix[n][i])
            n-=1
            for i in range(n,r-1,-1):
                res.append(matrix[i][c])
            c+=1
        return res[:len(matrix)*len(matrix[0])]
        
