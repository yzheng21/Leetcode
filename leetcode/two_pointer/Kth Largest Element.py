class solution:
    def quickselect(self,k,nums):
        return self.helper(nums,0,len(nums)-1,k)

    def helper(self,nums,left,right,k):
        pivot = nums[left]
        i = left
        j = right
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if left + k -1 <= j:
            return self.helper(nums,left,j,k)
        if left + k - 1 >= i:
            return self.helper(nums,i,right,k-(i-left))
        return nums[j+1]