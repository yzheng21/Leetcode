class solution:
    def reverse(self,head):
        cur = None
        while head != None:
            temp = head.next
            head.next = cur
            cur = head
            head = temp
        return cur
