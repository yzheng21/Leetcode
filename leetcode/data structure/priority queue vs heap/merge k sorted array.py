'''
Given k sorted integer arrays, merge them into one sorted array.
Example
Given 3 sorted arrays:
[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
'''

from heapq import heappush, heappop
class Solution:

    def mergeksortedarray(self,arrays):
        if not arrays or len(arrays) == 0:
            return []
        result = []
        min_heap = []
        for i,array in enumerate(arrays):
            if len(array) != 0:
                heappush(min_heap,(array[0],i,0))
        while min_heap:
            value,x,y = heappop(min_heap)
            result.append(value)
            if y+1 < len(arrays[x]):
                heappush(min_heap,(arrays[x][y+1],x,y+1))
        return result