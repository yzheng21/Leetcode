'''
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
Example
Given lists:
[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
'''

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = next
    def __repr__(self):
        return str(self.val)
    def print_all(self):
        result = ''
        node = self
        while node:
            result += node.__repr__() + '->'
            node = node.next
        print(result)

from heapq import heappush, heappop
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists_heap(self, lists):
        if not lists or len(lists) == 0:
            return
        min_heap = []
        for node in lists:
            if node:
                heappush(min_heap,(node.val,node))
        dummy = ListNode(0)
        tail = dummy
        while min_heap:
            value,node = heappop(min_heap)
            if node.next:
                heappush(min_heap,(node.next.val,node.next))
            tail.next = node
            tail = tail.next
        return dummy.next

    def mergeKlists_merge(self,lists):
        if not lists or len(lists) == 0:
            return

        return self.helper(lists, 0, len(lists) - 1)

    def helper(self,lists,start,end):
        if start == end:
            return lists[start]
        mid = start + (end-start)//2
        left = self.helper(lists,start,mid)
        right = self.helper(lists,mid+1,end)

        return self.merge_two_sorted_lists(left, right)

    def merge_two_sorted_lists(self, list_1, list_2):
        dummy = ListNode(0)
        tail = dummy
        head_1 = list_1
        head_2 = list_2

        while head_1 and head_2:
            if head_1.val < head_2.val:
                tail.next = head_1
                head_1 = head_1.next
            else:
                tail.next = head_2
                head_2 = head_2.next
            tail = tail.next

        if head_1:
            tail.next = head_1
        else:
            tail.next = head_2

        return dummy.next

