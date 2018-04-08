'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def buildTree(self, postorder, inorder):
        def dfs(pbegin,pend,ibegin,iend):
            if pbegin >= pend:
                return None
            if pbegin == pend - 1:
                return TreeNode(postorder[pend-1])
            i = inorder.index(postorder[pend-1])
            i -= ibegin
            ans = TreeNode(postorder[pend - 1])
            ans.left = dfs(pbegin,pbegin+i,ibegin,ibegin+i)
            ans.right = dfs(pbegin+i,pend-1,ibegin+i+1,iend)
            return ans
        return dfs(0,len(postorder),0,len(inorder))