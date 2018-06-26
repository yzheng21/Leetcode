'''
1 空节点 （NULL节点） ：  返回空

2 只有根节点：直接返回

3 有个左孩子： 父节点 left 指针 指向 下一个节点 即 左孩子 ，不变

                             right 指针 保持 为空 （注意 不是 循环链表，所以 prev 指针 不用指向 尾节点 ）, 即 父节点 保持 不变

                    左孩子 的 right 指针 指向 父节点 ，left 指针 指向空 不变

4 有个右孩子： 父节点 没有 左孩子，所以 右子树 链表 可以直接 加到 父节点下面 。所以 父节点 的 left 指针 指向 右孩子。right 指针 改为 指向 空

                    右孩子 没有 下一个节点了，所以 left 指针 为空 不变， 由于前面有父节点，所以 right 指针 指向 父节点

5 左右孩子：先转换 左子树，得到 一个双向链表 ，只有一个节点即左孩子，再转换 右节点 同理。

                第二步 将 右子树 的 链表 加到 左子树 的 后面，所以 左孩子的 left 指针 指向 右孩子，右孩子的 right 指针 指向 根节点的左孩子。

                第三步 根节点 作为 左孩子的前一个节点 也就是 整个链表的首节点，right 指针指向空，左孩子的 right 指向 根节点。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def toDlink(self):
        def _(node):
            assert node != None
            if node.left == None and node.right == None:
                return node
            if node.left == None:
                tail = _(node.right)
                node.right.right = node
                node.left = node.right
                node.right = None
            elif node.right == None:
                tail = _(node.left)
                node.left.right = node
            else:
                ltail = _(node.left)
                rtail = _(node.right)
                node.right.right = ltail
                ltail.left = node.right
                node.right = None
                node.left.right = node
                tail = rtail

            return tail





