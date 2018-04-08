'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example, If nums = [1,2,2], a solution is:

[ [2], [1], [1,2,2], [2,2], [1,2], [] ]
'''

def solution(nums):
    def dfs(nums, index, path, ans):
        ans.append(path)
        for i in range(index, len(nums)):
            if index != i and nums[i] == nums[i-1]:
                continue
            dfs(nums, i + 1, path+[nums[i]], ans)

    nums.sort()
    ans = []
    dfs(nums,0,[],ans)
    print(ans)


nums = [1,2,2]
solution(nums)