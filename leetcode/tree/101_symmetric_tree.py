'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

1
/
2 2 / \ /
3 4 4 3

But the following [1,2,2,null,3,null,3] is not:

1
/
2 2 \
3 3

Note: Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, node):
        """
       :type root: TreeNode
       :rtype: bool
       """
        def helper(root, mirror):
            if not root and not mirror:
                return True
            if root and mirror and root.val == mirror.val:
                return helper(root.left,mirror.right) and helper(root.right, mirror.left)
            return False
        return helper(node, node)