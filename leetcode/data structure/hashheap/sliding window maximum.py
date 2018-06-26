'''
Given an array of n integer with duplicate number,and a moving window(size k),
move the window at each iteration from the start of the array,
find the maximum number inside the window at each moving.
Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]
At first the window is at the start of the array like this
[|1, 2, 7| ,7, 8] , return the maximum 7;
then the window move one step forward.
[1, |2, 7 ,7|, 8], return the maximum 7;
then the window move one step forward again.
[1, 2, |7, 7, 8|], return the maximum 8;
Challenge
o(n) time and O(k) memory
'''
from collections import deque
from heapq import heappush,heappop
class solution:
    def maxslidingwindow(self,nums,k):
        q = deque()
        result = []
        if not nums or len(nums) == 0 or len(nums) < k or k == 0:
            return []
        n = len(nums)
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k -1:
                while q and q[0] <= i - k:
                    q.popleft()
                result.append(nums[q[0]])
        return result

    def maxslidingwindow2(self,nums,k):
        max_heap = []
        result = []
        if not nums or len(nums) == 0 or len(nums) < k or k == 0:
            return []
        n = len(nums)
        for i in range(n):
            if i >= k:
                heappop(max_heap)
            heappush(max_heap,-nums[i])
            if i + 1 >= k:
                result.append(-max_heap[0])
        return result

s = solution()
nums = [1, 2, 7, 7, 8]
k = 3
print(s.maxslidingwindow2(nums, k))




