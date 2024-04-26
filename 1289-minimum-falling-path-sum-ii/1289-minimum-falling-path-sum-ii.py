class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = {}
        def optimal(row, col):
            if row == n - 1:
                return grid[row][col]

            if (row, col) in m:
                return m[(row, col)]

            next_min= inf
            for next_row_col in range(n):
                if next_row_col != col:
                    next_min = min(next_min, optimal(row + 1, next_row_col))

            m[(row, col)] = grid[row][col] + next_min
            return m[(row, col)]

        answer = inf
        for col in range(n):
            answer = min(answer, optimal(0, col))

        return answer