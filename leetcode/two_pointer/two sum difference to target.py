class Solution1:
    """
    @param: nums: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if nums is None or len(nums) < 2:
            return []
        mapping = {}
        for i in range(len(nums)):
            if nums[i] - target in mapping:
                return sorted([i + 1, mapping[nums[i] - target] + 1])
            elif nums[i] + target in mapping:
                return sorted([i + 1, mapping[nums[i] + target] + 1])
            else:
                mapping[nums[i]] = i
        return []

class Solution2:

    def twoSum7(self, nums, target):
        res = [1] * 2
        if nums is None or len(nums) < 2:
            return res
        if target < 0:
            target = -target
        pair = list(nums)
        pair.sort()
        j = 0
        for i in range(len(nums)):
            if i == j:
                j += 1
            while j < len(nums) and pair[j] - pair[i] < target:
                j += 1
            if j < len(nums) and pair[j] - pair[i] == target:
                res[0] = nums.index(pair[i]) + 1
                res[1] = nums.index(pair[j]) + 1
                if res[0] > res[1]:
                    res[0], res[1] = res[1], res[0]
                return res
        return res

res = Solution2().twoSum7([2,7,15,24], 5)
print(res)

