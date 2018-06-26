#bfs version
import collections
from queue import Queue
class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        if len(edges) != n-1:
            return False

        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        visited = {}
        queue = Queue()
        queue.put(0)
        visited[0] = True
        while not queue.empty():
            cur = queue.get()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.put(node)
        return len(visited) == n

#union find version
class solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        root = [i for i in range(n)]
        for i in edges:
            root1 = self.find(root,i[0])
            root2 = self.find(root,i[1])
        if root1 == root2:
            return False
        else:
            root[root1] = root2
        return len(edges) == n-1

    def find(self,root,e):
        if root[e] == e:
            return e
        else:
            root[e] = self.find(root,root[e])
            return root[e]
