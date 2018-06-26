class solution1:
    def mergesortedarray(self,A,B):
        n, m = len(A),len(B)
        for i in range(n):
            A[i+m] = B[i]
        return A.sort()

class solution2:
    def mergesortedarray(self,A,m,B,n):
        i = m - 1
        j = n - 1
        index = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                index -= 1
                i -= 1
            else:
                A[index] = B[j]
                index -= 1
                j -= 1
        while i >= 0:
            A[index] = A[i]
            index -= 1
            i -= 1
        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1
        return A

