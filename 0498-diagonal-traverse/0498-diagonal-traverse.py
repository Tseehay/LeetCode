class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []

        for d in range(rows + cols - 1):
            if d % 2 == 0:
                for i in range(min(d, rows - 1), max(-1, d - cols), -1):
                    result.append(mat[i][d - i])
            else:
                for i in range(max(0, d - cols + 1), min(d + 1, rows)):
                    result.append(mat[i][d - i])

        return result