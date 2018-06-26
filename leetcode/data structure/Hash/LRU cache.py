'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.
get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value
if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
'''

class Node:
    def __init__(self, key= None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUcache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def movetotail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail

    def removenode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.removenode(node)
        self.movetotail(node)
        return node.value

    def set(self, key, value):
        if key in self.hash:
            self.hash[key].value = value
            node = self.hash[key]
            self.removenode(node)

        else:
            if len(self.hash) == self.capacity:
                del self.hash[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            node = Node(key,value)
            self.hash[key] = node

        self.movetotail(node)

def main():
    cache = LRUcache(2)
    cache.set(1,1)
    cache.set(2,2)
    print(cache.get(1))
    print(cache.get(2))
    cache.set(3,3)
    print(cache.get(1))

if __name__ == '__main__':
    main()
