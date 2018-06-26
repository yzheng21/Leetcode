#version 1
import collections

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class solution:
    def clonegraph(self,node):
        root = node
        if node is None:
            return node
        nodes = self.getNodes(node)
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.lael)

        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    #通过node的邻居找到所有的nodes
    def getNodes(self,node):
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result

#version2
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        if node == None:
            return None
        if node.label in self.dict:
            return self.dict[node.label]
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))
        return root



