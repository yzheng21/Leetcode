class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def serialize(self,root):
        if root is None:
            return
        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1

        while queue[-1] is None:
            queue.pop()

        return [str(node.val) if node is not None else '#' for node in queue]

    def deserialize(self,data):
        data = data.strip('\n')
        if data == '{}':
            return None
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftchild = True
        index = 0
        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if isLeftchild:
                    queue[index].left = node
                else:
                    queue[index].right = node
            if not isLeftchild:
                index += 1
            isLeftchild = not isLeftchild

        return root
