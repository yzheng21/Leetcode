'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example: Given binary tree [3,9,20,null,null,15,7],

3
/
9 20 /
15 7

return its zigzag level order traversal as:

[ [3], [20,9], [15,7] ]
'''
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def bfs(root,level):
            if root:
                if len(ans) < level+1:
                    ans.append([])
                ans[level].append(root.val)
                bfs(root.left, level+1)
                bfs(root.right, level+1)
        bfs(root,0)
        i=1
        while i < len(ans):
            ans[i].reverse()
            i += 2
        return ans
