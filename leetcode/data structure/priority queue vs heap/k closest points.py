'''
Given some points and a point origin in two dimensional space,
find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance,
sorted by x-axis, otherwise sorted by y-axis.
Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
'''

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'


from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def get_distance(self, point, origin):
        return abs(point.x - origin.x) ** 2 + abs(point.y - origin.y) ** 2

    def kclosest_hash(self,points,origin,k):
        result = []
        distances = defaultdict(list)
        for point in points:
            dist = self.get_distance(point,origin)
            distances[dist].append((point.x,point.y))
        i = 1
        for distance in sorted(distances.keys()):
            points = distances[distance]
            for x,y in sorted(points):
                result.append(Point(x,y))
                if i == k:
                    return result
                i += 1

    def kclosest_heap(self,points,origin,k):
        max_heap = []
        result = []

        for point in points:
            dist = self.get_distance(point,origin)
            if len(max_heap) < k:
                heappush(max_heap,[-dist,point.x,point.y])
            else:
                if dist < -max_heap[0][0]:
                    heappop(max_heap)
                    heappush(max_heap,[-dist,point.x,point.y])
                elif dist == -max_heap[0][0]:
                    if point.x < max_heap[0][1]:
                        heappop(max_heap)
                        heappush(max_heap, [-dist, point.x, point.y])
                    elif point.x == max_heap[0][1]:
                        if point.y < max_heap[0][2]:
                            heappop(max_heap)
                            heappush(max_heap, [-dist, point.x, point.y])

            for i in range(k):
                max_heap[i][0] = -max_heap[i][0]

            for dist,x,y in sorted(max_heap):
                result.append(Point(x,y))
            return result


