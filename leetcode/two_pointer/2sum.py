#two pointer

def twosum(nums,target):
    res = [1]*2
    if nums is None or len(nums)<2:
        return res
    copy = nums
    print(copy)
    low, high = 0, len(copy)-1

    while low < high:
        if copy[low] + copy[high] < target:
            low += 1
        elif copy[low] + copy[high] > target:
            high -= 1
        else:
            res[0] = copy[low]
            res[1] = copy[high]
            break
    print(res)
    index1,index2 = -1,-1
    for i in range(len(nums)):
        if nums[i] == res[0] and index1 == -1:
            index1 = i
        elif nums[i] == res[1] and index2 == -1:
            index2 = i
    res[0] = index1
    res[1] = index2
    print(res)

twosum([2, 2, 7, 11, 15],9)