'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example: Given binary tree [1,null,2,3],

1
2 / 3

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def inorderTraversal(self, root):

        res, stack = [], [(1,root)]

        while stack:
            p = stack.pop()
            if not p[1]:
                continue
            if p[0] != 0:
                stack.extend([(1,p[1].right), (0,p[1]), (1,p[1].left)])
            else:
                res.append(p[1].val)
        return res








