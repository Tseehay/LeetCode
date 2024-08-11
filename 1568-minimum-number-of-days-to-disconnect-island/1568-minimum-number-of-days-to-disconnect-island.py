class Solution(object):
    def minDays(self, grid):
        def countIslands():
            visited = [[False] * n for _ in range(m)]
            islands = 0
            
            def dfs(x, y):
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)
            return islands
        
        m, n = len(grid), len(grid[0])

        if countIslands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if countIslands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2