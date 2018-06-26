class solution:
    def twosum_greater(self,nums,target):
        if nums is None or len(nums) < 2:
            return 0
        nums.sort()
        start, end = 0, len(nums)-1
        count = 0
        while start < end:
            if nums[start] + nums[end] <= target:
                start += 1
            else:
                count += end - start
                end -= 1
        print(count)

s = solution()
s.twosum_greater([2, 7, 11, 15, 15],24)
