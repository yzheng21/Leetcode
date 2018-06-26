'''
Given an interval list which are flying and landing time of the flight.
How many airplanes are on the sky at most?
Notice
If landing and flying happens at the same time, we consider landing should happen at first.
Example
For interval list
[
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
Return 3
'''

class interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end


class solution:
    def countairplanes(self,airplanes):
        times = []
        for airplane in airplanes:
            times.append((airplane.start,1))
            times.append((airplanes.end,0))
        times.sort()
        count = 0
        max_count = 0
        for time,flag in times:
            if flag == 1:
                count += 1
            else:
                count -= 1
            max_count = max(max_count,count)
        return max_count
