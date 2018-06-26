class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

class solution:
    def findmiddle(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

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

    def sortlist(self,head):
        if not head or not head.next:
            return head
        mid = self.findmiddle(head)
        right = self.sortlist(mid.next)
        mid.next = None
        left = self.sortlist(head)
        return self.merge(left,right)