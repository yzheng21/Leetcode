class solution:
    def rainbowsorting(self,nums):
        if nums is None or len(nums) <= 1:
            return nums
        i,j,k = 0,0,len(nums)-1
        while j <= k:
            if nums[j] == -1:
                self.swap(nums,i,j)
                i += 1
                j += 1
            elif nums[j] == 0:
                j += 1
            elif nums[j] == 1:
                self.swap(nums,j,k)
                k -= 1
        return nums

    def swap(self,nums,i,j):
        if i == j: return
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

res = solution().rainbowsorting([1,-1,0,1,-1,0])
print(res)