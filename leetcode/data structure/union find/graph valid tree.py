'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Notice
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Have you met this question in a real interview? Yes
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
'''

class solution:
    def validtree(self,n,edges):
        class union_find:
            def __init__(self,n):
                self.father = [i for i in range(n)]
                self.count = n

            def connect(self,a,b):
                root_a = self.find(a)
                root_b = self.find(b)
                if root_a != root_b:
                    self.father[root_a] = root_b
                    self.count -= 1

            def find(self,x):
                if self.father[x] == x:
                    return x
                self.father[x] = self.find(self.father[x])
                return self.father[x]

            def query(self):
                return self.count

        if n != len(edges) + 1:
            return False
        union = union_find(n)
        for a,b in edges:
            union.connect(a,b)

        return union.query() == 1
