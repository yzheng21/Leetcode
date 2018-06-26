class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def level_queue(self,root):
        if root == None:
            return
        stack1 = []
        stack2 = []
        stack1.append(root)
        stack2.append(root)
        while stack1:
            node = stack1.pop(0)
            if node.left:
                stack1.append(node.left)
                stack2.append(node.left)
            if node.right:
                stack1.append(node.right)
                stack2.append(node.right)
        while stack2:
            print(stack2.pop(0).data)