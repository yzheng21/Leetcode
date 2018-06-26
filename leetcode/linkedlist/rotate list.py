'''
使用快慢指针的思路，让fast先走K步，然后快慢一起走，这样就能找到倒数第k个节点，slow.next为后面部分的表头，
slow.next = None,前后分开。 但是我们需要考虑k的大小，如果k>链表的长度，我们就不旋转了， k = k%len(list)
'''
class solution:
    def rotatelist(self,head,k):
        if head is None or k == 0:
            return head
        fast = head
        slow = head
        n = 0
        while fast:
            fast = fast.next
            n += 1
        k %= n
        if k == 0: return head
        fast = head
        while k>0:
            fast = fast.next
            k -= 1
        while fast.next:
            fast = fast.next
            slow =slow.next

        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead

class solution2:
    def rotatelist(self,head,k):
        if head is None or k == 0:
            return head
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        cur.next = head   #变成一个环
        m = n - k % n
        for i in range(m):   #寻找起始点的结点
            cur = cur.next

        newhead = cur.next
        cur.next = None
        return newhead