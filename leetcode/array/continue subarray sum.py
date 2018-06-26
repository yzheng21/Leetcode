#circular subarray
class solution:
    def continuesubarraysum(self,a):
        result = [0]*2
        max_sum = float('inf')
        total = 0
        for i in range(len(a)):
            total += a[i]
        sum = 0
        start, end = 0, -1
        for i in range(len(a)):
            if sum > 0:
                sum = a[i]
                start = end = i
            else:
                sum += a[i]
                end = i
            if total - sum > max_sum and not(start == 0 and end == len(a)-1):
                max_sum = total - sum
                result[0] = (end+1)%len(a)
                result[1] = (start-1)%len(a)