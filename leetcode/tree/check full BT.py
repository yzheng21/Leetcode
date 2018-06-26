class solution():
    def isfulltree(self,root):
        if root is None:
            return True
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        isleft = self.isfulltree(root.left)
        isright = self.isfulltree(root.right)

        return isleft and isright