'''
There is an integer matrix which has the following features:
The numbers in adjacent positions are different.
The matrix has n xs and m yumns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:
A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.
Notice
The matrix may contains multiple peeks, find any of them.
Example
Given a matrix:
[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])
Challenge
Solve it in O(n+m) time.
If you come up with an algorithm that
you thought it is O(n log m) or O(m log n),
can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
'''

class solution:

    def maxcol(self,a,row):
        i,j = 1, len(a[row]) - 2
        while i <= j:
            m = (i+j)//2
            if a[row][m] < a[row][m-1]:
                j = m - 1
            elif a[row][m] < a[row][m+1]:
                i = m + 1
            else:
                return m
        return 0

    def findpeak2(self,a):
        top, bottom = 1, len(a) - 2
        while top <= bottom:
            m = (top + bottom)//2
            col = self.maxcol(a,m)
            if a[m][col] < a[m-1][col]:
                bottom = m - 1
            elif a[m][col] < a[m+1][col]:
                top = m + 1
            else:
                result = [None] * 2
                result[0] = m
                result[1] = col
                return result

        return None
