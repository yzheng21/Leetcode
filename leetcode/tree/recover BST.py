class Solution_iterative:
    def recoverTree(self, root):
        first = second = pre = None
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre and pre.val > node.val:
                if first is None:
                    first = pre
                second = node
            pre = node
            node = node.right
        first.val, second.val = second.val, first.val

class Solution_recursive:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.pre = None, None, None
        def inorder(root):
            if root:
                inorder(root.left)
                if self.pre and self.pre.val > root.val:
                    if self.first is None:
                        self.first = self.pre
                    self.second = root
                self.pre = root
                inorder(root.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val