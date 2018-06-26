'''
lintcode
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
'''

#三步反转法 (X^TY^T)^T=YX
def reversestring(s,start,end):
    while start < end:
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1

def rotatestring(s,n,m):
    m %= n
    #反转[0..m - 1]，套用到上面举的例子中，就是X->X ^ T，即abc->cba
    reversestring(s,0,m-1)
    #反转[m..n - 1]，例如Y->Y^T，即 def->fed
    reversestring(s,m,n-1)
    #反转[0..n - 1]，即如整个反转，(X^TY^T)^T=YX，即 cbafed->defabc。
    reversestring(s,0,n-1)

'''
leetcode:
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
'''
#solution1
def rotatestring(str1,str2):
    return len(str1) == len(str2) and str2 in str1 + str1

#solution2:
# def rotatestring(a,b):
#     n = len(a)
#     if n != len(b): return False
#     if n == 0: return True
#     shifts = [1] * (n+1)
#     left = -1
#     for right in range(n):
#         while left >= 0 and b[left] != b[right]:
#             left -= shifts[left]
#         shifts[right + 1] = right - left
#         left += 1


