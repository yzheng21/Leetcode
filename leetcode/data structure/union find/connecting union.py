'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected
Have you met this question in a real interview? Yes
Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
'''

#union find
from collections import defaultdict
class ConnectingGraph:
    def __init__(self,n):
        self.father = [i for i in range(1+n)]

     #O(1)
    def connect(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
    #O(1)
    def query(self,a,b):
        return self.find(a) == self.find(b)

    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]


#BFS
from collections import defaultdict,deque
class ConnectingGraph_BFS:
    def __init__(self,n):
        self.mapping = defaultdict(set)

    def connect(self,a,b):
        self.mapping[a].add(b)
        self.mapping[b].add(a)

    def query(self,a,b):
        queue = deque([a])
        visited = set([a])
        while queue:
            node = queue.popleft()
            if node == b:
                return True
            neighbors = self.mapping[node]
            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return False


