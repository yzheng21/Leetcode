'''
Design a data structure that supports the following two operations: addWord(word) and search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.
 Notice
You may assume that all words are consist of lowercase letters a-z.
Have you met this question in a real interview? Yes
Example
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true
'''

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_complete_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addword(self,word):
        node = self.root
        for char in word:
            child = node.children.get(char)
            if not child:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.is_complete_word = True

    def search(self,word):
        if len(word) == 0:
            return False
        return self.search_recursive(word,self.root,0)

    def search_recursive(self,word,node,index):
        if len(word) == index:
            return node.is_complete_word

        char = word[index]
        if char == '.':
            for i in range(26):
                letter = chr(ord('a') + i)
                child = node.children.get(letter)
                if child:
                    if self.search_recursive(word,child,index+1):
                        return True
            return False
        else:
            child = node.children.get(char)
            if not child:
                return False
            return self.search_recursive(word,child,index+1)