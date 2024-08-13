class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for i in range(length):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

        for i in range(length):
            matrix[i] = matrix[i][::-1]
        