'''
Manacher algorithm
Manacher算法用一个辅助数组Len[i]表示以字符T[i]为中心的最长回文字串的最右字符到T[i]的长度，
比如以T[i]为中心的最长回文字串是T[l,r],那么Len[i]=r-i+1。Len数组有一个性质，那就是Len[i]-1
就是该回文子串在原字符串S中的长度。
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

