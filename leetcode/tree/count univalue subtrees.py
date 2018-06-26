# Time:  O(n)
# Space: O(h)
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class solution(object):
    def countunival(self,root):
        [isuni,count] = self.isunival(root,0)
        return count

    def isunival(self,root,count):
        if not root:
            return [True,count]

        [left,count] = self.isunival(root.left,count)
        [right,count] = self.isunival(root.right,count)
        if self.isSame(root,root.left,left) and self.isSame(root,root.right,right):
            count += 1
            return [True,count]
        return [False,count]

    def isSame(self,root,child,isuni):
        return not child or (isuni and root.val == child.val)
