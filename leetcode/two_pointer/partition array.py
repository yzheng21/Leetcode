class solution:
    def partition(self,nums,k):
        if nums is None: return 0
        start,end = 0,len(nums)-1
        while start < end:
            while start < end and nums[start] < k:
                start += 1
            while start < end and nums[end] >= k:
                end -= 1
            if start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        if nums[start] < k:
            return start+1
        else:
            return start

index = solution().partition([3,2,2,1],2)
print(index)

