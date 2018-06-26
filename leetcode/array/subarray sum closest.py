import math
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return None
        if len(nums) == 1:
            return [0,0]
        sums = [0 for i in range(len(nums))]
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        sortedSums = list(sums)
        sortedSums.sort()

        minDiff = math.inf
        for i in range(1, len(sortedSums)):
            if sortedSums[i] - sortedSums[i-1] < minDiff:
                minDiff = sortedSums[i] - sortedSums[i-1]
                num1 = sortedSums[i-1]
                num2 = sortedSums[i]
        index1 = sums.index(num1)
        index2 = sums.index(num2)
        if index1 > index2:
            tmp = index1
            index1 = index2 + 1
            index2 = tmp
        else:
            index1 = index1 + 1
        print([index1, index2])

Solution().subarraySumClosest([-3, 1, 1, -3, 5])