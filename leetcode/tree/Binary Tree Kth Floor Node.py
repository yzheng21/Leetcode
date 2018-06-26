'''
Run a level order traversal (BFS) untill level k.


'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def kthfloornode(self,root,k):
        if root == None:
            return 0
        q = [root]
        level = 0
        while q:
            next_q = []
            if level == k:
                return len(q)
            for i in q:
                if i.left:
                    next_q.append(i.left)
                if i.right:
                    next_q.append(i.right)
            q = next_q
            level += 1
        return 0


