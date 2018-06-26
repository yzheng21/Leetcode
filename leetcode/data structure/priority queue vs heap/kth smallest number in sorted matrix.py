"""
Find the kth smallest number in at row and column sorted matrix.
Example
Given k = 4 and a matrix:
[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
Challenge
Solve it in O(k log n) time where n is the bigger one between row size and column size.
"""

from heapq import heappop, heappush
class Solution:
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for i in range(m)]
        visited[0][0] = True
        min_heap = []
        heappush(min_heap,(matrix[0][0],0,0))
        for step in range(k):
            kth,x,y = heappop(min_heap)
            dx = [1,0]
            dy = [0,1]
            for i in range(2):
                newx = x + dx[i]
                newy = y + dy[i]
                if not visited[newx][newy] and  0 < newx < m and 0 < newy < n:
                    visited[newx][newy] = True
                    heappush(min_heap,(matrix[newx][newy],newx,newy))
        return kth