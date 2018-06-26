'''
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island.
If two 1 is adjacent, we consider them in the same island.
We only consider up/down/left/right adjacent.
Find the number of islands.
Example
Given graph:
[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
'''

class solution:
    def numberislands(self,grid):
        class union_find:
            def __init__(self, n):
                self.father = [i for i in range(n)]
                self.count = 0

            # O(1)
            def connect(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)
                if root_a != root_b:
                    self.father[root_a] = root_b
                    self.count -= 1

            # O(1)
            def query(self):
                return self.count

            def find(self, x):
                if self.father[x] == x:
                    return x
                self.father[x] = self.find(self.father[x])
                return self.father[x]

            def set_count(self,total):
                self.count = total

        m,n = len(grid),len(grid[0])
        if not grid or m == 0 or n == 0:
            return 0
        total_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total_islands += 1
        union = union_find(m*n)
        union.set_count(total_islands)
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    for i in range(4):
                        new_x = x + dx[i]
                        new_y = y + dy[i]
                        if 0<new_x<m and 0<new_y<n and grid[new_x][new_y]:
                            union.connect(x*n+y,new_x*n+new_y)
        return union.query()

    