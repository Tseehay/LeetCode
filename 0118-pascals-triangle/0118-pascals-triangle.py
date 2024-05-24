class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for _ in range(1, numRows):
            row = [1] + [triangle[-1][j] + triangle[-1][j + 1] for j in range(len(triangle[-1]) - 1)] + [1]
            triangle.append(row)

        return triangle[:numRows]