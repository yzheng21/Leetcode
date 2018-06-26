import collections
class solution:
    def del_duplicates(self,nums):
        dict = collections.defaultdict(set)
        for i,item in enumerate(nums):
            if item not in dict:
                dict[item] = 1
        return len(dict),dict

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
len,dict = solution().del_duplicates(duplicate)
print(len,dict)