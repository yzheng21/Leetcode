import math
class solution:
    def twosumclosest(self,nums,target):
        length = len(nums)
        minnum = -math.inf
        index1,index2 = 0,length-1
        p1,p2 = index1,index2
        while p1 < p2:
            s = nums[p1] + nums[p2]
            diff = abs(nums[p1]+nums[p2]-target)
            if diff < minnum:
                minnum = diff
                index1 = p1
                index2 = p2
            if s < target:
                p1 += 1
            else:
                p2 -= 1
        return [index1,index2]

    def threesumclosest(self,nums,target):
        if len(nums) < 3:
            return None
        nums.sort()
        res,closest = 0,0
        minnum = -math.inf
        for i, num in enumerate(nums):
            if i != 0 and num == nums[i-1]:
                continue
            if i > len(nums) - 3:
                break
            twotarget = target - num
            tworesult = self.twosumclosest(nums[i+1],twotarget)
            if tworesult:
                res = nums[i] + nums[tworesult[0]+i+1] + nums[tworesult[1]+i+1]
                if abs(res-target) < minnum:
                    minnum = abs(res - target)
                    closest = res
        return closest
