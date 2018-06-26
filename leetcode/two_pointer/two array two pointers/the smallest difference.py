'''
给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取 B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|)。返回最小差。
'''

class solution:
    def smallestdifference(self,A,B):
        if not A or len(A) == 0 or not B or len(B) == 0:
            return 0
        A.sort()
        B.sort()
        a,b = 0, 0
        diff = 0x7fffffff
        while a < len(A) and b < len(B):
            diff = min(diff,abs(A[a]-B[b]))
            if A[a] < B[b]:
                a += 1
            else:
                b += 1
        return diff
