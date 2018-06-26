'''
Given an integer array, heapify it into a min-heap array.
For a heap array A, A[0] is the root of heap, and for each A[i],
A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Clarification
What is heap?
Heap is a data structure, which usually have three methods:
push, pop and top.
where "push" add a new element the heap,
"pop" delete the minimum/maximum element in the heap,
"top" return the minimum/maximum element.
What is heapify?
Convert an unordered integer array into a heap array.
If it is min-heap, for each element A[i],
we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
What if there is a lot of solutions?
Return any of them.
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.
Challenge
O(n) time complexity
'''

class solution:
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]

    def left(self,i):
        return 2 * i + 1

    def right(self,i):
        return 2 * i + 2

    def parent(self,i):
        return (i - 1) //2

    def sifdown(self,i,nums):
        while self.left(i) < len(nums):
            child = self.left(i)
            if self.right(i) < len(nums) and nums[self.right(i)] < nums[self.left(i)]:
                child = self.right(i)
            if nums[i] < nums[child]:
                break
            self.swap(nums,i,child)
            i = child

    def sifup(self,i,nums):
        while self.parent(i) >= 0 and nums[self.parent(i)] > nums[i]:
            self.swap(nums,i,self.parent(i))
            i = self.parent(i)

    def heapify1(self,nums):
        for i in range(len(nums)//2,-1,-1):
            self.sifdown(i,nums)

    def heapify2(self,nums):
        for i in range(1,len(nums)):
            self.sifup(i,nums)

def main():
    s = solution()
    nums = [45, 39, 32, 11]
    s.heapify1(nums)
    print(nums)

    nums = [45, 39, 32, 11]
    s.heapify2(nums)
    print(nums)


if __name__ == '__main__':
    main()
