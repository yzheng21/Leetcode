'''
Implement a trie with insert, search, and startsWith methods.
Notice
You may assume that all inputs are consist of lowercase letters a-z.
Example
insert("lintcode")
search("code")
>>> false
startsWith("lint")
>>> true
startsWith("linterror")
>>> false
insert("linterror")
search("lintcode)
>>> true
startsWith("linterror")
>>> true
'''

"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_complete_word = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            child = node.children.get(char)
            if not child:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.is_complete_word = True
        node.word = word

    def search(self,word):
        node = self.root
        for char in word:
            child = node.children.get(char)
            if not child:
                return False
            node = child
        return node.is_complete_word

    def startwith(self,prefix):
        node = self.root

        for char in prefix:
            child = node.children.get(char)
            if not child:
                return False
            node = child
        return True

