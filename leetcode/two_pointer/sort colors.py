class solution:
    def sortcolor(self,nums):
        if nums is None:
            return 0
        red, white, blue = 0,0,len(nums)-1
        while white < blue:
            if nums[white] == 0:
                self.swap(nums,red,white)
                red += 1
                white += 1
            elif nums[white] == 1:
                red += 1
            else:
                self.swap(nums,blue,white)
                blue -= 1

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp