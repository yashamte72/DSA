class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        
        for j in cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0



