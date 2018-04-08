'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def buildTree(self, preorder, inorder):
        def dfs(pbegin,pend,ibegin,iend):
            if pbegin >= pend:
                return None
            if pbegin +1 == pend:
                return TreeNode(preorder[pbegin])
            i = inorder.index(preorder[pbegin])
            i -= ibegin
            ans = TreeNode(preorder[pbegin])
            ans.left = dfs(pbegin+1,pbegin+i+1,ibegin,ibegin+i)
            ans.right = dfs(pbegin+i+1,pend,ibegin+i+1,iend)
            return ans
        return dfs(0,len(preorder),0,len(inorder))

'''
题解找出前序遍历0位置值对应中序遍历中的位置
'''