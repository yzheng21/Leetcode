class solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,element):
        self.stack2.append(element)

    def pop(self):
        if len(self.stack1) == 0:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

    def top(self):
        if len(self.stack1) == 0:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2.pop())
        if len(self.stack1) != 0:
            return self.stack1[-1]
        return None

def main():
    queue = solution()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())
    print(queue.pop())
main()
