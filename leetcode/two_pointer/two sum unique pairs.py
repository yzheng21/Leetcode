class solution:
    def twosun_unique(self,nums,target):
        if nums is None or len(nums) <= 1:
            return 0
        nums.sort()
        start,end = 0, len(nums)
        count = 0
        while start < end:
            if nums[start] + nums[end] == target:
                count += 1
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start-1]:
                    start += 1
                while start < end and nums[end] == nums[end+1]:
                    end -= 1
            elif nums[start] + nums[end] <= target:
                start += 1
            else:
                end -= 1
        return count