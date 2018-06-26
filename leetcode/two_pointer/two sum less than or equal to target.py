class solution:
    def twosum_less(self,nums,target):
        if nums is None or len(nums) < 2:
            return 0
        nums.sort()
        start, end = 0, len(nums)-1
        count = 0
        while start < end:
            if nums[start] + nums[end] <= target:
                count += end - start
                start += 1
            else:
                end -= 1
        print(count)

solution().twosum_less([2, 7, 11, 15],24)