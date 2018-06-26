class Solution(object):
    def upsideDownBT(self,root):
        if (root == None or (root.left == None and root.right==None)):
            return root
        newroot = self.upsideDownBT(root.left)
        root.left.right = root.right
        root.left.right = root
        root.left = None
        root.right = None

        return newroot

class Solution2(object):
    def upsideBT(self,root):
        node,parent,right = root, None, None
        while(node != None):
            left = node.left
            node.left = right
            right = node.right
            node.right = parent
            parent = node
            node = left
        return parent

