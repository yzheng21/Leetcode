'''
Given a binary tree, flatten it to a linked list in-place.

For example, Given

     1
    / \
   2   5
  / \   \
 3   4   6
The flattened tree should look like:

1
2
3
4
5
6

click to show hints.

Hints: If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        if root.left == None and root.right == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp

'''
首先判断左子树是否为空，不为空就寻找到树根的左孩子节点，然后寻找该节点是否有右孩子，
如果有继续寻找，直到找到属于叶子节点的右孩子，此时，该节点的右子树“指向”当前树的右子树，
并将当前左子树变为树根的右孩子，将整棵树左孩子置为空。最后，根节点“指向”根节点的右孩子，
继续上述操作，直到整棵树遍历完即得到结果。
'''
