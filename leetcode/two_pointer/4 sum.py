class solution:
    def foursum(self,nums,target):
        if nums is None or len(nums) < 4:
            return 0
        res = []
        nums.sort()
        for j in range(len(nums)-2):
            if j == 0 or nums[j] != nums[j-1]:
                for i in range(j+1,len(nums)-1):
                    if i == j+1 or nums[i] != nums[i-1]:
                        start, end = i+1,len(nums)-1
                        sum = target - nums[i] - nums[j]
                        while start < end:
                            if nums[start] + nums[end] == sum:
                                temp = [nums[j],nums[i],nums[start],nums[end]]
                                #print([nums[j],nums[i],nums[start],nums[end]])
                                res.append(temp)
                                while start < end and nums[start] == nums[start+1]:
                                    start += 1
                                while start < end and nums[end] == nums[end-1]:
                                    end -= 1
                                start += 1
                                end -= 1
                            elif nums[start] + nums[end] < sum:
                                start += 1
                            else:
                                end -= 1
        return res

res = solution().foursum([1,0,-1,0,-2,2],0)
print(res)
