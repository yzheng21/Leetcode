from queue import Queue


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        if node is None or graph is None or values is None:
            return None
        if values[node] == target:
            return node
        queue = Queue()
        queue.put(node)
        arr = set([node])
        while not queue.empty():
            n = queue.get()
            for root in n.neighbors:
                if values[root] == target:
                    return root
                if root in arr:
                    continue
                else:
                    arr.add(root)
                    queue.put(root)
        return None