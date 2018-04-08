'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# class Solution(object):
def lengthOfLongestSubstring(self, s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
        if c in d:
            start = max(start,d[c]+1)
        d[c] = i
        ans = max(ans, i-start+1)
    return ans