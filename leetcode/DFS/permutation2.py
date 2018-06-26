class solution:
    def permute(self,nums):
        def dfs(result,temp,nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    #similar to subsets2 index != i and nums[i] == nums[i-1]
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    dfs(result,temp+[nums[i]],nums[:i]+nums[i+1:])
        if nums is None:
            return None
        if nums is []:
            return [[]]
        result = []
        dfs(result,[],sorted(nums))
        return result

result = solution().permute([1,2,2])
print(result)