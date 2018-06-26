class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

class solution:
    def swap(self,head,v1,v2):
        dummy = ListNode(0)
        dummy.next = head
        pre, cur, p1, p2 = dummy, dummy, None, None
        while cur.next:
            if cur.next.val == v1 or cur.next.val == v2:
                if p1:
                    p1 = cur.next
                    pre = cur
                else:
                    temp = cur.next.next
                    p2 = cur.next
                    pre.next = p2
                    if cur == p1:
                        p2.next = p1
                        p1.next = temp
                    else:
                        p2.next = p1.next
                        cur.next = p1
                        p1.next = temp
                    return dummy.next
            cur = cur.next
        return dummy.next