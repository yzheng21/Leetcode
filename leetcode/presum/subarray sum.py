
class solution:
    def subarraysum(self,nums):
        dict = {}
        dict[0] = -1
        sum = 0
        res = []
        for i, item in enumerate(nums):
            sum += item
            if sum in dict:
                res.append(dict[sum] + 1)
                res.append(i)
                return res
            dict[sum] = i

res = solution().subarraysum([-3, 1, 2, -3, 4])
print(res)