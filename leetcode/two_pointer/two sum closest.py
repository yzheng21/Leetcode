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
