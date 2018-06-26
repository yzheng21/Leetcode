"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if left:
            self.dfs(left)
        if right:
            self.dfs(right)
