class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstrow = False

        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i>0:
                        matrix[i][0]=0
                    else:
                        firstrow = True
                    matrix[0][j]=0

        
        for i in range(1,m):
            if matrix[i][0]==0:
                matrix[i]=[0]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[0][j]==0:
                    matrix[i][j]=0

        if firstrow==True:
            matrix[0]=[0]*n
