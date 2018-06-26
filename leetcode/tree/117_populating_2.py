'''
Follow up for problem "Populating Next Right Pointers in Each Node". What if the given tree could be any binary tree? Would your previous solution still work?

Note: You may only use constant extra space.

For example, Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        tmp1: the first pointer of this level
        tmp2: the first pointer of next level
        """
        if root:
            tmp, tmp1, tmp2 = root, None, None
            while tmp:
                if tmp.left:
                    if tmp1:
                        tmp1.next = tmp.left
                    tmp1 = tmp.left
                    if not tmp2:
                        tmp2 = tmp1
                if tmp.right:
                    if tmp1:
                        tmp1.next = tmp.right
                    tmp1 = tmp.right
                    if not tmp2:
                        tmp2 = tmp1
                tmp = tmp.next      #isnull?
            self.connect(tmp2)
