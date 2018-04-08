'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example: Given the below binary tree,

   1
  / \
 2   3
Return 6.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    current_max = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.current_max

    def dfs(self, root):
        if root == None:
            return 0
        l, r = map(self.dfs,[root.left, root.right])
        if not l or l < 0:
            l = 0
        if not r or r < 0:
            r = 0
        self.current_max = max(l+r+root.val, self.current_max)
        return max(l,r) + root.val     #返回当前父节点提供的最大路径

