# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution(object):

    def strtotree(self,s):
        if s is None or len(s) == 0:
            return None
        if s[0] == '(' and s[-1] == ')': s = s[1:-1]
        i = s.find('(')
        if i == -1: i = len(s)
        node = TreeNode(int(s[0:i]))
        count = 0
        j = i
        while (j < len(s)):
            if s[j] == '(':
                count += 1
            elif s[j] == ')':
                count -= 1
                if count == 0:
                    j += 1
                    break
            j += 1
        node.left = self.strtotree(s[i:j])
        node.right = self.strtotree(s[j:])
        return node

s = '4(2(3)(1))(6(5))'
print(solution().strtotree(s))
##solution2
# class Solution2(object):
#     def str2tree(self, s):
#         """
#         :type s: str
#         :rtype: TreeNode
#         """
#         def str2treeHelper(s, i):
#             start = i
#             if s[i] == '-': i += 1
#             while i < len(s) and s[i].isdigit(): i += 1
#             node = TreeNode(int(s[start:i]))
#             if i < len(s) and s[i] == '(':
#                 i += 1
#                 node.left, i = str2treeHelper(s, i)
#                 i += 1
#             if i < len(s) and s[i] == '(':
#                 i += 1
#                 node.right, i = str2treeHelper(s, i)
#                 i += 1
#             return node, i
#
#         return str2treeHelper(s, 0)[0] if s else None
#
#
#
