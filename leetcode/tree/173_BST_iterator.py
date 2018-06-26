class BSTIterator:
    # @param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.curt = root

    # @return: True if there has next node, or false
    def hasNext(self):
        return self.curt is not None or len(self.stack) > 0

    # @return: return next node
    def next(self):
        self.curt = self.stack.pop()
        nxt = self.curt

        if self.curt.right is not None:
            self.curt = self.curt.right
            while self.curt is not None:
                self.stack.append(self.curt)
                self.curt = self.curt.left

        return nxt