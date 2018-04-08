'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example: Given the below binary tree and sum = 22,

          5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
return

[ [5,4,11,2], [5,8,4,5] ]
'''
class Solution(object):
    def PathSum(self,root,sum):
        if root == None:
            return []
        ans = []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[sum]]
            else:
                return []
        l, r = self.PathSum(root.left,sum-root.val), self.PathSum(root.right,sum-root.val)
        for i in l:
            ans.append([root.val]+i)
        for i in r:
            ans.append([root.val]+i)
        return ans