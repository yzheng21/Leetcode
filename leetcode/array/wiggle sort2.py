class solution:
    def partition(self,nums,l,r,rank):
        left,right = l,r
        now = nums[left]
        while left < right:
            while left<right and nums[right]>=now:
                right -= 1
            nums[left] = nums[right]
            while left<right and nums[left]<=now:
                left += 1
            nums[right] = nums[left]

        if left-l == rank:
            return now
        elif left - l < rank:
            return self.partition(nums,left+1,r,rank-(left-l+1))
        else:
            return self.partition(nums,l,right-1,rank)

    def wigglesort(self,nums):
        tem = [0]*len(nums)
        for i in range(len(nums)):
            tem[i] = nums[i]
        mid = self.partition(tem,0,len(nums)-1,len(nums)/2)
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = mid
        if len(nums)%2 == 0:
            l = len(nums)-2
            r = 1
            for i in range(len(nums)):
                if nums[i]<mid:
                    ans[l] = nums[i]
                    l -= 2
                elif nums[i] > mid:
                    ans[r] = nums[i]
                    r += 2
        else:
            l = 0
            r = len(nums) - 2
            for i in range(len(nums)):
                if nums[i] < mid:
                    ans[l] = nums[i]
                    l += 2
                elif nums[i] > mid:
                    ans[r] = nums[i]
                    r -= 2
        for i in range(len(nums)):
            nums[i] = ans[i]
