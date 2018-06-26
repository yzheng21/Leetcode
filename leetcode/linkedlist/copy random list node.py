# no extra space
class RandomListNode:
    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None

class solution:
    def copynext(self,head):
        while head:
            newnode = RandomListNode(head.label)
            newnode.random = head.random
            newnode.next = head.next
            head.next = newnode
            head = head.next.next

    def copyrandom(self,head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next

    def splitlist(self,head):
        newhead = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return newhead

    def copyrandomlist(self,head):
        if head is None:
            return None
        self.copynext(head)
        self.copyrandom(head)
        return self.splitlist(head)

