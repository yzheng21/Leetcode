class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

class solution:
    def reverse(self,head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def findkth(self, head, k):
        for i in range(k):
            head = head.next
            if head is None:
                return None
        return head

    def main(self,head,m,n):
        dummy = ListNode(0)
        m_prev = self.findkth(dummy,m-1)
        m = m_prev.next
        n = self.findkth(dummy,n)
        n_next = n.next
        n.next = None

        self.reverse(m)
        m_prev.next = n
        m.next = n_next
        return dummy.next
