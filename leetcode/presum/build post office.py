class solution:
    def getsumdistance(self,a,n,ans):
        prefixsum1 = [None]*n
        prefixsum2 = [None]*n
        prefixsum1[0] = a[0]
        '''
        第一阶段，处理前缀。
    	prefixSum1记录数组 a 的前缀和，即:prefixSum1[i]=a[0]+a[1]+..+a[i].
    	prefixSum2记录数组 prefixSum1 前缀和，prefixSum2即为前 i 个点到第 i 个点的代价和。
        '''
        for i in range(1,n):
            prefixsum1[i] = prefixsum1[i-1] + a[i]
        prefixsum2[0] = 0
        for i in range(1,n):
            prefixsum2[i] = prefixsum2[i-1] + prefixsum1[i-1]
        for i in range(n):
            ans[i] = prefixsum2[i]
        '''
        第二阶段，处理后缀。
    	prefixSum1记录数组 a 的后缀和，即:prefixSum1[i]=a[n-1]+a[n-2]+..+a[i].
    	prefixSum2记录数组 prefixSum1 的后缀和，prefixSum2即为 i 之后的点到第 i 个点的代价和。
        '''
        prefixsum1[n-1] = a[n-1]
        for i in range(n-2,-1,-1):
            prefixsum1[i] = prefixsum1[i+1] + a[i]
        prefixsum2[n-1] = 0
        for i in range(n-2,-1,-1):
            prefixsum2[i] = prefixsum2[i+1] + prefixsum1[i+1]
        for i in range(n):
            ans[i] += prefixsum2[i]

    def haszero(self,grid,row,column):
        for i in range(row):
            for j in range(column):
                if grid[0][0] == 0:
                    return True
        return False

    def shortestdistance(self,grid):
        row, column = len(grid), len(grid[0])
        if row == 0 or column == 0 or not self.haszero(grid,row,column):
            return -1
        rowsum = [None]*row
        columnsum = [None]*column
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    rowsum[i] += 1
                    columnsum[i] += 1
        ansrow = [None] * row
        anscolumn = [None] * column
        self.getsumdistance(rowsum,row,ansrow)
        self.getsumdistance(columnsum,column,anscolumn)
        ans = float('inf')
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0 and ans > ansrow[i] + anscolumn[j]:
                    ans = ansrow[i] + anscolumn[j]
        return ans