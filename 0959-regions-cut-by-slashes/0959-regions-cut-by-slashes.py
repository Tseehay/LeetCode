class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:   
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                elif grid[i][j] == '\\':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                else:
                    union(root + 0, root + 1)
                    union(root + 1, root + 2)
                    union(root + 2, root + 3)

                if i < n - 1:
                    union(root + 2, (root + 4 * n) + 0)
                if j < n - 1:
                    union(root + 1, (root + 4) + 3)

        return sum(parent[i] == i for i in range(4 * n * n))