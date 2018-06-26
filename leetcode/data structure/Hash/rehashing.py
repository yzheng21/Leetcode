class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class solution:
    def addlistnode(self,node,number):
        if node.next != None:
            self.addlistnode(node.next,number)
        else:
            node.next = ListNode(number)

    def addnode(self,table,number):
        p = number % len(table)
        if table[p] == None:
            table[p] = ListNode(number)
        else:
            self.addlistnode(table[p],number)

    def rehashing(self,hashtable):
        hash_size = 2 * len(hashtable)
        table = [None for i in range(hash_size)]
        for item in hashtable:
            p = item
            while p:
                self.addnode(table,p.val)
                p = p.next
        return table