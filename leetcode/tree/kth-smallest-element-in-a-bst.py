# Time:  O(max(h, k))
# Space: O(h)

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and
# you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):
    def kthsmallest(self,root,k):
        next_queue , cur, rank = [], root, 0
        while next_queue or cur:
            if cur:
                next_queue.append(cur)
                cur = cur.left
            else:
                cur = next_queue.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right
        return float('-inf')

