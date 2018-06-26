class solution(object):
    def zombie(self,grid):
        sum_zombie = 0
        sum_wall = 0
        n = len(grid)
        m = len(grid[0])
        qzombie = []
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    qzombie.append([i,j,0])
                    sum_zombie += 1
                elif grid[i][j] == 2:
                    sum_wall += 1

        step = 0
        while qzombie:
            p = qzombie.pop(0)
            for i in range(4):
                x = p[0] + dx[i]
                y = p[1] + dy[i]
                if not (0 <= x <= n and 0 <= y <= m):
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    qzombie.append([x,y,p[2]+1])
                    sum_zombie += 1
            if not qzombie:
                step = p[2]
        if sum_zombie + sum_wall != n * m:
            return -1
        else:
            return step


