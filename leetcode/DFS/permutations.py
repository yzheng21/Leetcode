# class solution:
#     def permute(self,nums):
#         def dfs(result,temp,nums):
#             if nums == []:
#                 result += [temp]
#             else:
#                 for i in range(len(nums)):
#                     dfs(result,temp+[nums[i]],nums[:i]+nums[i+1:])
#         if nums is None:
#             return None
#         if nums is []:
#             return [[]]
#         result = []
#         dfs(result,[],sorted(nums))
#         return result
#
#
# class solution2:
#     def permute(self,nums):
#         alist = []
#         result = [];
#         if not nums:
#             return result
#
#         self.helper(nums, alist, result)
#
#         return result
#
#     def helper(self, nums, alist, ret):
#         if len(alist) == len(nums):
#             # new object
#             ret.append([] + alist)
#             return
#
#         for i, item in enumerate(nums):
#             if item not in alist:
#                 alist.append(item)
#                 self.helper(nums, alist, ret)
#                 alist.pop()
# print(solution2().permute([1,2,3]))

# Non-Recursion
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums is None:
            return []
        if nums == []:
            return [[]]
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations

res = Solution().permute([1,2,3])
print(res)