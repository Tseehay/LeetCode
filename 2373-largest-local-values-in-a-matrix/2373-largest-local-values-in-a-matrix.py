class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        res=[[0]*(n-2) for k in range(n-2)]
        
        for i in range(n-2):
            for j in range(n-2):
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        res[i][j]=max (res[i][j],grid[r][c])
    
        return res