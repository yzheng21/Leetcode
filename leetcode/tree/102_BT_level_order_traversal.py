'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example: Given binary tree [3,9,20,null,null,15,7],

3
/
9 20 /
15 7

return its level order traversal as:

[ [3], [9,20], [15,7] ]
'''

class Solution(object):
    def preorder(self,root,level,res):
        if root:
            if len(res)<level+1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left,level+1,res)
            self.preorder(root.right,level+1,res)

    def levelOrder(self, root):
        res = []
        self.preorder(root, 0, res)
        return res




