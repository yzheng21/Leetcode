class solution:
    def submatrixsum(self,matrix):
        result = [[0,0]*2]
        m,n = len(matrix), len(matrix[0])
        if m == 0:
            return result
        if n == 0:
            return result
        sum = [[0]*(n+1) for i in range(m+1)]
        for j in range(n+1):
            sum[0][j] = 0
        for i in range(m+1):
            sum[i][0] = 0
        for i in range(m):
            for j in range(n):
                sum[i+1][j+1] = matrix[i][j] + sum[i+1][j] + sum[i][j+1] - sum[i][j]

        for l in range(m):
            for h in range(l,m+1):
                dict = {}
                for j in range(n+1):
                    diff = sum[h][j] - sum[l][j]
                    if diff in dict:
                        k = dict[diff]
                        result[0][0] = l
                        result[0][1] = k
                        result[1][0] = h-1
                        result[1][1] = j-1
                        return result
                    else:
                        dict[diff] = j
        return result