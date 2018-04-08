'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example: Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

class Solution(object):
    def hasPathSum(self,root,sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        if root.left == None:
            return self.hasPathSum(root.right,sum-root.val)
        if root.right == None:
            return self.hasPathSum(root.left, sum-root.val)
        return self.hasPathSum(root.right,sum-root.val) or self.hasPathSum(root.left, sum-root.val)