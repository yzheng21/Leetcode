'''
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0
(the number zero, one, two),
find a place to build a post office so that the sum of the distance
from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

Notice

You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.

Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1),
the distance that post office to all the house sum is smallest.)

Challenge
Solve this problem within O(n^3) time.

'''

HOUSE = 1
WALL = 2
EMPTY = 0
MAXMIUM = float('inf')
from collections import deque
class Solution:
    """
    @param: grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        dist = [[MAXMIUM for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = MAXMIUM
        buildings = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1

        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        print(reachable_count)
        print(dist)
        return min_dist if min_dist != MAXMIUM else -1

    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = deque([(i, j, 0)])
        dx = [1, -1, 0, 0]
        dy = [0, 0 , 1, -1]

        while q:
            i, j, l = q.popleft()
            if dist[i][j] == MAXMIUM:
                dist[i][j] = 0
            dist[i][j] += l

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if self.is_unvisited_and_bound(nx,ny,visited):
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l + 1))
                        reachable_count[nx][ny] += 1

    def is_unvisited_and_bound(self, x, y, visited):
        m = len(visited)
        n = len(visited[0])
        if 0 <= x <= m - 1 and 0 <= y <= n - 1:
            return not visited[x][y]
        return False


def main():

    grid = [[0, 1, 0, 0, 0],
            [1, 0, 0, 2, 1],
            [0, 1, 0, 0, 0]]
    s = Solution()
    print(s.shortestDistance(grid))


if __name__ == '__main__':
    main()