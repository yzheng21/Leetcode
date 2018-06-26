'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

'''
题解：如果左子树高度和右子树高度差小于等于1，并且左子树是平衡树，右子树是平衡树，那么这棵树是平衡树。那么我们先用一个新的函数返回树的高度和是否平衡树。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def solve(root):
            if root == None:
                return 0
            left_h, right_h = map(solve,[root.left,root.right])
            if left_h < 0 or right_h < 0 or abs(left_h-right_h) > 1:
                return -1
            return max(left_h,right_h) + 1
        return (solve(root) >= 0)