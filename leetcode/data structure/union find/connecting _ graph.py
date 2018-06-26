'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
You need to support the following method:
1. connect(a, b), an edge to connect node a and node b
2. query(a), Returns the number of connected component nodes which include node a.
Example
5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3
'''


from collections import defaultdict
class ConnectingGraph:
    def __init__(self,n):
        self.father = [i for i in range(1+n)]
        self.size = [1 for i in range(n+1)]

     #O(1)
    def connect(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    #O(1)
    def query(self,a):
        root_a = self.find(a)
        return self.size[root_a]

    def find(self,x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]