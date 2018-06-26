import queue
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#     def __repr__(self):
#         return str(self.val)
#
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.head = None
#         self.tail = None
#
#     def push(self,val):
#         node = Node(val)
#         if not self.head:
#             self.head = node
#             self.tail = self.head
#         else:
#             node = Node(val)
#             self.tail.next = node
#             self.tail = node
#         self.size += 1
#
#     def pop(self):
#         if not self.isEmpty():
#             node = self.head
#             self.head = self.head.next
#             self.size -= 1
#             return node.val
#
#     def top(self):
#         return self.head.val
#
#     def isEmpty(self):
#         return self.size == 0


class Stack:
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()
        #self.size = 0

    def push(self,x):
        if self.queue1.empty():
            self.queue2.put(x)
        if self.queue2.empty():
            self.queue1.put(x)
        #self.size += 1

    def pop(self):
        if self.queue1.empty() and self.queue2.empty():
            return None

        if self.queue1.empty():
            while self.queue2.qsize() > 1:
                self.queue1.put(self.queue2.get())
            return self.queue2.get()

        if self.queue2.empty():
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get())
            return self.queue1.get()

        return None

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())

main()



