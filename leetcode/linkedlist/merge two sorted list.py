class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

class solution:
    def merge(self,head1,head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        return dummy.next
