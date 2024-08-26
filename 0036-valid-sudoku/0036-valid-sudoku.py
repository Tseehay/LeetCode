class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(a):
            s=set()
            for i in a:
                if i=='.':
                    continue
                if i in s:
                    return False
                s.add(i)
            return True
        
        for row in board:
            if not check(row):
                return False
        
        for i in range(9):
            column=[]
            for j in range(9):
                column.append(board[j][i])
            if not check(column):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                square=[]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        square.append(board[k][l])
                if not check(square):
                    return False
        return True