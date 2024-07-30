import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nor_mat=[]
        matrix=[]
        
        for sub in mat:
            for item in sub:
                nor_mat.append(item)
        if len(nor_mat)!=r*c:
            return mat
        else:
            for i in range(0,len(nor_mat),c):
                matrix.append(nor_mat[i:i+c])
        return matrix
                
        