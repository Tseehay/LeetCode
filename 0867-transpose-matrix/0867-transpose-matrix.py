class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tran=[[matrix[j][i] for j in range(len(matrix))]for i in range(len(matrix[0]))]
        return tran
    
        
            