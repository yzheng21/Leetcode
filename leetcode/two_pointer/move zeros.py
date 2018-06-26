class solution:
    def movezeros(self,nums):
        point = 0
        for i in range(len(nums)):
            if nums[i]:
                print(i, point)
                nums[point],nums[i] = nums[i], nums[point]
                point += 1
        print(nums)

solution().movezeros([1,0,3,0,5])