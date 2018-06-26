'''
二分答案的方法，时间复杂度 O(log(range) * (log(n) + log(m)))O(log(range)∗(log(n)+log(m)))

其中 range 为最小和最大的整数之间的范围。
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






