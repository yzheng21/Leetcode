'''
Ugly number is a number that only have factors 2, 3 and 5.
Design an algorithm to find the nth ugly number.
The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
Notice
Note that 1 is typically treated as an ugly number.
Example
If n=9, return 10.
Challenge
O(n log n) or O(n) time.
'''

from queue import PriorityQueue

class solution:
    def nthuglynum(self,n):
        if n <= 1:
            return n
        q = PriorityQueue()
        q.put(1)
        primes = [2,3,5]
        visited = set()
        for i in range(n):
            result = q.get()
            for j in range(len(primes)):
                if result * primes[j] not in visited:
                    q.put(result * primes[j])
                    visited.add(result * primes[j])
        return result

s = solution()
print(s.nthuglynum(9))


