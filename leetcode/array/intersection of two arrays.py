'''hashset:
num1 -> n
num2 -> m
binary search: O(nlogn) + O(mlogn) -> O((m+n)logn)
'''

class solution:
    def getintersectionNode(self, head1, head2):
        len1, len2 = 0, 0
        node1, node2 = head1, head2
        # 遍历长度
        while node1:
            len1 += 1
            node1 = node1.next
        while node2:
            len2 += 1
            node2 = node2.next
        #将长的链表向前移动差值(len1-len2)
        node1, node2 = head1, head2
        while len1 > len2:
            node1 = node1.next
            len1 -= 1
        while len2 > len1:
            node2 = node2.next
            len2 -= 1
        #两个指针一起前进，遇到相同的即是交点，如果没找到，返回null.
        while node1:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next
        return None


'''
我们让两条链表分别从各自的开头开始往后遍历，当其中一条遍历到末尾时，我们跳到另一个条链表的开头继续遍历。两个指针最终会相等，而且只有两种情况，一种情况是在交点处相遇，另一种情况是在各自的末尾的空节点处相等。为什么一定会相等呢，因为两个指针走过的路程相同，是两个链表的长度之和，所以一定会相等。
'''
class solution2:
    def getintersectionNode(self, head1, head2):
        if not head1 or not head2:
            return None
        a, b = head1, head2
        while a != b:
            if a:
                a = a.next
            else:
                a = head2
            if b:
                b = b.next
            else:
                b = head1
        return a