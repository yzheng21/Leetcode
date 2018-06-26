class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None

class solution:
    def maxtree(self,nums):
        stack = []
        for num in nums:
            node = TreeNode(num)
            if stack and num > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

    def maxtree_dfs(self,A):
        if not A or len(A) == 0:
            return
        return self.dfs_helper(A,0,len(A))

    def dfs_helper(self,A,left,right):
        if left > right:
            return
        max_value, max_idx = float('-inf'), None
        for i in range(left,right):
            if A[i] >= max_value:
                max_value = A[i]
                max_idx = i
        root = TreeNode(max_value)
        left_node = self.dfs_helper(A,left,max_idx)
        right_node = self.dfs_helper(A,max_idx+1,right)
        root.left = left_node
        root.right = right_node
        return root