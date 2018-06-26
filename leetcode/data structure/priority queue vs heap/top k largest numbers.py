'''
Given an integer array, find the top k largest numbers in it.
Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
'''

from queue import PriorityQueue

class solution:
    def topk(self,nums,k):
        q = PriorityQueue()
        result = []
        for num in nums:
            q.put(num)
            if q.qsize() > k:
                q.get()

        while not q.empty():
            result.append(q.get())

        return sorted(result,reverse=True)

s = solution()
print(s.topk([3,10,1000,-99,4,100],3))
