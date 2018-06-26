class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

class solution:
    def hascycle(self,head):
        if head is None or head.next is None:
            return None
        fast = head.next
        slow = head
        while fast != slow:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next

        #返回起点然后看看何时与慢指针相遇，像相遇点就是环的入口
        while head != slow.next:
            head = head.next
            slow = slow.next
        return head