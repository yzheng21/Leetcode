class solution1:
    def maxkilled(self,grid):
        m,n = len(grid), 0
        if m:
            n = len(grid[0])
        result, rows = 0, 0
        cols = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rows = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            rows += 1

                if i == 0 or grid[i - 1][j] == 'W':
                    cols[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            cols[j] += 1

                if grid[i][j] == '0' and rows + cols[j] > result:
                    result = rows + cols[j]

        return result


class solution2:
    def killed(self,grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        up = [[None for j in range(n)] for i in range(m)]
        down = [[None for j in range(n)] for i in range(m)]
        left = [[None for j in range(n)] for i in range(m)]
        right =[[None for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                up[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        up[i][j] = 1
                    if i - 1 >= 0:
                        up[i][j] += up[i-1][j]

        for i in range(m):
            for j in range(n):
                down[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        down[i][j] = 1
                    if i + 1 < m:
                        down[i][j] += down[i+1][j]

        for i in range(m):
            for j in range(n):
                left[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        left[i][j] = 1
                    if j - 1 >= 0:
                        left[i][j] += left[i][j-1]

        for i in range(m):
            for j in range(n):
                right[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        right[i][j] = 1
                    if j + 1 < n:
                        left[i][j] += left[i][j+1]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    t = up[i][j] + down[i][j] + left[i][j] + right[i][j]
                    if t > res:
                        res = t
        return res