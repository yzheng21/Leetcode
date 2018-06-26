class solution:
    def reorder(self, head):
        if head is None or head.next is None:
            return None
        preslow = None
        slow, fast = head, head
        while fast and fast.next:
            preslow = slow
            slow = slow.next
            fast = fast.next.next
        preslow.next = None   #前半段

        #反转后半部分
        pre = slow
        cur = pre.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        slow.next = None

        #fast > 1 > 2
        #pre > 5 > 4 > 3
        #合并
        fast = head
        preslow = None
        while fast:
            temp = pre.next
            pre.next = fast.next   # 5 > 2
            fast.next = pre        # 1 > 5
            fast = pre.next        # fast下移一位fast = 2
            preslow = pre          # 将pre保存
            pre = temp             # 将此时的pre下移一位pre = 4
        if pre:                    # 如果后面多一个，只要将多出的pre = 3 放入到preslow的后面
            preslow.next = pre

