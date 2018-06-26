class solution:
    def find(self,a,len,value):
        if a[len-1] < value:
            return len
        l,r = 0,len-1
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if value <= a[mid]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def subarraysum2(self,a,start,end):
        n = len(a)
        for i in range(1,n):
            a[i] += a[i-1]
        a.sort()
        cnt = 0
        for i in range(n):
            if a[i] >= start and a[i] <= end:
                cnt += 1
            l = a[i] - end
            r = a[i] - start
            cnt += self.find(a,n,r) - self.find(a,n,l)
        return cnt

s = solution()
a = [1,2,3,4]
cnt = s.subarraysum2(a,1,3)
print(cnt)