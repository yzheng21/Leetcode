'''
There are two properties in the node student id and scores,
to ensure that each student will have at least 5 points,
find the average of 5 highest scores for each person.
Have you met this question in a real interview? Yes
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
Return
'''

class record:
    def __init__(self,id,score):
        self.id = id
        self.score = score

from heapq import heappop,heappush
from collections import defaultdict

class solution:
    def score(self,records):
        scores = defaultdict(list)
        for record in records:
            heappush(scores[record.id],record.score)
            if len(scores[record.id]) > 5:
                heappop(scores[record.id])
        avg = {}
        for id in scores:
            avg[id] = sum(scores[id]) / 5.0
        return avg