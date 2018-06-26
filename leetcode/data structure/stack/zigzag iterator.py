'''
Given two 1d vectors, implement an iterator to return their elements alternately.
Example
Given two 1d vectors:
v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''

from collections import deque
v1 = [1,2]
v2 = [3,4,5,6]
queue = deque([v for v in (v1,v2) if v])
v = queue.popleft()
queue.append(v)
print(queue.popleft())
class zigzagIterator:
    def __init__(self,v1,v2):
        self.queue = deque([v for v in (v1,v2) if v])

    def next(self):
        v = self.queue.popleft()
        value = v.pop(0)
        if len(v) != 0:
            self.queue.append(v)
        return v

    def hasnext(self):
        return len(self.queue) != 0
