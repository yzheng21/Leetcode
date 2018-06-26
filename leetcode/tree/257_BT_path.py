'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

1 /
2 3
5

All root-to-leaf paths are: ["1->2->5", "1->3"]

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def helper(root, path, res):
            if root:
                path.append(str(root.val))
                left = helper(root.left,path,res)
                right = helper(root.right, path, res)
                if not left and not right:   #leaf
                    res.append('->'.join(path))
                path.pop()    #take the last path out
                return True
            res = []
            helper(root,[],res)
            return res