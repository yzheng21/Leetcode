
'''
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).
For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such windows,
you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import defaultdict
class solution:
    def minwindow(self,s,target):
        s_char = defaultdict(int)
        t_char = defaultdict(int)
        for char in target:
            t_char[char] += 1
        j = 0
        min_substring = ''
        min_length = float('inf')
        for i in range(len(s)):
            while j < len(s) and not self.iscontain(s_char,t_char):
                s_char[char] += 1
                j += 1
            if self.iscontain(s_char,t_char):
                if min_length > j -i:
                    min_length = j-i
                    min_substring = s[i:j]
            s_char[s[i]] -= 1
        return min_substring
    
    def iscontain(self,s_char,t_char):
        for char in t_char:
            if char not in s_char or s_char[char] < t_char[char]:
                return False
            return True