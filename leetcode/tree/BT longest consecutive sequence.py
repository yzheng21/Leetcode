class solution(object):

    def longest(self,root):
        self.maxlen = 0

        def dfs(root, cur, target):
            if root == None:
                return 0
            if root.val == target:
                cur += 1
            else:
                cur = 1
            self.maxlen = max(cur,self.maxlen)
            dfs(root.left, cur, root.val+1)
            dfs(root.right, cur, root.val + 1)
            return cur

        dfs(root, 0, root.val)
        return self.maxlen
