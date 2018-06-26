class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class solution:
    def partition(self, head, x):
        if head is None:
            return head
        ahead, bhead = ListNode(0), ListNode(0)
        a, b = ahead, bhead
        while head:
            if head.val < x:
                a.next = head
                a = a.next
            else:
                b.next = head
                b = b.next
            head = head.next
        b.next = None
        a.next = bhead.next
        return ahead.next