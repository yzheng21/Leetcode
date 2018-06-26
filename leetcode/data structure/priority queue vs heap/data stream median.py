'''
Numbers keep coming, return the median of numbers at every time a new number added.
What's the definition of Median?
- Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].
For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].
For numbers coming list: [2, 20, 100], return [2, 2, 20].
Challenge
Total run time in O(nlogn).
'''

'''
       idea:
       1. use Python build-in data structure heapq to maintain max_heap and min_heap
       However, heapq supports only min_heap, the way to maintain max_heap is
       convert the number (positive becomes negative, negative becomes positive),
       then push into max_heap by using heappush(max_heap, item)
       Then when we use heappop(max_heap) or max_heap[-1] to get/seek the max,
       We need to converse it again.
       2. maintain the size of max_heap and min_heap such that
       len(max_heap) == len(min_heap) or len(max_heap) = len(min_heap) + 1 are satisfied.
       so we can get median by seek the max from max_heap(meadian = - max_heap[-1])
       Definition: median = A[(n - 1) / 2], according to problem statement.
       '''

from heapq import heappush, heappop
class Solution:
    def median(self,nums):
        max_heap, min_heap = [], []
        result = []
        for num in nums:
            self.add_to_heap(max_heap,min_heap,num)
            self.balanced_heaps(max_heap,min_heap)
            median = -max_heap[0]
            result.append(median)
        return result

    def add_to_heap(self,max_heap,min_heap,num):
        if len(max_heap) == 0 or num < -max_heap[0]:
            heappush(max_heap,-num)
        else:
            heappush(min_heap,num)

    def balanced_heaps(self,max_heap,min_heap):
        while len(max_heap) < len(min_heap):
            heappush(max_heap,-heappop(min_heap))
        while len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))