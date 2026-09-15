class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #reverse rows, then take transpose
        n=len(matrix)
        i,j=0,n-1

        #swap rows
        while(i<j):
            matrix[i],matrix[j]=matrix[j],matrix[i]
            i+=1
            j-=1
        
        #transpose

        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        return matrix