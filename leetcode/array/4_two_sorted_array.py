'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3] nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2] nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
class Solution(object):
    def _findMedianSortedArrays(self, nums1, nums2):
        def find_kth(nums1, nums2, k):
            m, n = len(nums1), len(nums2)
            if (m > n): return find_kth(nums2, nums1, k)
            if (m == 0): return nums2[k - 1]
            if (k == 1): return min(nums1[0], nums2[0])

            pa = min(k / 2, m)
            pb = k - pa
            if (nums1[pa - 1] < nums2[pb - 1]):
                return find_kth(nums1[pa:], nums2, k - pa)
            elif (nums1[pa - 1] > nums2[pb - 1]):
                return find_kth(nums1, nums2[pb:], k - pb)
            else:
                return nums1[pa - 1]
        m, n = len(nums1), len(nums2)
        total = m + n
        if (total % 2 != 0):
            return find_kth(nums1, nums2, total / 2 + 1)
        else:
            return (find_kth(nums1, nums2, total / 2) +
                    find_kth(nums1, nums2, total / 2 + 1)) / 2






