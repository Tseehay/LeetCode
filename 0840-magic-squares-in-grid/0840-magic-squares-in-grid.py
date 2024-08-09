class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid),len(grid)
        res=0
        pattern1="438167294381672"
        pattern2="927618349276183"
        
        def magic(r,c):
            if grid[r][c]!=5:
                return 0
            neighbors=[
                [r-1,c],[r-1,c+1],
                [r,c+1],[r+1,c+1],
                [r+1,c],[r+1,c-1],
                [r,c-1],[r-1,c-1]
            ]
            seq=""
            for nr,nc in neighbors:
                seq+=str(grid[nr][nc])
            if seq in pattern1 or seq in pattern2:
                return 1
            return 0
        for r in range(1,rows-1):
            for c in range(1,cols-1):
                res+=magic(r,c)
                
        return res
        