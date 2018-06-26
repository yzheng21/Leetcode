'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"
'''
'''
思路：题目的字符串长度是1000，如果我们暴力解决，那么构造字符串时间复杂度（O（n^2）），判断字符串是不是回文字符串时间复杂度（O（n））总的时间复杂度是（O（n^3）），如果暴力解决，那么肯定是会TLE的。

     寻找回文字符串一般有两种方法。第一种是先构造一个字符串，从首尾开始判断是否对应相等。这种方法需要的时间复杂度比较大。第二种方法是从中间往两边找，直到找到两边不一样。这种方法我们要先确定中间的key字符，
     
     这里由于当重复字符出现的时候，应该把这些重复的字符捆在一起，因为重复字符出现的时候放中间可以保证满足是回文字符串。比如’'abbbbba’，如果我们将’bbbbb’捆在一起可以减少很多不必要的判断，
     
     而且可以避免回文字符串个数为偶数的时候被忽略的情况，比如’abba’。

     那么我们可以初始化回文子字符串为s[0]，长度是1，从第一个字符开始往两边找，记录从这个字符为中间字符搜索的回文字符串的长度，如果大于当前记录的回文，那么替换当前的字符串及其长度。
     
     从中间找到了最后一位或者以最后一个字符为中间key字符的时候结束。这种方法最坏的情况是’ababababababababa……bac’，这种情况的时间复杂度是（0 + 1 + 2 +…+n - 1） = (O(n^2))，由于字符串长度为1000，
     
     所以（O（n^2））的时间复杂度是可以接受的。
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 1:
            return s
        if size == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        maxp = 1
        ans = s[0]
        i = 0
        while i < size:
            j = i+1
            # 将相同的字符统一到一起
            while j < size:
                if s[i] == s[j]:
                    j += 1
                else:
                    break
            k = 0
            while i - k -1 > 0 and j + k <= size -1:
                if s[i - k -1] != s[j + k]:
                    break
                k += 1
            if j - i + 2*k > maxp:    #回文字符串长度
                maxp = j -i + 2*k
                ans = s[i-k : j+k]
            if j + k == size - 1:     #出口
                break
            i = j
        return ans