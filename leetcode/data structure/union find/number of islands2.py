'''
Given a n,m which means the row and column of the 2D matrix
and an array of pair A( size k).
Originally, the 2D matrix is all 0 which means there is only sea in the matrix.
The list pair has k operator and each operator has two integer A[i].x, A[i].y
means that you can change the grid matrix[A[i].x][A[i].y] from sea to island.
Return how many island are there in the matrix after each operator.
 Notice
0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
Have you met this question in a real interview? Yes
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].
return [1,1,2,2].
'''


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

    def set_count(self, total):
        self.count = total

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class solution:
    def is_bound(self, x, y, grid):
        n = len(grid)
        m = len(grid[0])
        return 0 <= x <= n - 1 and 0 <= y <= m - 1

    def numberofislands_2(self,n,m,operators):
        if n == 0 or m == 0 or not operators or len(operators) == 0:
            return []
        total = 0
        result = []
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        grid = [[0]*m for i in range(n)]
        union = union_find(n*m)
        for point in operators:
            x,y = point.x,point.y
            if grid[x][y] != 1:
                total += 1
                grid[x][y] = 1
                union.set_count(total)

                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if self.is_bound(new_x,new_y) and grid[new_x][new_y] == 1:
                        union.connect(x*m+y,new_x*m+new_y)
            total = union.query()
            result.append(total)
        return result