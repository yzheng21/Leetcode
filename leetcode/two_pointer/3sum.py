class solution:
    def threesum(self,nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                   res.append([nums[i],nums[left],nums[right]])
                   right -= 1
                   left += 1
                   while left < right and nums[left] == nums[left-1]:
                       left += 1
                   while left < right and nums[right] == nums[right+1]:
                       right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            print(res)

solution().threesum([-1 ,0 ,1 ,2 ,-1 ,-4])
