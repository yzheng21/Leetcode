'''
Given a list of words and an integer k, return the top k frequent words in the list.
Notice
You should order the words by the frequency of them in the return list,
the most frequent one comes first. If two words has the same frequency,
the one with lower alphabetical order come first.
Example
Given
[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
for k = 3, return ["code", "lint", "baby"].
for k = 4, return ["code", "lint", "baby", "yes"],
'''
from collections import defaultdict
from heapq import heappop, heappush

class solution:
    def topkfrequentwords(self,words,k):
        result = []
        words_count = defaultdict(int)
        for word in words:
            words_count[word] += 1
        max_heap = []
        for word in words_count:
            count = words_count[word]
            heappush(max_heap,(-count,word))
        for i in range(k):
            count,word = heappop(max_heap)
            result.append(word)

        return result
