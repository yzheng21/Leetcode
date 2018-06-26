import math
class solution1:
    def dp(self,nums,n):
        sum = 0
        m = -math.inf

        for i in range(n):
            sum += nums[i]
            m = max(m, sum)
            if sum < 0:
                sum = 0
        return m

class solution2:
    def maxsubarray(self,nums,n):
        return self.helper(nums,0,n-1,-math.inf)

    def helper(self,nums,left,right,m):
        if left > right:
            return None
        mid = left + (right - left)/2
        lmax = self.helper(nums,left,mid,m)
        rmax = self.helper(nums,mid+1,right,m)
        m = max(m,lmax,rmax)
        sum = 0
        mlsum = 0
        for i in range(left,mid-1,-1):
            sum += nums[i]
            mlmax = max(mlmax,sum)
        sum = 0
        mrsum = 0
        for i in range(mid + 1, right, -1):
            sum += nums[i]
            mlmax = max(mrsum, sum)
        m = max(m,nums[mid]+mlsum+mrsum)
        return m


