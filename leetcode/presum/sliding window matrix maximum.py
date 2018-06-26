class solution:
    def slidingmatrix(self,matrix,k):
        m,n = len(matrix), len(matrix[0])
        if m == 0:
            return 0
        if n == 0:
            return 0
        sum = [[0]*(n+1) for i in range(m+1)]
        for j in range(n+1):
            sum[0][j] = 0
        for i in range(m+1):
            sum[i][0] = 0
        for i in range(m):
            for j in range(n):
                sum[i+1][j+1] = matrix[i][j] + sum[i+1][j] + sum[i][j+1] - sum[i][j]
        max_num = float('inf')
        for i in range(k,m+1):
            for j in range(k,n+1):
                temp = sum[i][j] - sum[i-k][j] - sum[i][j-k] + sum[i-k][j-k]
                max_num = max(max_num,temp)
        return max_num
